from unittest.mock import patch, MagicMock
from analyzer.accessibility import check_accessibility


def test_accessibility_check_success():
    with patch('analyzer.accessibility.webdriver.Chrome') as mock_chromedriver:
        with patch('analyzer.accessibility.Axe') as mock_axe:
            mock_driver = MagicMock()
            mock_chromedriver.return_value = mock_driver

            mock_results = {
                "violations": [
                    {
                        "id": "color-contrast",
                        "description": "Elements must have sufficient color contrast.",
                        "impact": "serious",
                        "nodes": [{"html": "<div>Example Node</div>"}],
                    }
                ]
            }
            mock_axe.return_value.run.return_value = mock_results

            html_content = "<html><body><div>Test Content</div></body></html>"

            result = check_accessibility(html_content)

            expected_result = {
                "status": "success",
                "issues": [{
                    "id": "color-contrast",
                    "description": "Elements must have sufficient color contrast.",
                    "impact": "serious",
                    "nodes": ["<div>Example Node</div>"],
                }],
                "message": "Accessibility check completed",
            }

            assert result == expected_result


def test_accessibility_check_empty_html():
    with patch('analyzer.accessibility.webdriver.Chrome') as mock_chromedriver:
        mock_driver = MagicMock()
        mock_chromedriver.return_value = mock_driver

        mock_results = {
            "violations": []
        }

        mock_axe = MagicMock()
        mock_axe.return_value.run.return_value = mock_results

        html_content = ""

        result = check_accessibility(html_content)

        expected_result = {
            "status": "success",
            "issues": [],
            "message": "Accessibility check completed",
        }

        assert result == expected_result


def test_accessibility_check_temp_file_creation_error():
    with patch('tempfile.NamedTemporaryFile', side_effect=OSError("Temporary file creation failed")):

        html_content = "<html><body><div>Test Content</div></body></html>"

        result = check_accessibility(html_content)

        assert result["status"] == "error"
        assert "Temporary file creation failed" in result["message"]
