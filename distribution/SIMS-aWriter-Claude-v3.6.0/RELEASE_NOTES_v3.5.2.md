# SIMS Writer Claude v3.5.2

## Fixed
- Internal-link PUBLIC_OK After must now contain the actual destination URL in clickable link markup.
- Anchor-text-only After is explicitly rejected by the final gate.
- Writer must not leave manual href insertion to the user after claiming an internal link was added.
- Human Before/After and machine JSON must remain synchronized with the implemented link.

Shared baseline remains v3.5.1.
