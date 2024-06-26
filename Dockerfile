FROM python:3.10-slim
LABEL maintainer="Mr. Liid"

WORKDIR /app

COPY . .

ENTRYPOINT [ "python3", "main.py" ]