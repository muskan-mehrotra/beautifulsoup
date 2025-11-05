# Milestone 3: Technical Debrief for SoupReplacer API for BeautifulSoup 

## Overview
The **SoupReplacer** API extends BeautifulSoup to allow **tag name and attribute transformations during parsing**, similar in concept to `SoupStrainer`. Unlike the Milestone 2 version, which only supported simple tag replacements, this Milestone 3 version introduces a **flexible transformer-based approach**, enabling complex modifications to both tag names and attributes, as well as arbitrary side-effect transformations.

This API is designed to simplify the process of **modifying HTML/XML trees during parsing**, making BeautifulSoup more extensible and powerful for automated DOM transformations.

---

## Features

### 1. Simple Replacement (Milestone 2 Compatible)
Replace a specific tag with another tag during parsing:

```python
from modified_soupreplacer import BeautifulSoup, SoupReplacer

html_doc = "<b>Bold</b>"
replacer = SoupReplacer("b", "blockquote")
soup = BeautifulSoup(html_doc, replacer=replacer, features="html.parser")
print(soup.prettify())
```

### 2. Transformer API (Milestone 3)
The **SoupReplacer** now supports multiple **transformer functions**:

- **`name_xformer(tag)`** → Transform tag names conditionally.
- **`attrs_xformer(tag)`** → Transform or replace attributes.
- **`xformer(tag)`** → Apply arbitrary side-effect transformations.

### Example: Rename `<i>` to `<em>` and add class `"highlight"` to `<p>` tags

```python
def rename_tag(tag):
    if tag.name == "i":
        return "em"
    return tag.name

def add_class(tag):
    if tag.name == "p":
        attrs = dict(tag.attrs)
        attrs["class"] = "highlight"
        return attrs
    return tag.attrs

replacer = SoupReplacer(name_xformer=rename_tag, attrs_xformer=add_class)
soup = BeautifulSoup(html_doc, replacer=replacer, features="html.parser")
```

### 3. Side-effect Transformers

The xformer allows in-place modifications without returning new attributes:

```python 
def style_headers(tag):
    if tag.name.startswith("h"):
        tag.attrs["style"] = "color:red"

replacer = SoupReplacer(xformer=style_headers)
```

## Comparison: Milestone 2 vs. Milestone 3

| Feature               | Milestone 2          | Milestone 3                          |
|-----------------------|--------------------|--------------------------------------|
| Tag Replacement       | ✅ Single tag       | ✅ Conditional or simple replacement |
| Attribute Changes     | ❌ Not supported    | ✅ `attrs_xformer`                    |
| Side-Effect Logic     | ❌ Not supported    | ✅ `xformer`                          |
| Backward Compatible   | N/A                 | ✅ Supports Milestone 2 simple replacement |
| Application Timing    | During tag creation | Post-parsing traversal                |
| Flexibility / Power   | Low                 | High – multiple transformers combined |

## Key Takeaways

1. Milestone 2 is lightweight, best for simple tag swaps.
2. Milestone 3 is flexible and extensible, suitable for conditional transformations, attribute updates, and complex workflows.
3. Backward compatibility ensures that legacy simple replacements still work.

## Conclusion

1. The Milestone 3 SoupReplacer significantly expands BeautifulSoup’s capabilities:
2. Maintains backward compatibility with Milestone 2.
3. Supports tag renaming, attribute transformations, and arbitrary side-effects.
4. Provides a clean, flexible API suitable for complex HTML/XML processing tasks.
