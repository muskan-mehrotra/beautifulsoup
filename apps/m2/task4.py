"""
Milestone 2 - Part 1 - Task 4 of Milestone 1
Print out all tags that have an 'id' attribute using SoupStrainer
"""

from bs4 import BeautifulSoup, SoupStrainer
import sys
import os

# ---- Step 1: Handle command-line arguments ----
if len(sys.argv) < 2:
    print("Usage: python3 task4.py <html_or_xml_file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"File does not exist: {file_path}")
    sys.exit(1)

# ---- Step 2: Read the file ----
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# ---- Step 3: Using SoupStrainer to filter only tags that have an id attribute ----
only_id_tags = SoupStrainer(attrs={"id": True})

# ---- Step 4: Parse only those elements ----
try:
    soup = BeautifulSoup(content, "lxml", parse_only=only_id_tags)
    print("Using parser: lxml (with SoupStrainer)")
except Exception as e:
    print(f"lxml failed ({e}), using html.parser instead.")
    soup = BeautifulSoup(content, "html.parser", parse_only=only_id_tags)

# ---- Step 5: Single API call to find all tags with an id ----
tags_with_id = soup.find_all(attrs={"id": True})

# ---- Step 6: Print results ----
print("\nTags that have an 'id' attribute:")
if not tags_with_id:
    print("No tags with 'id' attribute found.")
else:
    for idx, tag in enumerate(tags_with_id, start=1):
        print(f"{idx}. <{tag.name}> id='{tag.get('id')}' → {str(tag)[:120]}...")