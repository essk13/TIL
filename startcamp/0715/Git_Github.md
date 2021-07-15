# Git & Github

## 1. CLI사용

- **경로**
  - **절대경로**
    - = 어디서든 해당 위치로 이동
  - **상대경로**
    - 특정 기준에서 위치 설명
  - **~/**
    - home/ 홈 경로
  - **/**
    - root 경로

- **Command**

  - **cd (command directory)**
    - 폴더 이동
    - cd .. = 상위 폴더로 이동
    - cd 하위 폴더 명 = 하위 폴더로 이동
    - 어느 정도 작성 후 Tab 키 = 자동완성

  - **ls (list)**
    - 현재 폴더의 하위 폴더, 파일 리스트 보기

  - **touch**
    - touch 파일 명 = 현재 폴더에 파일 명 파일 생성

  - **mkdir (makedirectory)**
    - mkdir 폴더 명 = 현재 폴더에 하위 폴더 명 폴더 생성

## 2. git 시스템이란?

- **버전 관리 시스템**
  - 일반적
    - 자료 간 차이(diff)를 확인하기 어려움
  - 버전 관리(git)
    - history, log를 함께 저장하여 자료 간 차이(diff)를 확인하기 용이함
- **분산 버전 관리 시스템**
  - 코드의 history 관리 도구
  - 프로젝트 이전 버전의 복원, 비교, 분석, 병합이 가능
- **다양한 버전 관리 시스템**
  - 로컬 버전 관리 시스템
    - 해당 PC 환경에서 버전 관리
  - 중앙집중식 버전 관리 시스템
    - 하나의 장소에서 버전 관리
  - 분산 버전 관리 시스템
    - 여러 장소에서 버전 관리

## 3. github 서비스 작업 흐름

- **git 작업 흐름**

  ![git_wave](Git_Github.assets/git_wave.PNG)

  |  n.  | command |                           content                            |
  | :--: | :-----: | :----------------------------------------------------------: |
  |  ①   |  init   | git 시스템 관리 시작 / .git 폴더 생성(숨긴폴더) / 3가지 가상 공간 생성(Working directory, Staging area, Commit) |
  |  ②   |   add   |   Working directory에서 관리할 파일을 Staging Area로 전달    |
  |  ③   | commit  | Staging Area에서 확인한 파일을 commit 영역으로 전달, 히스토리 축적(내PC) |
  |  ④   |  push   |         Commit영역의 파일, 히스토리를 github로 전달          |
  |  ⑤   |  clone  | github에 저장된 파일, 히스토리를 git 시스템으로 관리하지 않는 장소에 불러오기 |
  |  ⑥   |  pull   |          github에 저장된 파일, 히스토리를 내려받기           |

## 4. git(github) 사용방법

- **git init**

  - .git 폴더 생성 (git 시스템 관리 시작)
  - TERMINAL 절대주소에 (branch 명) 생성
    - init 전 branch 명 생성 확인 (중복 자제)

- **git add**

  - Working directory에서 관리할 파일을 Staging Area로 전달

    - ./ = 현재폴더, ../ = 상위폴더, 폴더명/ = 폴더

  - **git status**

    ```
    ▷ Changes to be committed (Staging Area)
    			new file : abc.py (add 한 항목)
    ▷ Untracked files (warking Directory)
    			efg.py (add 하지 않은 항목)
    ```

  - 파일 수정, 새 파일 생성 시

    - 수정 = 파일명 옆 M 표시
    - 생성 = 파일명 옆 U 표시

  - **.gitignore**

    - github에 업로드 하지 않을 파일 (민감한 자료, 쓸모 없는 자료)
    - Untraked 상황의 파일만 제거 (Staging 상황의 파일은 적용 X)

  - **git retore abc.py**

    - Staging Area에서 파일 제거

- **git commit -m 'log'**

  - commit 시 -m 'log' 작성 필수 (미작성 시 commit X)
  - 첫 commit log = 'first commit'

- **git push 업로드할 github brunch명**

  - github 사이트에서 new repository 생성

  - git remote add 이름 'git 주소'

    ```
    git push origin(github명) main(branch명)
    ```

- **git clone '주소'**

  - github에 저장된 파일, 히스토리를 git 시스템으로 관리하지 않는 장소에 불러오기

- **git pull**

  - github에 저장된 파일, 히스토리를 내려받기

- **git log**

  - key 'q' 입력 시 log 종료
  - **git log __oneline**
    - 로그 한줄로 보기

- **추가사항**

  - 실수로 push를 하지 않았을 경우

    - 다음번 pull 시 conflict(충돌) 발생

      → 올바른 파일 선택 후 merge(결합) 하여 pull 실시

      ※ merge를 하지 않고 수정 후 push 실시 → Error 발생 → 다시 pull 후 수정 → push 실시
