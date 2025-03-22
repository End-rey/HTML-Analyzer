from parser.html import parse

def test_parse_basic_html():
    html_content = "<html><body><p>Hello World</p></body></html>"
    expected_text = "Hello World"
    
    result = parse(html_content)
    assert result == expected_text

def test_parse_with_script_tags():
    html_content = """
        <html>
            <body>
                <script>console.log('test');</script>
                <p>Hello World</p>
            </body>
        </html>
    """
    expected_text = "Hello World"
    
    result = parse(html_content)
    assert result == expected_text

def test_parse_with_style_tags():
    html_content = """
        <html>
            <style>body { color: red; }</style>
            <body><p>Hello World</p></body>
        </html>
    """
    expected_text = "Hello World"
    
    result = parse(html_content)
    assert result == expected_text

def test_parse_empty_content():
    html_content = ""
    expected_text = ""
    
    result = parse(html_content)
    assert result == expected_text

def test_parse_multiple_elements():
    html_content = """
        <html>
            <body>
                <h1>Title</h1>
                <p>Paragraph 1</p>
                <p>Paragraph 2</p>
            </body>
        </html>
    """
    expected_text = "Title Paragraph 1 Paragraph 2"
    
    result = parse(html_content)
    assert result == expected_text