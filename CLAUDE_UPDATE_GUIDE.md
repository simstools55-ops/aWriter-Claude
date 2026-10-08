> v4.0.0: Manager正規依頼受付ゲートを追加。Claude Project Instructionsの更新が必須。詳細: docs/SIMS_WRITER_REQUEST_GATE_V4.md

# Claude Project更新ガイド

対象：SIMS Writer Claude 3.3.2-RC1

1. Claude Projectの既存Knowledgeファイルをすべて削除します。
2. `Claude-Upload/`を開き、中身をすべてアップロードします。
3. `CLAUDE_PROJECT_INSTRUCTIONS.md`の本文をProject Instructions欄へ貼り付けます。
4. 新しいチャットで`DEPLOYMENT_TEST.md`の確認文を実行します。
5. Product Version `3.3.2-RC1`、Shared Version `3.5.0`が一致することを確認します。

`shared/SNAPSHOT_MANIFEST.json`や`shared/VERSION`は投入禁止です。正本は`shared/platform/SNAPSHOT_MANIFEST.json`です。
