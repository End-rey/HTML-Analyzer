from bs4 import BeautifulSoup


def analyze_seo(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    title = soup.title.string if soup.title else "No title"
    meta_description = soup.find("meta", attrs={"name": "description"})
    description = meta_description["content"] if meta_description else "No description"
    return {
        "status": "success",
        "title": title,
        "description": description,
    }
