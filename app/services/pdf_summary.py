from pypdf import PdfReader

def extract_txt_from_pdf(file_path: str) -> str:
    try:
        reader = PdfReader(file_path)
        text = []

        for page in reader.pages:
            page_text = page.extract_text() or "" #return "" if extract_text returns None
            text.append(page_text.strip())

        return "\n".join(text) #each element of text is a page
    
    except Exception as e:
        print(f"Error while extracting text from pdf: {e}")
        return ""
        