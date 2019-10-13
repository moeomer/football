from flask import Flask, request, make_response
import base64
import pdfkit
import tempfile as tfile

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    options = {'footer-right': '[page]'} if request.form.get('pagenumbers') == 'true' else None
    toc = {'xsl-style-sheet': 'toc.xsl'} if request.form.get('toc') == 'true' else None

    cover_file = False
    if request.files.get('cover'):
        cover_file = tfile.NamedTemporaryFile(mode="w+", suffix=".html", prefix="cover")
        cover_file.write(request.files.get('cover').read().decode("ISO-8859-1"))
        cover_file.flush()
    
    cover = cover_file.name if cover_file else None
    
    pdf = pdfkit.PDFKit(request.files.get('file').read().decode("ISO-8859-1"), 'string',
                        options=options, cover=cover, toc=toc, cover_first=True).to_pdf()
    
    response = make_response(pdf)
    response.headers.set('Content-Type', 'application/pdf')
    response.headers.set('Content-Disposition', 'attachment',
                         filename=request.form.get('filename'))
    
    if cover_file:
        cover_file.close()
    
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0')
