# このプロジェクトをコピーして始める

このリポジトリは、物々交換を公開運営するためのOSSスターターです。サイト、交換ルール、Issueフォーム、運営手順、公開データ検査をまとめて再利用できます。

## 推奨: GitHub Templateとして複製する

1. リポジトリ上部の **Use this template** を押す
2. **Create a new repository** を選ぶ
3. 新しいリポジトリを作成する
4. ローカルへcloneする
5. 次のコマンドを実行する

```bash
python3 scripts/bootstrap.py \
  --name "あなたのプロジェクト名" \
  --tagline "あなたのタグライン" \
  --repo "https://github.com/YOUR-ACCOUNT/YOUR-REPOSITORY"
```

この処理で次をリセットします。

- サイト名、説明、GitHubリンク
- 現在の交換番号と交換品
- 交換履歴
- 交換記録

## 必ず確認する項目

- `RULES.md`: 対象地域、年齢、送料、禁止品、期限
- `PRIVATE_OPS.md`: 非公開連絡手段と削除手順
- `project/OPERATIONS.md`: 実際に運営できる手順か
- `.github/ISSUE_TEMPLATE/exchange-proposal.yml`: 入力項目
- `CONTENT-LICENSE.md`: 表示するクレジット

## GitHub設定

- Pages: `main` ブランチの `/docs` を公開
- Issues: On
- Discussions: 必要に応じてOn
- Actions: 公開データ検査を許可
- Template repository: 元リポジトリ側だけで必要。コピー先では任意

## ブランドと実績の扱い

仕組みや文章は再利用できますが、「わらしべコウタ」の名称・ロゴをそのまま使わないでください。また、原プロジェクトの実際の交換履歴や参加者写真を、自分の実績として掲載しないでください。

推奨クレジット例:

> Based on the Open Barter Project starter by わらしべコウタ: https://github.com/kota-kagarist/warashibe-kota

## 派生プロジェクトを知らせる

`PROJECTS.md` へPull Requestを送ると、派生プロジェクト一覧へ掲載できます。掲載は任意です。
