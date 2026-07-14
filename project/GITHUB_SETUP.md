# GitHub初期設定

## 公開リポジトリ

- Repository: `kota-kagarist/warashibe-kota`
- Visibility: Public
- Default branch: `main`
- Issues: On
- Discussions: On
- Projects: On
- Wiki: Off

## GitHub Pages

Settings → Pages → Source を **GitHub Actions** に設定します。

`main`へ変更が入ると `.github/workflows/deploy-pages.yml` が `docs/` を公開します。

## Discussionsの推奨カテゴリ

- Announcements — 交換成立、募集開始、ルール変更
- 交換アイデア — 具体提案前の相談
- アイデア — 企画やサイト改善
- Q&A — ルールへの質問
- Polls — 次の方向性に関する投票

交換として正式に検討する段階になったらIssueへ移します。

## 推奨ラベル

- `type:exchange`
- `type:improvement`
- `type:decision`
- `type:site`
- `status:inbox`
- `status:review`
- `status:negotiating`
- `status:agreed`
- `status:shipping`
- `status:completed`
- `status:declined`
- `privacy:check-required`

## GitHub Project

Project名: `わらしべコウタ — Public Roadmap`

推奨フィールド:

- Status: Inbox / Review / Negotiating / Agreed / Shipping / Completed / Declined
- Type: Exchange / Site / Rules / Decision
- Exchange No.: Number
- Public Update: Date
- Privacy Check: Not checked / Passed / Blocked

## 非公開運営

住所、電話番号、配送ラベル、追跡番号などはGitHubへ恒久保存しません。仮合意後だけ一時的な非公開連絡手段を使い、交換完了後に削除します。
