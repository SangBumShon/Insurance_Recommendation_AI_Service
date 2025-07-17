#!/bin/bash

echo "🚀 Talk2Sell 프로젝트 배포를 시작합니다..."

# 1. 백엔드 배포
echo "📦 백엔드 배포 중..."
cd backend

# 환경 변수 파일 생성 (실제 값으로 수정 필요)
if [ ! -f .env ]; then
    echo "⚠️  .env 파일이 없습니다. env_example.txt를 참고하여 .env 파일을 생성하세요."
    exit 1
fi

# Docker 이미지 빌드 및 실행
docker-compose down
docker-compose build
docker-compose up -d

echo "✅ 백엔드 배포 완료!"

# 2. 모델 서버 배포
echo "🤖 모델 서버 배포 중..."
cd ../model_server

# 포트 충돌 방지를 위해 포트 변경
sed -i 's/8000:8000/8001:8000/' docker-compose.yml

docker-compose down
docker-compose build
docker-compose up -d

echo "✅ 모델 서버 배포 완료!"

# 3. 프론트엔드 빌드 및 배포
echo "🌐 프론트엔드 배포 중..."
cd ../frontend

# 환경 변수 파일 생성 (실제 값으로 수정 필요)
if [ ! -f .env ]; then
    echo "⚠️  .env 파일이 없습니다. env_example.txt를 참고하여 .env 파일을 생성하세요."
    exit 1
fi

# 빌드
npm install
npm run build

# Nginx 설정 (선택사항)
echo "📝 Nginx 설정 예시:"
echo "sudo apt install nginx"
echo "sudo cp -r build/* /var/www/html/"
echo "sudo systemctl restart nginx"

echo "🎉 배포가 완료되었습니다!"
echo "📊 서비스 상태 확인:"
echo "  - 백엔드: http://your_server_ip:8000"
echo "  - 모델 서버: http://your_server_ip:8001"
echo "  - 프론트엔드: http://your_server_ip" 