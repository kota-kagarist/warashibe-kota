# わらしべコウタ

> 交換は、次の使い道で決める。

モノとモノの交換を通じて、価格だけでは測れない価値と物語の変化を記録する公開プロジェクトです。

## このリポジトリで公開するもの

- プロジェクトサイトのソース
- 現在の交換品と交換履歴
- 交換ルールと判断基準
- 交換提案の受付と公開検討
- サイト改善、運営改善、意思決定の履歴
- GitHub Projectによる進捗

## 公開しないもの

本名、住所、電話番号、メールアドレス、勤務先、配送ラベル、追跡番号、具体的な受け渡し場所など、個人を特定できる情報は公開しません。これらをIssue、Discussion、Pull Requestへ書き込まないでください。

交換が仮合意に進んだ後の連絡は、一時的な非公開手段で行い、完了後に不要な個人情報を削除します。

## ルールと運営

- [`RULES.md`](RULES.md) — 参加者向けの交換ルール
- [`project/OPERATIONS.md`](project/OPERATIONS.md) — 募集から完了までの運営手順
- [`PRIVATE_OPS.md`](PRIVATE_OPS.md) — 個人情報を扱う境界
- [`project/exchange-records/TEMPLATE.md`](project/exchange-records/TEMPLATE.md) — 交換記録テンプレート

## データの更新

サイトの現在地は、次の2ファイルから自動表示されます。

- `docs/data/project.json` — 現在の状態と交換品
- `docs/data/exchanges.json` — 公開可能な交換履歴

交換が成立したら、Issueで経緯を整理し、Pull RequestでJSONと記録を更新します。`main`へのマージ後、GitHub Pagesへ自動反映されます。

## ローカル確認

```bash
python3 -m http.server 8000 --directory docs
```

ブラウザで `http://localhost:8000` を開きます。

## GitHubの使い分け

| 機能 | 用途 |
|---|---|
| Issues | 交換提案、改善タスク、判断が必要な作業 |
| Discussions | 雑談、アイデア、公開相談、投票 |
| Pull Requests | サイト、ルール、交換履歴の正式変更 |
| Projects | Inboxから完了までの進捗管理 |
| Pages | 公開サイト |

## 初期セットアップ

`project/GITHUB_SETUP.md` に、Pages・Discussions・Projects・ラベルの設定手順を記載しています。

## ライセンス

- サイトのソースコード: `LICENSE-CODE`（MIT License）
- 文章、交換記録、写真などのコンテンツ: `CONTENT-LICENSE.md`
