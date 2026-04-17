import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file_path):
    text = ""
    doc = fitz.open(file_path)
    
    for page in doc:
        text += page.get_text()
    
    return text


def extract_text_from_docx(file_path):
    text = ""
    doc = docx.Document(file_path)
    
    for para in doc.paragraphs:
        text += para.text + "\n"
    
    return text


def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_text_from_pdf(file_path)
    
    elif file_path.endswith(".docx"):
        return extract_text_from_docx(file_path)
    
    else:
        return None
        