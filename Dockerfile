FROM python:3.9.19-slim

WORKDIR /api

COPY . .

RUN pip3 install --no-cache-dir -r requirements.txt

ENV MINIO_ACCESS_KEY: "MINIO_ACCESS_KEY"
ENV MINIO_SECRET_KEY: "MINIO_SECRET_KEY"

EXPOSE 5000

CMD ["python", "api/app.py"]