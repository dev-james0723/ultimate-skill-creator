#!/usr/bin/env python3
"""Offline README lint for the Ultimate Skill Creator house convention.

Checks the documented Markdown subset, not behavior, external URLs, or security.
Exit status: 0 passed, 1 findings, 2 invalid invocation/input.
"""

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit

SPEC_PATH = Path(__file__).resolve().parents[1] / "assets" / "readme-spec.json"


def outside_fences(text: str) -> str:
    """Hide fenced contents while retaining a marker for non-empty code sections."""
    lines, fence = [], None
    for line in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if fence:
            if match and match[1][0] == fence[0] and len(match[1]) >= len(fence) and not match[2].strip():
                fence = None
            lines.append("")
        elif match:
            fence = match[1]
            lines.append("[code block]")
        else:
            lines.append(line)
    return "\n".join(lines)


def slug(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value).strip().lower()
    value = "".join(c for c in value if c.isalnum() or c.isspace()
                    or c in "-_" or unicodedata.category(c).startswith("M"))
    return value.replace(" ", "-")


class HTMLLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.anchors: list[str] = []
        self.targets: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        data = dict(attrs)
        for key in ("id", "name"):
            if data.get(key):
                self.anchors.append(data[key])
        for key in ("href", "src"):
            if data.get(key):
                self.targets.append(data[key])


def anchors(text: str) -> set[str]:
    visible = outside_fences(text)
    parser = HTMLLinks()
    parser.feed(visible)
    result = set(parser.anchors)
    used: Counter[str] = Counter()
    for match in re.finditer(r"^ {0,3}#{1,6}\s+(.+?)(?:\s+#+)?\s*$", visible, re.M):
        base = slug(match[1])
        candidate = base
        while candidate in result:
            used[base] += 1
            candidate = f"{base}-{used[base]}"
        result.add(candidate)
    return result


def link_targets(text: str) -> tuple[list[str], list[str]]:
    visible = outside_fences(text)
    visible = re.sub(r"(`+).*?\1", "", visible)
    visible = visible.replace(r"\[", " ").replace(r"\]", " ")
    parser = HTMLLinks()
    parser.feed(visible)
    targets = list(parser.targets)
    definitions = {}
    for match in re.finditer(r'^ {0,3}\[([^\]]+)\]:\s*(?:<([^>]+)>|(\S+))', visible, re.M):
        definitions[match[1].casefold()] = match[2] or match[3]
    targets.extend(definitions.values())
    for match in re.finditer(r'(?<!!)\[[^\]\n]+\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+"[^"]*")?\s*\)|!\[[^\]\n]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+"[^"]*")?\s*\)', visible):
        targets.append(next(group for group in match.groups() if group is not None))
    errors = []
    for match in re.finditer(r"\[([^\]\n]+)\]\[([^\]\n]*)\]", visible):
        label = (match[2] or match[1]).casefold()
        if label not in definitions:
            errors.append(f"undefined reference link: {label}")
    return targets, errors


def validate(readme: Path, strict: bool = False, root: Path | None = None) -> dict:
    readme = readme.resolve()
    root = (root or readme.parent).resolve()
    if not readme.is_relative_to(root):
        raise ValueError("README must be inside --root")
    text = readme.read_text(encoding="utf-8")
    visible = outside_fences(text)
    spec = json.loads(SPEC_PATH.read_text(encoding="utf-8"))
    errors, warnings = [], []
    headings = list(re.finditer(r"^ {0,3}(#{1,6})\s+(.+?)(?:\s+#+)?\s*$", visible, re.M))
    titles = [h for h in headings if h[1] == "#"]
    if len(titles) != 1:
        errors.append("use exactly one Markdown H1 title outside code fences")
    elif not re.sub(r"<[^>]+>", "", visible[titles[0].end():headings[headings.index(titles[0]) + 1].start()
                      if headings.index(titles[0]) + 1 < len(headings) else len(visible)]).strip():
        errors.append("add a purpose sentence below the title")
    for section in spec["sections"]:
        names = {n.casefold() for n in [section["heading"], *section["aliases"]]}
        hits = [(i, h) for i, h in enumerate(headings) if len(h[1]) in (2, 3) and h[2].casefold() in names]
        if not hits:
            errors.append(f'missing section: {section["heading"]}')
            continue
        i, match = hits[0]
        end = next((h.start() for h in headings[i + 1:] if len(h[1]) <= len(match[1])), len(visible))
        if not visible[match.end():end].strip():
            errors.append(f'empty section: {section["heading"]}')
    if re.search(r"\b(?:TODO|TBD|FIXME)\b|\{\{[^}]+\}\}|^>\s*DRAFT:", text, re.M):
        (errors if strict else warnings).append("unresolved draft markers/placeholders; replace before publication")
    parser = HTMLLinks()
    parser.feed(visible)
    for name, count in Counter(parser.anchors).items():
        if count > 1:
            errors.append(f"duplicate explicit anchor: {name}")
    targets, reference_errors = link_targets(text)
    errors.extend(reference_errors)
    for target in dict.fromkeys(targets):
        parsed = urlsplit(target)
        if parsed.scheme in ("http", "https", "mailto") or target.startswith("//"):
            continue
        if parsed.scheme:
            errors.append(f"unsupported link scheme: {target}")
            continue
        path = (readme.parent / unquote(parsed.path)).resolve() if parsed.path else readme
        if not path.is_relative_to(root):
            errors.append(f"local link escapes repository: {target}")
        elif not path.exists():
            errors.append(f"missing local target: {target}")
        elif parsed.fragment and path.is_file() and path.suffix.lower() == ".md":
            if unquote(parsed.fragment) not in anchors(path.read_text(encoding="utf-8")):
                errors.append(f"missing local anchor: {target}")
    return {"spec_version": spec["version"], "passed": not errors,
            "errors": errors, "warnings": warnings,
            "scope": "README structure, draft markers, and supported local links only; external URLs and skill behavior are not tested"}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path)
    parser.add_argument("--root", type=Path, help="Repository boundary; defaults to README directory")
    parser.add_argument("--strict", action="store_true", help="Fail unresolved draft markers")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable report")
    args = parser.parse_args(argv)
    try:
        report = validate(args.readme, args.strict, args.root)
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print("PASS" if report["passed"] else "FAIL")
        for category in ("errors", "warnings"):
            for message in report[category]:
                print(f"{category}: {message}")
        print(report["scope"])
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
