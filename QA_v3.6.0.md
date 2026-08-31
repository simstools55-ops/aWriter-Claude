# aWriter v3.6.0 QA Summary

- Version / PRODUCT_IDENTITY: 3.6.0 aligned in Standard and Claude packages.
- Rich-copy regression tests: PASS.
  - Standard targeted suite: 6 passed.
  - Claude targeted suite: 7 passed.
- Human Layer: rendered tables / clickable internal links allowed for WYSIWYG copy.
- Machine Layer: destination URL and source-format link markup retained.
- Human rich-copy payloads must not be wrapped in code fences or blockquotes.
- Existing JSON contracts and Shared v3.5.1 baseline unchanged.

## Full legacy pytest note
The repository-wide legacy suites are not a clean release gate in the supplied source archives: Standard contains missing/legacy Doctor modules and an expected `claude/` path that is absent; Claude contains duplicated test module names across root, Claude-Upload and distribution trees, causing pytest collection collisions. These pre-existing collection issues are outside the v3.6.0 rich-copy change. The focused regression suites for the changed behavior pass.
