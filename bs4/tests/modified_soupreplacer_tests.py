import pytest
import sys
import os

# Add bs4 folder to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from soupreplacer import BeautifulSoup, SoupReplacer

# ------------------ Test 1: Simple replacement ------------------
def test_simple_replace():
    html = "<b>Bold</b>"
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    assert soup.find("blockquote").text == "Bold"
    assert soup.find("b") is None

# ------------------ Test 2: name_xformer ------------------
def test_name_xformer():
    html = "<i>Italic</i>"
    replacer = SoupReplacer(name_xformer=lambda tag: "em" if tag.name == "i" else tag.name)
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    assert soup.find("em").text == "Italic"
    assert soup.find("i") is None

# ------------------ Test 3: attrs_xformer ------------------
def test_attrs_xformer():
    html = '<p class="old" id="p1">Text</p>'
    def remove_class(tag):
        attrs = dict(tag.attrs)
        attrs.pop("class", None)
        return attrs

    replacer = SoupReplacer(attrs_xformer=remove_class)
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    tag = soup.find("p")
    assert tag.attrs.get("class") is None
    assert tag.attrs.get("id") == "p1"

# ------------------ Test 4: xformer (side-effect) ------------------
def test_xformer_side_effect():
    html = "<h1>Hello</h1>"
    def add_style(tag):
        tag.attrs["style"] = "color:red"

    replacer = SoupReplacer(xformer=add_style)
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    tag = soup.find("h1")
    assert tag.attrs.get("style") == "color:red"

# ------------------ Test 5: Combined transformers ------------------
def test_combined_transformers():
    html = '<div class="box">Hi</div>'
    def rename(tag): return "section" if tag.name == "div" else tag.name
    def strip_attrs(tag): return {}
    def add_style(tag): tag.attrs["style"] = "font-weight:bold"

    replacer = SoupReplacer(name_xformer=rename, attrs_xformer=strip_attrs, xformer=add_style)
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    tag = soup.find("section")
    assert tag is not None
    assert tag.attrs.get("class") is None
    assert tag.attrs.get("style") == "font-weight:bold"

# ------------------ Test 6: Backward compatibility (simple replace) ------------------
def test_backward_compatibility():
    html = "<b>Bold</b>"
    replacer = SoupReplacer("b", "strong")
    soup = BeautifulSoup(html, replacer=replacer, features="html.parser")
    tag = soup.find("strong")
    assert tag is not None
    assert tag.text == "Bold"
    assert soup.find("b") is None
    