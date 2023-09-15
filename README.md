# request-logger

A simple webserver that accepts all GET and POST requests. Useful for analyzing or troubleshooting HTTP requests. Requests are logged to stdout. The app listens by default on port 8080/tcp. Optionally, the port can be specified as an argument (e.g., `CMD`).

To run the app as a container:

```lang=shell
docker run -ti --rm -p 8080:8080 ghcr.io/mpepping/request-logger:latest
```

Or as a k8s deployment + service :

```lang=yaml
---
kind: Namespace
apiVersion: v1
metadata:
  name: request-logger
---
kind: Deployment
apiVersion: apps/v1
metadata:
  name: request-logger
  namespace: request-logger
  labels:
    app: request-logger
spec:
  replicas: 1
  selector:
    matchLabels:
      app: request-logger
  template:
    metadata:
      labels:
        app: request-logger
    spec:
      containers:
      - name: request-logger
        image: ghcr.io/mpepping/request-logger:latest
        args: ["80"]
        ports:
          - containerPort: 80
        resources:
          requests:
            memory: "512Mi" 
            cpu: 1
          limits:
            memory: "512Mi"
            cpu: 1
---
kind: Service
apiVersion: v1
metadata:
  name: request-logger
  namespace: request-logger
  labels:
    app: request-logger
spec:
  ports:
    - port: 80
      targetPort: 80
  selector:
    app: request-logger

```

