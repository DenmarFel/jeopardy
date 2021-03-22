import os
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

import csv

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './uploads/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/board', methods = ['POST'])
def board():
    # Get file
    file = request.files["questionsCSV"]

    # Secure file
    file_name = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(file_path)

    names = []
    questions = []

    # Open File
    with open(file_path) as open_file:
        csv_file = csv.reader(open_file)

        # Store questions in list
        names = next(csv_file)
        for row in csv_file:
            questions.append(row)

    
    return render_template('board.html', names = names, questions = questions)

if __name__ == '__main__':
    app.run(debug = True)