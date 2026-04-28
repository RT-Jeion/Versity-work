# Create a class 'Movie' to store and display movie details.

class Movie:
    def __init__(self, name: str, date: str, director: str, production: str, genre: list[str]):
        self.name = name
        self.date = date
        self.director = director
        self.production = production
        self.genre = genre

    def display(self):
        print("-------Movie---------")
        print("Title:", self.name)
        print("Release Date:", self.date)
        print("Directed by:", self.director)
        print("Produced by:", self.production)
        print("Genres:", end=" ")
        for g in self.genre:
            print(g, end=" ")

        print("\n")

blade = Movie("Blade", "20/03/2030", "RT Jeion", "RT ORG", ["Action", "Drama", "Romance", "Comedy", "Slide of Life"])

one_piece = Movie("One Piece", "01/01/1999", "Echiro Oda", "Toei", ["Action", "Drama", "Romance", "Comedy"])

blade.display()
one_piece.display()