#!/usr/bin/env python3
"""Initialize a copied Open Barter Project repository.

This script intentionally changes only project-specific public files. It never
creates or stores names, addresses, phone numbers, tracking numbers, or other
private exchange data.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]


def valid_repo_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme != "https" or parsed.netloc != "github.com":
        raise argparse.ArgumentTypeError("--repo must be an https://github.com/... URL")
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) != 2:
        raise argparse.ArgumentTypeError("--repo must point to owner/repository")
    return value.rstrip("/")


def write_json(path: Path, data: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a copied barter project")
    parser.add_argument("--name", required=True, help="Public project name")
    parser.add_argument("--tagline", required=True, help="Public tagline")
    parser.add_argument("--repo", required=True, type=valid_repo_url, help="New GitHub repository URL")
    parser.add_argument(
        "--description",
        default="物々交換の判断と履歴を公開するオープンプロジェクトです。",
    )
    parser.add_argument("--accent", default="#ff681c", help="CSS hex color, e.g. #ff681c")
    args = parser.parse_args()

    if not (args.accent.startswith("#") and len(args.accent) in {4, 7}):
        parser.error("--accent must be a 3- or 6-digit CSS hex color")

    site = json.loads((ROOT / "template/site.json").read_text(encoding="utf-8"))
    site.update(
        {
            "project_name": args.name,
            "tagline": args.tagline,
            "hero_line_1": args.tagline,
            "hero_line_2": "",
            "description": args.description,
            "repository_url": args.repo,
            "proposal_url": f"{args.repo}/issues/new?template=exchange-proposal.yml",
            "rules_url": f"{args.repo}/blob/main/RULES.md",
            "reuse_url": f"{args.repo}/blob/main/REUSE.md",
            "accent_color": args.accent,
            "theme_color": args.accent,
        }
    )
    write_json(ROOT / "docs/data/site.json", site)

    project = json.loads((ROOT / "template/project.json").read_text(encoding="utf-8"))
    project["repository_url"] = args.repo
    write_json(ROOT / "docs/data/project.json", project)
    shutil.copyfile(ROOT / "template/exchanges.json", ROOT / "docs/data/exchanges.json")

    record_dir = ROOT / "project/exchange-records"
    record_dir.mkdir(parents=True, exist_ok=True)
    for path in record_dir.glob("[0-9][0-9][0-9]-*.md"):
        path.unlink()
    shutil.copyfile(ROOT / "template/000-preparing.md", record_dir / "000-preparing.md")

    print("Initialized public project files.")
    print("Next: review RULES.md, PRIVATE_OPS.md, and project/OPERATIONS.md.")
    print("Then configure GitHub Pages to publish /docs and enable Issues.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
