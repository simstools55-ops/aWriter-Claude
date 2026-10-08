> v4.0.0: Manager正規依頼受付ゲートを追加。Claude Project Instructionsの更新が必須。詳細: docs/SIMS_WRITER_REQUEST_GATE_V4.md

# Claude Project更新手順

Version: 0.15.3-alpha.1

1. ClaudeでSIMS WriterのProjectを開きます。
2. 現在登録されている旧`CLAUDE_PROJECT_INSTRUCTIONS.md`の内容を削除します。
3. 本パッケージの`CLAUDE_PROJECT_INSTRUCTIONS.md`をProject Instructionsへ全文貼り付けます。
4. 旧Knowledge Packを削除します。
5. `knowledge/SIMS_WRITER_KNOWLEDGE_PACK.md`をProject Knowledgeへアップロードします。
6. 旧版と新版が同時に参照されていないことを確認します。
7. `partial`モードで実記事再テストを行います。
