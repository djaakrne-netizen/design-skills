#!/usr/bin/env python3
"""선택한 스킬을 기존 파일을 덮어쓰지 않고 설치합니다."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SKILLS = ("design-reference", "design-taste-frontend", "emil-design-eng")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", required=True, type=Path, help="에이전트의 스킬 디렉터리")
    parser.add_argument("--skill", action="append", choices=SKILLS, help="생략하면 세 스킬 설치")
    args = parser.parse_args()
    selected = list(dict.fromkeys(args.skill or SKILLS))
    source_root = Path(__file__).resolve().parent / "skills"
    destination = args.dest.expanduser().resolve()

    # 모든 충돌을 먼저 확인해 기존 설치를 그대로 보존합니다.
    if destination == source_root or source_root in destination.parents:
        parser.error("원본 skills 디렉터리 안에는 설치할 수 없습니다.")
    if destination.exists() and not destination.is_dir():
        parser.error("설치 대상은 디렉터리여야 합니다.")
    conflicts = [name for name in selected if (destination / name).exists() or (destination / name).is_symlink()]
    if conflicts:
        print("기존 스킬이 있어 설치하지 않았습니다: " + ", ".join(conflicts), file=sys.stderr)
        return 1
    for name in selected:
        if not (source_root / name / "SKILL.md").is_file():
            parser.error(f"스킬 원본을 찾을 수 없습니다: {name}")

    destination.mkdir(parents=True, exist_ok=True)
    for name in selected:
        shutil.copytree(
            source_root / name,
            destination / name,
            ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store"),
        )
        print(f"설치 완료: {destination / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
