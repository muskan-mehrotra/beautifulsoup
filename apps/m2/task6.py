"""
Implementing Task 6 of Milestone 1 as Part 3 of 
6. Change all the <b> tags to <blockquote> tags and write the tree onto a file.
"""

import sys
import os

# --- Ensure Python finds your custom bs4/SoupReplacer module ---
# Adjust path relative to this script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bs4")))

from soupreplacer import BeautifulSoup, SoupReplacer   # Import your custom API

# --- Check command line arguments ---
if len(sys.argv) < 2:
    print("Usage: python3 task6.py <html_or_xml_file>")
    sys.exit(1)

file_path = sys.argv[1]
if not os.path.isfile(file_path):
    print(f"File does not exist: {file_path}")
    sys.exit(1)

# --- Read input file ---
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Create a replacer rule to replace <b> with <blockquote> ---
b_to_blockquote = SoupReplacer("b", "blockquote")

# --- Parse the HTML using our custom BeautifulSoup with replacer ---
try:
    soup = BeautifulSoup(content, features="lxml", replacer=b_to_blockquote)
    print("Using parser: lxml")
except Exception:
    soup = BeautifulSoup(content, features="html.parser", replacer=b_to_blockquote)
    print("Using parser: html.parser")

# --- Write modified tree to output file ---
dir_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
name, ext = os.path.splitext(base_name)
output_file = os.path.join(dir_name, f"{name}_b_to_blockquote{ext}")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"Modified file saved as: {output_file}")