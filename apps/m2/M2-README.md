# Milestone-2

## Part 2 - Milestone-2
To explore the original source code of BeautifulSoup. Locate the exact files/lines of the definitions of ALL the API functions you used in Milestone 1 and in Part-1 of Milestone-2. The file names and line numbers should refer to the original source code, before you make any changes. 

## Answer - Part 2 - Milestone-2

| File Name                           | Line Number   | Function            | Use Case                                                                 |
|-------------------------------------|----------------|---------------------|--------------------------------------------------------------------------|
| ./bs4/element.py                    | 2601           | prettify()          | Returns a formatted (pretty-printed) string of the parsed tree           |
| ./bs4/element.py & ./bs4/filter.py  | 2715 & 137     | find_all()          | Finds all tags that match the given name or filter                       |
| ./bs4/element.py                    | 2160           | get()               | Retrieves the value of an attribute for a tag (returns None if it doesn’t exist) |
| ./bs4/element.py                    | 524            | get_text()          | Returns the text inside a tag, optionally stripping whitespace           |
| ./bs4/element.py                    | 992            | find_parent()       | Finds the direct parent tag of a tag                                     |
| ./bs4/__init__.py                   | 682            | new_tag()           | Creates a new tag that can be inserted into the tree                     |
| ./bs4/element.py                    | 552            | replace_with()      | Replaces a tag in the tree with another tag or content                   |
| ./bs4/element.py                    | 803            | find_next_sibling() | Returns the next sibling tag of a given tag (or None if none exists)     |
