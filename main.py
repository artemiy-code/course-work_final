from flask import Flask, render_template, request
import os
import re
from pypdf import PdfReader

app = Flask(__name__)


def extract_resume_info(file_path, resume_file):
    text = ""
    resume_data = {}
    # pdf
    if resume_file.filename.endswith('pdf'):
        reader = PdfReader(file_path)
        for i in range(len(reader.pages)):
            page = reader.pages[i]
            text += page.extract_text()
    else:
        # txt, docx
        with open(file_path, 'r', encoding='latin-1') as file:
            text = file.read().lower()

    text = text.replace(': \n', ' ')
    text = text.replace(':\n', ' ')
    patterns = {
        'name': r'name (.*?)\n',
        'Date_of_birth': r'date of birth (.*?)\n',
        'Phone_number': r'phone (.*?)\n',
        'email': r'email (.*?)\n',
        'address': r'address (.*?)\n',
        'university': r'university (.*?)\n',
        'faculty': r'faculty (.*?)\n',
        'experience': r'experience (.*?)\n',
        'languages': r'languages (.*?)\n',
        'skills': r'skills (.*?)\n',
        'salary': r'salary (.*?)\n'
    }
    for key, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            answer = match.group(1).strip().capitalize()
            answer = answer.replace(':', '').replace('-', '')
            split_answer = answer.split(".")
            if key != 'Date_of_birth' and key != 'email':
                answer = split_answer[0]
            resume_data[key.capitalize()] = answer
        else:
            resume_data[key.capitalize()] = None
    return resume_data


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    # Work with uploaded file
    if request.method == 'POST':
        resume_file = request.files['resume']
        if resume_file.filename == '':
            return render_template('index.html', message='No file selected')

        if resume_file:
            # Create directory 'temp', if it doesn't exist
            if not os.path.exists('temp'):
                os.makedirs('temp')
            # Save file in temporary directory
            resume_path = os.path.join('temp', resume_file.filename)
            resume_file.save(resume_path)
            # Call the main function
            resume_info = extract_resume_info(resume_path, resume_file)
            return render_template('result.html', resume_info=resume_info)


if __name__ == '__main__':
    app.run(debug=True)
