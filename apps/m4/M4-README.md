# Milestone 4 — Iterable BeautifulSoup

## Overview

In this milestone, we extend the BeautifulSoup library so that a `BeautifulSoup` object becomes directly iterable.

Example usage:

```python
soup = BeautifulSoup(html_doc, "html.parser")

for node in soup:
    print(node)
   ```
## Explanation:
Prior to this milestone, iteration was only possible over tag lists or specific selections—not directly over the root soup object.

⸻

Requirements
	•	The soup object must support direct iteration using the Python iterator protocol.
	•	Iteration must return every node in the document (tags, strings, comments, doctypes, etc.).
	•	Ordering must match BeautifulSoup’s natural depth-first document traversal.
	•	The solution must be memory-efficient and must not build a list of nodes before yielding them.
	•	Implementation must integrate cleanly with the existing BeautifulSoup class.

⸻

Solution Implemented

The core of BeautifulSoup already maintains a complete linked tree using next_element pointers, and provides a built-in generator called .descendants.
This generator:
	•	Steps through the tree in depth-first order
	•	Uses pointer-based navigation (next_element)
	•	Yields nodes lazily, one at a time
	•	Does not allocate additional structures or lists

Because .descendants already does exactly what Milestone-4 requires, the most correct and efficient approach was simply to expose it as the iterator for the soup object.

Code Added (in beautifulsoup/bs4/__init__.py)

```python
def __iter__(self):
    # Return the built-in generator that already performs
    # depth-first traversal of all nodes without building a list.
    return self.descendants
```

### Why This Works
	•	Depth-first traversal: .descendants naturally walks through every element as BeautifulSoup parses it.
	•	Memory efficient: It yields results lazily, meeting the “no list building” constraint.
	•	Full coverage: All node types (Tag, NavigableString, Comment, Doctype, etc.) are included because they participate in the next_element chain.
	•	Minimal and safe change: We do not modify tree structures or parsing logic—only provide an iteration interface on top of existing behavior.

This is the most direct and correct implementation that matches BeautifulSoup’s internal design.

⸻

## Tests Added
A new file was created:
beautifulsoup/bs4/tests/test_m4_iterable_soup.py

Five test cases verify:
	1.	Simple document iteration (basic structure and ordering)
	2.	Nested element traversal
	3.	Iterator type (must be a generator, not a list)
	4.	Inclusion of comments and non-tag nodes
	5.	Completeness in larger documents

These tests confirm correct traversal order, correctness across node types, and compliance with the memory constraints.

⸻

## Summary
Milestone 4 adds a clean and efficient iterable interface to BeautifulSoup by exposing its existing internal generator.
The solution is minimal, memory-safe, fully compatible with existing behavior, and backed by comprehensive unit tests.
