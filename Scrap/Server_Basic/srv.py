import http.server as ht
from cgi import parse_header


class RequestHandler(ht.SimpleHTTPRequestHandler):

    def do_PUT(self):
        len = int(self.headers["Content-Length"])
        number= str(self.rfile.read(len), 'utf-8')
        with open("save.txt","w") as file:
            file.write(number)
        self.send_response(200)
        self.end_headers()

    
if __name__ == "__main__":
    s = ht.HTTPServer(("",8080), RequestHandler)
    s.serve_forever()








