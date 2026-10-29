#!/usr/bin/env python3
"""공개 패키지의 자료 무결성과 이식·설치 동작을 확인합니다."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAMES = ("design-reference", "design-taste-frontend", "emil-design-eng")


def run(*arguments: str, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *arguments], cwd=cwd, capture_output=True, text=True, timeout=30
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def main() -> None:
    manifest = json.loads((ROOT / "sources.json").read_text())
    for entry in manifest["skills"]:
        path = ROOT / "skills" / entry["skill"] / "SKILL.md"
        require(hashlib.sha256(path.read_bytes()).hexdigest() == entry["packaged_skill_sha256"], f"변경된 스킬: {entry['skill']}")
        frontmatter = path.read_text().split("---", 2)[1]
        require(f"name: {entry['skill']}" in frontmatter, f"스킬 이름 불일치: {entry['skill']}")
        require("description:" in frontmatter, f"스킬 설명 누락: {entry['skill']}")
    for relative, expected in manifest["bundled_file_hashes"].items():
        require(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest() == expected, f"자료 변경: {relative}")

    with tempfile.TemporaryDirectory(prefix="design-skills-check-") as temporary:
        work = Path(temporary)
        listing = ROOT / "skills/design-reference/scripts/list_design_refs.py"
        result = run(str(listing), cwd=work)
        require(result.returncode == 0, result.stderr)
        require(len(result.stdout.splitlines()) == 54, "디자인 문서 수 불일치")
        result = run(str(listing), "linear", "--paths", cwd=work)
        require(result.returncode == 0 and "linear.app" in result.stdout, "브랜드 검색 실패")

        destination = work / "installed skills"
        result = run(str(ROOT / "install.py"), "--dest", str(destination), cwd=work)
        require(result.returncode == 0, result.stderr)
        for name in NAMES:
            require((destination / name / "SKILL.md").is_file(), f"설치 실패: {name}")
        result = run(str(destination / "design-reference/scripts/list_design_refs.py"), cwd=work)
        require(result.returncode == 0 and len(result.stdout.splitlines()) == 54, "설치 후 상대 경로 오류")

        marker = destination / "design-reference/user-marker.txt"
        marker.write_text("keep existing files")
        result = run(str(ROOT / "install.py"), "--dest", str(destination), cwd=work)
        require(result.returncode != 0 and marker.read_text() == "keep existing files", "기존 설치 보호 실패")

        selected = work / "selected"
        result = run(str(ROOT / "install.py"), "--dest", str(selected), "--skill", "emil-design-eng", cwd=work)
        require(result.returncode == 0, result.stderr)
        require(sorted(path.name for path in selected.iterdir()) == ["emil-design-eng"], "선택 설치 범위 오류")
        # 일부 스킬만 충돌해도 나머지 스킬을 복사하기 전에 중단해야 합니다.
        result = run(str(ROOT / "install.py"), "--dest", str(selected), cwd=work)
        require(result.returncode != 0, "부분 충돌 감지 실패")
        require(sorted(path.name for path in selected.iterdir()) == ["emil-design-eng"], "부분 충돌 시 파일 변경 발생")

    print("PASS: 3 skills, 54 references, integrity, relocated paths, install and conflict protection")


if __name__ == "__main__":
    main()
