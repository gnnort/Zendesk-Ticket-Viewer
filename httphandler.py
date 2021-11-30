from http.server import HTTPServer, BaseHTTPRequestHandler

class Requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):#handles get requests
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html')  #details content type that page will display
        self.end_headers()
        self.wfile.write(self.path.encode())








def run_server():
    PORT = 8080
    server = HTTPServer(('', PORT), Requesthandler)
    print('Server running on '+ str(PORT))
    server.serve_forever()

if __name__ == '__main__':
    run_server()
