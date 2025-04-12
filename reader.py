from docx import Document

def read_doc():
  doc = Document('./test.docx')

  highlited = []
  for para in doc.paragraphs:
    for run in para.runs:
      if run.font.highlight_color:
        highlited.append(run.text)

  return highlited

if __name__ == '__main__':
  print(read_doc())
