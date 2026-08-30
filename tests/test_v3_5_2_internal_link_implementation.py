from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_internal_link_after_requires_real_url_markup():
    q=(ROOT/'runtime/internal-link-referral-quality-v3.3.1-rc2.md').read_text(encoding='utf-8')
    g=(ROOT/'runtime/real-article-final-gate-v2.4.md').read_text(encoding='utf-8')
    i=(ROOT/'CLAUDE_PROJECT_INSTRUCTIONS.md').read_text(encoding='utf-8')
    assert 'destination URL present in after' in q
    assert '実URL付きリンクマークアップ' in g
    assert 'URLなしのAfterはPUBLIC_OK禁止' in i
