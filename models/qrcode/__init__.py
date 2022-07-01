import io
import base64
import qrcode

class ClientQRCode:
    def __init__(self, client_id):
        url = f'localhost:8000/client/{client_id}'
        buffer = io.BytesIO()
        img = qrcode.make(url)
        img.save(buffer, format='PNG')
        self._img_data = 'data:image/png;base64,' + base64.b64encode(buffer.getvalue()).decode('utf-8')

    @property
    def img(self):
        return self._img_data
