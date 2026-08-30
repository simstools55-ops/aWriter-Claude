from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]

def test_claude_instructions_lock_treatment_result():
    text=(ROOT/'CLAUDE_PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    assert 'Doctor Referral Treatmentで`SIMS_FEEDBACK_V2`を最終JSONとして返すこと' in text
    assert 'SIMS_WRITER_TREATMENT_RESULT_V1' in text
    assert 'return_contract' in text

def test_response_template_is_request_aware():
    text=(ROOT/'templates/response-template.md').read_text(encoding='utf-8')
    assert 'SIMS_WRITER_TREATMENT_RESULT_V1' in text
    assert 'SIMS_FEEDBACK_V2' in text

def test_compact_treatment_schema_present():
    assert (ROOT/'schemas/SIMS_WRITER_TREATMENT_RESULT_V1.schema.json').exists()
