import PyPDF2
from typing import List

class TextExtractor:

    def openIt(self, file :str) -> List[str]:
        with open(file, "rb") as pdf_file:
            read_pdf = PyPDF2.PdfFileReader(pdf_file)
            number_of_pages = read_pdf.getNumPages()
            content = []
            for page in read_pdf.pages:
                content.append(page.extractText())
        return content
    