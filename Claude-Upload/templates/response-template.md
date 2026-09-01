# 利用者向け回答Template v3.3.2-RC1

冒頭に公開可否を一文で表示する。

## 今回やること
Doctor Referralを含め、利用者が実作業を始められる説明を1〜3文で示す。Machine Layerの内部項目名は禁止。

## SERP比較結果
SERPが修正判断の根拠になった場合のみ表示する。

## 公開OK（そのままコピペ可能）

PUBLIC_OK変更を1件ずつ、必ず以下の5項目で表示する。Doctor Referralでも省略禁止。

### 変更箇所名
**Before**
> 完全な変更前テキスト

新規追加の場合：
> （該当箇所なし・新規追加）

**After**
> 完全な変更後テキスト

**理由**
平易な日本語で短く説明する。

**期待する効果**
読者側の改善点を平易に説明する。順位上昇などを断定しない。

## 利用者判断
該当時のみ表示。

## 今回変更しないもの
必要時のみ自然な日本語で表示する。`blocked_scope`等の内部名を出さない。

## 次の作業
SBM登録など、利用者が次に行う操作を示す。

内部リンク全件不採用時は「今回は追加できる内部リンクはありません。」だけを表示する。

表示禁止：`doctor_referral`、`allowed_scope`、`blocked_scope`、`actions_permitted`、`actions_prohibited`、Contract内部、Routing、Confidence数値、Evidenceコード、Validation、QA verdict。

最後にMachine Result JSONを1ブロックだけ出力し、その後に文章を付けない。

- 通常改善：`SIMS_FEEDBACK_V2` Contract 4.2
- `SIMS_WRITER_TREATMENT_REQUEST_V1` / `DOCTOR_REFERRAL_TREATMENT`：`SIMS_WRITER_TREATMENT_RESULT_V1` Contract 1.0
- 入力の`return_contract`がある場合は最優先。Doctor Referral時に`SIMS_FEEDBACK_V2`を返してはならない。

### Rich Copy / 見たままモード対応（v3.6.1）
AfterのHuman Layer表示は、利用者が原則そのままWYSIWYG編集画面へコピーできる完成形とする。

- 通常文章：完成した変更後文章を表示する。
- 内部リンク：アンカーテキストがクリック可能なレンダリング済みリンクとして表示する。標準コピペ対象に生のHTMLタグやMarkdownリンク記法を表示しない。
- 表：**必ずチャット画面上で実際の表としてレンダリングされる表そのものを表示する。** `A｜B｜C`のような疑似表、HTML tableコード、コードフェンス内Markdown表を完成形として表示しない。
- リンクまたは表を含むAfterのコピー対象部分は、コードフェンスおよびblockquoteで囲まない。
- Human Layerでは「HTML版」「Markdown版」「見たまま版」を並列提示しない。
- Machine Result JSONは元記事形式に必要なmarkupを保持してよい。
- Human LayerとMachine Layerでは文章の意味、destination URL、アンカー、表の見出し・セル内容・順序を一致させる。markup表現の差だけを不一致とみなさない。

#### 表を変更・追加する場合のAfter表示例
`**After**` の直後に、コードフェンスやblockquoteを使わず、通常のMarkdown表を置いてチャットUIに実表としてレンダリングさせる。利用者に見える完成形は表そのものとし、pipe文字列を文章として見せない。

### Human Layer完成表示ゲート（v3.6.1 実運用補強）
Human LayerのPUBLIC_OKに表示するBefore/Afterは、はてなブログ等のWYSIWYG編集画面へコピーするための**完成表示**とする。

- 改行：`<br>`、`<br/>`、`<br />`、文字としての`\n`/`/n`を見せず、実際の改行・段落としてレンダリングする。
- 箇条書き：`<br>・項目`等の連結文字列ではなく、実際の箇条書きとしてレンダリングする。
- 表全体だけでなく、表の1行・1セル・一部分の変更も表変更として扱い、Human Layerでは差し替え可能な実表をレンダリングする。pipe区切りの1行テキストで代用しない。
- 内部リンク：クリック可能なレンダリング済みアンカーとして表示する。
- Machine Result JSON内では`\n`、HTML、元記事形式のリンクmarkup等を保持してよい。
- Human LayerとMachine Layerは意味・順序・リンク先・アンカー・表セル内容を一致させるが、表示用markupのbyte一致は要求しない。

