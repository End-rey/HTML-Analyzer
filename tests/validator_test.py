from unittest.mock import patch
from analyzer.validator import validate_html


def test_validate_html_success():
    html_content = "<html><head><title>Test</title></head><body><div>Content</div></body></html>"

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = ""

        expected_result = {"status": "success", "message": "HTML is valid"}
        result = validate_html(html_content)

        assert result == expected_result
        mock_post.assert_called_once()


def test_validate_html_failure():
    html_content = "<html><head><title>Test</title></head><body><div>Content</body></html>"

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 400
        mock_post.return_value.text = "Invalid HTML"

        expected_result = {"status": "error", "message": "Invalid HTML"}
        result = validate_html(html_content)

        assert result == expected_result
        mock_post.assert_called_once()


def test_validate_html_empty_content():
    html_content = ""

    with patch('requests.post') as mock_post:
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = ""

        expected_result = {"status": "success", "message": "HTML is valid"}
        result = validate_html(html_content)

        assert result == expected_result
        mock_post.assert_called_once()
