FROM python:3.11-slim-bullseye

LABEL maintainer = "Martijn Pepping <martijn.pepping@automiq.nl>"
LABEL org.opencontainers.image.authors = "Martijn Pepping <martijn.pepping@automiq.nl>"
LABEL org.opencontainers.image.description = "A simple webserver that accepts all incoming GET and POST requests"
LABEL org.opencontainers.image.source = "https://github.com/mpepping/request-logger"
LABEL org.opencontainers.image.title = "Request Logger"
LABEL org.opencontainers.image.url = "https://github.com/mpepping/request-logger/pkgs/container/request-logger"

ADD . /opt/app-root/src/
WORKDIR /opt/app-root/src

RUN python3 -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

ENV PATH=/opt/venv/bin:$PATH

EXPOSE 8080

ENTRYPOINT ["python", "run.py"]
