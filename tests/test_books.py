import unittest
from ..app.models import Books

#id,title,authors,publishedDate,description,language
class BookTest(unittest.TestCase):
    def setUp(self) -> None:
        self.new_book = Books(1,"The 5AM Club","Robin Sharma","20/09/1990","Lorem Ipsum","Eng")

    def tearDown(self) -> None:
        self.book_list = []

    def test_init(self):
        self.assertEqual(self.new_book.id,1)
        self.assertEqual(self.new_book.title,"The 5AM Club")
        self.assertEqual(self.new_book.authors,"Robin Sharma")
        self.assertEqual(self.new_book.publishedDate,"20/09/1990")
        self.assertEqual(self.new_book.description,"Lorem Ipsum")
        self.assertEqual(self.new_book.language,"Eng")

if __name__ == '__main__':
    unittest.main()