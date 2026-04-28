#!/bin/bash

# 프로젝트 폴더가 없으면 생성
if [ ! -d "hello_world" ]; then
  echo "🚀 Creating new Flutter project..."
  flutter create hello_world
fi

cd hello_world

# 웹 서버 모드로 실행 (포트 8080)
echo "🌐 Starting Flutter Web Server on port 8080..."
flutter run -d web-server --web-port 8080 --web-hostname 0.0.0.0
