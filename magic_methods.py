class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __eq__(self, other):
        return self.title == other.title

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return self.num_pages + other.num_pages

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key {key} was not found"


book1 = Book("The Hobbit", "J.R.R. Tolkin", 300)
book2 = Book("Harry Potter", "J>K> Rowling", 999)
book3 = Book("The Lion", "C.S. Lewis", 172)

print(book1)
print(book1 == book2)
print(book1 < book3)
print(book1 > book3)
print(book1 + book3)
print("Lion" in book3)
print(book1["title"])