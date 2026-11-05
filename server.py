import http.server
import socketserver
import os

PORT = int(os.environ.get("PORT", 8080))

class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    def log_message(self, format, *args):
        print(f"[SERVER] {self.address_string()} - {format % args}")

print(f"[ABH] Alfa Bot Hoster server starting on port {PORT}")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"[ABH] Live at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
