from analyzer.optimizer import optimize_html


def test_optimize_html_success():
    html_content = "<html><head><title>Test</title></head><body><div>Hello World</div></body></html>"
    expected_optimized_html = "<html><head><title>Test</title></head><body><div> Hello World </div></body></html>"

    result = optimize_html(html_content)
    assert result["status"] == "success"
    assert result["optimized_html"] == expected_optimized_html


def test_optimize_html_with_comments():
    html_content = "<!-- This is a comment --><html><head><title>Test</title></head><body><div>Hello World</div></body></html>"
    expected_optimized_html = "<html><head><title>Test</title></head><body><div> Hello World </div></body></html>"

    result = optimize_html(html_content)
    assert result["status"] == "success"
    assert result["optimized_html"] == expected_optimized_html

def test_optimize_html_empty_content():
    html_content = ""
    expected_optimized_html = ""

    result = optimize_html(html_content)
    assert result["status"] == "success"
    assert result["optimized_html"] == expected_optimized_html


def test_optimize_html_with_empty_tags():
    html_content = "<html><body><div></div><span>Text</span></body></html>"
    expected_optimized_html = "<html><body><span> Text </span></body></html>"

    result = optimize_html(html_content)
    assert result["status"] == "success"
    assert result["optimized_html"] == expected_optimized_html
