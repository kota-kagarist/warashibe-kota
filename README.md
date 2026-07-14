# わらしべコウタ

> 交換は、次の使い道で決める。

モノとモノの交換を通じて、価格だけでは測れない価値と物語の変化を記録する公開プロジェクトです。同時に、同じ取り組みを始めたい人がコピーできる**OSSスターター**として運営しています。

## 自分の交換プロジェクトを始める

このリポジトリをGitHub Templateとして複製し、初期化スクリプトを実行すると、サイト・ルール・Issueフォーム・運営手順をまとめて再利用できます。

```bash
python3 scripts/bootstrap.py \
  --name "あなたのプロジェクト名" \
  --tagline "あなたのタグライン" \
  --repo "https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY"
```

詳しい手順: [`REUSE.md`](REUSE.md)

## このリポジトリで公開するもの

- プロジェクトサイトのソース
- 現在の交換品と交換履歴
- 交換ルールと判断基準
- 交換提案の受付と公開検討
- サイト改善、運営改善、意思決定の履歴
- 再利用用テンプレートと初期化スクリプト

## 公開しないもの

本名、住所、電話番号、メールアドレス、勤務先、配送ラベル、追跡番号、具体的な受け渡し場所など、個人を特定できる情報は公開しません。これらをIssue、Discussion、Pull Requestへ書き込まないでください。

交換が仮合意に進んだ後の連絡は、一時的な非公開手段で行い、完了後に不要な個人情報を削除します。

## ルールと運営

- [`RULES.md`](RULES.md) — 参加者向けの交換ルール
- [`project/OPERATIONS.md`](project/OPERATIONS.md) — 募集から完了までの運営手順
- [`PRIVATE_OPS.md`](PRIVATE_OPS.md) — 個人情報を扱う境界
- [`project/exchange-records/TEMPLATE.md`](project/exchange-records/TEMPLATE.md) — 交換記録テンプレート
- [`REUSE.md`](REUSE.md) — コピーして開始する手順

## サイトの設定とデータ

- `docs/data/site.json` — 名称、タグライン、リンク、テーマ色
- `docs/data/project.json` — 現在の状態と交換品
- `docs/data/exchanges.json` — 公開可能な交換履歴

交換が成立したら、Issueで経緯を整理し、Pull RequestでJSONと記録を更新します。`main`へのマージ後、GitHub Pagesへ反映されます。

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

## ライセンス

- コード: MIT License (`LICENSE-CODE`)
- ルール、運営文書、テンプレート、サンプル: CC BY 4.0 (`CONTENT-LICENSE.md`)
- 詳細な区分: [`LICENSE.md`](LICENSE.md)

プロジェクト名・ロゴ・実際の参加者コンテンツは、ライセンス対象外または個別条件です。コピー時は名称を変更してください。
