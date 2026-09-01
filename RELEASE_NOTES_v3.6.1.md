# Release Notes v3.6.1

## Patch scope

v3.6.1 is the post-operational-test patch for the v3.6 rich-copy output feature.

- Human Layer table output is mandatory as a rendered table, including partial row/cell changes.
- Human Layer must not expose literal `<br>`, `\n`, or `/n` as copy payload.
- Paragraphs and lists must be rendered as completed human-readable structure.
- Internal links remain rendered/clickable in Human Layer while Machine Layer preserves implementation markup.
- Machine Result JSON may retain escaped newlines and source-format markup required for downstream processing.

No Contract 4.2 schema change. Shared Knowledge baseline remains unchanged.
