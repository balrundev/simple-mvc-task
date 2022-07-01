from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
from clientsdb import *

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        import views.client as client_view
        import views.form as form_view

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        result = ''
        
        if self.path == '/':
            result = form_view.render_form()
        elif self.path[:8] == '/clients':
            clients = db.clients
            print(clients)
            result = client_view.render_clients(clients)
        elif self.path[:8] == '/client/':
            client_id = self.path[8:]
            client = db.get_client_data(client_id)
            result = client_view.render_client(client)

        result = bytes(result, 'utf-8')

        self.wfile.write(result)


    def do_POST(self):
        import models
        import views.message as message_view
        import views.qrcode as qrcode_view

        self.send_response(200)
        self.send_header('Content-Type', 'text/html, charset="utf-8"')
        self.end_headers()

        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)

        body = str(body, 'utf-8')
        data = parse_qs(body, keep_blank_values=True)
        data = {k: v[0] for k, v in data.items()}

        try:
            client = models.client.Client(
                data['surname'],
                data['name'],
                data['email'],
                data['city'],
                data['postal-code'],
                data['address']
            )

            client_id = db.register_client(client)

            client_qrcode = models.qrcode.ClientQRCode(client_id)
            result = qrcode_view.render_qrcode(client_qrcode.img)

        except ValueError as e:
            result = message_view.render_message(str(e))

        result = bytes(result,'utf-8')

        self.wfile.write(result)


db = ClientsDB()
httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
httpd.serve_forever()