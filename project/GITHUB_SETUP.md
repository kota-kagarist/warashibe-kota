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

Settings → Pages → Source を **Deploy from a branch / main / docs** に設定します。

`main`の `docs/` に変更が入るとGitHub Pagesへ反映されます。Actions方式へ切り替える場合は `.github/workflows/deploy-pages.yml` を使用します。

## Discussionsの推奨カテゴリ

- Announcements — 交換成立、募集開始、ルール変更
- 交換アイデア — 具体提案前の相談
- アイデア — 企画やサイト改善
- Q&A — ルールへの質問
- Polls — 次の方向性に関する投票

交換として正式に検討する段階になったらIssueへ移します。

## 推奨ラベル

### Type

- `type:exchange`
- `type:improvement`
- `type:decision`
- `type:site`
- `type:rules`

### Status

- `status:preparing`
- `status:inbox`
- `status:open`
- `status:review`
- `status:provisional`
- `status:shipping`
- `status:verifying`
- `status:completed`
- `status:paused`
- `status:declined`
- `status:cancelled`
- `status:expired`

### Privacy

- `privacy:check-required`
- `privacy:passed`
- `privacy:blocked`

## GitHub Project

Project名: `わらしべコウタ — Public Roadmap`

推奨フィールド:

- Status: Preparing / Inbox / Open / Review / Provisional / Shipping / Verifying / Completed / Paused / Declined / Cancelled / Expired
- Type: Exchange / Site / Rules / Decision
- Exchange No.: Number
- Public Update: Date
- Privacy Check: Not checked / Passed / Blocked
- Deadline: Date

## 非公開運営

住所、電話番号、配送ラベル、追跡番号などはGitHubへ恒久保存しません。仮合意後だけ一時的な非公開連絡手段を使い、交換完了・中止後30日以内に削除します。
