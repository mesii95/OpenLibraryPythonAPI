import unittest
from BookMeta.OpenLib import OpenLib
from BookMeta.CustomException import ISBNFormatException, ISBNNotFoundException


class BookMetaTests(unittest.TestCase):

    def setUp(self):
        self.goodISBN_1 = "9781285741550"
        self.goodISBN_2 = "978-1285741550"
        self.goodISBN_3 = "0134076427"
        self.goodISBN_edition_in_title = "978-1259642586"

        self.badISBN_1 = "0000000000"
        self.badISBN_2 = "000-0000000000"
        self.badISBN_3 = "1234"
        self.badISBN_4 = "12345678910111213"
        self.badISBN_5 = ""
        self.badISBN_6 = "1941691242"

    def test_tooshort(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_3)

    def test_empty(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_5)

    def test_tooLong(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_4)

    def test_booknotfound_1(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_1)

    def test_booknotfound_2(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_2)

    def test_booknotfound_3(self):
        with self.assertRaises(Exception):
            OpenLib(self.badISBN_6)

    def test_validISBN13_1(self):
        book = OpenLib(self.goodISBN_1)

        self.assertEqual("Calculus", book.title())
        self.assertEqual("early transcendentals", book.subtitle())
        self.assertEqual("8", book.edition())
        self.assertEqual("James Stewart", book.author()[0])
        self.assertEqual(None, book.publisher())
        self.assertEqual("Calculus", book.subject()[0])
        self.assertEqual("Textbooks", book.subject()[1])
        self.assertEqual("9781285741550", book.input_isbn())
        self.assertEqual("1285741552", book.all_isbn_10()[0])
        self.assertEqual("1305270363", book.all_isbn_10()[1])
        self.assertEqual("9781285741550", book.all_isbn_13()[0])
        self.assertEqual("9781305272354", book.all_isbn_13()[1])
        self.assertEqual("9781305270367", book.all_isbn_13()[2])

    def test_validISBN13_2(self):
        book = OpenLib(self.goodISBN_2)

        self.assertEqual("Calculus", book.title())
        self.assertEqual("early transcendentals", book.subtitle())
        self.assertEqual("8", book.edition())
        self.assertEqual("James Stewart", book.author()[0])
        self.assertEqual(None, book.publisher())
        self.assertEqual("Calculus", book.subject()[0])
        self.assertEqual("Textbooks", book.subject()[1])
        self.assertEqual("9781285741550", book.input_isbn())
        self.assertEqual("1285741552", book.all_isbn_10()[0])
        self.assertEqual("1305270363", book.all_isbn_10()[1])
        self.assertEqual("9781285741550", book.all_isbn_13()[0])
        self.assertEqual("9781305272354", book.all_isbn_13()[1])
        self.assertEqual("9781305270367", book.all_isbn_13()[2])

    def test_validISBN10_1(self):
        book = OpenLib(self.goodISBN_3)

        self.assertEqual("Computer Science", book.title())
        self.assertEqual("An Interdisciplinary Approach", book.subtitle())
        self.assertEqual(None, book.edition())
        self.assertEqual("Robert Sedgewick", book.author()[0])
        self.assertEqual("Kevin Wayne", book.author()[1])
        self.assertEqual("Addison-Wesley Professional", book.publisher()[0])
        self.assertEqual(None, book.subject())
        self.assertEqual("0134076427", book.input_isbn())
        self.assertEqual("0134076427", book.all_isbn_10()[0])
        self.assertEqual("9780134076423", book.all_isbn_13()[0])

    def test_edition_in_title(self):
        book = OpenLib(self.goodISBN_edition_in_title)

        self.assertEqual("Standard Handbook for Electrical Engineers, Seventeenth Edition", book.title())
        self.assertEqual(None, book.subtitle())
        self.assertEqual("17", book.edition())
        self.assertEqual("Surya Santoso", book.author()[0])
        self.assertEqual("H. Wayne Beaty", book.author()[1])
        self.assertEqual("McGraw-Hill Education", book.publisher()[0])
        self.assertEqual(None, book.subject())
        self.assertEqual("9781259642586", book.input_isbn())
        self.assertEqual("1259642585", book.all_isbn_10()[0])
        self.assertEqual("9781259642586", book.all_isbn_13()[0])


if __name__ == '__main__':
    unittest.main()

