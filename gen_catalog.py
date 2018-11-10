# coding: utf-8

import os
import re
import operator

from utils import load_articles


def gen_catalog(posts_dir, output_file, headers, footers, relative_path):
    articles = load_articles("./articles")

    with open(output_file, "w+") as f:
        # clear all the contents in file
        f.truncate()

        for header in headers:
            f.write(header)
            f.write("\n\n")

        # write catalog
        for title, date, filename in articles:
            f.write(
                "- {date} - [{title}](https://jiajunhuang.com/{relative_path}/{filename}.html)\n".format(
                    date=date,
                    title=title,
                    relative_path=relative_path,
                    filename=filename,
                )
            )

        for footer in footers:
            f.write(footer)
            f.write("\n\n")


if __name__ == "__main__":
    # README.md
    readme_headers = [
        "# Jiajun's Blog",
        "会当凌绝顶，一览众山小。",
        "- [关于我](https://jiajunhuang.com/aboutme)",
        "- 欢迎订阅Telegram Channel：分享后端相关的精选文章",
        "https://t.me/jiajunhuangcom",
        "## 目录",
    ]
    readme_footers = [
        "\n",
        "--------------------------------------------",
        "禁止转载",
    ]
    gen_catalog(
        "articles",
        "./README.md",
        readme_headers,
        readme_footers,
        "articles",
    )
