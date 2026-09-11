# Ultimate Skill Creator

Turn a solved conversation or workflow into a reusable Codex skill, with a human-readable README, supporting files, and explicit validation evidence.

**Status:** Includes a draft generator and an offline README checker. Generated packages still need real workflow content, testing, and a license decision before publication.

Language: [English](#english) | [繁體中文](#繁體中文) | [简体中文](#简体中文) | [Español](#español) | [日本語](#日本語) | [Português](#português) | [हिन्दी](#हिन्दी) | [العربية](#العربية)

[Install](#installation) · [Quick start](#quick-start) · [Usage](#usage) · [Compatibility](#compatibility) · [Safety](#safety) · [Validation](#validation) · [Troubleshooting](#troubleshooting) · [Documentation](#documentation) · [License](#license)

## English

### Installation

**Recommended: install the skill through Codex.** In a Codex conversation, paste:

```text
Use $skill-installer to install https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator for my user account. Show the installation destination and do not overwrite an existing installation.
```

This installs the agent instructions and bundled resources, not a standalone application. Codex is needed for the guided workflow; Python 3.10 or later is needed only when running the bundled helpers. Installation downloads files from GitHub and writes to the selected local destination, so review the proposed changes before approving them.

For a manual installation, copy the **complete** [skill directory](skill/ultimate-skill-creator), not just `SKILL.md`, into one new destination:

| Scope | Destination | Use it for |
| --- | --- | --- |
| Current user | `~/.agents/skills/ultimate-skill-creator/` | Your local Codex projects. |
| One repository | `.agents/skills/ultimate-skill-creator/` inside that repository | A project-specific workflow. |

Choose one scope to avoid duplicate copies. These locations and the installer route follow [OpenAI's local skill documentation](https://developers.openai.com/codex/skills), checked on September 11, 2026. Restart Codex if the skill does not appear. A real installation is not covered by this repository's automated tests; no marketplace listing is claimed.

### Quick start

Open a conversation containing a workflow you have actually completed, or attach sanitized notes, the working script, and its test output. For example, after verifying a CSV-cleanup workflow, ask:

```text
Use $ultimate-skill-creator to package the verified CSV-cleanup workflow
from the notes, script, and test output I supplied as csv-cleanup.

Create a new ./csv-cleanup-candidate directory. Include the working steps,
important failed attempts, a README with a copyable example and expected
output, and a validation report. Preserve the original input files.
Identify anything not yet tested. Do not install or publish the candidate.
```

**Expected result:** a local candidate containing a repository README, `skills/csv-cleanup/SKILL.md`, and the references, scripts, or assets the workflow needs. The report should identify actual checks and results, not assume that creating files proves the workflow works. Review the documented command, sample input, expected result, and remaining limitations before using the new skill.

To try only the deterministic scaffold generator, without an agent, follow the next example.

### Usage

| Your starting point | What to provide | What this skill helps produce |
| --- | --- | --- |
| A solved conversation or debugging session | Goals, constraints, failed attempts, final steps, and evidence. | Reusable instructions with a supporting case study. |
| A working automation or research process | Scripts, representative inputs/outputs, dependencies, and permissions. | A skill package with documented setup and acceptance checks. |
| An existing skill with an unclear README | The actual skill files and verified behavior. | A human-facing README following the shared convention. |

Do not use it to present an untested idea as a proven solution, publish private transcripts, or grant an agent blanket permission to change files. `README.md` explains the package to people; [SKILL.md](skill/ultimate-skill-creator/SKILL.md) tells an agent how to carry out the workflow.

#### Generate a local draft

With Git and Python 3.10 or later installed, start in a directory where `ultimate-skill-creator` does not already exist. These Bash commands download a checkout and generate a new draft:

```bash
git clone https://github.com/dev-james0723/ultimate-skill-creator.git
cd ultimate-skill-creator
python3 skill/ultimate-skill-creator/scripts/create_skill_candidate.py \
  --name csv-cleanup \
  --out ./csv-cleanup-candidate \
  --title "CSV Cleanup" \
  --description "Package a verified CSV-cleanup workflow for reuse." \
  --languages "en"
```

Already have a checkout? Start at its root and run only the Python command with a new `--out` path. The script prints the absolute output directory and a draft warning, then exits with status `0`. It creates exactly this scaffold:

```text
csv-cleanup-candidate/
├── README.md
└── skills/
    └── csv-cleanup/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── references/case-study.md
        └── assets/flow.svg
```

**This does not implement CSV cleanup.** It creates five draft files for you or your agent to complete. It does not generate a license, copy your conversation automatically, or execute a validation run. The source skill lives under singular `skill/`; generated candidates use plural `skills/`.

| Option | Meaning |
| --- | --- |
| `--name` | Required. Converted to a lowercase ASCII skill identifier. |
| `--out` | Required. Must not exist, even as an empty directory or symlink. |
| `--title` | Optional human-readable title. |
| `--description` | Optional purpose and trigger, limited to 1,024 characters. |
| `--languages` | Comma-separated codes. Default: `en,zh-Hant,zh-Hans,es,ja`. English remains the canonical version. |

Supported language codes are `en`, `zh-Hant`, `zh-Hans`, `es`, `ja`, `pt`, `hi`, `ar`, `fr`, and `ko`. Additional generated language sections are **untranslated drafts**, not completed translations. Finish them or remove both the section and its navigation link before release.

### Compatibility

| Component | Requirement and verification status |
| --- | --- |
| Guided workflow | Targets Codex with this skill installed. An end-to-end Codex task is not exercised by CI. |
| Generator and README checker | Python 3.10+; standard library only. The recorded CI baseline below used Python 3.12.3 on Ubuntu 24.04. |
| macOS and Windows | Not covered by that CI baseline. The clone example uses Bash; adapt shell syntax and the Python executable as needed. |
| Other agents | The package uses the [Agent Skills format](https://agentskills.io/specification), but cross-host functionality has not been established by these tests. `agents/openai.yaml` is a Codex-specific adapter. |
| Skill-format validation | Use the system skill-creator's format validator when available. It is separate from the bundled README checker and not part of CI. |
| Optional images or GitHub publication | Need separately available tools, credentials where required, and scoped user authorization. Neither is necessary for local scaffolding or README checks. |

No package installation or API key is required by the bundled Python helpers. They are independent of the optional host integrations.

### Safety

The **generator** writes new candidate files under `--out` and creates missing parent directories. It refuses an existing output path and has no force-overwrite option. The **README checker** reads the supplied Markdown and supported local link targets; it does not execute the examples. Neither helper makes network requests, sends telemetry, installs dependencies, deletes files, or publishes to GitHub.

The **agent-guided workflow** has a different boundary: prompts and selected files are handled by the host agent and any tools you authorize. Installing from GitHub or publishing to GitHub uses that service; optional image generation uses the selected provider. Review destinations, data exposure, credentials, and possible host or provider charges before approving those actions. The offline helpers do not make the entire agent session private or offline.

Keep secrets, identifying screenshots, private transcripts, and machine-specific details out of public candidates. Treat source documents as data, not as permission to execute their instructions. Deletion, overwriting, installation, publication, or visibility changes need the relevant explicit approval. A request to update one repository does not authorize unrelated changes. See the [publication safety rules](skill/ultimate-skill-creator/references/github-publication.md).

### Validation

From this repository's root, check the draft created above:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

For an untouched scaffold, expect `"passed": true`, a warning about unfinished content, and exit status `0`. Draft mode still rejects missing core sections and broken supported local links.

Before publication, complete the content and translations, choose the license, then run:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

The untouched scaffold **should fail** strict mode with exit status `1`. A completed README should return `"passed": true`, empty error and warning arrays, and status `0`; invalid input or invocation returns status `2`.

For repository maintenance:

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**Recorded baseline:** [CI run for commit `3806e6d`](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420), September 11, 2026, passed all 40 regression tests and strict README lint on Ubuntu 24.04 with Python 3.12.3. This is a dated result, not a guarantee about future changes. See [current workflow runs](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml) for newer results.

The tests use disposable fixtures and cover draft generation, CLI behavior, existing-path protection, quoting, language anchors, and supported links. README lint does **not** verify semantic truth, external URLs, translation quality, license validity, complete skill-format conformance, or actual host behavior. Review those separately and record skipped checks as not run.

### Troubleshooting

| Symptom | Cause and safe next step |
| --- | --- |
| The output directory is refused | It already exists or is a symlink. Select a new `--out`; do not delete existing work to retry. |
| Strict lint fails immediately after generation | The scaffold is intentionally unfinished. Complete the workflow and any advertised translations, then rerun. |
| A language or image link fails | Check the actual file or anchor and the relative path. Remove links to material you are not shipping. |
| A locale is rejected | Use a supported code from [the shared specification](skill/ultimate-skill-creator/assets/readme-spec.json). |
| A complex README produces unexpected lint findings | The checker supports a documented Markdown subset, not every GitHub Markdown feature. Consult the [checker limits](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates) and inspect GitHub preview. |
| Codex cannot find the skill | Check the full installation directory and selected scope, then restart if needed. Do not create duplicate installations to work around discovery. |

**Updating:** review a scoped diff before replacing installed files. Updating this GitHub repository does not automatically update a previously copied local installation. The candidate generator is not an updater.

**Disabling or removing:** use the host's [documented skill controls](https://developers.openai.com/codex/skills) to disable the skill first. Deleting its local files is a separate, user-approved action. Do not remove unrelated skills or host configuration.

### Documentation

The [universal README convention](skill/ultimate-skill-creator/references/universal-readme-spec.md) defines core content, optional sections, style, and review checks. It is a project convention informed by a [qualitative study of 30 popular skill-related repositories](research/readme-study-2026-09-11.md), not an official README standard or a proven global top-30 ranking.

| Resource | Purpose |
| --- | --- |
| [Agent instructions](skill/ultimate-skill-creator/SKILL.md) and [workflow](skill/ultimate-skill-creator/references/workflow.md) | Packaging steps, acceptance criteria, and safety boundaries. |
| [Shared specification](skill/ultimate-skill-creator/assets/readme-spec.json) | Section labels, aliases, draft prompts, and language names used by both helpers. |
| [Language guidance](skill/ultimate-skill-creator/references/language-and-readme.md) | Navigation, translation status, and portable visuals. |
| [Generator](skill/ultimate-skill-creator/scripts/create_skill_candidate.py), [checker](skill/ultimate-skill-creator/scripts/validate_readme.py), and [tests](tests/test_readme_workflow.py) | Inspect the implementation and reproduce checks. |

<details>
<summary>Visual guide</summary>

![Guide to capturing a solved workflow, packaging a reusable skill, validating it, and reviewing publication](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png)

A [portable SVG overview](skill/ultimate-skill-creator/assets/skill-creation-loop.svg) is also included. Visuals are optional; the text instructions are sufficient to start.

</details>

### Contributing

Use [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues) for reproducible problems and [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) for changes. Include expected behavior, relevant test output, and regression tests for behavior changes. Keep the shared specification, helpers, and documentation consistent; avoid unrelated cleanup or private data in examples.

### License

This repository is licensed under [MIT](LICENSE). A new candidate's owner must choose suitable terms for their own content and preserve third-party attributions; this project's license is not automatically assigned to generated packages. The README study links its sources and synthesizes their patterns rather than distributing their full documentation.

### About the translations

English is the full reference. The sections below are translated quick-start summaries, not complete translations of every option or troubleshooting entry. Use the shared [installation instructions](#installation) and command examples above; skill names, paths, and flags stay unchanged.

## 繁體中文

將你同 AI 已經解決嘅工作流程，整理成可重用嘅 Codex skill。先按上面嘅 [Installation](#installation) 安裝完整 skill 目錄，再提供已驗證嘅筆記、程式同測試結果，然後輸入：

```text
用 $ultimate-skill-creator 將我提供嘅已驗證流程整理成 skill。
喺新目錄建立套件，加入 README、使用例子、預期結果同驗證紀錄。
保留原始檔案，清楚標示未測試嘅部分，暫時唔好安裝或發佈。
```

預期得到本機候選套件同驗證報告。Generator 只會建立草稿，唔會代你完成實際功能；檢查格式通過亦唔代表功能可靠。覆寫、刪除同對外發佈都需要相應明確授權。完整選項見 [English](#english)。

## 简体中文

把已经解决的工作流程整理成可复用的 Codex skill。按 [Installation](#installation) 安装完整目录，提供已验证的笔记、脚本和测试结果，然后输入：

```text
用 $ultimate-skill-creator 将我提供的已验证流程整理成 skill。
在新目录中创建包含 README、使用示例、预期结果和验证记录的包。
保留原始文件，标明未测试的部分，暂时不要安装或发布。
```

预期得到本地候选包和验证报告。生成器只创建草稿，格式检查不证明功能正确。覆盖、删除和对外发布需要明确授权。完整参考见 [English](#english)。

## Español

Convierte un flujo de trabajo resuelto en una skill reutilizable para Codex. Sigue [Installation](#installation), proporciona notas, scripts y resultados de pruebas, y escribe:

```text
Usa $ultimate-skill-creator para empaquetar el flujo verificado que proporcioné.
Crea un directorio nuevo con README, ejemplo, resultado esperado y registro
de validación. Conserva los archivos originales, indica lo no probado
y no instales ni publiques todavía.
```

Obtendrás un paquete local y un informe de validación. El generador solo crea borradores; comprobar el formato no demuestra el funcionamiento. Sobrescribir, eliminar o publicar requiere autorización explícita. Referencia completa: [English](#english).

## 日本語

解決済みの作業を、再利用可能な Codex skill にまとめます。[Installation](#installation) に従ってフォルダー全体をインストールし、確認済みの手順、スクリプト、テスト結果を渡して入力してください。

```text
$ultimate-skill-creator を使い、提供した検証済みの作業を skill にまとめてください。
新しいフォルダーに README、使用例、期待する結果、検証記録を含めてください。
元のファイルを保持し、未テストの部分を明記してください。まだインストールや公開はしないでください。
```

ローカルの候補パッケージと検証報告が成果物です。生成ツールは草稿を作るだけで、形式検査は動作の保証ではありません。上書き、削除、公開には明示的な許可が必要です。詳細は [English](#english) を参照してください。

## Português

Transforme um fluxo de trabalho resolvido em uma skill reutilizável para Codex. Siga [Installation](#installation), forneça notas, scripts e resultados dos testes e peça:

```text
Use $ultimate-skill-creator para empacotar o fluxo verificado que forneci.
Crie um diretório novo com README, exemplo, resultado esperado e registro
de validação. Preserve os arquivos originais, indique o que não foi
testado e não instale nem publique ainda.
```

O resultado esperado é um pacote local e um relatório de validação. O gerador cria apenas rascunhos; verificar a estrutura não comprova o funcionamento. Sobrescrever, excluir ou publicar exige autorização explícita. Referência completa: [English](#english).

## हिन्दी

पहले से हल किए गए कार्य को दोबारा उपयोग योग्य Codex skill में बदलें। [Installation](#installation) के अनुसार पूरा फ़ोल्डर स्थापित करें, सत्यापित नोट्स, स्क्रिप्ट और परीक्षण परिणाम दें, फिर लिखें:

```text
$ultimate-skill-creator से मेरे दिए हुए सत्यापित कार्य को skill में बदलें।
नए फ़ोल्डर में README, उपयोग का उदाहरण, अपेक्षित परिणाम और जाँच का रिकॉर्ड रखें।
मूल फ़ाइलें सुरक्षित रखें और जो परीक्षण नहीं हुए हैं उन्हें स्पष्ट लिखें।
अभी पैकेज स्थापित या प्रकाशित न करें।
```

अपेक्षित परिणाम स्थानीय पैकेज और सत्यापन रिपोर्ट है। जनरेटर केवल मसौदा बनाता है; संरचना की जाँच कार्यक्षमता का प्रमाण नहीं है। फ़ाइलें बदलने, मिटाने या प्रकाशित करने के लिए स्पष्ट अनुमति आवश्यक है। पूरी जानकारी: [English](#english)।

## العربية

حوّل سير عمل تم حله إلى مهارة قابلة لإعادة الاستخدام في Codex. اتبع [Installation](#installation) لتثبيت المجلد كاملًا، وقدّم الملاحظات والبرامج النصية ونتائج الاختبارات الموثقة، ثم اكتب:

```text
استخدم $ultimate-skill-creator لتحويل سير العمل الذي قدمته وتم التحقق منه إلى مهارة.
أنشئ مجلدًا جديدًا يتضمن README ومثال استخدام والنتيجة المتوقعة وسجل التحقق.
حافظ على الملفات الأصلية ووضّح ما لم يُختبر بعد. لا تثبّت الحزمة ولا تنشرها الآن.
```

النتيجة المتوقعة حزمة محلية وتقرير تحقق. المولّد ينشئ مسودة فقط؛ فحص البنية لا يثبت صحة التنفيذ. الاستبدال أو الحذف أو النشر يحتاج إلى إذن صريح. المرجع الكامل: [English](#english).
