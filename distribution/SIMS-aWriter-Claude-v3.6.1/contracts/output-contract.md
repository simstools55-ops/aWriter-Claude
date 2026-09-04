# SIMS Writer Machine Output Contract Routing

Machine result contract is selected by the incoming SBM request.

## Doctor Referral Treatment
If any of the following is true:
- `format == SIMS_WRITER_TREATMENT_REQUEST_V1`
- `request_mode == DOCTOR_REFERRAL_TREATMENT`
- `return_contract.format == SIMS_WRITER_TREATMENT_RESULT_V1`

return exactly one final JSON block using `SIMS_WRITER_TREATMENT_RESULT_V1` Contract 1.0. `return_contract` is authoritative. Do not emit `SIMS_FEEDBACK_V2` for this route.

Required compact SBM-facing fields include `format`, `contract_version`, `case_id`, `article_id`, `treatment_status`, `referral_compliance`, `publication_result`, and `return_to`. Before/After shown in the Human Layer must remain synchronized with `publication_result.public_ok_changes`.

## Standard Writer Improvement
For non-Doctor-Referral requests, retain `SIMS_FEEDBACK_V2` Contract 4.2 with `publication_result` as the canonical publication payload.

## Final Contract Gate
Before replying, internally compare:
`INPUT REQUEST -> EXPECTED OUTPUT CONTRACT -> ACTUAL FINAL JSON`.
If format or contract version differs, regenerate the machine JSON before output.
