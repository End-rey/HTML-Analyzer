from bs4 import BeautifulSoup


def check_syntax(html_content):
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        errors = []
        for tag in soup.find_all(True):
            if not tag.name.isalnum():
                errors.append(f"Invalid tag: {tag}")
        return {"status": "success" if not errors else "error", "errors": errors}
    except Exception as e:
        return {"status": "error", "errors": [str(e)]}
