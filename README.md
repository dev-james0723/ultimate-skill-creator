# Ultimate Skill Creator

Language: [English](#english) | [繁體中文](#繁體中文) | [简体中文](#简体中文) | [Español](#español) | [日本語](#日本語) | [Português](#português) | [हिन्दी](#हिन्दी) | [العربية](#العربية)

![Ultimate Skill Creator guide](skill/ultimate-skill-creator/assets/ultimate-skill-creator-guide.png)

## English

`ultimate-skill-creator` is a Codex skill for turning a solved problem into a reusable, validated, GitHub-ready skill package.

It is designed for moments like:

- you and an AI agent solved a hard automation problem
- the useful knowledge is scattered across a long conversation
- the process included failed attempts, discoveries, scripts, screenshots, and final validation
- you want to preserve the solution as a clean `SKILL.md` with references, scripts, images, README content, language options, and GitHub publication flow

The reusable skill folder is here:

```text
skill/ultimate-skill-creator/
```

### What This Skill Helps An Agent Do

- Extract the durable workflow from a conversation.
- Separate reusable knowledge from one-off details.
- Create a clean skill folder with `SKILL.md`, `references/`, `scripts/`, `assets/`, and `agents/openai.yaml`.
- Add multilingual quick starts and generated or portable visual assets.
- Build a repository-level README that humans can understand.
- Validate the skill locally.
- Prepare GitHub publication safely.
- Ask for explicit confirmation before pushing to external repositories.

### The Core Loop

```text
Solve the problem
   ↓
Capture instructions, failures, commands, evidence, and final logic
   ↓
Package as SKILL.md + references + scripts + assets
   ↓
Validate locally
   ↓
Create a GitHub candidate
   ↓
Publish only after confirmation
```

### Included Files

```text
skill/ultimate-skill-creator/
├── SKILL.md
├── agents/openai.yaml
├── assets/
│   ├── ultimate-skill-creator-guide.png
│   └── skill-creation-loop.svg
├── references/
│   ├── github-publication.md
│   ├── language-and-readme.md
│   └── workflow.md
└── scripts/
    └── create_skill_candidate.py
```

### Quick Start For Codex

Ask Codex:

```text
Use $ultimate-skill-creator to package what we just solved into a validated skill and GitHub publication candidate.
```

The skill should guide Codex to:

1. Reconstruct the user goal and constraints.
2. Capture the final working path and the important failed paths.
3. Create the skill folder.
4. Add references, scripts, assets, and language quick starts.
5. Run validators and script checks.
6. Prepare a GitHub candidate.
7. Ask before push.

### Skeleton Generator

This repo includes a small helper for creating a candidate layout:

```bash
python3 skill/ultimate-skill-creator/scripts/create_skill_candidate.py \
  --name "my-new-skill" \
  --out ./candidate \
  --title "My New Skill" \
  --languages "en,zh-Hant,zh-Hans,es,ja,pt,hi,ar"
```

The generated skeleton is intentionally minimal. Replace placeholders with the actual workflow before publishing.

### Validation Checklist

- `SKILL.md` has valid YAML frontmatter with `name` and `description`.
- The description clearly says when to use the skill.
- Long case history lives in `references/`, not in the main skill body.
- Reusable deterministic code lives in `scripts/`.
- Images, diagrams, or templates live in `assets/`.
- `agents/openai.yaml` matches the skill.
- A repo-level README explains purpose, setup, validation, and known limitations.
- Publication target, visibility, branch, and push strategy are confirmed before using GitHub.

### GitHub Safety Rule

Do not push first and explain later. Create a local candidate, validate it, summarize exactly what will be published, and get explicit user confirmation.

This matters because skills often contain:

- conversation history
- local paths
- screenshots
- logs
- customer or account names
- commands that may reveal environment details

### Example Use Cases

- Package a local macOS automation into a reusable skill.
- Turn a research workflow into a repeatable investigation skill.
- Convert a debugging session into a deployment or troubleshooting skill.
- Create multilingual README material for a public GitHub repo.
- Add generated diagrams that explain a workflow visually.

## 繁體中文

呢個 repo 係一套獨立嘅 Codex skill，目的係將「你同 AI 一齊解決咗一個真問題」呢個過程，打包成可重用、可驗證、可上 GitHub 嘅 skill。

適合用喺：

- 長對話入面有好多重要 instruction、失敗、修正、驗證
- 想將經驗變成 `SKILL.md`
- 想加 references、scripts、assets、README、多語言 quick start
- 想安全咁 publish 去 GitHub

流程：

1. 回收目標、限制、失敗路線、成功邏輯。
2. 將核心 workflow 放入 `SKILL.md`。
3. 長內容放入 `references/`。
4. 可重用工具放入 `scripts/`。
5. 圖片、diagram、template 放入 `assets/`。
6. 跑 validator。
7. 發佈前先問清楚 GitHub repo、visibility、branch。

## 简体中文

这个 repo 是一套独立的 Codex skill，用来把你和 AI 一起解决问题的过程，打包成可复用、可验证、可上传 GitHub 的 skill。

流程：提取目标和限制，记录失败和成功逻辑，写 `SKILL.md`，整理 references/scripts/assets，生成 README，运行验证，然后在用户确认后发布。

## Español

Este repositorio contiene una skill independiente para convertir una solución real en una skill reutilizable, validada y lista para GitHub.

Flujo: resolver, capturar evidencia, empaquetar, validar, preparar candidato local y publicar solo después de confirmación explícita.

## 日本語

このリポジトリは、解決済みの会話や作業を、再利用可能で検証済みの GitHub-ready skill に変換するための独立した Codex skill です。

基本フロー: 解決、記録、パッケージ化、検証、候補作成、確認後に公開。

## Português

Este repositório contém uma skill independente para transformar uma solução real em uma skill reutilizável, validada e pronta para GitHub.

Fluxo: resolver, capturar, empacotar, validar, criar candidato local e publicar apenas após confirmação.

## हिन्दी

यह repository solved workflow को reusable, validated, GitHub-ready skill package में बदलने के लिए standalone Codex skill रखती है।

Flow: solve, capture, package, validate, create local candidate, then publish only after confirmation.

## العربية

يحتوي هذا المستودع على skill مستقلة لتحويل حل واقعي إلى skill قابلة لإعادة الاستخدام والتحقق والنشر على GitHub.

المسار: حل المشكلة، توثيق الأدلة، التغليف، التحقق، إنشاء candidate محلي، ثم النشر بعد موافقة واضحة.
