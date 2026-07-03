#!/usr/bin/env python3
"""Copy README files into docs/ for MkDocs build (single source of truth stays in plugin folders)."""

from __future__ import annotations

import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO_LICENSE_URL = "https://github.com/shiyuugohirao/BrightAuthor-Plugins/blob/main/LICENSE"
LANG_SWITCH_LINE = re.compile(
    r"^> \[(?:日本語版はこちら|English version)\]\([^)]+\)\s*\n",
    re.MULTILINE,
)

PLUGIN_DIRS = [
    "Blank-Plugin-Template",
    "4K-Image-Playback",
    "Download-and-Play",
    "Framerate-Matcher",
    "Play-File",
    "Rotate-and-Seek",
    "Screenshot-and-Playback",
    "Subtitles-Widget",
    "Media-Server",
    "Media-Server-RTSP",
    "TCP-Network-Command",
    "UDP-CR-Command-Sender",
    "UDP-Hex-CR-Command-Sender",
    "Telnet-Enable",
    "Pronto-Hex-Transmitter",
    "Widget-Hide-or-Show",
    "Change-Ticker-Separator",
    "Touch-Audio-Feedback",
    "Send-User-Variables-To-HTML",
    "HTMLZoneMessage",
    "ChromaLuma-Key-Editor",
    "Set-Video-Mode",
    "Screenshot-with-URL",
    "Add-To-Cloud",
    "Setup-with-Publish",
    "Publish-Node",
    "Add-Client-Certificates",
    "Restore-Presentation",
    "Player-Rename-Local-File-Networking",
    "System-Log-Saver",
    "PDF-Printer",
    "Variable-Countdown",
]


def rewrite_links(content: str, *, japanese: bool) -> str:
    """Rewrite GitHub-oriented README links for MkDocs paths."""
    suffix = "ja" if japanese else ""
    index_name = f"index.{suffix}.md" if japanese else "index.md"
    other_index = "index.md" if japanese else "index.ja.md"

    for plugin in PLUGIN_DIRS:
        if japanese:
            content = content.replace(
                f"]({plugin}/README_ja.md)",
                f"](plugins/{plugin}/{index_name})",
            )
            content = content.replace(
                f"](../{plugin}/README_ja.md)",
                f"](../{plugin}/{index_name})",
            )
            content = content.replace(
                f"](../{plugin}/)",
                f"](../{plugin}/{index_name})",
            )
        else:
            content = content.replace(
                f"]({plugin}/README.md)",
                f"](plugins/{plugin}/{index_name})",
            )
            content = content.replace(
                f"](../{plugin}/README.md)",
                f"](../{plugin}/{index_name})",
            )
            content = content.replace(
                f"](../{plugin}/)",
                f"](../{plugin}/{index_name})",
            )

    if japanese:
        content = content.replace("](README.md)", f"]({other_index})")
        content = content.replace("](README_ja.md)", "](index.ja.md)")
    else:
        content = content.replace("](README_ja.md)", f"]({other_index})")
        content = content.replace("](README.md)", "](index.md)")

    content = LANG_SWITCH_LINE.sub("", content)
    content = re.sub(r"\]\(LICENSE\)", f"]({REPO_LICENSE_URL})", content)
    return content


def copy_readme(src: Path, dest: Path, *, japanese: bool) -> None:
    if not src.is_file():
        raise FileNotFoundError(f"Missing source file: {src}")
    dest.parent.mkdir(parents=True, exist_ok=True)
    content = src.read_text(encoding="utf-8")
    dest.write_text(rewrite_links(content, japanese=japanese), encoding="utf-8")


def sync_assets() -> None:
    assets = ROOT / "site-assets" / "stylesheets"
    if not assets.is_dir():
        return
    dest = DOCS / "stylesheets"
    dest.mkdir(parents=True, exist_ok=True)
    for css in assets.glob("*.css"):
        shutil.copy2(css, dest / css.name)


def main() -> None:
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()

    copy_readme(ROOT / "README.md", DOCS / "index.md", japanese=False)
    copy_readme(ROOT / "README_ja.md", DOCS / "index.ja.md", japanese=True)

    for plugin in PLUGIN_DIRS:
        plugin_root = ROOT / plugin
        plugin_docs = DOCS / "plugins" / plugin
        copy_readme(plugin_root / "README.md", plugin_docs / "index.md", japanese=False)
        copy_readme(
            plugin_root / "README_ja.md",
            plugin_docs / "index.ja.md",
            japanese=True,
        )

    sync_assets()
    print(f"Synced documentation into {DOCS.relative_to(ROOT)}/")


if __name__ == "__main__":
  main()
