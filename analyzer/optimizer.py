from htmlmin import minify
from bs4 import BeautifulSoup


def optimize_html(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    optimized_html = soup.prettify(formatter="html5")
    optimized_html = minify(
        optimized_html, remove_comments=True, remove_empty_space=True
    )
    return {"status": "success", "optimized_html": optimized_html}
