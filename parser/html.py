from bs4 import BeautifulSoup

def parse(html_content: str) -> str:
    """
    Extract all text from HTML content using BeautifulSoup.
    
    Args:
        html_content (str): HTML content as string
    
    Returns:
        str: Extracted text with preserved whitespace
    """
    
    soup: BeautifulSoup = BeautifulSoup(html_content, 'html.parser')
    
    for script in soup(["script", "style"]):
        script.decompose()
    
    text: str = soup.get_text(separator=' ', strip=True)
    
    return text
