"""
Milestone 2 - Part 1 - Task 2 of Milestone 1
Using SoupStrainer to extract all hyperlinks (<a> tags) efficiently from large HTML/XML files.
"""

from bs4 import BeautifulSoup, SoupStrainer
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python3 task2.py <html_or_xml_file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"File does not exist: {file_path}")
    sys.exit(1)

# Defining and using SoupStrainer to parse only <a> tags
only_a_tags = SoupStrainer("a")

with open(file_path, "r", encoding="utf-8") as f:
    try:
        soup = BeautifulSoup(f, "lxml", parse_only=only_a_tags)
    except:
        f.seek(0)
        soup = BeautifulSoup(f, "html.parser", parse_only=only_a_tags)

print("\nAll hyperlinks found in the file:")

a_tags = soup.find_all("a")

if not a_tags:
    print("No <a> tags found in this file.")
else:
    for idx, a_tag in enumerate(a_tags, start=1):
        href = a_tag.get("href", "[No href attribute]")
        text = a_tag.get_text(strip=True)
        print(f"{idx}. Text: '{text}', Href: {href}")
