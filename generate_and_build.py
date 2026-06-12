"""armwrestling-girls-navi 自動記事生成エントリ
fitness_auto_post_lib.run() を呼ぶ薄ラッパ。
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
# 共通ライブラリは 007_自動投稿ブログ/ 配下
sys.path.insert(0, str(Path.home() / "000_ClaudeCode" / "007_自動投稿ブログ"))
import fitness_auto_post_lib as lib  # noqa: E402

CLAUDE_MD = (HERE / "CLAUDE.md").read_text(encoding="utf-8") if (HERE / "CLAUDE.md").exists() else ""

CFG = {
    "site_dir": HERE,
    "blog_name": "アームレスリング女子ナビ",
    "site_url": "https://musclelove-777.github.io/armwrestling-girls-navi",
    "twitter_site": "@MuscleGirlLove7",
    "accent_color": "#ff5722",
    "categories": [
        "選手紹介", "大会情報", "テクニック解説", "トレーニング", "コラム",
    ],
    "seed_topics": CLAUDE_MD,
    "image_query": "arm wrestling women",
}

if __name__ == "__main__":
    res = lib.run(CFG)
    print(res)
