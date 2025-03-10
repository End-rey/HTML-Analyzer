from selenium import webdriver
from axe_selenium_python import Axe
import tempfile
import os


def check_accessibility(html_content: str) -> dict:
    """
    Check the given HTML content for accessibility issues using
    the axe-selenium-python library.

    Args:
        html_content (str): The HTML content to check

    Returns:
        dict: A dictionary containing the result of the check
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    # Create a temporary file with the given HTML content
    with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
        temp_file.write(html_content.encode("utf-8"))
        temp_file_path = temp_file.name

    try:
        # Start a headless Chrome instance
        driver = webdriver.Chrome(options=options)

        # Load the temporary file in the browser
        driver.get(f"file://{temp_file_path}")

        axe = Axe(driver)
        axe.inject()
        results = axe.run()

        # Extract the accessibility issues from the results
        accessibility_issues = []
        for violation in results["violations"]:
            issue = {
                "id": violation["id"],
                "description": violation["description"],
                "impact": violation["impact"],
                "nodes": [node["html"] for node in violation["nodes"]],
            }
            accessibility_issues.append(issue)

        return {
            "status": "success",
            "issues": accessibility_issues,
            "message": "Accessibility check completed",
        }

    except Exception as e:
        return {"status": "error", "message": str(e)}

    finally:
        # Quit the browser instance
        driver.quit()

        # Delete the temporary file
        if "temp_file_path" in locals():
            os.unlink(temp_file_path)
