# Write a class 'Book' with title, author, and price plus a display method.

class Book:
    def __init__(self, title: str, author: str, price: int):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book Title:", self.title)
        print("Author:", self.author)
        if self.price == 0:
            print("It's Free.")
        else:
            print(f"Price: ${self.price}")

        print()


purnota = Book("Purnota", "RT Jeion", 000)

one_piece = Book("One Piece", "Echiro Oda", 10)

purnota.display()
one_piece.display()