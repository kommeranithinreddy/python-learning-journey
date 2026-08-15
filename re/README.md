# Python `re` Module

This folder contains my practice programs for Python's **`re` (Regular Expression)** module.

I practiced using regular expressions to search, match, extract, and replace patterns in strings.

## Topics Covered

* Finding all matches using `re.findall()`
* Matching patterns using `re.match()`
* Checking complete string matches using `re.fullmatch()`
* Working with match objects
* Finding digits and numbers
* Finding letters and specific characters
* Character ranges such as `[a-z]`, `[A-Z]`, and `[0-9]`
* Escape sequences such as `\d`, `\w`, `\s`
* Quantifiers for matching one or more characters
* Matching exact numbers of digits
* Matching consecutive digits
* Matching words based on specific patterns
* Using `^` and `$` for string boundaries
* Case-insensitive matching with `re.IGNORECASE`
* Replacing matched patterns using `re.sub()`
* Extracting numbers containing decimal points
* Finding numbers at specific positions
* Working with words beginning or ending with specific characters
* Practical pattern extraction and replacement

## Practice Programs

The programs in this folder include examples for:

* Extracting decimal points
* Extracting only numbers
* Extracting all numbers
* Extracting digits using ranges
* Extracting one or more digits
* Finding consecutive digits
* Finding escape sequences
* Finding all occurrences
* Finding vowels
* Finding specific characters
* Finding exactly 3 digits at the end
* Finding exactly 3-letter words
* Finding starting uppercase characters
* Finding words containing specific patterns
* Finding words with `py`
* Finding uppercase letters
* Finding numbers with exactly 3 digits
* Replacing ages with `XX`
* Replacing escape sequences with spaces
* Replacing number words
* Replacing words
* Finding strings starting with `Python`
* Finding words ending with `@`
* Checking match objects

## Key Functions Practiced

```python
re.findall()
re.match()
re.fullmatch()
re.sub()
```

## Key Regex Concepts

```text
\d      Digit
\w      Word character
\s      Whitespace
[a-z]   Lowercase letters
[A-Z]   Uppercase letters
[0-9]   Digits
+       One or more
{n}     Exactly n occurrences
^       Start of string
$       End of string
```

## Purpose

These exercises were completed to build a practical understanding of regular expressions for **Python development, data cleaning, data extraction, validation, automation, and Data Science/AI workflows**.
