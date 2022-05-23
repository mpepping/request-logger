# request-logger

A simple webserver that accepts all GET and POST requests. Useful for analyzing or troubleshooting HTTP requests. The app listens by default on port 8080/tcp. Optionally, the port can be specified as an argument (e.g., `CMD`).

## To build the container

`docker build -t docker.io/mpepping/request-logger:latest`

## To run the container

`docker run -ti --rm -p 8080:8080 docker.io/mpepping/request-logger:latest`
