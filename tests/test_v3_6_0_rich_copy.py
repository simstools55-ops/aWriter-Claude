from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_rich_copy_policy_present():
    ins=(ROOT/'CLAUDE_PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    tpl=(ROOT/'templates/response-template.md').read_text(encoding='utf-8')
    val=(ROOT/'runtime/output-validator.md').read_text(encoding='utf-8')
    link=(ROOT/'runtime/internal-link-referral-quality-v3.3.1-rc2.md').read_text(encoding='utf-8')
    assert 'Hatena Visual Mode / Rich Copy Support (v3.6.0)' in ins
    assert 'コードフェンスおよびblockquoteで囲まない' in ins
    assert 'Rich Copy / 見たままモード対応（v3.6.0）' in tpl
    assert 'Rich Copy Gate v3.6.0' in val
    assert 'difference only in markup/rendering representation is not a mismatch' in link

def test_version_360():
    assert (ROOT/'VERSION').read_text(encoding='utf-8').strip()=='3.6.0'
