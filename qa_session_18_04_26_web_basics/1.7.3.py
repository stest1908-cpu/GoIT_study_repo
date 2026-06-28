# QA сесія 18.04.26 | Основи веб
# Тема: 1.7.3
# Розглянуто:
# -----------------------------------------------

from http.server import BaseHTTPRequestHandler, HTTPServer
import json

users = []  # наша "база"


class MyHandler(BaseHTTPRequestHandler):

    def _send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _read_body(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        return json.loads(body) if body else {}

    # GET
    def do_GET(self):
        if self.path == "/users":
            self._send_json(users)

        elif self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])
            user = next((u for u in users if u["id"] == user_id), None)

            if user:
                self._send_json(user)
            else:
                self._send_json({"error": "not found"}, 404)

        else:
            self._send_json({"message": "hello"})

    # POST (створення)
    def do_POST(self):
        if self.path == "/users":
            data = self._read_body()

            new_user = {
                "id": len(users) + 1,
                "name": data.get("name")
            }

            users.append(new_user)
            self._send_json(new_user, 201)

    # PUT (повне оновлення)
    def do_PUT(self):
        if self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])
            data = self._read_body()

            for user in users:
                if user["id"] == user_id:
                    user["name"] = data.get("name")
                    return self._send_json(user)

            self._send_json({"error": "not found"}, 404)

    # DELETE
    def do_DELETE(self):
        if self.path.startswith("/users/"):
            user_id = int(self.path.split("/")[-1])

            global users
            users = [u for u in users if u["id"] != user_id]

            self._send_json({"status": "deleted"})


server = HTTPServer(("localhost", 8000), MyHandler)
print("http://localhost:8000")
server.serve_forever()