from http.server import HTTPServer, BaseHTTPRequestHandler
from types import CodeType

CODE = 'Error'

class Requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):#handles get requests
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html')  #details content type that page will display
        self.end_headers()
        if 'hello' in self.path:
            global CODE 
            CODE = self.path[1:]
            

class Httpserver(HTTPServer):
    timeout = 5 #seconds until handle request times out
    def handle_timeout(self) -> None:
        print("Session timed out after 5 seconds!")
        return super().handle_timeout()
    
    def handle_request(self) -> None:
        return super().handle_request()

def run_server():
    PORT = 8080
    server = Httpserver(('', PORT), Requesthandler)
    print('Server running on '+ str(PORT))
    server.handle_request()

def get_code():
    print(CODE)
    return CODE



if __name__ == '__main__':
    get_code()
    run_server()
    
