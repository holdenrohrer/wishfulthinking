from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from book import Book
import vectors
import rec_test

app = Flask(__name__)

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')

@app.route('/display', methods = ['GET', 'POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        uploaded_book = Book(file, basic_text=True)
        
        #vectors.similarity(uploaded_book.make_vector(), placeholder_vector)
        content = rec_test.call_example(uploaded_book)
        
        
        #content = file.read()   
        
    return render_template('content.html', content=content) 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug = True)