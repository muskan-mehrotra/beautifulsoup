import sys
import os

# Add bs4 folder to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))

from soupreplacer import BeautifulSoup, SoupReplacer

"""
This test verifies that the SoupReplacer correctly replaces matching tags while
 preserving all tag attributes, and that non-matching tags remain unchanged.
It ensures that attributes like id and class are retained after the replacement.
"""

def test_tag_replacement_with_attributes():
    """Ensure replaced tags keep their attributes and non-matching tags stay unchanged"""
    replacer = SoupReplacer("i", "em")
    soup = BeautifulSoup("", replacer=replacer)

    # Create an <i> tag with attributes using attrs dict
    tag1 = soup.new_tag("i", attrs={"id": "italic1", "class": ["text"]})
    # Create a non-matching <b> tag with attributes
    tag2 = soup.new_tag("b", attrs={"id": "bold1", "class": ["strong"]})

    soup.append(tag1)
    soup.append(tag2)

    # Assertions for replaced tag
    assert tag1.name == "em"
    assert tag1.get("id") == "italic1"
    assert tag1.get("class") == ["text"]

    # Assertions for non-replaced tag
    assert tag2.name == "b"
    assert tag2.get("id") == "bold1"
    assert tag2.get("class") == ["strong"]

# Allow running directly
if __name__ == "__main__":
    import pytest
    pytest.main([__file__])
