import os
import docx2txt
from pdfminer.high_level import extract_text

def parse_resume(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext == '.pdf':
        return extract_text(file_path)
    elif ext == '.docx':
        return docx2txt.process(file_path)
    else:
        return "Unsupported file format"
