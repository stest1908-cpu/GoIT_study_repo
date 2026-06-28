# QA сесія 18.04.26 | Основи веб
# Тема: 1.7
# Розглянуто:
# -----------------------------------------------

#Простий REST сервер на BASEHTTPRequestHandler

from http.server import BaseHTTPRequestHandler, HTTPServer


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(b'{"message": "Hello world"}')


server = HTTPServer(("localhost", 8000), MyHandler)
print("Server running on http://localhost:8000")

server.serve_forever()