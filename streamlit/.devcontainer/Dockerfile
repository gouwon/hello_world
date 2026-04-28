FROM python:3.11-slim

# 패키지 업데이트와 필수 라이브러리 최소 설치
RUN apt-get update && apt-get install -y \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Streamlit 설치
RUN pip install --no-cache-dir streamlit
