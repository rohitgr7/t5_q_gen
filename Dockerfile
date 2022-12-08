FROM tiangolo/uvicorn-gunicorn:python3.9-slim

COPY requirements/base.txt /tmp/base.txt
ENV MAX_WORKERS="1"
ENV WEB_CONCURRENCY="1"
RUN pip install --no-cache-dir -r /tmp/base.txt

COPY ./app /app