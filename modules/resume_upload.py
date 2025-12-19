import PyPDF2

def extract_text_from_pdf(uploaded_file):
    """
    This function extracts text from an uploaded PDF file.
    """

    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""

    # Loop through all pages in the PDF
    for page in pdf_reader.pages:
        text += page.extract_text()

    return text
