from analyzer.seo_analyzer import analyze_seo


def test_analyze_seo_success():
    html_content = """
    <html>
        <head>
            <title>Test Title</title>
            <meta name="description" content="This is a test description.">
        </head>
        <body>
            <div>Content</div>
        </body>
    </html>
    """
    expected_result = {
        "status": "success",
        "title": "Test Title",
        "description": "This is a test description.",
    }

    result = analyze_seo(html_content)
    assert result == expected_result


def test_analyze_seo_no_title():
    html_content = """
    <html>
        <head>
            <meta name="description" content="This is a test description.">
        </head>
        <body>
            <div>Content</div>
        </body>
    </html>
    """
    expected_result = {
        "status": "success",
        "title": "No title",
        "description": "This is a test description.",
    }

    result = analyze_seo(html_content)
    assert result == expected_result


def test_analyze_seo_no_description():
    html_content = """
    <html>
        <head>
            <title>Test Title</title>
        </head>
        <body>
            <div>Content</div>
        </body>
    </html>
    """
    expected_result = {
        "status": "success",
        "title": "Test Title",
        "description": "No description",
    }

    result = analyze_seo(html_content)
    assert result == expected_result


def test_analyze_seo_empty_html():
    html_content = ""
    expected_result = {
        "status": "success",
        "title": "No title",
        "description": "No description",
    }

    result = analyze_seo(html_content)
    assert result == expected_result


def test_analyze_seo_invalid_html():
    html_content = "<html><head><title>Test Title</title><meta name='description' content='Test</head><body></body>"
    expected_result = {
        "status": "success",
        "title": "Test Title",
        "description": "No description", # because of incorrect html
    }

    result = analyze_seo(html_content)
    assert result == expected_result
