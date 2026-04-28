# Streamlit Hello World 프로젝트

이 프로젝트는 [Streamlit](https://streamlit.io/)을 사용한 간단한 "Hello, World" 웹 앱 예제입니다. VS Code Dev Container를 사용하여 격리된 환경에서 실행하거나, 로컬 Python 환경에서 직접 실행할 수 있습니다.

## 🚀 1. Dev Container로 실행하기 (권장)

개발 환경을 설정할 필요 없이 VS Code와 Docker만 있으면 즉시 실행 가능합니다.

1.  프로젝트 폴더를 VS Code로 엽니다.
2.  VS Code 오른쪽 하단에 "Reopen in Container" 알림이 뜨면 클릭합니다.
    * (알림이 없다면 `F1` 키 입력 -> `Dev Containers: Reopen in Container` 선택)
3.  컨테이너가 빌드될 때까지 잠시 기다립니다.
4.  VS Code 내장 터미널이 열리면 다음 명령어를 입력합니다:
    ```bash
    streamlit run app.py
    ```
5.  터미널에 출력된 URL(일반적으로 `http://localhost:8501`)을 클릭하여 접속합니다.

---

## 💻 2. 로컬 환경에서 직접 실행하기

Docker를 사용하지 않고 로컬 Python 환경에서 실행하는 방법입니다.

### 사전 요구 사항
* Python 3.8 이상이 설치되어 있어야 합니다.

### 실행 단계
1.  프로젝트 폴더로 이동합니다.
2.  필요한 패키지를 설치합니다:
    ```bash
    pip install -r requirements.txt
    ```
3.  앱을 실행합니다:
    ```bash
    streamlit run app.py
    ```
4.  브라우저에서 `http://localhost:8501`로 접속합니다.

---

## 📂 프로젝트 구조

* `.devcontainer/`: Dev Container 설정을 위한 파일들 (`devcontainer.json`, `Dockerfile`)
* `app.py`: Streamlit 앱 메인 코드
* `requirements.txt`: 의존성 라이브러리 목록