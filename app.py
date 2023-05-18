import http.server
import socketserver
import socket
import json

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(bytes(json.dumps({'ok': 'true'}), "utf8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            hostname = socket.gethostname()
            message = f"The hostname is {hostname}"
            self.wfile.write(bytes(message, "utf8"))
        return

PORT = 8000

Handler = MyHttpRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
