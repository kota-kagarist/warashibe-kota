# ADR-000: プロジェクトを公開管理する

- Status: Accepted
- Date: 2026-07-14

## Context

交換の経緯、判断、サイト更新を一か所に集約し、企画の透明性と継続性を高めたい。

## Decision

- サイト、ルール、交換履歴、改善作業を公開GitHubリポジトリで管理する
- タスクはIssues、会話はDiscussions、正式変更はPull Requestsで扱う
- GitHub Pagesでサイトを公開する
- 個人を特定できる情報は公開しない
- 住所等の機微情報をGitHubへ恒久保存しない

## Consequences

- 意思決定と変更履歴が公開される
- 交換提案は公開情報だけで行う必要がある
- 公開前のプライバシーチェックが必須になる
