# Language and README patterns

Read [the universal README convention](universal-readme-spec.md) before generating or revising repository documentation. Its core content, optional modules, style, and review gates replace the previous short generic README template.

## Languages

The shared [specification data](../assets/readme-spec.json) supports English, Traditional Chinese, Simplified Chinese, Spanish, Japanese, Portuguese, Hindi, Arabic, French, and Korean. English is the generator's canonical version. Preserve the existing CLI's default five-language selection; the user can request one or more supported codes with `--languages`.

A language section must actually exist before adding a navigation link. Generated locale sections are explicitly unfinished drafts, not purported translations. Complete them before publishing or remove both the section and its navigation link. When the user requests broad language coverage, offer the existing eight-language set: `en,zh-Hant,zh-Hans,es,ja,pt,hi,ar`. Do not produce unnecessary full translations for a small task.

Use language names rather than flags. Prefer explicit stable anchors in new generated documents:

```markdown
Language: [English](#lang-en) | [繁體中文](#lang-zh-hant)

<a id="lang-en"></a>
## English

Purpose, installation, an example, expected result, and safety boundaries.

<a id="lang-zh-hant"></a>
## 繁體中文

用途、安裝方式、使用例子、預期結果同安全限制。
```

Preserve existing working anchors when updating established repositories. For long translations, separate files are acceptable; link only files that exist. Keep commands, paths, environment variable names, frontmatter keys, and status tokens unchanged. Check that the source language and translations describe the same current behavior.

## Visuals and privacy

Use diagrams or screenshots only when they explain an output or important decision. Keep assets portable, give images useful alt text, and review rights and accidental personal information. Do not copy third-party tracking images or imply that an external badge proves local test success. The packaged SVG is a fallback; image generation is optional and requires an available image tool.
