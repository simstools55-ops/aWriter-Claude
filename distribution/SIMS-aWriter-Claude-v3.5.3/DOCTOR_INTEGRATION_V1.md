# SIMS Article Doctor Integration v1

When input `format` is `SIMS_DOCTOR_WRITER_REQUEST_V1`:

1. Preserve `case.case_id` and `treatment.treatment_id`.
2. Validate Doctor diagnosis; do not accept it blindly.
3. Respect `editing_scope.prohibited_actions`, protected intents, and winner queries.
4. Use the existing Writer publication policy.
5. Return the existing Writer result plus Doctor treatment assessment.
6. Never merge, delete, noindex, redirect, or change URL under a Writer treatment.


## Human Presentation Addendum

SBMが生成した`SIMS_WRITER_TREATMENT_REQUEST_V1`または`DOCTOR_REFERRAL_TREATMENT`を受けても、利用者向け本文にDoctor ReferralのMachine Layerを表示しない。
PUBLIC_OK変更は通常Writerと同じく、対象 / Before / After / 理由 / 期待する効果を必ず表示する。


## Output Contract Lock RC3

SBMが`SIMS_WRITER_TREATMENT_REQUEST_V1`または`request_mode: DOCTOR_REFERRAL_TREATMENT`を送った場合、最終JSONは必ず`SIMS_WRITER_TREATMENT_RESULT_V1` Contract 1.0とする。
`return_contract`がある場合はその指定を最優先する。Human Presentationを通常Writerと同品質で表示した後、Treatment Result JSONを最後に1ブロックだけ返す。`SIMS_FEEDBACK_V2`へのフォールバックは禁止する。
