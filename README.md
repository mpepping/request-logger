# request-logger

A simple webserver that accepts all GET and POST requests. Useful for analyzing or troubleshooting HTTP requests. The app listens by default on port 8080/tcp. Optionally, the port can be specified as an argument (e.g., `CMD`).

## Running the container

```lang=shell
docker run -ti --rm -p 8080:8080 docker pull ghcr.io/mpepping/request-logger:latest
```
