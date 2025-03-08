import re
from html.parser import HTMLParser
from typing import List, Tuple, Dict


class HTMLSyntaxChecker(HTMLParser):
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
        if not re.match(r'^[a-zA-Z0-9-]+$', tag) or tag not in self.valid_tags:
            self.errors.append((self.getpos()[0], f"Invalid tag: <{tag}>"))
            return
            
        if tag not in self.void_elements:
            self.stack.append(tag)
                
    def handle_endtag(self, tag: str):
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
        self.stack = []
        self.errors = []
        self.closed_tags = set()
        
        try:
            self.feed(html_content)
        except Exception as e:
            self.errors.append((self.getpos()[0], f"Parsing error: {str(e)}"))
        
        print(self.closed_tags)
        while self.stack:
            tag = self.stack.pop()
            if tag not in self.closed_tags:
                self.errors.append((0, f"Unclosed tag: <{tag}>"))
            
        return self.errors


def check_syntax(html_content: str) -> Dict[str, any]:
    try:
        errors = []
        checker = HTMLSyntaxChecker()
        raw_errors = checker.check(html_content)
        
        for line, error_msg in raw_errors:
            errors.append(f"Line {line}: {error_msg}")
        
        return {"status": "success" if not errors else "error", "errors": errors}
    
    except Exception as e:
        return {"status": "error", "errors": [f"Fatal error: {str(e)}"]}
