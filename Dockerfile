FROM python:3.8-alpine
COPY requirements.txt /
RUN apk add --no-cache --update bash curl && \
    apk add --no-cache --virtual builddeps python3-dev libffi-dev openssl-dev cargo && \
    pip3 install -r /requirements.txt && \
    apk del builddeps
COPY *.py /
COPY *.json /
ENTRYPOINT ["python3", "/main.py"]
