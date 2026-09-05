import json

book = {
    "title": "Atomic Habits",
    "author": "James Clear",
    "price": 'None'
}

with open('book.json', 'w') as fobj:
    json.dump(book, fobj, indent = 4)