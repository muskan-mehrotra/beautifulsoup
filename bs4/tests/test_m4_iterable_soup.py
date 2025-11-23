import pytest
from bs4 import BeautifulSoup, Comment, NavigableString

# TEST 1: Simple iteration returns nodes in document order
def test_simple_iteration():
    """Iterating over soup should yield nodes in document order."""
    html = "<html><body><p>Hello</p></body></html>"
    soup = BeautifulSoup(html, "html.parser")

    nodes = list(soup)  # convert to list for comparison
    names = [getattr(n, "name", None) for n in nodes]

    # Should see: [document], html, body, p, "Hello"
    assert names[0] == "[document]"
    assert "html" in names
    assert "body" in names
    assert "p" in names
    assert any(isinstance(n, NavigableString) and n == "Hello" for n in nodes)

# TEST 2: Nested elements are visited in correct depth-first order
def test_nested_iteration_order():
    """Ensure deep nesting is visited in the correct order."""
    html = "<div><span><b>Deep</b></span><i>Level</i></div>"
    soup = BeautifulSoup(html, "html.parser")

    seq = [str(x) for x in soup if isinstance(x, NavigableString)]
    assert seq == ["Deep", "Level"]


# TEST 3: Iteration returns a generator-like object (not a list)
def test_iteration_is_generator():
    """__iter__ must return a generator-like object (not a list)."""
    html = "<p>A</p><p>B</p>"
    soup = BeautifulSoup(html, "html.parser")

    itr = iter(soup)

    # Must NOT be a list - descendants is a generator
    assert not isinstance(itr, list)
    # Must behave like a generator
    assert hasattr(itr, "__next__")

# TEST 4: Iteration includes comments in traversal
def test_iteration_includes_comments():
    """Iteration should include comment nodes."""
    html = "<div>Hello<!--test-->World</div>"
    soup = BeautifulSoup(html, "html.parser")

    comments = [n for n in soup if isinstance(n, Comment)]
    assert len(comments) == 1
    assert comments[0] == "test"

# TEST 5: Iteration over larger document includes all expected text nodes
def test_iteration_over_large_doc():
    """Iterating should not skip nodes in a larger tree."""
    html = """
    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
    </ul>
    """
    soup = BeautifulSoup(html, "html.parser")

    strings = [s for s in soup if isinstance(s, NavigableString)]

    # Check all li text nodes are present
    assert "One" in strings
    assert "Two" in strings
    assert "Three" in strings