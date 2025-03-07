import requests


def validate_html(html_content):
    url = "https://validator.w3.org/nu/"
    headers = {"Content-Type": "text/html; charset=utf-8"}
    response = requests.post(url, data=html_content.encode("utf-8"), headers=headers)
    if response.status_code == 200:
        return {"status": "success", "message": "HTML is valid"}
    else:
        return {"status": "error", "message": response.text}
