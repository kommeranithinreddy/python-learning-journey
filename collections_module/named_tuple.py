from collections import namedtuple

Book = namedtuple("Book", ["title", "author", "year"])

book1 = Book("Atomic Habits", "James Clear", 2018)
book2 = Book("Deep Work", "Cal Newport", 2016)

print(book1.title)
print(book1.author)
print(book1.year)

print()
print(book2.title)
print(book2.author)
print(book2.year)
