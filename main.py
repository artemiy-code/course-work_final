from flask import Flask, render_template, request
import os
import re
from pypdf import PdfReader
from patterns import name, Date_of_birth, phone, email, address, university, faculty, experience, languages, skills, \
    salary

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
            text = file.read()
            # delete unwanted symbols
    text = ''.join(char for char in text if ord(char) < 128)
    text = text.encode('latin-1', errors='ignore').decode('latin-1')
    text = text.lower()
    text = text.replace(': \n', ' ').replace(':\n', ' ').replace(':', ' ')
    text = text.replace('|', '.').replace('-', ' ').replace(': ', ' ')
    pattern = [name, Date_of_birth, phone, email, address, university, faculty, experience, languages, skills, salary]

    vocab = ["name", "Date_of_birth", "phone", "email", "address", "university", "faculty", "experience", "languages",
             "skills", "salary"]
    for word in vocab:
        text = text.replace(word + "\n", word + " ")
        text = text.replace(word + " \n", word + " ")

    i = 0
    for attribute in pattern:
        iterator = 0
        for regular_expression in attribute:
            match = re.search(regular_expression, text)
            if match:
                if (i == 1 and iterator <= 3) or (i == 2 and iterator <= 8) or (i == 3 and iterator == 0) \
                        or (i == 4 and iterator <= 4):
                    answer = match.group(0).strip()
                    if i != 3:
                        answer = answer.capitalize()
                else:
                    answer = match.group(1).strip().capitalize()
                answer = answer.replace(':', '').replace('-', '')
                split_answer = answer.split(".")
                if vocab[i] != 'Date_of_birth' and vocab[i] != 'email':
                    if split_answer[0] is not None:
                        answer = split_answer[0]
                resume_data[vocab[i].capitalize()] = answer
                break
            else:
                resume_data[vocab[i].capitalize()] = None
            iterator += 1
        i += 1
    if resume_data["Name"] is None:
        if ("summary" or "resume" or "cv") not in text.splitlines()[0]:
            resume_data["Name"] = (text.split()[0].capitalize() + " " + text.split()[1].capitalize())
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
