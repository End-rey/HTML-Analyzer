from bs4 import BeautifulSoup

VALID_TAGS = {
    "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "blockquote", "body",
    "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del",
    "details", "dfn", "dialog", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer",
    "form", "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "i", "iframe", "img", "input",
    "ins", "kbd", "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noscript",
    "object", "ol", "optgroup", "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt",
    "ruby", "s", "samp", "script", "section", "select", "small", "source", "span", "strong", "style", "sub",
    "summary", "sup", "svg", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "time",
    "title", "tr", "track", "u", "ul", "var", "video", "wbr"
}


def check_syntax(html_content):
    try:
        soup = BeautifulSoup(html_content, "html5lib")
        errors = []
        for tag in soup.find_all(True):
            if not tag.name.isalnum() or tag.name not in VALID_TAGS:
                errors.append(f"Invalid tag: {tag}")
        return {"status": "success" if not errors else "error", "errors": errors}
    except Exception as e:
        return {"status": "error", "errors": [str(e)]}
