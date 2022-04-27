import unittest
from app.models import Books

'''
BDD:
    1. Save an object
    2. Save multiple objects
    3. Display all objects
'''
class BookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_book = Books(1,"The 5AM Club","Robin Sharma","20/09/1990","Lorem Ipsum","eng")

    def tearDown(self) -> None:
        Books.books_list = []

    def test_init(self):
        self.assertEqual(self.new_book.id,1)
        self.assertEqual(self.new_book.title,"The 5AM Club")
        self.assertEqual(self.new_book.authors,"Robin Sharma")
        self.assertEqual(self.new_book.publishedDate,"20/09/1990")
        self.assertEqual(self.new_book.description,"Lorem Ipsum")
        self.assertEqual(self.new_book.language,"eng")

    def test_save_book(self):
        self.new_book.save_book()
        self.assertEqual(len(Books.books_list),1)

    def test_multiple_books(self):
        self.new_book.save_book()
        test_book = Books(2,"Gifted Hands","Ben Carson","23/12/1994","Lorem Ipsum","eng")
        test_book.save_book()
        self.assertEqual(len(Books.books_list),2)

    def test_display_all_books(self):
        self.assertEqual(Books.display_books(), Books.books_list)

if __name__ == '__main__':
    unittest.main()