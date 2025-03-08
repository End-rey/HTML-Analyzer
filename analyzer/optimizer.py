from htmlmin import minify
from bs4 import BeautifulSoup
import re


def optimize_html(html_content: str) -> dict:
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        if not soup.renderContents():
            raise ValueError("Incorrect HTML content")
        
        # Remove empty tags
        for tag in soup.find_all():
            if not tag.contents:
                tag.decompose()
        
        optimized_html = soup.prettify(formatter="html5")

        optimized_html = re.sub(r">\s+<", "><", optimized_html)
        optimized_html = minify(
            optimized_html, remove_comments=True, remove_empty_space=True
        )
        return {"status": "success", "optimized_html": optimized_html}
    except Exception as e:
        raise ValueError(f"Error during HTML optimization: {str(e)}")
