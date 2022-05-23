FROM python:3.10-slim-bullseye

LABEL maintainer "Martijn Pepping <martijn.pepping@automiq.nl>"
LABEL org.opencontainers.image.source https://github.com/mpepping/request-logger

ADD . /opt/app-root/src/
WORKDIR /opt/app-root/src

RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PATH=/opt/venv/bin:$PATH

EXPOSE 8080

ENTRYPOINT ["python", "run.py"]
