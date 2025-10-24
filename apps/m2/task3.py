"""
Milestone 2 - Part 1 - Task 3 of Milestone 1
Print out all tags in the document using BeautifulSoup's SoupStrainer
"""

from bs4 import BeautifulSoup, SoupStrainer
import sys
import os

# ---- Step 1: Check command-line arguments ----
if len(sys.argv) < 2:
    print("Usage: python3 task3.py <html_or_xml_file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f" File does not exist: {file_path}")
    sys.exit(1)

# ---- Step 2: Read the HTML/XML file ----
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# ---- Step 3: Create SoupStrainer that targets all tags ----
# parse_only=None will parse everything, but we can optimize to skip text nodes
only_tags = SoupStrainer(True)   # True matches *all tags*

# ---- Step 4: Parse only the tag nodes ----
try:
    soup = BeautifulSoup(content, "lxml", parse_only=only_tags)
    print("Using parser: lxml (with SoupStrainer)")
except Exception as e:
    print(f" lxml failed ({e}), using html.parser instead.")
    soup = BeautifulSoup(content, "html.parser", parse_only=only_tags)

# ---- Step 5: Collect all tag names ----
all_tags = [tag.name for tag in soup.find_all(True)]  # True finds all tags

# ---- Step 6: Print the results ----
print("\nAll tags in the document (including duplicates, in order):")
if not all_tags:
    print("No tags found.")
else:
    print(", ".join(all_tags))
