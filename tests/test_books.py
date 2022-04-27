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

if __name__ == '__main__':
    unittest.main()