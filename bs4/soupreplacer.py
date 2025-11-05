"""
Modified SoupReplacer API (Milestone 3)
Extends the BeautifulSoup parser to perform tag name and attribute
transformations during parsing, similar to SoupStrainer.

Now supports:
  - Simple replacement: SoupReplacer("b", "blockquote")
  - Transformer API:
        SoupReplacer(name_xformer=None, attrs_xformer=None, xformer=None)
"""

from bs4 import BeautifulSoup as OriginalBeautifulSoup
from bs4.element import Tag

class SoupReplacer:
    """
    A tag transformation/replacement utility used during BeautifulSoup parsing.
    """

    def __init__(self, og_tag=None, alt_tag=None, name_xformer=None, attrs_xformer=None, xformer=None):
        # Milestone 2 (simple replacement with more tags)
        self.og_tag = og_tag
        self.alt_tag = alt_tag

        # Milestone 3 (transformer functions)
        self.name_xformer = name_xformer
        self.attrs_xformer = attrs_xformer
        self.xformer = xformer

    def should_replace(self, tag_name):
       #Check if this tag should be replaced (Milestone 2 mode)
        return self.og_tag is not None and tag_name == self.og_tag

    def transform_tag(self, tag):
        """
        Apply transformations in the following order:
          1. Simple replacement (Milestone 2)
          2. name_xformer / attrs_xformer
          3. xformer (side-effect transformer)
        """
        # 1. Simple replace mode
        if self.should_replace(tag.name):
            tag.name = self.alt_tag

        # 2. Transformer functions (Milestone 3)
        if self.name_xformer:
            tag.name = self.name_xformer(tag)
        if self.attrs_xformer:
            tag.attrs = self.attrs_xformer(tag)
        if self.xformer:
            self.xformer(tag)

        return tag

class BeautifulSoup(OriginalBeautifulSoup):
    #Subclass of BeautifulSoup that supports 'replacer' during parsing.
    def __init__(self, markup="", replacer=None, **kwargs):
        self.replacer = replacer
        super().__init__(markup, **kwargs)
        if self.replacer:
            self.apply_replacer(self.replacer)

    def apply_replacer(self, replacer):
        #Apply SoupReplacer transformations on all tags.
        for tag in self.find_all(True):
            replacer.transform_tag(tag)
