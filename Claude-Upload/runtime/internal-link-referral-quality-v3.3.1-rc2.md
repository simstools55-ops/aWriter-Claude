# Internal Link Referral Quality v3.3.1-RC2

Applies to `DOCTOR_REFERRAL_TREATMENT`.

## Input
Prefer `doctor_referral.internal_link_recommendations` when present. Each item may include URL, title, reason, relationship, suggested context, and anchor hint. `candidate_urls` is fallback compatibility input only.

## Writer responsibility
Writer must read the source article and decide the final placement, surrounding sentence, and anchor wording. Doctor/SBM metadata is guidance, not final copy.

## Quality rules
- Do not mechanically append article titles to a related-links list merely because URLs were approved.
- Place each adopted link where the reader naturally needs the adjacent topic whenever a suitable section exists.
- Write one short contextual sentence that explains why the linked article is useful.
- Anchor wording must be natural in the sentence and must not be forced to equal the article title.
- Respect `max_links` / allowed scope. Never add unapproved destinations in Doctor Referral mode.
- If a recommended link is not naturally placeable, do not force it; report it as not performed with a plain reason.
- Human output remains target / Before / After / reason / expected effect.

## Mandatory link implementation gate (v3.6.0)
When an internal link is adopted as PUBLIC_OK, the Machine Layer `after` is not complete unless the destination is actually encoded as a clickable link. Mentioning only the anchor text or article title is a FAIL.

- The Machine Layer `after` field must contain the adopted destination URL in the link markup used by the source article (for example an existing HTML `<a href="...">...</a>` style when the article body is HTML).
- If the source format is Markdown, use a Markdown link `[anchor](URL)`. Do not silently change the article's markup convention.
- Plain text anchor/title without the destination URL is not an implemented internal link.
- Before final output, verify for every adopted internal-link URL: `destination URL present in after` AND `anchor text is inside link markup`.
- If the destination cannot be encoded safely from the available article format, do not report the link as completed. Never ask the user to add the href manually after a PUBLIC_OK result.
- Human-readable After may render the same destination as a clickable anchor for rich-copy use and does not need to expose literal HTML/Markdown markup.
- Human Layer and Machine Layer must preserve the same sentence meaning, anchor text, and destination URL. A difference only in markup/rendering representation is not a mismatch.
- If sentence meaning, anchor text, or destination URL differs between Human Layer and Machine Layer, validation must FAIL.
