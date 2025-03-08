from analyzer.syntax_checker import check_syntax


def test_check_syntax_valid_html():
    html_content = "<html><head><title>Test</title></head><body><div>Content</div></body></html>"
    expected_result = {"status": "success", "errors": []}

    result = check_syntax(html_content)
    assert result == expected_result


def test_check_syntax_invalid_tags():
    html_content = "<html><head><title>Test</title></head><body><invalid>Content</invalid></body></html>"
    expected_result = {"status": "error", "errors": [
        'Line 1: Invalid tag: <invalid>',
        'Line 1: Tag mismatch: expected </body>, received </invalid>',
    ]}

    result = check_syntax(html_content)
    assert result == expected_result


def test_check_syntax_no_tags():
    html_content = "Just some text without HTML tags."
    expected_result = {"status": "success", "errors": []}

    result = check_syntax(html_content)
    assert result == expected_result


def test_check_syntax_empty_html():
    html_content = ""
    expected_result = {"status": "success", "errors": []}

    result = check_syntax(html_content)
    assert result == expected_result


def test_check_syntax_invalid_html_structure():
    html_content = "<html><head><title>Test</title></head><body><div>Content</body></html>"
    expected_result = {"status": "error", "errors": [
        'Line 1: Tag mismatch: expected </div>, received </body>',
        'Line 1: Tag mismatch: expected </div>, received </html>',
        'Line 0: Unclosed tag: <div>',
    ]}

    result = check_syntax(html_content)
    assert result == expected_result
