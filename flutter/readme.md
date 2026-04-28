# 🚀 Flutter Hello World (Dev Container)

이 프로젝트는 Docker Dev Container 환경에서 플러터를 실행하기 위한 예제입니다.

## 🛠 실행 방법

### 1. Dev Container에서 실행 (권장)
이 방식은 로컬에 플러터를 설치할 필요가 없습니다.
1.  VS Code에서 이 폴더를 엽니다.
2.  `F1` 키를 누르고 **"Dev Containers: Reopen in Container"**를 선택합니다.
3.  컨테이너 빌드가 완료되면 터미널에서 다음 스크립트를 실행합니다:
    ```bash
    ./run_app.sh
    ```
4.  브라우저에서 `http://localhost:8080`으로 접속합니다.

### 2. 로컬 환경에서 실행
로컬에 Flutter SDK가 이미 설치되어 있어야 합니다.
1.  터미널을 엽니다.
2.  프로젝트 생성 및 실행:
    ```bash
    flutter create hello_world
    cd hello_world
    flutter run -d chrome
    ```

## 📝 참고 사항
- 컨테이너 내부에서 실행 시 `--web-hostname 0.0.0.0` 옵션을 주어야 외부(호스트 OS) 브라우저에서 접근이 가능합니다.
- `flutter doctor` 명령을 통해 언제든 개발 환경 상태를 점검할 수 있습니다.
