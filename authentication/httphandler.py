from http.server import HTTPServer, BaseHTTPRequestHandler








CODE = "Error"                                                      #this is the default value of CODE


class Requesthandler(BaseHTTPRequestHandler):
    def do_GET(self):                                               #handles get requests
        self.send_response(200)
        self.send_header('Content-Type:', 'text/html')              #details content type that page will display
        self.end_headers()
        htmlListSUCCESS = [
        '<html><body>',
        '<h2><center>Authorized! You may now close this window &#9786;</center><h2>'
                    ]
        htmlListFAILED = [
        '<html><body>',
        '<h2><center>You denied the request! You may now close this window &#9786;</center><h2>'
                    ]
        outputSUCCESS, outputFAILED = '', ''
        for line1 in htmlListSUCCESS:
            outputSUCCESS += line1
        for line2 in htmlListFAILED:
            outputFAILED += line2
        if 'code' in self.path:                                     #happy path
            global CODE 
            CODE = self.path[7:]                                    #extract code from link
            self.wfile.write(outputSUCCESS.encode())
        elif 'access_denied' in self.path:
            self.wfile.write(outputFAILED.encode())

class Httpserver(HTTPServer):
    timeout = 30                                                    #seconds until handle request times out
    def handle_timeout(self) -> None:
        print("Session timed out after 30 seconds!")
        return super().handle_timeout()
    
    def handle_request(self) -> None:
        return super().handle_request()


#functions start here
def run_server():
    PORT = 8080
    server = Httpserver(('', PORT), Requesthandler)
    print('Server running on '+ str(PORT))
    server.handle_request()                                        #handles one request and times out
    return CODE


if __name__ == '__main__':
    run_server()
    
