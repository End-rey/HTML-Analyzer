from selenium import webdriver
from axe_selenium_python import Axe
import tempfile
import os


def check_accessibility(html_content: str) -> dict:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".html") as temp_file:
            temp_file.write(html_content.encode("utf-8"))
            temp_file_path = temp_file.name

        driver.get(f"file://{temp_file_path}")

        axe = Axe(driver)
        axe.inject()
        results = axe.run()

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
        driver.quit()
        if "temp_file_path" in locals():
            os.unlink(temp_file_path)
