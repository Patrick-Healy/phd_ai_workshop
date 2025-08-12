import requests
import pandas as pd
from PyPDF2 import PdfReader
import tempfile
from tqdm import tqdm  # Import tqdm for the progress bar

def extract_paper_info(url):
    # Define a temporary file to store the downloaded PDF
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
        # Download the PDF file from the URL
        response = requests.get(url)
        temp_pdf.write(response.content)
        temp_pdf_path = temp_pdf.name

    # Extract text from the downloaded PDF by page and store as a list
    reader = PdfReader(temp_pdf_path)
    pdf_text_by_page = [page.extract_text() for page in reader.pages]

    # Extract the first two pages (Title and Abstract)
    title_abstract = "\n".join(pdf_text_by_page[:2])

    # Define the keywords to search for Conclusion
    keywords = ["Conclusion", "Bibliography", "References"]

    # Function to find pages containing keywords
    def find_conclusion_pages(pdf_text, keywords):
        pages_with_conclusion = []
        for page_num, text in enumerate(pdf_text):
            if any(keyword.lower() in text.lower() for keyword in keywords):
                pages_with_conclusion.append(page_num)
        return pages_with_conclusion

    # Find pages with conclusion or references-related keywords
    relevant_pages = find_conclusion_pages(pdf_text_by_page, keywords)

    # Extract Conclusion section (from the first page with Conclusion until References/Bibliography)
    conclusion_text = ""
    if relevant_pages:
        start_page = relevant_pages[0]
        end_page = relevant_pages[1] if len(relevant_pages) > 1 else len(pdf_text_by_page)

        for page_num in range(start_page, end_page):
            conclusion_text += pdf_text_by_page[page_num] + "\n"
    
    # Create a dictionary for the data
    paper_info = {
        "Paper URL": url,
        "Title_Abstract": title_abstract.strip(),
        "Conclusion": conclusion_text.strip()
    }

    return paper_info

def process_papers(url_list):
    # Create an empty list to store paper info dictionaries
    paper_data = []
    
    # Use tqdm to show progress bar while processing URLs
    for url in tqdm(url_list, desc="Processing papers", unit="paper"):
        paper_info = extract_paper_info(url)
        paper_data.append(paper_info)

    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(paper_data)
    return df
