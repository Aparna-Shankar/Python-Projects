

"""
This is a book catalogue application, that will allow users to manage their book collection
and find any book they want.
Here’s the three main features:
• First, the application allows to add new books to the collection;
• The application allows users to view all the books in their collection;
• The application also allows users to find any particular book by any of its attributes


Books = [
    {
        'title':   'God of Small Things',
        'author':  'Arundathi Roy',
        'genre':   'Fiction'
    },
    {
        'title':   'Kite Runner',
        'author':  'Khalid Hosseini',
        'genre':   'Fiction'
    },
    {
        'title':    'Da Vinci Code',
        'author':   'Dan Brown',
        'genre':    'Fiction'
    }
]

"""
Books = []

def menu():

    choice = input("\nEnter 'a' to add a book, 'l' to see your books, 'f' to find a book and 'q' to quit: ")
    while choice != 'q':

        if choice == 'a':
            add_books()

        elif choice == 'l':
            list_books(Books)

        elif choice == 'f':
            find_books()

        else:
            print("You've entered an invalid choice. Please try again! ")

        choice = input("\nEnter 'a' to add a book, 'l' to see your books, 'f' to find a book and 'q' to quit: ")


def add_books():

    print('Enter the following values for the new book: ')
    new_title = input('Title :')
    new_author = input('Author :')
    new_genre = input('Genre :')

    Books.append({
        'title': new_title,
        'author': new_author,
        'genre': new_genre
    })

    print( Books )


def list_books(book_list):
    print( 'List of books: ')
    for each_book in book_list:
        book_details(each_book)


def book_details(each_book):
    print(f"Title : {each_book['title']}")
    print(f"Author : {each_book['author']}")
    print(f"Genre : {each_book['genre']}")


def find_books():

    attribute = input( 'Find books by author/genre?: ')
    attr_value = input( f' Enter {attribute}: ')

    books_found = find_items_by_attribute(Books, attr_value, lambda x: x[attribute])
    list_books(books_found)


def find_items_by_attribute(items, expected_val, finder):

    """ This is a truly generic function that can be used to find any item by the attribute that is passed.
    Here the item can be a list, dictionary or anything. In this case the item is a Book which is a list.
    """

    found = []

    for each_item in items:
        if finder(each_item) == expected_val:
            found.append(each_item)
    return found


menu()
