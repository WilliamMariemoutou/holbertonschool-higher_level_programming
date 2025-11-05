#!/usr/bin/python3

import http.server
import json


class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        elif self.path == '/info':
            self.handle_info()  # Add this to handle the /info endpoint
        else:
            self.handle_404()

    def handle_root(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))

    def handle_status(self):
        status = {"status": "OK"}
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(status).encode('utf-8'))

    def handle_info(self):
        # Add the /info endpoint to return version and description
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(info).encode('utf-8'))

    def handle_404(self):
        self.send_response(404)  # Return 404 for undefined paths
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        error_message = {"error": "Endpoint not found"}
        self.wfile.write(json.dumps(error_message).encode('utf-8'))


def run(server_class=http.server.HTTPServer, handler_class=MyRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on http://localhost:8000...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
