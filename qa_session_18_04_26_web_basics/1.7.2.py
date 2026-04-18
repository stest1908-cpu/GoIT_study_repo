from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            response = {"message": "Hello world"}
            self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        if self.path == "/data":
            content_length = int(self.headers['Content-Length'])
            body = self.rfile.read(content_length)

            data = json.loads(body)

            response = {"you_sent": data}

            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())


server = HTTPServer(("localhost", 8000), SimpleHandler)
print("Server running on http://localhost:8000")

server.serve_forever()