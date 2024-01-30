from flask import Flask, send_file, request, Response, json
from weasyprint import HTML
import io

app = Flask(__name__)


def html_to_pdf(html_content):
    # Create a PDF from HTML content
    pdf_io = io.BytesIO()
    HTML(string=html_content).write_pdf(pdf_io)
    pdf_io.seek(0)
    return pdf_io


@app.get('/')
def home():
    return 'Ok'


@app.get('/health')
def health():
    return Response(status=200, mimetype='application/json', response=json.dumps({'status': 'ok'}))


@app.post('/generate-pdf')
def generate_pdf():
    data = request.get_json()
    response_type = data.get('response_type')
    html_content = data.get('html')
    pdf_io = html_to_pdf(html_content)
    if response_type == 'base64':
        import base64
        pdf_base64 = base64.b64encode(pdf_io.read())
        return Response(status=200, mimetype='application/json', response=json.dumps({'pdf': pdf_base64.decode('utf-8')}))
    else:
        return send_file(pdf_io, mimetype='application/pdf')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
