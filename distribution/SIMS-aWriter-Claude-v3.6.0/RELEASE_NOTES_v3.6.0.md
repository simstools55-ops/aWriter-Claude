# aWriter v3.6.0

## Human Layer rich-copy support
- PUBLIC_OKの表を、Human Layerではレンダリング済み表として提示できるようにしました。
- PUBLIC_OKの内部リンクを、Human Layerではクリック可能なアンカーとして提示できるようにしました。
- リンク/表のHuman Layerコピー対象は、コードフェンスやblockquoteで囲まずWYSIWYGへコピーしやすい形にします。
- Machine Layerは元記事形式のHTML/Markdown等の実装markupとdestination URLを保持します。
- Human/Machine間は意味、URL、アンカー、表内容を一致させ、markup表現の差だけではFAILにしません。
- JSON ContractとShared v3.5.1 baselineは変更しません。

## Compatibility
- Existing internal-link implementation gate is retained on the Machine Layer.
- No manual href insertion is left to the user after PUBLIC_OK.
