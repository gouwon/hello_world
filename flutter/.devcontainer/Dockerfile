FROM mcr.microsoft.com/devcontainers/base:ubuntu
# 플러터 실행에 필요한 라이브러리 설치
RUN apt-get update && apt-get install -y \
    curl git unzip xz-utils zip libglu1-mesa
# 플러터 SDK 다운로드 및 설정
RUN git clone https://github.com/flutter/flutter.git -b stable /opt/flutter
ENV PATH="/opt/flutter/bin:$PATH"
RUN git config --global --add safe.directory /opt/flutter
RUN chown -R vscode:vscode /opt/flutter

# 환경 변수 설정
ENV PATH="/opt/flutter/bin:$PATH"

# 사용자 전환 후 플러터 사전 준비
USER vscode
RUN flutter doctor
