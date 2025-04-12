from docx import Document
from flask import Flask, render_template

def read_doc():
  doc = Document('./test.docx')

  highlited = []
  paragraphs = doc.paragraphs
  for para in doc.paragraphs:
    for run in para.runs:
      if run.font.highlight_color:
        highlited.append(run.text)

  return (highlited, paragraphs)

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def index():
  (highlited, paragraphs ) = read_doc()
  return render_template('edit.html', items=highlited, doc=paragraphs)