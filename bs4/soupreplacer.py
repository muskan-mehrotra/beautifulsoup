"""
SoupReplacer API
Implements a lightweight extension to BeautifulSoup that allows
tag replacement during parsing rather than after, similar in design
to SoupStrainer.

Usage example:
    from soup_replacer import BeautifulSoup, SoupReplacer

    html_doc = "<b>Bold</b><b>Text</b>"
    b_to_blockquote = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html_doc, replacer=b_to_blockquote)
    print(soup.prettify())
"""

from bs4 import BeautifulSoup as OriginalBeautifulSoup
from bs4.element import Tag

class SoupReplacer:
    """
    Defining a simple rule for replacing one tag with another during parsing.
    Parameters for replacing og_tag with alt_tag:
        og_tag (str): The original tag name to be replaced.
        alt_tag (str): The tag name to replace it with.
    """
    def __init__(self, og_tag, alt_tag):
        self.og_tag = og_tag
        self.alt_tag = alt_tag

    def should_replace(self, tag_name):
        # Return True if this tag should be replaced
        return tag_name == self.og_tag

    def get_replacement(self, tag_name):
        # Return the replacement tag name
        return self.alt_tag if self.should_replace(tag_name) else tag_name


class BeautifulSoup(OriginalBeautifulSoup):
    """
    A subclass of BeautifulSoup that accepts an optional 'replacer'
    argument. When provided, tag creation will respect the replacement
    rules defined by the SoupReplacer object.
    """

    def __init__(self, markup="", features=None, replacer=None, **kwargs):
        self.replacer = replacer
        # Initialize using parent class constructor
        super().__init__(markup, features=features, **kwargs)

    # Override the internal tag creation mechanism
    def new_tag(self, name, namespace=None, nsprefix=None, **attrs):
        # Intercept tag creation
        if self.replacer and self.replacer.should_replace(name):
            name = self.replacer.get_replacement(name)
        return super().new_tag(name, namespace=namespace, nsprefix=nsprefix, **attrs)
