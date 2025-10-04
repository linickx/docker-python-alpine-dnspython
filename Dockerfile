FROM python:alpine
LABEL maintainer="Nick <linickx.com>"
LABEL version="0.1"

COPY test.py /app/

WORKDIR /app

RUN pip install dnspython

ENTRYPOINT ["python"]
CMD ["test.py"]
