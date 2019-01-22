class Books:
    book_count = 0

    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        Books.book_count += 1


    def show_books(self):

