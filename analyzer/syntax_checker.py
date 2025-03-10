import re
from html.parser import HTMLParser
from typing import List, Tuple, Dict


class HTMLSyntaxChecker(HTMLParser):
    """
    This class is responsible for checking the syntax of HTML content.

    Usage:
    >>> checker = HTMLSyntaxChecker()
    >>> errors = checker.check(html_content)
    >>> if errors:
    ...     print(f"Syntax errors found: {', '.join([f'{line}: {error}' for line, error in errors])}")
    """

    def __init__(self):
        super().__init__()
        self.stack: List[str] = []
        self.errors: List[Tuple[int, str]] = []
        self.closed_tags: set = set()
        self.void_elements = {
            'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input',
            'link', 'meta', 'param', 'source', 'track', 'wbr'
        }
        self.valid_tags = {
            'a', 'abbr', 'address', 'area', 'article', 'aside', 'audio', 'b', 'base', 'bdi', 
            'bdo', 'blockquote', 'body', 'br', 'button', 'canvas', 'caption', 'cite', 'code', 
            'col', 'colgroup', 'data', 'datalist', 'dd', 'del', 'details', 'dfn', 'dialog', 
            'div', 'dl', 'dt', 'em', 'embed', 'fieldset', 'figcaption', 'figure', 'footer', 
            'form', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'head', 'header', 'hr', 'html', 'i', 
            'iframe', 'img', 'input', 'ins', 'kbd', 'label', 'legend', 'li', 'link', 'main', 
            'map', 'mark', 'meta', 'meter', 'nav', 'noscript', 'object', 'ol', 'optgroup', 
            'option', 'output', 'p', 'param', 'picture', 'pre', 'progress', 'q', 'rp', 'rt', 
            'ruby', 's', 'samp', 'script', 'section', 'select', 'small', 'source', 'span', 
            'strong', 'style', 'sub', 'summary', 'sup', 'table', 'tbody', 'td', 'template', 
            'textarea', 'tfoot', 'th', 'thead', 'time', 'title', 'tr', 'track', 'u', 'ul', 
            'var', 'video', 'wbr'
        }
        
    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]):
        """
        Handle start tags and check if they are valid.
        """
        if not re.match(r'^[a-zA-Z0-9-]+$', tag) or tag not in self.valid_tags:
            self.errors.append((self.getpos()[0], f"Invalid tag: <{tag}>"))
            return
            
        if tag not in self.void_elements:
            self.stack.append(tag)
                
    def handle_endtag(self, tag: str):
        """
        Handle end tags and check if they are valid.
        """
        if not self.stack:
            self.errors.append((self.getpos()[0], f"Extra closing tag: </{tag}>"))
            return
        if tag not in self.void_elements:
            self.closed_tags.add(tag)
            last_tag = self.stack[-1]
            if last_tag != tag:
                self.errors.append((self.getpos()[0], 
                                 f"Tag mismatch: expected </{last_tag}>, received </{tag}>"))
            else:
                self.stack.pop()

    def check(self, html_content: str) -> List[Tuple[int, str]]:
        """
        Check the syntax of the given HTML content and return a list of errors.

        Args:
            html_content (str): The HTML content to check

        Returns:
            List[Tuple[int, str]]: A list of errors where each error is a tuple of (line, error message)
        """
        self.stack = []
        self.errors = []
        self.closed_tags = set()
        
        try:
            self.feed(html_content)
        except Exception as e:
            self.errors.append((self.getpos()[0], f"Parsing error: {str(e)}"))
        
        while self.stack:
            tag = self.stack.pop()
            if tag not in self.closed_tags:
                self.errors.append((0, f"Unclosed tag: <{tag}>"))
            
        return self.errors


def check_syntax(html_content: str) -> Dict[str, any]:
    """
    Check the syntax of the given HTML content.

    This function returns a dictionary with two possible statuses:
    - "success": if the HTML content is valid
    - "error": if the HTML content contains errors

    The dictionary also contains a list of errors, which is empty if
    the HTML content is valid.

    Args:
        html_content (str): The HTML content to check

    Returns:
        Dict[str, any]: A dictionary containing the result of the check
    """
    try:

        checker = HTMLSyntaxChecker()
        raw_errors = checker.check(html_content)

        errors = []
        for line, error_msg in raw_errors:
            errors.append(f"Line {line}: {error_msg}")
        return {"status": "success" if not errors else "error", "errors": errors}
    except Exception as e:
        return {"status": "error", "errors": [f"Fatal error: {str(e)}"]}
