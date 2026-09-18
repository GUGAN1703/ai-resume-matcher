import re
import pdf_parser


def cleaned_text():
    pdf_parser.extracted_text= re.sub("•"," ",pdf_parser.extracted_text)
    pdf_parser.extracted_text= re.sub("\|"," ",pdf_parser.extracted_text)
    pdf_parser.extracted_text= re.sub(" +"," ",pdf_parser.extracted_text)


cleaned_text()
print(pdf_parser.extracted_text)
