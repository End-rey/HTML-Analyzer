from bs4 import BeautifulSoup


def analyze_seo(html_content: str) -> dict:
    """
    Analyze the given HTML content for SEO.

    Args:
        html_content (str): The HTML content to analyze

    Returns:
        dict: A dictionary containing the result of the analysis
    """
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title.string if soup.title else "No title"
    meta_description = soup.find("meta", attrs={"name": "description"})
    description = meta_description["content"] if meta_description else "No description"
    return {
        "status": "success",
        "title": title,
        "description": description,
    }
