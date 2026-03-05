from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 8000

Handler = SimpleHTTPRequestHandler

with TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
