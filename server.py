from http.server import BaseHTTPRequestHandler, HTTPServer

counter = 0

class CounterServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global counter

        if self.path == '/':
            with open('index.html', 'rb') as fh:
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                html = fh.read()
                self.wfile.write(html)
        elif self.path == '/counter':
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(str(counter).encode(encoding='utf_8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

    def do_POST(self):
        global counter
        if self.path == '/add':
            counter += 1
            self.send_response(204)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        elif self.path == '/subtract':
            counter -= 1
            self.send_response(204)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

if __name__ == "__main__":
    webServer = HTTPServer(('localhost', 8080), CounterServer)
    print("Server started at port 8080")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
