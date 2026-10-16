from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        html = """
        <html>
          <head><title>My First Docker Project</title></head>
          <body>
            <h1>Hello from Madhu's Docker Project!</h1>
            <p>This application is running inside a Docker container.</p>
          </body>
        </html>
        """
        self.wfile.write(html.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)
print("Server running on port 8000")
server.serve_forever()
