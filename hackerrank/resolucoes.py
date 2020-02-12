# Declare your class here.
#     /**
#     *   Class Constructor
#     *
#     *   @param title The book's title.
#     *   @param author The book's author.
#     *   @param price The book's price.
#     **/
#     // Write your constructor here
#
#     /**
#     *   Method Name: display
#     *
#     *   Print the title, author, and price in the specified format.
#     **/
#     // Write your method here
#
# End class

from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


# Write MyBook class
class MyBook(Book):
    price = 0

    def __init__(self, title, author, price):
        super(Book, self).__init__()
        self.price = price

    def display(self):
        print(f"Title: {title}")
        print(f"Author: {author}")
        print(f"Price: {price}")


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
