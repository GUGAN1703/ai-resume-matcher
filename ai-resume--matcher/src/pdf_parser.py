from pypdf import PdfReader
import re

def extract_resume_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""

    for page in reader.pages:
        text = page.extract_text()
        if text is None:
            continue
        else:
            full_text+=text + "\n"
    return full_text

    

extracted_text = extract_resume_text(r"D:\ai-resume--matcher\data\resumes\ml_resume.pdf")
print(extracted_text)
