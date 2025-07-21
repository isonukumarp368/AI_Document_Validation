from flask import Flask, render_template, request
import os
from werkzeug.utils import secure_filename
from utils.ocr_reader import extract_text_from_file
from utils.validator import validate_document

UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/validate', methods=['POST'])
def validate():
    file = request.files['document']
    if file:
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        extracted_text = extract_text_from_file(filepath)
        result = validate_document(extracted_text)

        return render_template('result.html', result=result, text=extracted_text)

    return 'File not uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
