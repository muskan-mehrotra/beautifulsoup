"""
Implementing Task 7 of Milestone 1 as Milestone-3 submission for modified soupreplacer
7. Find all the <p> tags and add (or replace) a class attribute class="test" then 
write the tree onto a file.
"""

import sys
import os

# --- Ensure Python finds your custom bs4/SoupReplacer module ---
# Adjust path relative to this script
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../bs4")))

from soupreplacer import BeautifulSoup, SoupReplacer   # Import your custom API

if len(sys.argv) < 2:
    print("Usage: python3 task7.py <html_or_xml_file>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"File does not exist: {file_path}")
    sys.exit(1)

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# --- Transformer to update attributes ---
def set_class_attrs(tag):
    # Only modify <p> tags
    if tag.name == "p":
        attrs = dict(tag.attrs)
        attrs["class"] = "test"
        return attrs
    return tag.attrs  # leave other tags unchanged

# --- Create SoupReplacer with attrs_xformer ---
replacer = SoupReplacer(attrs_xformer=set_class_attrs)

# --- Parse and apply replacer ---
try:
    soup = BeautifulSoup(content, replacer=replacer, features="lxml")
    print("Using parser: lxml")
except Exception:
    soup = BeautifulSoup(content, replacer=replacer, features="html.parser")
    print("Using parser: html.parser")

# --- Writing modified tree to a new file ---
dir_name = os.path.dirname(file_path)
base_name = os.path.basename(file_path)
name, ext = os.path.splitext(base_name)
output_file = os.path.join(dir_name, f"{name}_p_class_test{ext}")

with open(output_file, "w", encoding="utf-8") as f:
    f.write(soup.prettify())

print(f"Modified file saved as: {output_file}")
