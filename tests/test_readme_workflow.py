"""Regression checks for the generated README contract and file-safety boundaries."""

import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "skill/ultimate-skill-creator/scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


generator = load("create_skill_candidate")
linter = load("validate_readme")


class ReadmeWorkflowTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.candidate = self.root / "candidate"

    def draft(self, **kwargs):
        files = generator.build_files("sample-skill", **kwargs)
        generator.create_candidate(self.candidate, files)
        return self.candidate / "README.md"

    def complete(self, extra=""):
        spec = json.loads(generator.SPEC_PATH.read_text(encoding="utf-8"))
        text = "# Sample skill\n\nTurns a supplied paragraph into a summary.\n\n"
        for section in spec["sections"]:
            text += f'## {section["heading"]}\n\nDocumented contract for this area.\n\n'
        text += "[License](LICENSE)\n" + extra
        path = self.root / "README.md"
        path.write_text(text, encoding="utf-8")
        (self.root / "LICENSE").write_text("Fixture license, not a generated license.")
        return path

    def test_default_draft_structurally_valid(self):
        report = linter.validate(self.draft())
        self.assertTrue(report["passed"], report)
        self.assertTrue(report["warnings"])

    def test_draft_fails_strict(self):
        self.assertFalse(linter.validate(self.draft(), strict=True)["passed"])

    def test_complete_readme_passes_strict(self):
        self.assertTrue(linter.validate(self.complete(), strict=True)["passed"])

    def test_existing_directory_preserved(self):
        self.candidate.mkdir()
        protected = self.candidate / "README.md"
        protected.write_text("Keep my work")
        with self.assertRaises(FileExistsError):
            generator.create_candidate(self.candidate, generator.build_files("x"))
        self.assertEqual(protected.read_text(), "Keep my work")
        self.assertEqual(list(self.candidate.iterdir()), [protected])

    def test_existing_file_preserved(self):
        self.candidate.write_text("Keep")
        with self.assertRaises(FileExistsError):
            generator.create_candidate(self.candidate, generator.build_files("x"))
        self.assertEqual(self.candidate.read_text(), "Keep")

    def test_output_symlink_rejected(self):
        self.candidate.symlink_to(self.root / "missing", target_is_directory=True)
        with self.assertRaises(FileExistsError):
            generator.create_candidate(self.candidate, generator.build_files("x"))
        self.assertFalse((self.root / "missing").exists())

    def test_language_links_exist(self):
        path = self.draft(languages="en,zh-Hant,zh-Hans,es,ja,pt,hi,ar,fr,ko")
        text = path.read_text(encoding="utf-8")
        self.assertEqual(len([a for a in linter.anchors(text) if a.startswith("lang-")]), 10)
        self.assertTrue(linter.validate(path)["passed"])

    def test_duplicate_languages_deduplicated(self):
        text = generator.build_files("x", languages="ja,ja,en")["README.md"]
        self.assertEqual(text.count('id="lang-ja"'), 1)

    def test_english_canonical_added(self):
        self.assertIn('id="lang-en"', generator.build_files("x", languages="ar")["README.md"])

    def test_invalid_language_rejected(self):
        with self.assertRaises(ValueError):
            generator.build_files("x", languages="en,../bad")

    def test_empty_languages_rejected(self):
        with self.assertRaises(ValueError):
            generator.build_files("x", languages=" , ")

    def test_slug_truncation_valid(self):
        name = generator.slugify("a" * 62 + "-long")
        self.assertFalse(name.endswith("-"))
        self.assertLessEqual(len(name), 64)

    def test_slug_fallback(self):
        self.assertEqual(generator.slugify("中文 !!!"), "new-skill")

    def test_svg_title_escaped(self):
        files = generator.build_files("x", title='A & B <test> "quote"')
        root = ET.fromstring(files["skills/x/assets/flow.svg"])
        self.assertIn("A & B <test>", root.find("{http://www.w3.org/2000/svg}title").text)

    def test_multiline_title_rejected(self):
        with self.assertRaises(ValueError):
            generator.build_files("x", title="Title\n## Injected")

    def test_description_yaml_quoted(self):
        desc = 'Read "quotes": safely # with punctuation'
        text = generator.build_files("x", description=desc)["skills/x/SKILL.md"]
        self.assertEqual(json.loads(text.splitlines()[2].split(": ", 1)[1]), desc)

    def test_description_limit(self):
        with self.assertRaises(ValueError):
            generator.build_files("x", description="a" * 1025)

    def test_adapter_and_package_layout(self):
        files = generator.build_files("x")
        self.assertIn("skills/x/agents/openai.yaml", files)
        self.assertNotIn("skills/x/README.md", files)
        self.assertNotIn("LICENSE", files)

    def test_missing_required_section(self):
        path = self.complete()
        path.write_text(path.read_text().replace("## Safety", "## Something else"))
        self.assertIn("missing section: Safety", linter.validate(path)["errors"])

    def test_heading_alias(self):
        path = self.complete()
        path.write_text(path.read_text().replace("## Installation", "## Setup"))
        self.assertTrue(linter.validate(path)["passed"])

    def test_fenced_heading_does_not_satisfy_requirement(self):
        path = self.complete("\n```md\n## Safety\nNot real.\n```\n")
        path.write_text(path.read_text().replace("## Safety", "## Other", 1))
        self.assertFalse(linter.validate(path)["passed"])

    def test_fenced_links_are_not_checked(self):
        path = self.complete("\n~~~md\n[Example](missing.md)\n~~~\n")
        self.assertTrue(linter.validate(path)["passed"])

    def test_code_only_section_is_not_empty(self):
        path = self.complete()
        path.write_text(path.read_text().replace("## Installation\n\nDocumented contract for this area.",
                                                 "## Installation\n\n```sh\nexample-command\n```"))
        self.assertTrue(linter.validate(path)["passed"])

    def test_missing_image(self):
        self.assertFalse(linter.validate(self.complete("![Demo](missing.svg)\n"))["passed"])

    def test_missing_anchor(self):
        report = linter.validate(self.complete("[Go](#does-not-exist)\n"))
        self.assertIn("missing local anchor: #does-not-exist", report["errors"])

    def test_encoded_anchor(self):
        path = self.complete('<a id="中文"></a>\n[Go](#%E4%B8%AD%E6%96%87)\n')
        self.assertTrue(linter.validate(path)["passed"])

    def test_duplicate_explicit_anchor(self):
        self.assertFalse(linter.validate(self.complete('<a id="x"></a><a id="x"></a>'))["passed"])

    def test_duplicate_heading_fragments(self):
        self.assertTrue(linter.validate(self.complete("## Notes\nA\n## Notes\nB\n[Go](#notes-1)"))["passed"])

    def test_link_escape_rejected(self):
        report = linter.validate(self.complete("[Outside](../outside.md)"))
        self.assertTrue(any("escapes repository" in e for e in report["errors"]))

    def test_link_symlink_escape_rejected(self):
        outside = self.root.parent / "outside-nonexistent.md"
        (self.root / "escape.md").symlink_to(outside)
        self.assertFalse(linter.validate(self.complete("[Outside](escape.md)"))["passed"])

    def test_html_image_and_link(self):
        self.assertFalse(linter.validate(self.complete('<img src="no.png"><a href="#missing">Go</a>'))["passed"])

    def test_reference_links(self):
        self.assertTrue(linter.validate(self.complete("[Terms][terms]\n\n[terms]: LICENSE\n"))["passed"])
        self.assertFalse(linter.validate(self.complete("[Terms][missing]\n"))["passed"])

    def test_external_urls_not_contacted(self):
        self.assertTrue(linter.validate(self.complete("[Remote](https://invalid.example/not-tested)"))["passed"])

    def test_dangerous_link_scheme(self):
        self.assertFalse(linter.validate(self.complete('<a href="javascript:alert(1)">Go</a>'))["passed"])

    def test_cli_end_to_end(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "create_skill_candidate.py"),
                                 "--name", "demo", "--out", str(self.candidate), "--languages", "en,zh-Hant"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate_readme.py"),
                                 str(self.candidate / "README.md"), "--json"], capture_output=True, text=True)
        self.assertTrue(json.loads(result.stdout)["passed"])
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate_readme.py"),
                                 str(self.candidate / "README.md"), "--strict", "--json"], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)

    def test_bad_cli_input_creates_nothing(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "create_skill_candidate.py"),
                                 "--name", "demo", "--out", str(self.candidate), "--languages", "bad"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertFalse(self.candidate.exists())

    def test_invalid_readme_cli_exit(self):
        result = subprocess.run([sys.executable, str(SCRIPTS / "validate_readme.py"), str(self.root / "none")],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)

    def test_unicode_combining_marks_in_anchor(self):
        self.assertTrue(linter.validate(self.complete("## हिन्दी\nText\n[Go](#हिन्दी)"))["passed"])

    def test_literal_brackets_in_title(self):
        self.assertTrue(linter.validate(self.draft(title="Read [input](file) & output"))["passed"])

    def test_help_commands(self):
        for script in ("create_skill_candidate.py", "validate_readme.py"):
            result = subprocess.run([sys.executable, str(SCRIPTS / script), "--help"], capture_output=True)
            self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
