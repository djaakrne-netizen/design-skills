# Design Skills

기존 디자인 스킬 3개를 다른 컴퓨터에서도 사용할 수 있도록 묶은 저장소입니다. 특정 과제에 맞춰 축약하지 않았으며, 로컬에 설치돼 있던 지침을 보존했습니다.

| 스킬 | 역할 |
| --- | --- |
| [design-reference](skills/design-reference/SKILL.md) | 브랜드별 디자인 문서, 한국·글로벌 UI, Figma 및 코드 컴포넌트 참고 자료 선택 |
| [design-taste-frontend](skills/design-taste-frontend/SKILL.md) | 소개 페이지·포트폴리오·리디자인의 시각적 방향과 구현 지침 |
| [emil-design-eng](skills/emil-design-eng/SKILL.md) | 인터페이스 사용성, 컴포넌트, 모션과 세부 상호작용 지침 |

## 바로 사용하기

```bash
git clone --depth 1 https://github.com/djaakrne-netizen/design-skills.git
```

클론한 프로젝트의 코딩 에이전트에 다음처럼 요청할 수 있습니다. 별도 설치 없이 파일을 직접 읽는 방식입니다.

```text
design-skills/skills/design-reference/SKILL.md를 읽고 적용해줘.
프로젝트의 목적과 기존 구성을 확인한 뒤 필요한 참고 문서만 읽어줘.
```

```text
design-skills/skills/design-taste-frontend/SKILL.md를 읽고
이번 소개 페이지의 디자인과 구현에 적용해줘.
```

```text
design-skills/skills/emil-design-eng/SKILL.md를 읽고
현재 화면의 버튼·메뉴·팝업과 모션을 검토해줘.
```

실제 클론 위치가 다르면 위 파일 경로를 변경하세요. 세 스킬을 매번 동시에 적용할 필요는 없습니다.

## 스킬 폴더로 설치하기

Python 3.10 이상만 필요하며 추가 라이브러리를 설치하지 않습니다. 대상 경로는 사용하는 에이전트가 지원하는 스킬 디렉터리로 지정하세요.

Codex 사용자 스킬 디렉터리를 사용하는 환경의 예:

```bash
python3 design-skills/install.py --dest "$HOME/.codex/skills"
```

한 개만 설치하려면:

```bash
python3 design-skills/install.py --dest "$HOME/.codex/skills" --skill design-reference
```

- 대상에 같은 이름의 폴더가 하나라도 있으면 아무것도 복사하지 않고 중단합니다. 기존 스킬을 자동으로 덮어쓰지 않습니다.
- 기존 설치가 있다면 별도 경로를 지정하거나, 위의 파일 직접 읽기 방식을 이용하세요.
- 설치 후 새 세션에서 스킬 목록을 확인하세요. 자동 인식 여부는 에이전트와 버전에 따라 다르며, 인식되지 않으면 파일을 직접 읽도록 요청할 수 있습니다.
- API 키, 계정 로그인, MCP 서버, 플러그인은 설치하지 않습니다.

## 동봉된 디자인 참고 자료

`design-reference/references/brands/`에는 [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)의 브랜드별 `DESIGN.md` 54개가 포함돼 있습니다. 원문 파일은 그대로 보존했으며 해당 저작권과 라이선스도 함께 제공합니다. 각 자료는 브랜드에서 공식 배포한 디자인 시스템으로 간주하지 마세요.

어느 작업 디렉터리에서도 목록을 확인할 수 있습니다.

```bash
python3 design-skills/skills/design-reference/scripts/list_design_refs.py
python3 design-skills/skills/design-reference/scripts/list_design_refs.py linear --paths
```

설치된 스킬이라면 경로의 `design-skills/skills/` 부분을 실제 설치 경로로 바꾸세요.

동봉된 문서는 오프라인으로 읽을 수 있습니다. UI Bowl·Figma·Select Codes 등 라이브 자료는 별도의 네트워크 접근·계정·도구가 필요할 수 있습니다. 이 저장소가 그러한 연결이나 접근 권한을 제공하지는 않습니다.

## 보존 범위와 변경 사항

- `design-taste-frontend`와 `emil-design-eng`의 `SKILL.md`는 패키징 당시의 로컬 설치본과 동일합니다. 최신 upstream 버전으로 교체하지 않았습니다.
- `design-reference`는 개인 PC의 절대 경로를 동봉 자료의 상대 경로로 변경했습니다. 외부 로컬 저장소에 대한 필수 의존성을 제거했습니다.
- 참고 자료 목록 스크립트는 자신의 설치 위치를 기준으로 자료를 찾습니다. `--root` 옵션으로 다른 자료 폴더를 지정할 수도 있습니다.
- 개인적으로 저장한 Figma 파일 식별자는 포함하지 않습니다. 현재 작업에서 접근 가능한 공개 키트나 사용자가 제공한 파일을 선택하도록 안내합니다.
- Taste의 `blocks/` 설명은 확장용 구조이며 이 스냅샷에 블록 구현 파일은 포함되지 않습니다.

출처와 라이선스 구분은 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), 스냅샷 정보는 [sources.json](sources.json)을 확인하세요.

## 검증하기

```bash
python3 scripts/validate_package.py
```

저장소 루트에서 실행합니다. 파일 무결성, 스킬 구조, 동봉 자료 수, 다른 작업 경로에서의 목록 조회, 설치 및 기존 파일 보존 동작을 확인합니다. 이 검증은 실제 AI 결과물의 디자인 품질이나 모든 에이전트 버전의 자동 스킬 인식을 보장하지 않습니다.

## 라이선스

패키징 코드와 `design-reference` 지침에는 루트의 [MIT License](LICENSE)가 적용됩니다. 외부 스킬 및 디자인 문서에는 각각 동봉된 원저작자의 라이선스가 적용됩니다. 링크된 웹사이트·글꼴·이미지·Figma 자료 등은 이 저장소의 라이선스에 포함되지 않습니다.
