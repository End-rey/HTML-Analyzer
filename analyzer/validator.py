import requests


def validate_html(html_content: str) -> dict:
    """
    Validate the given HTML content using the W3C's HTML5 validator.

    The validator is a service provided by the W3C which validates HTML5
    documents. The service is accessible via a web-based interface and
    via an API.

    This function calls the API with the given HTML content and
    returns a dictionary with a status and message. The status is
    either "success" if the HTML is valid or "error" if it is not. The
    message is either "HTML is valid" or the error message from the
    validator.

    Args:
        html_content (str): The HTML content to validate.

    Returns:
        dict: A dictionary with a status and message.
    """
    url = "https://validator.w3.org/nu/"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    response = requests.post(url, data=html_content.encode("utf-8"), headers=headers)
    if response.status_code == 200:
        return {"status": "success", "message": "HTML is valid"}
    else:
        return {"status": "error", "message": response.text}
