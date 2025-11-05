import sys
import os

# Add bs4 folder to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from soupreplacer import BeautifulSoup, SoupReplacer 

#The tests validate that the API correctly replaces target tags and preserves all non-target tags.

def test_new_tag_replacement():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("", replacer=replacer)

    tag1 = soup.new_tag("b")
    tag2 = soup.new_tag("i")

    assert tag1.name == "blockquote"
    assert tag2.name == "i"

def test_multiple_tags():
    replacer = SoupReplacer("i", "em")
    soup = BeautifulSoup("", replacer=replacer)

    tag1 = soup.new_tag("i")
    tag2 = soup.new_tag("b")

    assert tag1.name == "em"
    assert tag2.name == "b"

def test_no_replacement_on_non_matching_tags():
    replacer = SoupReplacer("b", "blockquote")
    soup = BeautifulSoup("", replacer=replacer)

    tag = soup.new_tag("p")
    assert tag.name == "p"

if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
