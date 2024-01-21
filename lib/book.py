class Book:

    def __init__(self, title='The rising of Boniface cheruiyot', page_count=200):
        self._title = title
        self._page_count = page_count
    

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        self._title = new_title

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, page_count):
        if type(page_count) is int:
            self._page_count = page_count
        else:
            print("page_count must be an integer")


    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

    title = property(get_title, set_title)
    page_count = property(get_page_count, set_page_count)

# Instantiate the Book class
my_book = Book(title='Boniface cheruiyot')
print(my_book.title)  # Output: Boniface cheruiyot

my_book.turn_page()  # Output: Flipping the page...wow, you read fast!
