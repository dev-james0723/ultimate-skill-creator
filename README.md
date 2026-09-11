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

All eight language sections cover the same installation, usage, options, safety, validation, troubleshooting, documentation, contribution, and licensing information. English is the maintenance source; commands, paths, flags, and result tokens remain unchanged. Supporting reference files and the shared visual assets remain in their original language.

When changing a command, option, safety rule, or limitation, update all eight sections in the same change. The translated guides below are complete guides, not quick-start summaries; each has its own section navigation.

## 繁體中文

將已解決的對話或工作流程整理成可重用的 Codex skill，附上易讀的 README、所需檔案及明確的驗證紀錄。

**目前狀態：**提供草稿產生器與離線 README 檢查器。產生的套件仍需補齊實際流程、完成測試並決定授權條款，才適合發佈。本節是完整指南；英文版作為維護基準，指令、路徑及參數保持原樣。連結的參考文件與共用圖片保留原本語言。

[安裝](#zh-hant-installation) · [快速開始](#zh-hant-quick-start) · [使用方式](#zh-hant-usage) · [相容性](#zh-hant-compatibility) · [安全](#zh-hant-safety) · [驗證](#zh-hant-validation) · [疑難排解](#zh-hant-troubleshooting) · [文件](#zh-hant-documentation) · [參與貢獻](#zh-hant-contributing) · [授權](#zh-hant-license)

<a id="zh-hant-installation"></a>
### 安裝

**建議透過 Codex 安裝。**在 Codex 對話中貼上：

```text
使用 $skill-installer，從 https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator 為目前使用者安裝此 skill。顯示安裝位置，不要覆寫現有安裝。
```

安裝的是 agent 指令及隨附資源，不是獨立應用程式。由 agent 引導的流程需要 Codex；執行隨附工具時才需要 Python 3.10 或以上版本。安裝會從 GitHub 下載檔案並寫入選定的本機位置，請先檢查預計變更，再批准執行。

手動安裝時，請將**完整的 [skill 目錄](skill/ultimate-skill-creator)**複製到一個尚未存在的位置，不要只複製 `SKILL.md`：

| 範圍 | 位置 | 用途 |
| --- | --- | --- |
| 目前使用者 | `~/.agents/skills/ultimate-skill-creator/` | 在自己的本機 Codex 專案使用。 |
| 單一儲存庫 | 該儲存庫內的 `.agents/skills/ultimate-skill-creator/` | 限於特定專案的流程。 |

選擇一個範圍，避免重複安裝。這些位置與安裝方式依據 [OpenAI 本機 skill 文件](https://developers.openai.com/codex/skills)，核對日期為 2026 年 9 月 11 日。若 skill 沒有出現，請重新啟動 Codex。本儲存庫的自動測試不包含真實安裝；亦未聲稱已上架任何 marketplace。

<a id="zh-hant-quick-start"></a>
### 快速開始

開啟包含已完成工作流程的對話，或附上已移除敏感資料的筆記、可正常運作的程式及測試輸出。例如，驗證 CSV 清理流程後，可輸入：

```text
使用 $ultimate-skill-creator，根據我提供的筆記、程式和測試輸出，
將已驗證的 CSV 清理流程整理成名為 csv-cleanup 的 skill。

建立新的 ./csv-cleanup-candidate 目錄。加入有效步驟、重要失敗嘗試、
包含可複製範例及預期輸出的 README，以及驗證報告。保留原始輸入檔案。
標明尚未測試的部分。不要安裝或發佈候選套件。
```

**預期結果：**本機候選套件包含儲存庫 README、`skills/csv-cleanup/SKILL.md`，以及流程所需的參考資料、程式或素材。報告須列出真正執行的檢查與結果，不能把「已建立檔案」當成「流程已成功」。使用新 skill 前，請核對文件中的指令、範例輸入、預期結果及剩餘限制。

只想試用不需要 agent 的固定模板產生器，可使用下一個範例。

<a id="zh-hant-usage"></a>
### 使用方式

| 目前已有的資料 | 需要提供 | 協助產出的內容 |
| --- | --- | --- |
| 已解決的對話或除錯紀錄 | 目標、限制、失敗嘗試、最終步驟與證據。 | 可重用的指令與案例說明。 |
| 已正常運作的自動化或研究流程 | 程式、代表性輸入與輸出、依賴項目與權限。 | 具備設定說明及驗收檢查的 skill 套件。 |
| README 不清楚的現有 skill | 實際 skill 檔案及已驗證的行為。 | 符合共用規格、供人閱讀的 README。 |

不要用它將未測試的構想包裝成已證實的解決方案、公開私人對話，或授予 agent 任意更動檔案的權限。`README.md` 向人解釋套件；[SKILL.md](skill/ultimate-skill-creator/SKILL.md) 告訴 agent 如何執行流程。

#### 產生本機草稿

先安裝 Git 與 Python 3.10 或以上版本，並在尚未包含 `ultimate-skill-creator` 的目錄開始。以下 Bash 指令會下載儲存庫副本並產生草稿：

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

已有儲存庫副本時，從根目錄執行 Python 指令即可，並為 `--out` 選擇新路徑。程式會印出輸出目錄的絕對路徑及草稿警告，然後以狀態碼 `0` 結束。產生的結構如下：

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

**這不會實作 CSV 清理功能。**它只建立五個草稿檔案，供你或 agent 完成；不會產生授權檔案、自動複製對話或自行執行驗證。來源 skill 使用單數 `skill/` 目錄，產生的候選套件使用複數 `skills/`。

| 選項 | 說明 |
| --- | --- |
| `--name` | 必填；轉換成小寫 ASCII skill 識別名稱。 |
| `--out` | 必填；路徑不可已存在，包括空目錄或符號連結。 |
| `--title` | 選填；供人閱讀的標題。 |
| `--description` | 選填；用途及觸發條件，最多 1,024 個字元。 |
| `--languages` | 以逗號分隔的語言代碼；預設 `en,zh-Hant,zh-Hans,es,ja`，英文始終是基準版本。 |

支援的代碼為 `en`、`zh-Hant`、`zh-Hans`、`es`、`ja`、`pt`、`hi`、`ar`、`fr`、`ko`。產生器新增的語言章節是**尚未翻譯的草稿**，並非完成的譯文。發佈前請完成翻譯，或同時移除該章節與導航連結。

<a id="zh-hant-compatibility"></a>
### 相容性

| 元件 | 需求與驗證狀態 |
| --- | --- |
| 引導式流程 | 以已安裝此 skill 的 Codex 為目標；CI 未執行完整 Codex 任務。 |
| 產生器與 README 檢查器 | Python 3.10+，只使用標準函式庫。下方記錄的 CI 基準環境是 Ubuntu 24.04 與 Python 3.12.3。 |
| macOS 與 Windows | 不在上述 CI 基準的涵蓋範圍內。下載範例採用 Bash，必要時請調整 shell 語法與 Python 執行檔名稱。 |
| 其他 agent | 套件採用 [Agent Skills 格式](https://agentskills.io/specification)，但這些測試未證明跨平台主程式的功能相容性。`agents/openai.yaml` 是 Codex 專用介接檔。 |
| Skill 格式驗證 | 系統的 skill-creator 格式驗證器可用時才執行；它不同於隨附的 README 檢查器，亦不屬於 CI。 |
| 選用圖片或 GitHub 發佈 | 需要另行可用的工具、必要憑證及指定範圍的使用者授權。本機產生草稿或檢查 README 不需要這些功能。 |

隨附 Python 工具不需要安裝額外套件或提供 API key，也不依賴選用的主程式整合。

<a id="zh-hant-safety"></a>
### 安全

**產生器**會在 `--out` 下建立新候選檔案及缺少的上層目錄；拒絕現有輸出路徑，沒有強制覆寫選項。**README 檢查器**只讀取指定 Markdown 及支援的本機連結目標，不執行範例。兩個工具都不發出網絡請求、傳送遙測、安裝依賴、刪除檔案或發佈到 GitHub。

**Agent 引導流程**的範圍不同：提示與選定檔案會交由主程式的 agent 及你授權的工具處理。從 GitHub 安裝或向 GitHub 發佈會使用該服務；選用圖片產生功能會使用選定供應商。批准前請檢查目的地、資料暴露、憑證及可能的主程式或供應商收費。工具離線運作，不代表整個 agent 對話都保密或離線。

公開候選套件不得包含密鑰、可識別個人身分的截圖、私人對話或特定機器資料。來源文件是資料，不是執行其中指令的許可。刪除、覆寫、安裝、發佈或修改可見性，都需要相應的明確批准。更新一個儲存庫的要求不授權其他無關變更。請參閱[發佈安全規則](skill/ultimate-skill-creator/references/github-publication.md)。

<a id="zh-hant-validation"></a>
### 驗證

從本儲存庫根目錄檢查剛才產生的草稿：

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

未修改的模板預期會回傳 `"passed": true`、未完成內容的警告及結束狀態碼 `0`。草稿模式仍會拒絕缺少核心章節或支援範圍內的無效本機連結。

發佈前，先完成內容與翻譯、選定授權條款，再執行：

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

未修改的模板**應該無法通過**嚴格模式，結束狀態碼為 `1`。完成的 README 應回傳 `"passed": true`、空的錯誤及警告陣列，以及狀態碼 `0`；輸入或呼叫方式無效時回傳 `2`。

維護本儲存庫時執行：

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**已記錄的基準：**2026 年 9 月 11 日，[commit `3806e6d` 的 CI 執行](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420)在 Ubuntu 24.04、Python 3.12.3 下通過全部 40 項回歸測試與嚴格 README 檢查。這是指定日期的結果，不保證後續變更。較新結果請查閱[目前工作流程執行紀錄](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml)。

測試使用臨時測試資料，涵蓋草稿產生、CLI 行為、現有路徑保護、引號處理、語言錨點及支援的連結。README 檢查**不會**驗證內容真實性、外部網址、翻譯品質、授權有效性、完整 skill 格式相容性或實際主程式行為。請分別檢查，未執行的檢查須標明未執行。

<a id="zh-hant-troubleshooting"></a>
### 疑難排解

| 症狀 | 原因及安全處理方式 |
| --- | --- |
| 輸出目錄被拒絕 | 目錄已存在或是符號連結。選擇新的 `--out`；不要為了重試而刪除現有資料。 |
| 產生後立即無法通過嚴格檢查 | 模板本來就是未完成內容。補齊流程及列出的翻譯，再重新檢查。 |
| 語言或圖片連結無效 | 核對實際檔案、錨點及相對路徑；移除不會隨套件提供的內容連結。 |
| 語言代碼被拒絕 | 使用[共用規格](skill/ultimate-skill-creator/assets/readme-spec.json)支援的代碼。 |
| 複雜 README 出現意外檢查結果 | 檢查器僅支援已說明的 Markdown 子集，不支援所有 GitHub Markdown 功能。請查看[檢查器限制](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates)，並檢視 GitHub 預覽。 |
| Codex 找不到 skill | 核對完整安裝目錄與範圍，必要時重新啟動。不要以重複安裝繞過探索問題。 |

**更新：**替換已安裝檔案前，先檢查指定範圍的差異。更新 GitHub 儲存庫不會自動更新先前複製的本機安裝；候選套件產生器不是更新器。

**停用或移除：**先使用主程式[文件列出的 skill 控制功能](https://developers.openai.com/codex/skills)停用。刪除本機檔案是需要使用者批准的另一項操作；不要移除無關 skill 或主程式設定。

<a id="zh-hant-documentation"></a>
### 文件

[通用 README 規格](skill/ultimate-skill-creator/references/universal-readme-spec.md)定義核心內容、選用章節、文風及檢查要求。這是參考[30 個熱門 skill 相關儲存庫的質性研究](research/readme-study-2026-09-11.md)制定的專案規格，不是官方 README 標準，也不是已證實的全球前 30 名排名。

| 資源 | 用途 |
| --- | --- |
| [Agent 指令](skill/ultimate-skill-creator/SKILL.md)與[工作流程](skill/ultimate-skill-creator/references/workflow.md) | 打包步驟、驗收條件與安全界線。 |
| [共用規格](skill/ultimate-skill-creator/assets/readme-spec.json) | 兩個工具共用的章節名稱、別名、草稿提示與語言名稱。 |
| [語言指南](skill/ultimate-skill-creator/references/language-and-readme.md) | 導航、翻譯狀態及可攜式圖片。 |
| [產生器](skill/ultimate-skill-creator/scripts/create_skill_candidate.py)、[檢查器](skill/ultimate-skill-creator/scripts/validate_readme.py)與[測試](tests/test_readme_workflow.py) | 檢查實作及重現驗證。 |

共用的[圖解指南](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png)和[可攜式 SVG 概覽](skill/ultimate-skill-creator/assets/skill-creation-loop.svg)保留原本語言。圖片是選用項目，單靠文字指引即可開始。

<a id="zh-hant-contributing"></a>
### 參與貢獻

可重現的問題請提交至 [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues)，修改請使用 [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls)。附上預期行為、相關測試輸出，行為變更須有回歸測試。保持共用規格、工具及文件一致；不要加入無關清理或含私人資料的範例。更改指令、選項、安全規則或限制時，請在同一次修改中更新全部八種語言。

<a id="zh-hant-license"></a>
### 授權

本儲存庫採用 [MIT 授權](LICENSE)。新候選套件的擁有者須為自己的內容選擇適當條款，並保留第三方來源標示；產生的套件不會自動套用本專案授權。README 研究透過連結標示來源並歸納共通模式，不會散佈來源文件全文。

## 简体中文

将已解决的对话或工作流程整理成可复用的 Codex skill，附上易读的 README、所需文件和明确的验证记录。

**当前状态：**提供草稿生成器和离线 README 检查器。生成的包仍需补齐实际流程、完成测试并决定许可条款，才适合发布。本节是完整指南；英文版作为维护基准，命令、路径和参数保持原样。链接的参考文档和共用图片保留原本语言。

[安装](#zh-hans-installation) · [快速开始](#zh-hans-quick-start) · [使用方式](#zh-hans-usage) · [兼容性](#zh-hans-compatibility) · [安全](#zh-hans-safety) · [验证](#zh-hans-validation) · [故障排查](#zh-hans-troubleshooting) · [文档](#zh-hans-documentation) · [参与贡献](#zh-hans-contributing) · [许可证](#zh-hans-license)

<a id="zh-hans-installation"></a>
### 安装

**建议通过 Codex 安装。**在 Codex 对话中粘贴：

```text
使用 $skill-installer，从 https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator 为当前用户安装此 skill。显示安装位置，不要覆盖现有安装。
```

安装的是 agent 指令和随附资源，不是独立应用程序。由 agent 引导的流程需要 Codex；执行随附工具时才需要 Python 3.10 或更高版本。安装会从 GitHub 下载文件并写入选定的本地位置，请先检查预计变更，再批准执行。

手动安装时，请将**完整的 [skill 目录](skill/ultimate-skill-creator)**复制到一个尚不存在的位置，不要只复制 `SKILL.md`：

| 范围 | 位置 | 用途 |
| --- | --- | --- |
| 当前用户 | `~/.agents/skills/ultimate-skill-creator/` | 在自己的本地 Codex 项目中使用。 |
| 单一仓库 | 该仓库内的 `.agents/skills/ultimate-skill-creator/` | 限于特定项目的流程。 |

选择一个范围，避免重复安装。这些位置和安装方式依据 [OpenAI 本地 skill 文档](https://developers.openai.com/codex/skills)，核对日期为 2026 年 9 月 11 日。若 skill 没有出现，请重启 Codex。本仓库的自动测试不包含真实安装，也未声称已上架任何 marketplace。

<a id="zh-hans-quick-start"></a>
### 快速开始

打开包含已完成工作流程的对话，或附上已移除敏感信息的笔记、可正常运行的脚本及测试输出。例如，验证 CSV 清理流程后，可以输入：

```text
使用 $ultimate-skill-creator，根据我提供的笔记、脚本和测试输出，
将已验证的 CSV 清理流程整理成名为 csv-cleanup 的 skill。

创建新的 ./csv-cleanup-candidate 目录。加入有效步骤、重要失败尝试、
包含可复制示例及预期输出的 README，以及验证报告。保留原始输入文件。
标明尚未测试的部分。不要安装或发布候选包。
```

**预期结果：**本地候选包包含仓库 README、`skills/csv-cleanup/SKILL.md`，以及流程所需的参考资料、脚本或资源。报告须列出真正执行的检查和结果，不能把“已创建文件”当成“流程已成功”。使用新 skill 前，请核对文档中的命令、示例输入、预期结果和剩余限制。

只想试用不需要 agent 的固定模板生成器，可使用下一个示例。

<a id="zh-hans-usage"></a>
### 使用方式

| 目前已有的资料 | 需要提供 | 协助生成的内容 |
| --- | --- | --- |
| 已解决的对话或调试记录 | 目标、限制、失败尝试、最终步骤和证据。 | 可复用的指令及案例说明。 |
| 已正常运行的自动化或研究流程 | 脚本、代表性输入与输出、依赖项和权限。 | 具备配置说明和验收检查的 skill 包。 |
| README 不清楚的现有 skill | 实际 skill 文件及已验证的行为。 | 符合共用规范、供人阅读的 README。 |

不要用它将未测试的构想包装成已证实的解决方案、公开私人对话，或授予 agent 任意改动文件的权限。`README.md` 向人解释包的用途；[SKILL.md](skill/ultimate-skill-creator/SKILL.md) 告诉 agent 如何执行流程。

#### 生成本地草稿

先安装 Git 和 Python 3.10 或更高版本，并在尚未包含 `ultimate-skill-creator` 的目录开始。以下 Bash 命令会下载仓库副本并生成草稿：

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

已有仓库副本时，从根目录执行 Python 命令即可，并为 `--out` 选择新路径。脚本会打印输出目录的绝对路径及草稿警告，然后以状态码 `0` 结束。生成的结构如下：

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

**这不会实现 CSV 清理功能。**它只创建五个草稿文件，供你或 agent 完成；不会生成许可证文件、自动复制对话或自行执行验证。源 skill 使用单数 `skill/` 目录，生成的候选包使用复数 `skills/`。

| 选项 | 说明 |
| --- | --- |
| `--name` | 必填；转换成小写 ASCII skill 标识符。 |
| `--out` | 必填；路径不可已存在，包括空目录或符号链接。 |
| `--title` | 选填；供人阅读的标题。 |
| `--description` | 选填；用途和触发条件，最多 1,024 个字符。 |
| `--languages` | 以逗号分隔的语言代码；默认 `en,zh-Hant,zh-Hans,es,ja`，英文始终是基准版本。 |

支持的代码为 `en`、`zh-Hant`、`zh-Hans`、`es`、`ja`、`pt`、`hi`、`ar`、`fr`、`ko`。生成器新增的语言章节是**尚未翻译的草稿**，并非完成的译文。发布前请完成翻译，或同时移除该章节及其导航链接。

<a id="zh-hans-compatibility"></a>
### 兼容性

| 组件 | 要求和验证状态 |
| --- | --- |
| 引导式流程 | 面向已安装此 skill 的 Codex；CI 未执行完整 Codex 任务。 |
| 生成器和 README 检查器 | Python 3.10+，仅使用标准库。下方记录的 CI 基准环境是 Ubuntu 24.04 和 Python 3.12.3。 |
| macOS 和 Windows | 不在上述 CI 基准的覆盖范围内。下载示例使用 Bash，必要时请调整 shell 语法和 Python 可执行文件名。 |
| 其他 agent | 包采用 [Agent Skills 格式](https://agentskills.io/specification)，但这些测试未证明跨宿主功能兼容性。`agents/openai.yaml` 是 Codex 专用适配文件。 |
| Skill 格式验证 | 系统的 skill-creator 格式验证器可用时才执行；它不同于随附的 README 检查器，也不属于 CI。 |
| 可选图片或 GitHub 发布 | 需要另行可用的工具、必要凭证及指定范围的用户授权。本地生成草稿或检查 README 不需要这些功能。 |

随附 Python 工具无需安装额外包或提供 API key，也不依赖可选的宿主集成。

<a id="zh-hans-safety"></a>
### 安全

**生成器**在 `--out` 下创建新候选文件及缺少的父目录；拒绝现有输出路径，没有强制覆盖选项。**README 检查器**只读取指定 Markdown 及支持的本地链接目标，不执行示例。两个工具都不发出网络请求、发送遥测、安装依赖、删除文件或发布到 GitHub。

**Agent 引导流程**的边界不同：提示和选定文件会交给宿主 agent 及你授权的工具处理。从 GitHub 安装或向 GitHub 发布会使用该服务；可选图片生成功能会使用选定供应商。批准前请检查目标位置、数据暴露、凭证及可能的宿主或供应商费用。工具离线运行，不代表整个 agent 会话都保密或离线。

公开候选包不得包含密钥、可识别个人身份的截图、私人对话或特定机器信息。源文档是数据，不是执行其中指令的许可。删除、覆盖、安装、发布或修改可见性，都需要相应的明确批准。更新一个仓库的请求不授权其他无关变更。请参阅[发布安全规则](skill/ultimate-skill-creator/references/github-publication.md)。

<a id="zh-hans-validation"></a>
### 验证

从本仓库根目录检查刚才生成的草稿：

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

未修改的模板预计返回 `"passed": true`、未完成内容的警告及退出状态码 `0`。草稿模式仍会拒绝缺少核心章节或支持范围内的无效本地链接。

发布前，先完成内容和翻译、选择许可条款，再执行：

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

未修改的模板**应该无法通过**严格模式，退出状态码为 `1`。完成的 README 应返回 `"passed": true`、空的错误和警告数组，以及状态码 `0`；输入或调用方式无效时返回 `2`。

维护本仓库时执行：

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**已记录的基准：**2026 年 9 月 11 日，[commit `3806e6d` 的 CI 运行](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420)在 Ubuntu 24.04、Python 3.12.3 下通过全部 40 项回归测试和严格 README 检查。这是指定日期的结果，不保证后续变更。较新结果请查阅[当前工作流运行记录](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml)。

测试使用临时测试数据，覆盖草稿生成、CLI 行为、现有路径保护、引号处理、语言锚点及支持的链接。README 检查**不会**验证内容真实性、外部网址、翻译质量、许可证有效性、完整 skill 格式合规性或实际宿主行为。请分别检查，未执行的检查须明确标注。

<a id="zh-hans-troubleshooting"></a>
### 故障排查

| 症状 | 原因和安全处理方式 |
| --- | --- |
| 输出目录被拒绝 | 目录已存在或是符号链接。选择新的 `--out`；不要为了重试而删除现有数据。 |
| 生成后立即无法通过严格检查 | 模板本来就是未完成内容。补齐流程和列出的翻译，再重新检查。 |
| 语言或图片链接无效 | 核对实际文件、锚点及相对路径；移除不会随包提供的内容链接。 |
| 语言代码被拒绝 | 使用[共用规范](skill/ultimate-skill-creator/assets/readme-spec.json)支持的代码。 |
| 复杂 README 出现意外检查结果 | 检查器仅支持已说明的 Markdown 子集，不支持所有 GitHub Markdown 功能。请查看[检查器限制](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates)，并检查 GitHub 预览。 |
| Codex 找不到 skill | 核对完整安装目录和范围，必要时重启。不要用重复安装绕过发现问题。 |

**更新：**替换已安装文件前，先检查指定范围的差异。更新 GitHub 仓库不会自动更新先前复制的本地安装；候选包生成器不是更新器。

**停用或移除：**先使用宿主[文档列出的 skill 控制功能](https://developers.openai.com/codex/skills)停用。删除本地文件是需要用户批准的另一项操作；不要移除无关 skill 或宿主配置。

<a id="zh-hans-documentation"></a>
### 文档

[通用 README 规范](skill/ultimate-skill-creator/references/universal-readme-spec.md)定义核心内容、可选章节、文风及检查要求。这是参考[30 个热门 skill 相关仓库的定性研究](research/readme-study-2026-09-11.md)制定的项目规范，不是官方 README 标准，也不是已证实的全球前 30 名排名。

| 资源 | 用途 |
| --- | --- |
| [Agent 指令](skill/ultimate-skill-creator/SKILL.md)和[工作流程](skill/ultimate-skill-creator/references/workflow.md) | 打包步骤、验收条件和安全边界。 |
| [共用规范](skill/ultimate-skill-creator/assets/readme-spec.json) | 两个工具共用的章节名称、别名、草稿提示和语言名称。 |
| [语言指南](skill/ultimate-skill-creator/references/language-and-readme.md) | 导航、翻译状态及可移植的图片。 |
| [生成器](skill/ultimate-skill-creator/scripts/create_skill_candidate.py)、[检查器](skill/ultimate-skill-creator/scripts/validate_readme.py)和[测试](tests/test_readme_workflow.py) | 检查实现及复现验证。 |

共用的[图解指南](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png)和[可移植 SVG 概览](skill/ultimate-skill-creator/assets/skill-creation-loop.svg)保留原本语言。图片是可选项目，单靠文字指引即可开始。

<a id="zh-hans-contributing"></a>
### 参与贡献

可复现的问题请提交至 [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues)，修改请使用 [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls)。附上预期行为、相关测试输出，行为变更须有回归测试。保持共用规范、工具和文档一致；不要加入无关清理或含私人数据的示例。更改命令、选项、安全规则或限制时，请在同一次修改中更新全部八种语言。

<a id="zh-hans-license"></a>
### 许可证

本仓库采用 [MIT 许可证](LICENSE)。新候选包的所有者须为自己的内容选择适当条款，并保留第三方来源标注；生成的包不会自动采用本项目许可证。README 研究通过链接标注来源并归纳共通模式，不会分发源文档全文。

## Español

Convierte una conversación o un flujo de trabajo resuelto en una skill reutilizable para Codex, con un README legible, archivos de apoyo y evidencia explícita de validación.

**Estado:** incluye un generador de borradores y un comprobador de README sin conexión. Los paquetes generados todavía necesitan el contenido real del flujo, pruebas y una decisión sobre la licencia antes de publicarse. Esta sección es una guía completa. El inglés es la fuente de mantenimiento; los comandos, las rutas y las opciones no se traducen. Los documentos de referencia y las imágenes compartidas conservan su idioma original.

[Instalación](#es-installation) · [Inicio rápido](#es-quick-start) · [Uso](#es-usage) · [Compatibilidad](#es-compatibility) · [Seguridad](#es-safety) · [Validación](#es-validation) · [Solución de problemas](#es-troubleshooting) · [Documentación](#es-documentation) · [Contribuciones](#es-contributing) · [Licencia](#es-license)

<a id="es-installation"></a>
### Instalación

**Recomendado: instala la skill mediante Codex.** Pega esto en una conversación de Codex:

```text
Usa $skill-installer para instalar https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator para mi cuenta de usuario. Muestra el destino y no sobrescribas una instalación existente.
```

Se instalan instrucciones para el agente y los recursos incluidos, no una aplicación independiente. El flujo guiado necesita Codex; Python 3.10 o posterior solo es necesario para ejecutar las herramientas incluidas. La instalación descarga archivos de GitHub y escribe en el destino local elegido. Revisa los cambios propuestos antes de autorizarlos.

Para instalar manualmente, copia el **[directorio completo de la skill](skill/ultimate-skill-creator)**, no solo `SKILL.md`, en un destino nuevo:

| Alcance | Destino | Uso |
| --- | --- | --- |
| Usuario actual | `~/.agents/skills/ultimate-skill-creator/` | Tus proyectos locales de Codex. |
| Un repositorio | `.agents/skills/ultimate-skill-creator/` dentro de ese repositorio | Un flujo específico del proyecto. |

Elige un solo alcance para evitar duplicados. Estas ubicaciones y la ruta de instalación siguen la [documentación de skills locales de OpenAI](https://developers.openai.com/codex/skills), consultada el 11 de septiembre de 2026. Reinicia Codex si la skill no aparece. Las pruebas automatizadas no cubren una instalación real; no se afirma que este proyecto figure en ningún marketplace.

<a id="es-quick-start"></a>
### Inicio rápido

Abre una conversación con un flujo que hayas completado, o adjunta notas sin información sensible, el script que funciona y sus resultados de pruebas. Por ejemplo, después de verificar un proceso de limpieza de CSV, pide:

```text
Usa $ultimate-skill-creator para empaquetar como csv-cleanup el flujo
verificado de limpieza de CSV a partir de las notas, el script y los
resultados de pruebas que proporcioné.

Crea un directorio nuevo ./csv-cleanup-candidate. Incluye los pasos que
funcionan, los intentos fallidos importantes, un README con un ejemplo
copiable y su salida esperada, y un informe de validación. Conserva los
archivos de entrada originales. Indica lo no probado. No instales ni publiques el paquete.
```

**Resultado esperado:** un paquete local con el README del repositorio, `skills/csv-cleanup/SKILL.md` y las referencias, scripts o recursos necesarios. El informe debe identificar las comprobaciones realizadas y sus resultados; crear archivos no demuestra que el flujo funcione. Revisa el comando documentado, la entrada de ejemplo, el resultado esperado y las limitaciones pendientes antes de usar la nueva skill.

Para probar únicamente el generador determinista de estructuras, sin un agente, sigue el ejemplo siguiente.

<a id="es-usage"></a>
### Uso

| Punto de partida | Qué proporcionar | Qué ayuda a producir |
| --- | --- | --- |
| Una conversación o sesión de depuración resuelta | Objetivos, restricciones, intentos fallidos, pasos finales y evidencia. | Instrucciones reutilizables y un caso de estudio. |
| Una automatización o investigación que funciona | Scripts, entradas y salidas representativas, dependencias y permisos. | Un paquete con configuración documentada y comprobaciones de aceptación. |
| Una skill existente con un README poco claro | Los archivos reales y el comportamiento verificado. | Un README para personas que siga la convención compartida. |

No lo uses para presentar una idea sin probar como una solución demostrada, publicar conversaciones privadas ni conceder permiso ilimitado para modificar archivos. `README.md` explica el paquete a las personas; [SKILL.md](skill/ultimate-skill-creator/SKILL.md) indica al agente cómo ejecutar el flujo.

#### Generar un borrador local

Con Git y Python 3.10 o posterior instalados, empieza en un directorio donde todavía no exista `ultimate-skill-creator`. Estos comandos de Bash descargan una copia del repositorio y generan un borrador:

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

¿Ya tienes una copia? Desde su raíz, ejecuta solo el comando de Python con una ruta nueva para `--out`. El script muestra el directorio absoluto de salida y una advertencia de borrador, y termina con el código `0`. Crea exactamente esta estructura:

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

**Esto no implementa la limpieza de CSV.** Crea cinco archivos de borrador para que tú o el agente los completéis. No genera una licencia, no copia automáticamente la conversación ni ejecuta una validación. La skill de origen usa `skill/`, en singular; los paquetes generados usan `skills/`, en plural.

| Opción | Significado |
| --- | --- |
| `--name` | Obligatoria. Se convierte en un identificador ASCII en minúsculas. |
| `--out` | Obligatoria. La ruta no puede existir, ni siquiera como directorio vacío o enlace simbólico. |
| `--title` | Título legible opcional. |
| `--description` | Propósito y condición de uso opcionales; máximo de 1.024 caracteres. |
| `--languages` | Códigos separados por comas. Predeterminado: `en,zh-Hant,zh-Hans,es,ja`. El inglés sigue siendo la versión canónica. |

Se admiten `en`, `zh-Hant`, `zh-Hans`, `es`, `ja`, `pt`, `hi`, `ar`, `fr` y `ko`. Las secciones adicionales creadas por el generador son **borradores sin traducir**, no traducciones terminadas. Complétalas o elimina tanto la sección como su enlace de navegación antes de publicar.

<a id="es-compatibility"></a>
### Compatibilidad

| Componente | Requisitos y estado de verificación |
| --- | --- |
| Flujo guiado | Diseñado para Codex con esta skill instalada. CI no ejecuta una tarea completa en Codex. |
| Generador y comprobador de README | Python 3.10+; solo la biblioteca estándar. La referencia de CI registrada abajo utilizó Python 3.12.3 en Ubuntu 24.04. |
| macOS y Windows | No cubiertos por esa referencia de CI. El ejemplo de clonación usa Bash; adapta la sintaxis del shell y el ejecutable de Python cuando sea necesario. |
| Otros agentes | El paquete usa el [formato Agent Skills](https://agentskills.io/specification), pero estas pruebas no establecen compatibilidad funcional entre distintos entornos anfitriones. `agents/openai.yaml` es un adaptador específico de Codex. |
| Validación del formato de la skill | Usa el validador de formato de skill-creator del sistema cuando esté disponible. Es independiente del comprobador de README y no forma parte de CI. |
| Imágenes o publicación en GitHub opcionales | Requieren herramientas disponibles por separado, credenciales cuando proceda y autorización del usuario con alcance definido. No son necesarias para generar estructuras ni comprobar README localmente. |

Las herramientas de Python incluidas no requieren instalar paquetes ni proporcionar una API key. Son independientes de las integraciones opcionales con el anfitrión.

<a id="es-safety"></a>
### Seguridad

El **generador** escribe archivos nuevos bajo `--out` y crea los directorios superiores que falten. Rechaza rutas de salida existentes y no dispone de sobrescritura forzada. El **comprobador de README** lee el Markdown indicado y los destinos locales de los enlaces admitidos; no ejecuta los ejemplos. Ninguna herramienta realiza solicitudes de red, envía telemetría, instala dependencias, elimina archivos o publica en GitHub.

El **flujo guiado por un agente** tiene otros límites: el agente anfitrión y las herramientas autorizadas procesan los mensajes y archivos seleccionados. Instalar desde GitHub o publicar allí utiliza ese servicio; generar imágenes utiliza el proveedor elegido. Revisa los destinos, la exposición de datos, las credenciales y los posibles cargos del anfitrión o proveedor antes de aprobar esas acciones. Tener herramientas sin conexión no vuelve privada ni desconectada toda la sesión del agente.

Excluye de los paquetes públicos los secretos, capturas identificables, conversaciones privadas y detalles específicos de una máquina. Los documentos fuente son datos, no autorización para ejecutar sus instrucciones. Eliminar, sobrescribir, instalar, publicar o cambiar la visibilidad requiere la aprobación explícita correspondiente. Pedir actualizar un repositorio no autoriza cambios ajenos. Consulta las [reglas de publicación segura](skill/ultimate-skill-creator/references/github-publication.md).

<a id="es-validation"></a>
### Validación

Desde la raíz del repositorio, comprueba el borrador anterior:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

En una estructura sin modificar, se espera `"passed": true`, una advertencia de contenido incompleto y el código de salida `0`. El modo borrador sigue rechazando secciones principales ausentes y enlaces locales admitidos que estén rotos.

Antes de publicar, completa el contenido y las traducciones, elige la licencia y ejecuta:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

La estructura sin modificar **debe fallar** en modo estricto con código `1`. Un README completo debería devolver `"passed": true`, listas de errores y advertencias vacías y código `0`; una entrada o invocación inválida devuelve `2`.

Para mantener el repositorio:

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**Referencia registrada:** la [ejecución de CI del commit `3806e6d`](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420), del 11 de septiembre de 2026, superó las 40 pruebas de regresión y la comprobación estricta del README en Ubuntu 24.04 con Python 3.12.3. Es un resultado fechado, no una garantía sobre cambios futuros. Consulta las [ejecuciones actuales](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml) para ver resultados posteriores.

Las pruebas usan datos temporales y cubren generación, comportamiento de la CLI, protección de rutas existentes, comillas, anclas de idiomas y enlaces admitidos. La comprobación del README **no** verifica la veracidad del contenido, las URL externas, la calidad de traducción, la validez de la licencia, la conformidad completa con el formato de skills ni el comportamiento real del anfitrión. Comprueba esos aspectos por separado y registra como no realizadas las verificaciones omitidas.

<a id="es-troubleshooting"></a>
### Solución de problemas

| Síntoma | Causa y siguiente paso seguro |
| --- | --- |
| Se rechaza el directorio de salida | Ya existe o es un enlace simbólico. Elige otro `--out`; no borres trabajo existente para volver a intentarlo. |
| La comprobación estricta falla justo después de generar | El borrador está incompleto por diseño. Completa el flujo y las traducciones anunciadas, y vuelve a comprobar. |
| Falla un enlace de idioma o imagen | Revisa el archivo o ancla real y la ruta relativa. Elimina enlaces a contenido que no vayas a distribuir. |
| Se rechaza un código de idioma | Usa un código admitido por la [especificación compartida](skill/ultimate-skill-creator/assets/readme-spec.json). |
| Un README complejo produce resultados inesperados | El comprobador admite un subconjunto documentado de Markdown, no todas las funciones de GitHub Markdown. Consulta sus [limitaciones](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates) y revisa la vista previa de GitHub. |
| Codex no encuentra la skill | Revisa el directorio completo y el alcance elegido; reinicia si hace falta. No dupliques instalaciones para resolver la detección. |

**Actualizar:** revisa el diff del alcance autorizado antes de sustituir archivos instalados. Actualizar este repositorio en GitHub no actualiza automáticamente una instalación local copiada anteriormente. El generador de paquetes no es un actualizador.

**Desactivar o eliminar:** utiliza primero los [controles de skills documentados](https://developers.openai.com/codex/skills) del anfitrión. Eliminar archivos locales es una acción distinta que requiere aprobación del usuario. No elimines skills ajenas ni configuración del anfitrión.

<a id="es-documentation"></a>
### Documentación

La [convención universal de README](skill/ultimate-skill-creator/references/universal-readme-spec.md) define contenido principal, secciones opcionales, estilo y controles de revisión. Es una convención del proyecto basada en un [estudio cualitativo de 30 repositorios populares relacionados con skills](research/readme-study-2026-09-11.md), no un estándar oficial ni una clasificación global demostrada de los 30 primeros.

| Recurso | Propósito |
| --- | --- |
| [Instrucciones del agente](skill/ultimate-skill-creator/SKILL.md) y [flujo](skill/ultimate-skill-creator/references/workflow.md) | Pasos de empaquetado, criterios de aceptación y límites de seguridad. |
| [Especificación compartida](skill/ultimate-skill-creator/assets/readme-spec.json) | Nombres de secciones, alias, indicaciones de borrador e idiomas usados por ambas herramientas. |
| [Guía de idiomas](skill/ultimate-skill-creator/references/language-and-readme.md) | Navegación, estado de traducción y recursos visuales portátiles. |
| [Generador](skill/ultimate-skill-creator/scripts/create_skill_candidate.py), [comprobador](skill/ultimate-skill-creator/scripts/validate_readme.py) y [pruebas](tests/test_readme_workflow.py) | Inspeccionar la implementación y reproducir las comprobaciones. |

La [guía visual](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png) y el [resumen SVG portátil](skill/ultimate-skill-creator/assets/skill-creation-loop.svg) son compartidos y conservan su idioma original. Son opcionales; las instrucciones de texto bastan para empezar.

<a id="es-contributing"></a>
### Contribuciones

Usa [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues) para problemas reproducibles y [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) para cambios. Incluye el comportamiento esperado, resultados de pruebas pertinentes y pruebas de regresión si cambia el comportamiento. Mantén coherentes la especificación, las herramientas y la documentación; evita limpiezas ajenas y datos privados en los ejemplos. Al cambiar un comando, opción, regla de seguridad o limitación, actualiza las ocho versiones en el mismo cambio.

<a id="es-license"></a>
### Licencia

Este repositorio se distribuye bajo [MIT](LICENSE). El propietario de un paquete nuevo debe elegir términos adecuados para su contenido y conservar las atribuciones de terceros; la licencia del proyecto no se asigna automáticamente a los paquetes generados. El estudio de README enlaza las fuentes y sintetiza sus patrones, sin redistribuir su documentación completa.

## 日本語

解決済みの会話や作業手順を、再利用できる Codex skill にまとめます。人が読める README、必要なファイル、実際の検証記録を含めます。

**現在の状態：**草稿の生成ツールと、オフラインの README 検査ツールを備えています。生成されたパッケージを公開する前に、実際の手順を記入し、テストを行い、ライセンスを決める必要があります。この節は完全な利用ガイドです。保守の原文は英語版とし、コマンド、パス、オプションは変更しません。リンク先の参考文書と共通画像は元の言語のままです。

[インストール](#ja-installation) · [クイックスタート](#ja-quick-start) · [使い方](#ja-usage) · [互換性](#ja-compatibility) · [安全性](#ja-safety) · [検証](#ja-validation) · [トラブルシューティング](#ja-troubleshooting) · [ドキュメント](#ja-documentation) · [貢献](#ja-contributing) · [ライセンス](#ja-license)

<a id="ja-installation"></a>
### インストール

**Codex 経由のインストールを推奨します。** Codex の会話に貼り付けてください。

```text
$skill-installer を使い、https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator から現在のユーザー用に skill をインストールしてください。保存先を表示し、既存のインストールは上書きしないでください。
```

インストールされるのはエージェント用の指示と付属リソースであり、独立したアプリではありません。エージェントが進める作業には Codex が必要です。Python 3.10 以降が必要なのは、付属ツールを実行する場合だけです。インストールでは GitHub からファイルを取得し、選んだローカルの場所に書き込むため、変更内容を確認してから許可してください。

手動でインストールする場合は、`SKILL.md` だけでなく、**[skill ディレクトリ全体](skill/ultimate-skill-creator)**を新しい保存先にコピーします。

| 範囲 | 保存先 | 用途 |
| --- | --- | --- |
| 現在のユーザー | `~/.agents/skills/ultimate-skill-creator/` | 自分のローカル Codex プロジェクト。 |
| 1 つのリポジトリ | そのリポジトリ内の `.agents/skills/ultimate-skill-creator/` | 特定のプロジェクト専用の作業。 |

重複を避けるため、範囲はどちらか一方を選びます。保存先とインストール方法は、2026 年 9 月 11 日に確認した [OpenAI のローカル skill ドキュメント](https://developers.openai.com/codex/skills)に基づきます。表示されない場合は Codex を再起動してください。実際のインストールは本リポジトリの自動テストの対象外です。マーケットプレイスへの掲載も主張していません。

<a id="ja-quick-start"></a>
### クイックスタート

実際に完了した作業を含む会話を開くか、機密情報を取り除いたメモ、動作するスクリプト、テスト出力を添付してください。例えば、CSV 整理の手順を検証した後、次のように依頼します。

```text
$ultimate-skill-creator を使い、提供したメモ、スクリプト、テスト出力をもとに、
検証済みの CSV 整理手順を csv-cleanup という skill にまとめてください。

新しい ./csv-cleanup-candidate ディレクトリを作成してください。
動作した手順、重要な失敗例、コピーできる使用例と期待する出力を含む README、
検証報告を入れてください。元の入力ファイルを保持し、未テストの部分を明記してください。
候補パッケージのインストールや公開はしないでください。
```

**期待する成果物：**リポジトリの README、`skills/csv-cleanup/SKILL.md`、必要な参考資料・スクリプト・素材を含むローカルの候補パッケージです。報告には実行済みの検査と結果を記載します。ファイルを作っただけで動作を確認したことにはできません。新しい skill を使う前に、記載されたコマンド、入力例、期待する結果、残る制約を確認してください。

エージェントを使わず、決まったひな形を作る生成ツールだけを試す場合は、次の例を使います。

<a id="ja-usage"></a>
### 使い方

| 出発点 | 提供するもの | 作成を支援するもの |
| --- | --- | --- |
| 解決済みの会話やデバッグ作業 | 目標、制約、失敗した試み、最終手順、根拠。 | 再利用できる指示と補足のケーススタディ。 |
| 動作する自動化や調査の手順 | スクリプト、代表的な入出力、依存関係、権限。 | セットアップと受け入れ検査を記載した skill パッケージ。 |
| README が分かりにくい既存の skill | 実際の skill ファイルと検証済みの動作。 | 共通規約に沿った、人向けの README。 |

未テストの構想を実証済みの解決策として見せたり、非公開の会話を公開したり、無制限のファイル変更権限を与えたりするために使わないでください。`README.md` は人向けにパッケージを説明し、[SKILL.md](skill/ultimate-skill-creator/SKILL.md) はエージェントに実行手順を指示します。

#### ローカル草稿の生成

Git と Python 3.10 以降を用意し、`ultimate-skill-creator` がまだ存在しないディレクトリから始めます。以下の Bash コマンドはリポジトリを取得し、新しい草稿を作成します。

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

取得済みのリポジトリがある場合は、そのルートから Python コマンドだけを実行し、`--out` に新しいパスを指定します。スクリプトは出力先の絶対パスと草稿の警告を表示し、終了コード `0` で終わります。生成される構造は次のとおりです。

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

**CSV 整理の機能そのものは実装されません。** 自分またはエージェントが仕上げる 5 個の草稿ファイルを作るだけです。ライセンスの生成、会話の自動コピー、検証の実行も行いません。元の skill は単数の `skill/`、生成する候補は複数の `skills/` を使います。

| オプション | 内容 |
| --- | --- |
| `--name` | 必須。小文字の ASCII skill 識別子に変換されます。 |
| `--out` | 必須。空のディレクトリやシンボリックリンクを含め、既存のパスは指定できません。 |
| `--title` | 任意。人向けのタイトル。 |
| `--description` | 任意。用途と使用条件。最大 1,024 文字。 |
| `--languages` | カンマ区切りの言語コード。既定値は `en,zh-Hant,zh-Hans,es,ja`。英語が常に基準版です。 |

対応コードは `en`、`zh-Hant`、`zh-Hans`、`es`、`ja`、`pt`、`hi`、`ar`、`fr`、`ko` です。生成ツールが追加する他言語の節は**未翻訳の草稿**であり、完成した翻訳ではありません。公開前に翻訳を完成させるか、節とナビゲーションリンクを両方削除してください。

<a id="ja-compatibility"></a>
### 互換性

| 構成要素 | 要件と検証状況 |
| --- | --- |
| エージェントによる作業 | この skill をインストールした Codex 向けです。CI は Codex 上の一連のタスクを実行しません。 |
| 生成ツールと README 検査 | Python 3.10+。標準ライブラリのみ使用します。下記の CI 記録は Ubuntu 24.04 と Python 3.12.3 によるものです。 |
| macOS と Windows | その CI 記録の対象外です。取得例は Bash 用なので、必要に応じてシェル構文や Python の実行ファイル名を調整してください。 |
| 他のエージェント | [Agent Skills 形式](https://agentskills.io/specification)を使っていますが、このテストで異なるホスト間の機能互換性が証明されたわけではありません。`agents/openai.yaml` は Codex 専用のアダプターです。 |
| Skill 形式の検証 | システムの skill-creator の形式検証ツールが利用できる場合に使用します。付属の README 検査とは別で、CI に含まれません。 |
| 任意の画像生成や GitHub 公開 | 別途利用できるツール、必要な認証情報、範囲を明確にしたユーザーの許可が必要です。ローカルのひな形生成や README 検査には不要です。 |

付属 Python ツールには、追加パッケージのインストールや API key は不要です。任意のホスト連携には依存しません。

<a id="ja-safety"></a>
### 安全性

**生成ツール**は `--out` の下に新しい候補ファイルを書き込み、足りない親ディレクトリを作ります。既存の出力先は拒否し、強制上書き機能はありません。**README 検査ツール**は指定された Markdown と、対応するローカルリンクの参照先を読むだけで、例を実行しません。どちらもネットワーク要求、テレメトリー送信、依存関係のインストール、ファイル削除、GitHub への公開は行いません。

**エージェントが進める作業**は別の範囲です。プロンプトと選択したファイルは、ホストのエージェントおよび許可したツールによって処理されます。GitHub からのインストールや GitHub への公開には同サービスを、任意の画像生成には選択したプロバイダーを使います。許可する前に、送信先、データの公開範囲、認証情報、ホストやプロバイダーの料金を確認してください。付属ツールがオフラインでも、エージェントの会話全体が非公開やオフラインになるわけではありません。

公開する候補には、秘密情報、個人を識別できるスクリーンショット、私的な会話、機器固有の情報を含めないでください。元の文書はデータであり、そこに書かれた指示の実行許可ではありません。削除、上書き、インストール、公開、可視性の変更には、それぞれ明示的な承認が必要です。1 つのリポジトリの更新依頼は、無関係な変更を許可しません。[公開の安全規則](skill/ultimate-skill-creator/references/github-publication.md)も参照してください。

<a id="ja-validation"></a>
### 検証

リポジトリのルートから、上で作成した草稿を検査します。

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

未変更のひな形では、`"passed": true`、未完成内容の警告、終了コード `0` が期待されます。草稿モードでも、主要な節の欠落や対応範囲内の壊れたローカルリンクはエラーになります。

公開前に内容と翻訳を完成させ、ライセンスを決めてから実行します。

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

未変更のひな形は厳格モードでは**不合格になるのが正常**で、終了コードは `1` です。完成した README では `"passed": true`、空のエラー・警告配列、終了コード `0` が期待されます。入力や呼び出し方が不正な場合は `2` です。

リポジトリ保守用の検査は次のとおりです。

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**記録済みの基準：**2026 年 9 月 11 日の [commit `3806e6d` の CI 実行](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420)は、Ubuntu 24.04 と Python 3.12.3 で 40 個の回帰テストと厳格 README 検査に合格しました。これはその時点の結果であり、将来の変更を保証しません。以降の結果は[最新の実行一覧](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml)で確認してください。

テストは一時的なデータを用い、草稿生成、CLI の動作、既存パスの保護、引用符、言語アンカー、対応リンクを検査します。README 検査では、内容の真実性、外部 URL、翻訳品質、ライセンスの有効性、skill 形式への完全準拠、実際のホスト動作は**確認しません**。それぞれ別途確認し、実行していない検査は未実行と記録してください。

<a id="ja-troubleshooting"></a>
### トラブルシューティング

| 症状 | 原因と安全な対処 |
| --- | --- |
| 出力先が拒否される | 既存のパスかシンボリックリンクです。別の `--out` を指定し、再試行のために既存の作業を削除しないでください。 |
| 生成直後に厳格検査で不合格になる | ひな形は意図的に未完成です。作業内容と掲載している翻訳を完成させてから再実行します。 |
| 言語や画像のリンクが開かない | 実際のファイル、アンカー、相対パスを確認します。配布しない内容へのリンクは外してください。 |
| 言語コードが拒否される | [共通仕様](skill/ultimate-skill-creator/assets/readme-spec.json)で対応しているコードを指定します。 |
| 複雑な README で想定外の指摘が出る | 検査ツールは文書化された Markdown の一部に対応し、GitHub Markdown 全機能には対応しません。[検査の制限](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates)と GitHub のプレビューを確認してください。 |
| Codex が skill を見つけない | ディレクトリ全体と選択した範囲を確認し、必要なら再起動します。検出の問題を重複インストールで回避しないでください。 |

**更新：**インストール済みファイルを置き換える前に、許可された範囲の差分を確認します。この GitHub リポジトリを更新しても、以前コピーしたローカルのインストールは自動更新されません。候補生成ツールは更新ツールではありません。

**無効化・削除：**まずホストの[文書化された skill 設定](https://developers.openai.com/codex/skills)で無効にしてください。ローカルファイルの削除はユーザーの承認を要する別の操作です。無関係な skill やホスト設定は削除しないでください。

<a id="ja-documentation"></a>
### ドキュメント

[共通 README 規約](skill/ultimate-skill-creator/references/universal-readme-spec.md)は、主要内容、任意の節、文体、レビュー項目を定義します。[人気のある skill 関連リポジトリ 30 件の定性調査](research/readme-study-2026-09-11.md)に基づく本プロジェクトの規約であり、公式標準でも、厳密に証明された世界上位 30 件の順位でもありません。

| 資料 | 用途 |
| --- | --- |
| [エージェント用指示](skill/ultimate-skill-creator/SKILL.md)と[ワークフロー](skill/ultimate-skill-creator/references/workflow.md) | パッケージ化の手順、受け入れ条件、安全上の境界。 |
| [共通仕様](skill/ultimate-skill-creator/assets/readme-spec.json) | 両ツールが使う節名、別名、草稿用の指示、言語名。 |
| [言語ガイド](skill/ultimate-skill-creator/references/language-and-readme.md) | ナビゲーション、翻訳状況、可搬性のある画像。 |
| [生成ツール](skill/ultimate-skill-creator/scripts/create_skill_candidate.py)、[検査ツール](skill/ultimate-skill-creator/scripts/validate_readme.py)、[テスト](tests/test_readme_workflow.py) | 実装の確認と検査の再現。 |

共通の[図解ガイド](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png)と[可搬性のある SVG 概要図](skill/ultimate-skill-creator/assets/skill-creation-loop.svg)は元の言語のままです。図は任意で、テキストの指示だけで使い始められます。

<a id="ja-contributing"></a>
### 貢献

再現可能な問題は [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues)、変更提案は [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) を使ってください。期待する動作と関連するテスト出力を添え、動作変更には回帰テストを含めます。共通仕様、ツール、文書を整合させ、無関係な整理や例への個人情報の混入を避けてください。コマンド、オプション、安全規則、制限を変えるときは、同じ変更で 8 言語すべてを更新してください。

<a id="ja-license"></a>
### ライセンス

本リポジトリは [MIT](LICENSE) ライセンスです。新しい候補の所有者は自分の内容に適した条件を選び、第三者への帰属表示を保持する必要があります。本プロジェクトのライセンスが生成物に自動適用されるわけではありません。README 調査は出典をリンクし、共通パターンを整理したもので、元の文書全文を再配布するものではありません。

## Português

Transforme uma conversa ou um fluxo de trabalho resolvido em uma skill reutilizável para Codex, com um README legível, arquivos de apoio e evidências explícitas de validação.

**Status:** inclui um gerador de rascunhos e um verificador de README offline. Os pacotes gerados ainda precisam do conteúdo real do fluxo, de testes e de uma decisão sobre a licença antes da publicação. Esta seção é um guia completo. O inglês é a fonte de manutenção; comandos, caminhos e opções permanecem inalterados. As referências e imagens compartilhadas mantêm o idioma original.

[Instalação](#pt-installation) · [Início rápido](#pt-quick-start) · [Uso](#pt-usage) · [Compatibilidade](#pt-compatibility) · [Segurança](#pt-safety) · [Validação](#pt-validation) · [Solução de problemas](#pt-troubleshooting) · [Documentação](#pt-documentation) · [Contribuições](#pt-contributing) · [Licença](#pt-license)

<a id="pt-installation"></a>
### Instalação

**Recomendado: instale a skill pelo Codex.** Cole em uma conversa do Codex:

```text
Use $skill-installer para instalar https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator para minha conta de usuário. Mostre o destino e não sobrescreva uma instalação existente.
```

Isso instala instruções para o agente e os recursos incluídos, não um aplicativo independente. O fluxo guiado precisa do Codex; Python 3.10 ou superior só é necessário para executar os utilitários incluídos. A instalação baixa arquivos do GitHub e grava no destino local escolhido. Revise as alterações propostas antes de autorizá-las.

Na instalação manual, copie o **[diretório completo da skill](skill/ultimate-skill-creator)**, não apenas `SKILL.md`, para um destino novo:

| Escopo | Destino | Uso |
| --- | --- | --- |
| Usuário atual | `~/.agents/skills/ultimate-skill-creator/` | Seus projetos locais no Codex. |
| Um repositório | `.agents/skills/ultimate-skill-creator/` dentro desse repositório | Um fluxo específico do projeto. |

Escolha apenas um escopo para evitar cópias duplicadas. Os locais e o método de instalação seguem a [documentação de skills locais da OpenAI](https://developers.openai.com/codex/skills), consultada em 11 de setembro de 2026. Reinicie o Codex se a skill não aparecer. Os testes automatizados não cobrem uma instalação real; não se afirma que o projeto esteja listado em um marketplace.

<a id="pt-quick-start"></a>
### Início rápido

Abra uma conversa com um fluxo que você realmente concluiu ou anexe notas sem dados sensíveis, o script funcional e sua saída de testes. Por exemplo, após verificar um fluxo de limpeza de CSV, peça:

```text
Use $ultimate-skill-creator para empacotar como csv-cleanup o fluxo
verificado de limpeza de CSV, usando as notas, o script e os resultados
de testes que forneci.

Crie um diretório novo ./csv-cleanup-candidate. Inclua os passos que
funcionam, as tentativas malsucedidas importantes, um README com exemplo
copiável e saída esperada, e um relatório de validação. Preserve os
arquivos de entrada originais. Indique o que não foi testado. Não instale nem publique o pacote.
```

**Resultado esperado:** um pacote local com o README do repositório, `skills/csv-cleanup/SKILL.md` e as referências, scripts ou recursos necessários. O relatório deve identificar verificações realmente executadas e seus resultados; criar arquivos não comprova que o fluxo funciona. Revise o comando documentado, a entrada de exemplo, o resultado esperado e as limitações restantes antes de usar a nova skill.

Para experimentar somente o gerador determinístico de estrutura, sem um agente, siga o próximo exemplo.

<a id="pt-usage"></a>
### Uso

| Ponto de partida | O que fornecer | O que a skill ajuda a produzir |
| --- | --- | --- |
| Uma conversa ou sessão de depuração resolvida | Objetivos, restrições, tentativas malsucedidas, passos finais e evidências. | Instruções reutilizáveis com um estudo de caso de apoio. |
| Uma automação ou pesquisa funcional | Scripts, entradas e saídas representativas, dependências e permissões. | Um pacote com configuração documentada e verificações de aceitação. |
| Uma skill existente com README pouco claro | Arquivos reais e comportamento verificado. | Um README para pessoas, seguindo a convenção compartilhada. |

Não use a ferramenta para apresentar uma ideia não testada como solução comprovada, publicar conversas privadas ou conceder permissão irrestrita para alterar arquivos. `README.md` explica o pacote às pessoas; [SKILL.md](skill/ultimate-skill-creator/SKILL.md) orienta o agente a executar o fluxo.

#### Gerar um rascunho local

Com Git e Python 3.10 ou superior instalados, comece em um diretório onde `ultimate-skill-creator` ainda não exista. Estes comandos Bash baixam uma cópia do repositório e geram um rascunho:

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

Já tem uma cópia? Na raiz dela, execute apenas o comando Python com um caminho novo para `--out`. O script mostra o caminho absoluto da saída e um aviso de rascunho, encerrando com código `0`. A estrutura criada é exatamente esta:

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

**Isso não implementa a limpeza de CSV.** São criados cinco arquivos de rascunho para você ou o agente completar. O gerador não cria uma licença, não copia automaticamente a conversa nem executa a validação. A skill de origem fica em `skill/`, no singular; os pacotes gerados usam `skills/`, no plural.

| Opção | Significado |
| --- | --- |
| `--name` | Obrigatória. Convertida em um identificador ASCII minúsculo. |
| `--out` | Obrigatória. O caminho não pode existir, nem como diretório vazio ou link simbólico. |
| `--title` | Título legível opcional. |
| `--description` | Propósito e condição de uso opcionais, com limite de 1.024 caracteres. |
| `--languages` | Códigos separados por vírgulas. Padrão: `en,zh-Hant,zh-Hans,es,ja`. O inglês permanece como versão canônica. |

Os códigos aceitos são `en`, `zh-Hant`, `zh-Hans`, `es`, `ja`, `pt`, `hi`, `ar`, `fr` e `ko`. As seções de idiomas adicionais criadas pelo gerador são **rascunhos ainda não traduzidos**, não traduções concluídas. Complete-as ou remova tanto a seção quanto seu link de navegação antes de publicar.

<a id="pt-compatibility"></a>
### Compatibilidade

| Componente | Requisitos e status da verificação |
| --- | --- |
| Fluxo guiado | Destinado ao Codex com esta skill instalada. CI não executa uma tarefa completa no Codex. |
| Gerador e verificador de README | Python 3.10+; somente a biblioteca padrão. A referência de CI abaixo usou Python 3.12.3 no Ubuntu 24.04. |
| macOS e Windows | Não cobertos por essa referência de CI. O exemplo de clonagem usa Bash; adapte a sintaxe do shell e o executável Python quando necessário. |
| Outros agentes | O pacote utiliza o [formato Agent Skills](https://agentskills.io/specification), mas esses testes não estabelecem compatibilidade funcional entre ambientes hospedeiros. `agents/openai.yaml` é um adaptador específico do Codex. |
| Validação do formato da skill | Use o validador de formato do skill-creator do sistema quando disponível. Ele é separado do verificador de README e não faz parte de CI. |
| Imagens ou publicação opcional no GitHub | Exigem ferramentas disponíveis separadamente, credenciais quando necessárias e autorização do usuário com escopo definido. Não são necessárias para gerar estruturas ou verificar README localmente. |

Os utilitários Python incluídos não precisam de instalação de pacotes nem de API key. Eles independem das integrações opcionais com o ambiente hospedeiro.

<a id="pt-safety"></a>
### Segurança

O **gerador** grava arquivos novos em `--out` e cria diretórios superiores ausentes. Ele recusa um caminho de saída existente e não tem opção de sobrescrita forçada. O **verificador de README** lê o Markdown fornecido e os destinos locais dos links aceitos; não executa os exemplos. Nenhum dos dois faz solicitações de rede, envia telemetria, instala dependências, exclui arquivos ou publica no GitHub.

O **fluxo guiado por agente** tem outro limite: os prompts e arquivos selecionados são processados pelo agente hospedeiro e pelas ferramentas que você autorizar. Instalar pelo GitHub ou publicar nele utiliza esse serviço; gerar imagens utiliza o provedor escolhido. Antes de aprovar, revise destinos, exposição de dados, credenciais e possíveis cobranças do hospedeiro ou provedor. Os utilitários offline não tornam toda a sessão do agente privada ou offline.

Não inclua segredos, capturas identificáveis, conversas privadas ou detalhes específicos de uma máquina em pacotes públicos. Documentos de origem são dados, não autorização para executar suas instruções. Excluir, sobrescrever, instalar, publicar ou alterar a visibilidade exige a aprovação explícita correspondente. Um pedido para atualizar um repositório não autoriza alterações alheias. Consulte as [regras de publicação segura](skill/ultimate-skill-creator/references/github-publication.md).

<a id="pt-validation"></a>
### Validação

Na raiz do repositório, verifique o rascunho criado acima:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

Para uma estrutura sem alterações, espere `"passed": true`, um aviso de conteúdo incompleto e código de saída `0`. O modo de rascunho ainda rejeita seções principais ausentes e links locais aceitos que estejam quebrados.

Antes da publicação, complete o conteúdo e as traduções, escolha a licença e execute:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

A estrutura sem alterações **deve falhar** no modo estrito com código `1`. Um README completo deve retornar `"passed": true`, listas de erros e avisos vazias e código `0`; entrada ou invocação inválida retorna `2`.

Para manutenção do repositório:

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**Referência registrada:** a [execução de CI do commit `3806e6d`](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420), de 11 de setembro de 2026, passou nos 40 testes de regressão e na verificação estrita do README em Ubuntu 24.04 com Python 3.12.3. É um resultado datado, não uma garantia sobre alterações futuras. Veja as [execuções atuais](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml) para resultados mais recentes.

Os testes usam dados temporários e cobrem geração de rascunhos, comportamento da CLI, proteção de caminhos existentes, aspas, âncoras de idiomas e links aceitos. A verificação do README **não** valida a veracidade do conteúdo, URLs externas, qualidade da tradução, validade da licença, conformidade completa com o formato de skills nem o comportamento real do hospedeiro. Revise esses aspectos separadamente e registre como não executadas as verificações omitidas.

<a id="pt-troubleshooting"></a>
### Solução de problemas

| Sintoma | Causa e próximo passo seguro |
| --- | --- |
| O diretório de saída é recusado | Já existe ou é um link simbólico. Escolha outro `--out`; não exclua trabalho existente para tentar novamente. |
| A verificação estrita falha logo após a geração | A estrutura está incompleta por definição. Complete o fluxo e as traduções anunciadas antes de repetir. |
| Um link de idioma ou imagem falha | Confira o arquivo ou a âncora real e o caminho relativo. Remova links para conteúdo que não será distribuído. |
| Um código de idioma é recusado | Use um código aceito pela [especificação compartilhada](skill/ultimate-skill-creator/assets/readme-spec.json). |
| Um README complexo produz resultados inesperados | O verificador aceita um subconjunto documentado de Markdown, não todos os recursos do GitHub Markdown. Consulte os [limites](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates) e confira a prévia no GitHub. |
| O Codex não encontra a skill | Confira o diretório completo e o escopo escolhido; reinicie se necessário. Não duplique instalações para contornar a descoberta. |

**Atualização:** revise um diff dentro do escopo autorizado antes de substituir arquivos instalados. Atualizar este repositório no GitHub não atualiza automaticamente uma instalação local copiada anteriormente. O gerador de pacotes não é um atualizador.

**Desativação ou remoção:** use primeiro os [controles documentados de skills](https://developers.openai.com/codex/skills) do hospedeiro para desativar. Excluir os arquivos locais é uma ação separada que exige aprovação do usuário. Não remova skills alheias nem configurações do hospedeiro.

<a id="pt-documentation"></a>
### Documentação

A [convenção universal de README](skill/ultimate-skill-creator/references/universal-readme-spec.md) define conteúdo principal, seções opcionais, estilo e verificações de revisão. É uma convenção do projeto baseada em um [estudo qualitativo de 30 repositórios populares relacionados a skills](research/readme-study-2026-09-11.md), não um padrão oficial nem uma classificação global comprovada dos 30 primeiros.

| Recurso | Propósito |
| --- | --- |
| [Instruções do agente](skill/ultimate-skill-creator/SKILL.md) e [fluxo](skill/ultimate-skill-creator/references/workflow.md) | Etapas de empacotamento, critérios de aceitação e limites de segurança. |
| [Especificação compartilhada](skill/ultimate-skill-creator/assets/readme-spec.json) | Nomes de seções, aliases, orientações de rascunho e idiomas usados pelos dois utilitários. |
| [Guia de idiomas](skill/ultimate-skill-creator/references/language-and-readme.md) | Navegação, status da tradução e recursos visuais portáveis. |
| [Gerador](skill/ultimate-skill-creator/scripts/create_skill_candidate.py), [verificador](skill/ultimate-skill-creator/scripts/validate_readme.py) e [testes](tests/test_readme_workflow.py) | Inspecionar a implementação e reproduzir verificações. |

O [guia visual](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png) e a [visão geral em SVG portátil](skill/ultimate-skill-creator/assets/skill-creation-loop.svg) são compartilhados e mantêm o idioma original. São opcionais; as instruções de texto bastam para começar.

<a id="pt-contributing"></a>
### Contribuições

Use [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues) para problemas reproduzíveis e [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) para alterações. Inclua comportamento esperado, saídas de testes relevantes e testes de regressão quando houver mudança de comportamento. Mantenha especificação, utilitários e documentação consistentes; evite limpezas alheias ou dados privados nos exemplos. Ao alterar um comando, opção, regra de segurança ou limitação, atualize os oito idiomas na mesma alteração.

<a id="pt-license"></a>
### Licença

Este repositório usa a licença [MIT](LICENSE). O proprietário de um novo pacote deve escolher termos adequados para seu conteúdo e preservar atribuições de terceiros; a licença deste projeto não é aplicada automaticamente aos pacotes gerados. O estudo de README apresenta links para as fontes e sintetiza seus padrões, sem redistribuir a documentação completa.

## हिन्दी

हल की जा चुकी बातचीत या कार्यप्रणाली को दोबारा उपयोग योग्य Codex skill में बदलें। इसमें पढ़ने योग्य README, सहायक फ़ाइलें और सत्यापन के स्पष्ट प्रमाण शामिल होते हैं।

**स्थिति:** इसमें मसौदा बनाने वाला जनरेटर और ऑफ़लाइन README जाँचकर्ता शामिल हैं। प्रकाशित करने से पहले बनाए गए पैकेज में वास्तविक कार्यप्रणाली लिखना, परीक्षण करना और लाइसेंस तय करना अभी भी ज़रूरी है। यह अनुभाग पूरी मार्गदर्शिका है। रखरखाव के लिए अंग्रेज़ी मूल संदर्भ है; कमांड, पथ और विकल्प अपरिवर्तित रहते हैं। जुड़े हुए संदर्भ दस्तावेज़ और साझा चित्र अपनी मूल भाषा में हैं।

[स्थापना](#hi-installation) · [त्वरित शुरुआत](#hi-quick-start) · [उपयोग](#hi-usage) · [अनुकूलता](#hi-compatibility) · [सुरक्षा](#hi-safety) · [सत्यापन](#hi-validation) · [समस्या निवारण](#hi-troubleshooting) · [दस्तावेज़](#hi-documentation) · [योगदान](#hi-contributing) · [लाइसेंस](#hi-license)

<a id="hi-installation"></a>
### स्थापना

**सुझाया गया तरीका: Codex के माध्यम से skill स्थापित करें।** Codex की बातचीत में यह लिखें:

```text
$skill-installer का उपयोग करके https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator से मेरे उपयोगकर्ता खाते के लिए यह skill स्थापित करें। स्थापना का स्थान दिखाएँ और मौजूदा स्थापना के ऊपर न लिखें।
```

इससे एजेंट के निर्देश और साथ दिए गए संसाधन स्थापित होते हैं, कोई अलग ऐप नहीं। एजेंट द्वारा निर्देशित कार्य के लिए Codex चाहिए; साथ दिए गए सहायक प्रोग्राम चलाने के लिए ही Python 3.10 या बाद का संस्करण आवश्यक है। स्थापना GitHub से फ़ाइलें डाउनलोड करके चुने हुए स्थानीय स्थान पर लिखती है। अनुमति देने से पहले प्रस्तावित बदलाव देखें।

मैन्युअल स्थापना के लिए केवल `SKILL.md` नहीं, बल्कि **[skill की पूरी डायरेक्टरी](skill/ultimate-skill-creator)** किसी नए स्थान पर कॉपी करें:

| दायरा | स्थान | उपयोग |
| --- | --- | --- |
| वर्तमान उपयोगकर्ता | `~/.agents/skills/ultimate-skill-creator/` | आपके स्थानीय Codex प्रोजेक्ट। |
| एक रिपॉज़िटरी | उस रिपॉज़िटरी के अंदर `.agents/skills/ultimate-skill-creator/` | किसी विशेष प्रोजेक्ट की कार्यप्रणाली। |

दोहरी प्रतियों से बचने के लिए एक ही दायरा चुनें। ये स्थान और स्थापना विधि [OpenAI के स्थानीय skill दस्तावेज़](https://developers.openai.com/codex/skills) पर आधारित हैं, जिन्हें 11 सितंबर 2026 को जाँचा गया था। Skill न दिखे तो Codex दोबारा शुरू करें। इस रिपॉज़िटरी के स्वचालित परीक्षण वास्तविक स्थापना को नहीं जाँचते; किसी marketplace पर सूचीबद्ध होने का दावा भी नहीं किया गया है।

<a id="hi-quick-start"></a>
### त्वरित शुरुआत

ऐसी बातचीत खोलें जिसमें आपने वास्तव में कार्य पूरा किया हो, या संवेदनशील जानकारी हटाए हुए नोट्स, काम करने वाली स्क्रिप्ट और उसके परीक्षण परिणाम संलग्न करें। उदाहरण के लिए, CSV साफ़ करने की प्रक्रिया सत्यापित करने के बाद लिखें:

```text
$ultimate-skill-creator से मेरे दिए हुए नोट्स, स्क्रिप्ट और परीक्षण परिणामों
के आधार पर सत्यापित CSV-सफ़ाई प्रक्रिया को csv-cleanup नाम की skill में बदलें।

नई ./csv-cleanup-candidate डायरेक्टरी बनाएँ। काम करने वाले चरण, महत्वपूर्ण
असफल प्रयास, कॉपी करने योग्य उदाहरण और अपेक्षित आउटपुट वाला README,
तथा सत्यापन रिपोर्ट शामिल करें। मूल इनपुट फ़ाइलें सुरक्षित रखें।
जो भाग नहीं जाँचे गए हैं उन्हें बताएँ। अभी पैकेज स्थापित या प्रकाशित न करें।
```

**अपेक्षित परिणाम:** एक स्थानीय पैकेज जिसमें रिपॉज़िटरी का README, `skills/csv-cleanup/SKILL.md` और कार्य के लिए आवश्यक संदर्भ, स्क्रिप्ट या संसाधन हों। रिपोर्ट में वास्तव में किए गए परीक्षण और परिणाम बताए जाने चाहिए; फ़ाइलें बन जाना कार्यप्रणाली के काम करने का प्रमाण नहीं है। नई skill इस्तेमाल करने से पहले दिए गए कमांड, उदाहरण इनपुट, अपेक्षित परिणाम और शेष सीमाएँ देखें।

एजेंट के बिना केवल तय ढाँचा बनाने वाले जनरेटर को आज़माने के लिए अगला उदाहरण अपनाएँ।

<a id="hi-usage"></a>
### उपयोग

| आपकी शुरुआती सामग्री | क्या देना है | क्या बनाने में मदद मिलती है |
| --- | --- | --- |
| हल की गई बातचीत या डिबगिंग सत्र | लक्ष्य, सीमाएँ, असफल प्रयास, अंतिम चरण और प्रमाण। | दोबारा उपयोग योग्य निर्देश और सहायक केस स्टडी। |
| काम करने वाली स्वचालन या शोध प्रक्रिया | स्क्रिप्ट, प्रतिनिधि इनपुट/आउटपुट, निर्भरताएँ और अनुमतियाँ। | सेटअप और स्वीकृति-जाँच सहित skill पैकेज। |
| मौजूदा skill जिसका README अस्पष्ट है | वास्तविक skill फ़ाइलें और सत्यापित व्यवहार। | साझा नियमों के अनुसार लोगों के लिए लिखा README। |

बिना परीक्षण के विचार को प्रमाणित समाधान दिखाने, निजी बातचीत प्रकाशित करने या एजेंट को फ़ाइलें बदलने की असीमित अनुमति देने के लिए इसका उपयोग न करें। `README.md` लोगों को पैकेज समझाता है; [SKILL.md](skill/ultimate-skill-creator/SKILL.md) एजेंट को प्रक्रिया चलाने के निर्देश देता है।

#### स्थानीय मसौदा बनाना

Git और Python 3.10 या बाद का संस्करण स्थापित होने पर ऐसी डायरेक्टरी में शुरू करें जहाँ `ultimate-skill-creator` पहले से न हो। ये Bash कमांड रिपॉज़िटरी की प्रति डाउनलोड करके नया मसौदा बनाते हैं:

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

प्रति पहले से है? उसकी मूल डायरेक्टरी से केवल Python कमांड चलाएँ और `--out` के लिए नया पथ दें। स्क्रिप्ट आउटपुट डायरेक्टरी का पूर्ण पथ और मसौदे की चेतावनी दिखाती है, फिर स्थिति कोड `0` के साथ समाप्त होती है। बिल्कुल यह ढाँचा बनता है:

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

**इससे CSV साफ़ करने की कार्यक्षमता लागू नहीं होती।** यह पाँच मसौदा फ़ाइलें बनाता है जिन्हें आप या एजेंट पूरा करेंगे। यह लाइसेंस नहीं बनाता, बातचीत अपने-आप कॉपी नहीं करता और सत्यापन नहीं चलाता। मूल skill एकवचन `skill/` में है; बनाए गए पैकेज बहुवचन `skills/` इस्तेमाल करते हैं।

| विकल्प | अर्थ |
| --- | --- |
| `--name` | आवश्यक। छोटे ASCII अक्षरों वाले skill पहचानकर्ता में बदला जाता है। |
| `--out` | आवश्यक। पथ मौजूद नहीं होना चाहिए, खाली डायरेक्टरी या प्रतीकात्मक लिंक के रूप में भी नहीं। |
| `--title` | वैकल्पिक, पढ़ने योग्य शीर्षक। |
| `--description` | वैकल्पिक उद्देश्य और उपयोग की शर्त; अधिकतम 1,024 वर्ण। |
| `--languages` | कॉमा से अलग किए गए कोड। डिफ़ॉल्ट: `en,zh-Hant,zh-Hans,es,ja`। अंग्रेज़ी आधार संस्करण रहती है। |

मान्य कोड `en`, `zh-Hant`, `zh-Hans`, `es`, `ja`, `pt`, `hi`, `ar`, `fr` और `ko` हैं। जनरेटर द्वारा बनाए गए अतिरिक्त भाषा अनुभाग **अभी अनूदित नहीं हुए मसौदे** हैं, पूरी हो चुकी अनुवाद सामग्री नहीं। प्रकाशन से पहले उन्हें पूरा करें या अनुभाग और उसका नेविगेशन लिंक दोनों हटा दें।

<a id="hi-compatibility"></a>
### अनुकूलता

| भाग | आवश्यकताएँ और सत्यापन स्थिति |
| --- | --- |
| निर्देशित कार्यप्रणाली | यह skill स्थापित किए हुए Codex के लिए है। CI पूरा Codex कार्य नहीं चलाता। |
| जनरेटर और README जाँचकर्ता | Python 3.10+; केवल मानक लाइब्रेरी। नीचे दर्ज CI आधार परीक्षण Ubuntu 24.04 पर Python 3.12.3 में चला था। |
| macOS और Windows | उस CI आधार परीक्षण में शामिल नहीं हैं। क्लोन करने का उदाहरण Bash में है; ज़रूरत के अनुसार शेल सिंटैक्स और Python निष्पादन फ़ाइल बदलें। |
| अन्य एजेंट | पैकेज [Agent Skills प्रारूप](https://agentskills.io/specification) इस्तेमाल करता है, लेकिन ये परीक्षण अलग-अलग होस्ट में कार्यक्षमता स्थापित नहीं करते। `agents/openai.yaml` Codex का विशिष्ट अडैप्टर है। |
| Skill प्रारूप का सत्यापन | सिस्टम के skill-creator का प्रारूप जाँचकर्ता उपलब्ध होने पर इस्तेमाल करें। यह README जाँचकर्ता से अलग है और CI का हिस्सा नहीं है। |
| वैकल्पिक चित्र या GitHub प्रकाशन | अलग से उपलब्ध उपकरण, जहाँ आवश्यक हों वहाँ क्रेडेंशियल और निश्चित दायरे की उपयोगकर्ता अनुमति चाहिए। स्थानीय ढाँचा बनाने या README जाँचने के लिए ये आवश्यक नहीं हैं। |

साथ दिए गए Python प्रोग्रामों को अतिरिक्त पैकेज स्थापित करने या API key देने की ज़रूरत नहीं है। वे वैकल्पिक होस्ट एकीकरण से स्वतंत्र हैं।

<a id="hi-safety"></a>
### सुरक्षा

**जनरेटर** `--out` के भीतर नई पैकेज फ़ाइलें और अनुपस्थित ऊपरी डायरेक्टरियाँ बनाता है। वह मौजूदा आउटपुट पथ को अस्वीकार करता है और उसमें जबरन ओवरराइट का विकल्प नहीं है। **README जाँचकर्ता** दिए गए Markdown और समर्थित स्थानीय लिंक के लक्ष्य पढ़ता है; उदाहरण चलाता नहीं है। दोनों प्रोग्राम नेटवर्क अनुरोध, टेलीमेट्री भेजना, निर्भरताएँ स्थापित करना, फ़ाइलें मिटाना या GitHub पर प्रकाशित करना नहीं करते।

**एजेंट द्वारा निर्देशित कार्यप्रणाली** की सीमा अलग है: प्रॉम्प्ट और चुनी गई फ़ाइलें होस्ट एजेंट और आपके अधिकृत उपकरणों द्वारा संसाधित होती हैं। GitHub से स्थापना या वहाँ प्रकाशन में वह सेवा इस्तेमाल होती है; वैकल्पिक चित्र निर्माण में चुना हुआ प्रदाता इस्तेमाल होता है। अनुमति देने से पहले गंतव्य, डेटा का खुलासा, क्रेडेंशियल और होस्ट या प्रदाता के संभावित शुल्क देखें। ऑफ़लाइन सहायक प्रोग्राम पूरी एजेंट बातचीत को निजी या ऑफ़लाइन नहीं बना देते।

सार्वजनिक पैकेज में गोपनीय कुंजियाँ, पहचान बताने वाले स्क्रीनशॉट, निजी बातचीत या मशीन-विशिष्ट विवरण न रखें। स्रोत दस्तावेज़ डेटा हैं, उनके निर्देश चलाने की अनुमति नहीं। हटाने, ओवरराइट करने, स्थापित करने, प्रकाशित करने या दृश्यता बदलने के लिए संबंधित स्पष्ट अनुमति चाहिए। एक रिपॉज़िटरी को अपडेट करने का अनुरोध असंबंधित बदलावों की अनुमति नहीं है। [सुरक्षित प्रकाशन के नियम](skill/ultimate-skill-creator/references/github-publication.md) देखें।

<a id="hi-validation"></a>
### सत्यापन

इस रिपॉज़िटरी की मूल डायरेक्टरी से ऊपर बनाए गए मसौदे की जाँच करें:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

बिना बदले ढाँचे के लिए `"passed": true`, अधूरी सामग्री की चेतावनी और निकास कोड `0` अपेक्षित हैं। मसौदा मोड भी मुख्य अनुभागों की कमी और समर्थित स्थानीय लिंक टूटने को अस्वीकार करता है।

प्रकाशन से पहले सामग्री और अनुवाद पूरे करें, लाइसेंस चुनें, फिर चलाएँ:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

बिना बदला ढाँचा सख्त मोड में **असफल होना चाहिए**, जिसका निकास कोड `1` है। पूरा README `"passed": true`, त्रुटियों और चेतावनियों की खाली सूचियाँ तथा कोड `0` लौटाना चाहिए; अमान्य इनपुट या गलत आह्वान पर कोड `2` मिलता है।

रिपॉज़िटरी के रखरखाव के लिए:

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**दर्ज आधार परिणाम:** 11 सितंबर 2026 की [commit `3806e6d` की CI रन](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420) ने Ubuntu 24.04 और Python 3.12.3 पर सभी 40 रिग्रेशन परीक्षण तथा सख्त README जाँच पास की थी। यह उस तारीख का परिणाम है, भविष्य के बदलावों की गारंटी नहीं। नए परिणाम [वर्तमान वर्कफ़्लो रन](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml) में देखें।

परीक्षण अस्थायी डेटा का इस्तेमाल करते हैं और मसौदा निर्माण, CLI व्यवहार, मौजूदा पथों की सुरक्षा, उद्धरण चिह्न, भाषा एंकर और समर्थित लिंक जाँचते हैं। README जाँच सामग्री की सत्यता, बाहरी URL, अनुवाद की गुणवत्ता, लाइसेंस की वैधता, पूरे skill प्रारूप का अनुपालन या वास्तविक होस्ट व्यवहार **सत्यापित नहीं करती**। इन्हें अलग से जाँचें और छोड़ी गई जाँचों को नहीं चलाया गया के रूप में दर्ज करें।

<a id="hi-troubleshooting"></a>
### समस्या निवारण

| समस्या | कारण और सुरक्षित अगला कदम |
| --- | --- |
| आउटपुट डायरेक्टरी अस्वीकार होती है | वह पहले से मौजूद है या प्रतीकात्मक लिंक है। नया `--out` चुनें; दोबारा कोशिश करने के लिए पुराना काम न मिटाएँ। |
| बनाने के तुरंत बाद सख्त जाँच असफल होती है | ढाँचा जानबूझकर अधूरा है। कार्यप्रणाली और सूचीबद्ध अनुवाद पूरे करके फिर जाँचें। |
| भाषा या चित्र का लिंक नहीं चलता | वास्तविक फ़ाइल या एंकर और सापेक्ष पथ देखें। जो सामग्री पैकेज में नहीं देंगे उसके लिंक हटाएँ। |
| भाषा कोड अस्वीकार होता है | [साझा विनिर्देश](skill/ultimate-skill-creator/assets/readme-spec.json) में समर्थित कोड इस्तेमाल करें। |
| जटिल README पर अप्रत्याशित परिणाम मिलते हैं | जाँचकर्ता Markdown के दस्तावेज़ित हिस्से को समर्थन देता है, GitHub Markdown की हर सुविधा को नहीं। [जाँच की सीमाएँ](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates) और GitHub पूर्वावलोकन देखें। |
| Codex को skill नहीं मिलती | पूरी स्थापना डायरेक्टरी और चुना हुआ दायरा जाँचें; आवश्यकता हो तो पुनः शुरू करें। खोज की समस्या के लिए दोहरी स्थापना न बनाएँ। |

**अपडेट:** स्थापित फ़ाइलें बदलने से पहले अधिकृत दायरे का diff देखें। GitHub पर इस रिपॉज़िटरी का अपडेट पहले कॉपी की गई स्थानीय स्थापना को अपने-आप अपडेट नहीं करता। पैकेज जनरेटर अपडेटर नहीं है।

**निष्क्रिय करना या हटाना:** पहले होस्ट के [दस्तावेज़ित skill नियंत्रण](https://developers.openai.com/codex/skills) से skill निष्क्रिय करें। स्थानीय फ़ाइलें मिटाना अलग कार्रवाई है जिसके लिए उपयोगकर्ता की अनुमति चाहिए। असंबंधित skills या होस्ट सेटिंग न हटाएँ।

<a id="hi-documentation"></a>
### दस्तावेज़

[साझा README नियम](skill/ultimate-skill-creator/references/universal-readme-spec.md) मुख्य सामग्री, वैकल्पिक अनुभाग, शैली और समीक्षा-जाँच तय करते हैं। ये [30 लोकप्रिय skill-संबंधित रिपॉज़िटरी के गुणात्मक अध्ययन](research/readme-study-2026-09-11.md) से बने प्रोजेक्ट के नियम हैं, कोई आधिकारिक README मानक या प्रमाणित वैश्विक शीर्ष-30 रैंकिंग नहीं।

| संसाधन | उद्देश्य |
| --- | --- |
| [एजेंट के निर्देश](skill/ultimate-skill-creator/SKILL.md) और [कार्यप्रणाली](skill/ultimate-skill-creator/references/workflow.md) | पैकेज बनाने के चरण, स्वीकृति मानदंड और सुरक्षा सीमाएँ। |
| [साझा विनिर्देश](skill/ultimate-skill-creator/assets/readme-spec.json) | दोनों प्रोग्रामों के अनुभाग नाम, वैकल्पिक नाम, मसौदा निर्देश और भाषा नाम। |
| [भाषा मार्गदर्शिका](skill/ultimate-skill-creator/references/language-and-readme.md) | नेविगेशन, अनुवाद स्थिति और पोर्टेबल चित्र। |
| [जनरेटर](skill/ultimate-skill-creator/scripts/create_skill_candidate.py), [जाँचकर्ता](skill/ultimate-skill-creator/scripts/validate_readme.py) और [परीक्षण](tests/test_readme_workflow.py) | कार्यान्वयन देखना और जाँचों को दोहराना। |

साझा [चित्र मार्गदर्शिका](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png) और [पोर्टेबल SVG अवलोकन](skill/ultimate-skill-creator/assets/skill-creation-loop.svg) अपनी मूल भाषा में हैं। चित्र वैकल्पिक हैं; शुरुआत के लिए लिखित निर्देश पर्याप्त हैं।

<a id="hi-contributing"></a>
### योगदान

दोहराई जा सकने वाली समस्याओं के लिए [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues) और बदलावों के लिए [pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) इस्तेमाल करें। अपेक्षित व्यवहार, संबंधित परीक्षण आउटपुट और व्यवहार बदलने पर रिग्रेशन परीक्षण जोड़ें। साझा विनिर्देश, सहायक प्रोग्राम और दस्तावेज़ एक-दूसरे से मेल खाने चाहिए; उदाहरणों में निजी डेटा और असंबंधित सफ़ाई से बचें। किसी कमांड, विकल्प, सुरक्षा नियम या सीमा को बदलते समय उसी बदलाव में आठों भाषाएँ अपडेट करें।

<a id="hi-license"></a>
### लाइसेंस

यह रिपॉज़िटरी [MIT](LICENSE) लाइसेंस के अंतर्गत है। नए पैकेज के मालिक को अपनी सामग्री के लिए उपयुक्त शर्तें चुननी होंगी और तीसरे पक्ष के श्रेय बनाए रखने होंगे; इस प्रोजेक्ट का लाइसेंस बनाए गए पैकेज पर अपने-आप लागू नहीं होता। README अध्ययन स्रोतों के लिंक देता है और उनके सामान्य ढाँचों का सार प्रस्तुत करता है, उनके पूरे दस्तावेज़ वितरित नहीं करता।

## العربية

حوّل محادثة أو سير عمل تم حله إلى مهارة قابلة لإعادة الاستخدام في Codex، مع ملف README واضح وملفات مساندة وأدلة صريحة على التحقق.

**الحالة:** يتضمن المشروع مولّد مسودات وأداة لفحص README دون اتصال. ما زالت الحزم الناتجة تحتاج إلى كتابة سير العمل الفعلي واختباره وتحديد الترخيص قبل النشر. هذا القسم دليل كامل. الإنجليزية هي المصدر المعتمد للصيانة؛ تبقى الأوامر والمسارات والخيارات كما هي. تحتفظ المستندات المرجعية والصور المشتركة بلغتها الأصلية.

[التثبيت](#ar-installation) · [البدء السريع](#ar-quick-start) · [الاستخدام](#ar-usage) · [التوافق](#ar-compatibility) · [السلامة](#ar-safety) · [التحقق](#ar-validation) · [حل المشكلات](#ar-troubleshooting) · [التوثيق](#ar-documentation) · [المساهمة](#ar-contributing) · [الترخيص](#ar-license)

<a id="ar-installation"></a>
### التثبيت

**الطريقة الموصى بها: تثبيت المهارة عبر Codex.** الصق في محادثة Codex:

```text
استخدم $skill-installer لتثبيت المهارة من https://github.com/dev-james0723/ultimate-skill-creator/tree/main/skill/ultimate-skill-creator لحساب المستخدم الخاص بي. اعرض موقع التثبيت ولا تستبدل تثبيتًا موجودًا.
```

يُثبّت هذا تعليمات الوكيل والموارد المرفقة، لا تطبيقًا مستقلًا. يتطلب سير العمل الذي يقوده الوكيل وجود Codex؛ ولا يلزم Python 3.10 أو أحدث إلا عند تشغيل الأدوات المساعدة المرفقة. ينزّل التثبيت ملفات من GitHub ويكتبها في الموقع المحلي المحدد. راجع التغييرات المقترحة قبل الموافقة عليها.

للتثبيت اليدوي، انسخ **[مجلد المهارة كاملًا](skill/ultimate-skill-creator)**، وليس `SKILL.md` وحده، إلى موقع جديد:

| النطاق | الموقع | الاستخدام |
| --- | --- | --- |
| المستخدم الحالي | `~/.agents/skills/ultimate-skill-creator/` | مشاريع Codex المحلية الخاصة بك. |
| مستودع واحد | `.agents/skills/ultimate-skill-creator/` داخل ذلك المستودع | سير عمل خاص بالمشروع. |

اختر نطاقًا واحدًا لتجنب النسخ المكررة. تتبع المواقع وطريقة التثبيت [توثيق المهارات المحلية من OpenAI](https://developers.openai.com/codex/skills)، الذي روجع في 11 سبتمبر 2026. أعد تشغيل Codex إن لم تظهر المهارة. لا تشمل الاختبارات الآلية في هذا المستودع تثبيتًا حقيقيًا، ولا يدّعي المشروع أنه مدرج في أي marketplace.

<a id="ar-quick-start"></a>
### البدء السريع

افتح محادثة تحتوي على سير عمل أنجزته فعلًا، أو أرفق ملاحظات أزلت منها البيانات الحساسة، والبرنامج النصي الذي يعمل، ونتائج اختباراته. مثلًا، بعد التحقق من عملية تنظيف CSV، اطلب:

```text
استخدم $ultimate-skill-creator لتجميع عملية تنظيف CSV التي تم التحقق منها
باسم csv-cleanup، اعتمادًا على الملاحظات والبرنامج النصي ونتائج الاختبارات التي قدمتها.

أنشئ مجلدًا جديدًا ./csv-cleanup-candidate. أدرج الخطوات التي نجحت، والمحاولات
الفاشلة المهمة، وREADME يحتوي على مثال قابل للنسخ ومخرجات متوقعة، وتقرير تحقق.
حافظ على ملفات الإدخال الأصلية وحدد الأجزاء التي لم تُختبر بعد.
لا تثبّت الحزمة المرشحة ولا تنشرها.
```

**النتيجة المتوقعة:** حزمة محلية تتضمن README للمستودع و`skills/csv-cleanup/SKILL.md` والمراجع أو البرامج النصية أو الموارد اللازمة. يجب أن يحدد التقرير الفحوص المنفذة فعلًا ونتائجها؛ إنشاء الملفات وحده لا يثبت نجاح سير العمل. قبل استخدام المهارة الجديدة، راجع الأمر الموثق ومثال الإدخال والنتيجة المتوقعة والقيود المتبقية.

لتجربة مولّد البنية المحددة فقط دون وكيل، اتبع المثال التالي.

<a id="ar-usage"></a>
### الاستخدام

| نقطة البداية | ما يجب تقديمه | ما تساعد المهارة على إنتاجه |
| --- | --- | --- |
| محادثة أو جلسة تصحيح أُنجز حلها | الأهداف والقيود والمحاولات الفاشلة والخطوات النهائية والأدلة. | تعليمات قابلة لإعادة الاستخدام مع دراسة حالة مساندة. |
| عملية أتمتة أو بحث تعمل فعلًا | البرامج النصية وأمثلة ممثلة للمدخلات والمخرجات والاعتماديات والأذونات. | حزمة مهارة مع إعداد موثق وفحوص قبول. |
| مهارة موجودة ذات README غير واضح | ملفات المهارة الفعلية والسلوك الذي تم التحقق منه. | README موجّه للأشخاص وفق القواعد المشتركة. |

لا تستخدمها لتقديم فكرة غير مختبرة بوصفها حلًا مثبتًا، أو لنشر محادثات خاصة، أو لمنح الوكيل إذنًا مطلقًا بتعديل الملفات. يشرح `README.md` الحزمة للأشخاص، بينما يوجّه [SKILL.md](skill/ultimate-skill-creator/SKILL.md) الوكيل إلى تنفيذ سير العمل.

#### إنشاء مسودة محلية

بعد تثبيت Git وPython 3.10 أو أحدث، ابدأ في مجلد لا يحتوي على `ultimate-skill-creator` مسبقًا. تنزّل أوامر Bash التالية نسخة من المستودع وتنتج مسودة جديدة:

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

لديك نسخة بالفعل؟ ابدأ من جذرها وشغّل أمر Python فقط مع مسار جديد للخيار `--out`. يعرض البرنامج المسار المطلق لمجلد الإخراج وتحذيرًا بأن الناتج مسودة، ثم ينتهي برمز `0`. ينشئ هذه البنية بالضبط:

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

**هذا لا ينفّذ وظيفة تنظيف CSV.** إنما ينشئ خمسة ملفات مسودة لتكملها أنت أو الوكيل. لا ينشئ ترخيصًا، ولا ينسخ المحادثة تلقائيًا، ولا يشغّل عملية تحقق. المهارة المصدر موجودة تحت `skill/` بالمفرد؛ والحزم الناتجة تستخدم `skills/` بالجمع.

| الخيار | المعنى |
| --- | --- |
| `--name` | مطلوب؛ يُحوّل إلى معرّف مهارة بأحرف ASCII صغيرة. |
| `--out` | مطلوب؛ يجب ألا يكون المسار موجودًا، حتى لو كان مجلدًا فارغًا أو رابطًا رمزيًا. |
| `--title` | عنوان اختياري مقروء للأشخاص. |
| `--description` | وصف اختياري للغرض وحالة الاستخدام، بحد أقصى 1,024 محرفًا. |
| `--languages` | رموز مفصولة بفواصل. الافتراضي: `en,zh-Hant,zh-Hans,es,ja`. تبقى الإنجليزية النسخة المرجعية. |

الرموز المدعومة هي `en` و`zh-Hant` و`zh-Hans` و`es` و`ja` و`pt` و`hi` و`ar` و`fr` و`ko`. أقسام اللغات الإضافية التي ينشئها المولّد هي **مسودات لم تُترجم بعد**، وليست ترجمات مكتملة. أكملها أو احذف القسم ورابط التنقل إليه معًا قبل النشر.

<a id="ar-compatibility"></a>
### التوافق

| المكوّن | المتطلبات وحالة التحقق |
| --- | --- |
| سير العمل الموجّه | يستهدف Codex مع تثبيت هذه المهارة. لا ينفّذ CI مهمة كاملة داخل Codex. |
| المولّد وفاحص README | Python 3.10+، باستخدام المكتبة القياسية فقط. استُخدم Python 3.12.3 على Ubuntu 24.04 في نتيجة CI المرجعية المسجلة أدناه. |
| macOS وWindows | غير مشمولين بتلك النتيجة المرجعية. يستخدم مثال الاستنساخ Bash؛ عدّل صياغة الصدفة وملف Python التنفيذي عند الحاجة. |
| الوكلاء الآخرون | تستخدم الحزمة [تنسيق Agent Skills](https://agentskills.io/specification)، لكن الاختبارات لا تثبت التوافق الوظيفي بين البيئات المضيفة. الملف `agents/openai.yaml` محوّل خاص بـCodex. |
| التحقق من تنسيق المهارة | استخدم أداة التحقق من التنسيق الخاصة بـskill-creator في النظام إن توفرت. وهي منفصلة عن فاحص README وليست ضمن CI. |
| الصور أو النشر الاختياري على GitHub | يتطلب أدوات متاحة بشكل منفصل، وبيانات اعتماد عند الحاجة، وإذنًا محدد النطاق من المستخدم. لا يلزم أي منهما لإنشاء البنية أو فحص README محليًا. |

لا تتطلب أدوات Python المرفقة تثبيت حزم إضافية أو توفير API key. وهي مستقلة عن عمليات التكامل الاختيارية مع المضيف.

<a id="ar-safety"></a>
### السلامة

يكتب **المولّد** ملفات مرشحة جديدة تحت `--out` وينشئ المجلدات الأم الناقصة. يرفض مسار إخراج موجودًا، ولا يوفر خيارًا للكتابة القسرية فوقه. يقرأ **فاحص README** ملف Markdown المحدد وأهداف الروابط المحلية المدعومة؛ ولا ينفّذ الأمثلة. لا ترسل أي من الأداتين طلبات شبكة أو بيانات قياس، ولا تثبّت اعتماديات أو تحذف ملفات أو تنشر على GitHub.

أما **سير العمل الذي يقوده الوكيل** فله حدود مختلفة: يعالج الوكيل المضيف والأدوات التي تسمح بها المطالبات والملفات المختارة. يستخدم التثبيت من GitHub أو النشر عليه تلك الخدمة؛ ويستخدم إنشاء الصور الاختياري المزوّد المحدد. راجع الوجهات وكشف البيانات وبيانات الاعتماد والرسوم المحتملة للمضيف أو المزوّد قبل الموافقة. كون الأدوات المساعدة تعمل دون اتصال لا يجعل جلسة الوكيل كلها خاصة أو غير متصلة.

لا تُضمّن أسرارًا أو لقطات شاشة تكشف الهوية أو محادثات خاصة أو تفاصيل خاصة بالجهاز في الحزم العامة. المستندات المصدر بيانات وليست إذنًا لتنفيذ ما فيها من تعليمات. الحذف أو الاستبدال أو التثبيت أو النشر أو تغيير الظهور يتطلب الموافقة الصريحة المناسبة. طلب تحديث مستودع واحد لا يسمح بتغييرات غير مرتبطة. راجع [قواعد النشر الآمن](skill/ultimate-skill-creator/references/github-publication.md).

<a id="ar-validation"></a>
### التحقق

من جذر المستودع، افحص المسودة التي أُنشئت أعلاه:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --json
```

للبنية غير المعدلة، توقّع `"passed": true` وتحذيرًا بالمحتوى غير المكتمل ورمز خروج `0`. ما زال وضع المسودة يرفض غياب الأقسام الأساسية والروابط المحلية المدعومة التي لا تعمل.

قبل النشر، أكمل المحتوى والترجمات واختر الترخيص، ثم شغّل:

```bash
python3 skill/ultimate-skill-creator/scripts/validate_readme.py \
  ./csv-cleanup-candidate/README.md --strict --json
```

**من المتوقع أن تفشل** البنية غير المعدلة في الوضع الصارم برمز `1`. ينبغي أن يعيد README المكتمل `"passed": true` وقائمتين فارغتين للأخطاء والتحذيرات ورمز `0`؛ أما الإدخال أو الاستدعاء غير الصحيح فيعيد `2`.

لصيانة المستودع:

```bash
python3 -m unittest discover -s tests -v
python3 skill/ultimate-skill-creator/scripts/validate_readme.py README.md --strict --json
```

**النتيجة المرجعية المسجلة:** اجتاز [تشغيل CI للالتزام `3806e6d`](https://github.com/dev-james0723/ultimate-skill-creator/actions/runs/34563197420)، في 11 سبتمبر 2026، اختبارات الانحدار الأربعين كلها والفحص الصارم لـREADME على Ubuntu 24.04 مع Python 3.12.3. هذه نتيجة مؤرخة، وليست ضمانًا للتغييرات اللاحقة. راجع [التشغيلات الحالية](https://github.com/dev-james0723/ultimate-skill-creator/actions/workflows/validate.yml) للاطلاع على نتائج أحدث.

تستخدم الاختبارات بيانات مؤقتة، وتغطي إنشاء المسودات وسلوك CLI وحماية المسارات الموجودة وعلامات الاقتباس ومراسي اللغات والروابط المدعومة. فحص README **لا يتحقق** من صحة المحتوى أو الروابط الخارجية أو جودة الترجمة أو صلاحية الترخيص أو المطابقة الكاملة لتنسيق المهارة أو السلوك الفعلي للمضيف. راجع هذه الجوانب منفصلة وسجّل الفحوص التي لم تُنفّذ على أنها لم تُنفّذ.

<a id="ar-troubleshooting"></a>
### حل المشكلات

| العرض | السبب والخطوة الآمنة التالية |
| --- | --- |
| رُفض مجلد الإخراج | موجود بالفعل أو رابط رمزي. اختر `--out` جديدًا؛ لا تحذف عملًا موجودًا لإعادة المحاولة. |
| فشل الفحص الصارم بعد الإنشاء مباشرة | البنية غير مكتملة عمدًا. أكمل سير العمل والترجمات المذكورة ثم أعد الفحص. |
| لا يعمل رابط لغة أو صورة | تحقق من الملف أو المرساة الفعلية والمسار النسبي. أزل روابط المحتوى الذي لن يُرفق بالحزمة. |
| رُفض رمز لغة | استخدم رمزًا مدعومًا في [المواصفات المشتركة](skill/ultimate-skill-creator/assets/readme-spec.json). |
| نتائج غير متوقعة مع README معقد | يدعم الفاحص مجموعة موثقة من Markdown، لا جميع ميزات GitHub Markdown. راجع [حدود الفاحص](skill/ultimate-skill-creator/references/universal-readme-spec.md#review-gates) وافحص معاينة GitHub. |
| لا يجد Codex المهارة | تحقق من مجلد التثبيت الكامل والنطاق المختار، وأعد التشغيل عند الحاجة. لا تكرر التثبيت للتحايل على مشكلة الاكتشاف. |

**التحديث:** راجع الفروق ضمن النطاق المصرح به قبل استبدال الملفات المثبتة. تحديث هذا المستودع على GitHub لا يحدّث تلقائيًا نسخة محلية نُسخت سابقًا. مولّد الحزم ليس أداة تحديث.

**التعطيل أو الإزالة:** استخدم أولًا [عناصر التحكم بالمهارات الموثقة](https://developers.openai.com/codex/skills) لدى المضيف لتعطيل المهارة. حذف الملفات المحلية إجراء منفصل يحتاج إلى موافقة المستخدم. لا تزل مهارات غير مرتبطة أو إعدادات المضيف.

<a id="ar-documentation"></a>
### التوثيق

تحدد [قواعد README المشتركة](skill/ultimate-skill-creator/references/universal-readme-spec.md) المحتوى الأساسي والأقسام الاختيارية والأسلوب وفحوص المراجعة. إنها قواعد لهذا المشروع تستند إلى [دراسة نوعية لـ30 مستودعًا شائعًا متعلقًا بالمهارات](research/readme-study-2026-09-11.md)، وليست معيارًا رسميًا أو ترتيبًا عالميًا مثبتًا لأفضل 30 مستودعًا.

| المورد | الغرض |
| --- | --- |
| [تعليمات الوكيل](skill/ultimate-skill-creator/SKILL.md) و[سير العمل](skill/ultimate-skill-creator/references/workflow.md) | خطوات التجميع ومعايير القبول وحدود السلامة. |
| [المواصفات المشتركة](skill/ultimate-skill-creator/assets/readme-spec.json) | أسماء الأقسام والأسماء البديلة وإرشادات المسودات وأسماء اللغات المستخدمة في الأداتين. |
| [دليل اللغات](skill/ultimate-skill-creator/references/language-and-readme.md) | التنقل وحالة الترجمة والصور القابلة للنقل. |
| [المولّد](skill/ultimate-skill-creator/scripts/create_skill_candidate.py) و[الفاحص](skill/ultimate-skill-creator/scripts/validate_readme.py) و[الاختبارات](tests/test_readme_workflow.py) | مراجعة التنفيذ وإعادة إجراء الفحوص. |

يحافظ [الدليل المرئي](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png) و[مخطط SVG القابل للنقل](skill/ultimate-skill-creator/assets/skill-creation-loop.svg) المشتركان على لغتهما الأصلية. الصور اختيارية؛ تكفي التعليمات النصية للبدء.

<a id="ar-contributing"></a>
### المساهمة

استخدم [issues](https://github.com/dev-james0723/ultimate-skill-creator/issues) للمشكلات القابلة لإعادة الإنتاج، و[pull requests](https://github.com/dev-james0723/ultimate-skill-creator/pulls) للتغييرات. أرفق السلوك المتوقع ونتائج الاختبارات ذات الصلة، واختبارات انحدار عند تغيير السلوك. حافظ على اتساق المواصفات والأدوات والمستندات، وتجنب التنظيف غير المرتبط أو البيانات الخاصة في الأمثلة. عند تغيير أمر أو خيار أو قاعدة سلامة أو قيد، حدّث اللغات الثماني في التغيير نفسه.

<a id="ar-license"></a>
### الترخيص

هذا المستودع مرخّص بموجب [MIT](LICENSE). على مالك الحزمة الجديدة اختيار شروط مناسبة لمحتواه والحفاظ على نسب مواد الأطراف الأخرى إلى أصحابها؛ لا يُطبّق ترخيص المشروع تلقائيًا على الحزم الناتجة. تربط دراسة README مصادرها وتلخّص أنماطها، بدلًا من إعادة توزيع مستنداتها كاملة.
