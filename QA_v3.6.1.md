# aWriter v3.6.1 QA Summary

- Version / PRODUCT_IDENTITY: 3.6.1 aligned in Standard and Claude packages.
- Rich-copy regression tests: PASS.
  - Standard targeted suite: 6 passed.
  - Claude targeted suite: 7 passed.
- Human Layer: table changes require actual rendered tables; clickable internal links remain required for WYSIWYG copy.
- Machine Layer: destination URL and source-format link markup retained.
- Human rich-copy payloads must not be wrapped in code fences or blockquotes.
- Operational verification (Hatena Blog visual/WYSIWYG mode): copying the rendered table from the chat UI preserved the table structure successfully. Pipe-delimited pseudo-table text did not; the validator now rejects that form.
- Existing JSON contracts and Shared v3.5.1 baseline unchanged.

## Full legacy pytest note
The repository-wide legacy suites are not a clean release gate in the supplied source archives: Standard contains missing/legacy Doctor modules and an expected `claude/` path that is absent; Claude contains duplicated test module names across root, Claude-Upload and distribution trees, causing pytest collection collisions. These pre-existing collection issues are outside the v3.6.1 rich-copy change. The focused regression suites for the changed behavior pass.


## WYSIWYG Human Layer実運用補強
- PASS: レンダリング済み表をHatena Blog「見たままモード」へコピーし、表構造を保持して編集できた実運用確認を反映。
- Regression: 表の部分変更（1行・1セル）も実表レンダリング必須。
- Regression: Human Layerに`<br>`、文字としての`\n`/`/n`を露出させない。実改行・段落・箇条書きへ投影する。
- Machine Layer JSONのescape/HTML保持は許可し、Human/Machineの意味同値を検証する。
