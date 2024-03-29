#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Very simple HTTP server in python for logging requests
Usage:
    ./run.py [<port>]
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging


class Server(BaseHTTPRequestHandler):
    """
    Server class
    """

    def _set_response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        """
        Process GET request
        """
        logging.info(
            "GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers)
        )
        self._set_response()
        self.wfile.write("GET request for {}\n".format(self.path).encode("utf-8"))

    def do_POST(self):
        """
        Process POST request
        """
        content_length = int(self.headers.get("content-length", 0))  # data size
        post_data = self.rfile.read(content_length)  # data payload
        logging.info(
            "POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
            str(self.path),
            str(self.headers),
            post_data.decode("utf-8"),
        )

        self._set_response()
        self.wfile.write("POST request for {}\n".format(self.path).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=Server, port=8080):
    """
    Runner
    """
    logging.basicConfig(level=logging.INFO)
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    logging.info("Starting HTTP server ..\n")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info("Stopping HTTP server ..\n")


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
