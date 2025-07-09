# Dockerfile
# 주석문 아래의 내용으로 파일 생성

# Flask와 Python이 설치된 tiangolo 이미지 사용
FROM tiangolo/uwsgi-nginx-flask:python3.9
 
# 작업 디렉터리 설정
WORKDIR /app
 
# Flask 애플리케이션 파일 복사
COPY app.py /app
 
# 필요 시 추가 패키지 설치
# RUN pip install <additional-packages>
 
# uWSGI와 Nginx 비활성화 및 Flask 직접 실행
CMD ["python", "app.py"]
