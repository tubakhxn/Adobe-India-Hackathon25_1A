from flask import Flask, render_template, request, send_file
import os
from extractor import process_pdf
import tempfile
import json

def start_web():
    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        outline = None
        json_text = ""
        file_url = None
        if request.method == 'POST':
            pdf_file = request.files['pdf']
            with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tf:
                pdf_file.save(tf.name)
                outline = process_pdf(tf.name)
                json_text = json.dumps(outline, ensure_ascii=False, indent=2)
                out_path = tf.name.replace('.pdf', '.json')
                with open(out_path, 'w', encoding='utf-8') as f:
                    f.write(json_text)
                file_url = '/download?fname=' + os.path.basename(out_path)
        return render_template('index.html', outline=json_text, file_url=file_url)

    @app.route('/download')
    def download():
        fname = request.args.get('fname')
        out_path = os.path.join(tempfile.gettempdir(), fname)
        return send_file(out_path, as_attachment=True, download_name='outline.json')

    app.run(host='0.0.0.0', port=8080, debug=False)
