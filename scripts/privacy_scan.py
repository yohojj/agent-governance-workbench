from __future__ import annotations

import re
import sys
from pathlib import Path

# Prefixes are assembled from fragments so this scanner does not flag its own detector strings.
SECRET_PATTERNS = [
    re.compile("s" + "k-" + r"[A-Za-z0-9_-]{20,}"),
    re.compile("g" + "hp_" + r"[A-Za-z0-9_]{20,}"),
    re.compile("github" + "_pat_" + r"[A-Za-z0-9_]{20,}"),
    re.compile(r"Bearer\s+[A-Za-z0-9._-]{20,}", re.IGNORECASE),
    re.compile(r"(api[_-]?key|token|secret|password)\s*[:=]", re.IGNORECASE),
]

BLOCKED_FILES = {".env", ".DS_Store"}
BLOCKED_SUFFIXES = {".log", ".pid", ".pem", ".key"}
SKIP_DIRS = {".git", ".venv", "__pycache__"}
ALLOWED_BINARY_ASSET_SUFFIXES = {".gif", ".jpeg", ".jpg", ".png", ".webp"}
ALLOWED_BINARY_ASSET_PARTS = ("docs", "assets")
MAX_REVIEWED_ASSET_BYTES = 1_000_000


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file():
            yield path


def is_reviewed_public_asset(rel: Path, path: Path) -> bool:
    return (
        rel.parts[:2] == ALLOWED_BINARY_ASSET_PARTS
        and path.suffix.lower() in ALLOWED_BINARY_ASSET_SUFFIXES
        and path.stat().st_size <= MAX_REVIEWED_ASSET_BYTES
    )


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    findings: list[str] = []

    for path in iter_files(root):
        rel = path.relative_to(root)
        if path.name in BLOCKED_FILES or path.suffix in BLOCKED_SUFFIXES:
            findings.append(f"blocked file: {rel}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            if is_reviewed_public_asset(rel, path):
                continue
            findings.append(f"binary or non-utf8 file requires review: {rel}")
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"secret-like pattern in {rel}: {pattern.pattern}")

    if findings:
        print("PRIVACY_SCAN_FAIL")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("PRIVACY_SCAN_PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
