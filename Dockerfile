FROM python:alpine
LABEL maintainer="Nick <linickx.com>"
LABEL version="0.1"

WORKDIR /app

RUN pip install dnspython

ENTRYPOINT ["python"]
