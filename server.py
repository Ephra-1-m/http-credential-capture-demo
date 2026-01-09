#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.parse

PORT = 8080

class SimpleLoginHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Serve a basic HTML login form
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        html = """
        <html>
        <head><title>Login Page</title></head>
        <body>
            <h2>Test Login</h2>
            <form method="POST" action="/">
                Username: <input type="text" name="username"><br>
                Password: <input type="password" name="password"><br>
                <input type="submit" value="Login">
            </form>
        </body>
        </html>
        """
        self.wfile.write(html.encode("utf-8"))

    def do_POST(self):
        # Receive credentials
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))
        username = params.get('username', [''])[0]
        password = params.get('password', [''])[0]

        # Display a confirmation page
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        response = f"""
        <html>
        <body>
            <h3>Login received</h3>
            <p>Username: {username}</p>
            <p>Password: {password}</p>
            <p>Submit another or close the browser.</p>
        </body>
        </html>
        """
        self.wfile.write(response.encode("utf-8"))

        # Print credentials to terminal (simulate capture)
        print(f"[Captured] username: {username} | password: {password}")


if __name__ == "__main__":
    server_address = ('0.0.0.0', PORT)  # Listen on all interfaces
    httpd = HTTPServer(server_address, SimpleLoginHandler)
    print(f"Serving HTTP login page on port {PORT}...")
    httpd.serve_forever()
