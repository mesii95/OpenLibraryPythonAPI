import requests
import json
from BookMeta.CustomException.ISBNFormatException import ISBNFormatException
from BookMeta.CustomException.ISBNNotFoundException import ISBNNotFoundException


class OpenLib:

    _title = None
    _subtitle = None
    _edition = None
    _author = None
    _publisher = None
    _subject = None
    _input_isbn = None
    _all_isbn_10 = None
    _all_isbn_13 = None

    def __init__(self, isbn: str):
        """Creates an OpenLib object from an ISBN 10 or ISBN 13.
        The OpenLib object contains meta data about a book.
        A meta data field is set to None if the field could not be
        found.

        :param isbn: a valid ISBN 10 or ISBN 13, represented as a string.
        """

        isbn = isbn.replace('-', '')

        OpenLib._check_isbn_format(isbn)

        isbn_content = OpenLib._create_dictionary_from_isbn(isbn)

        self._title = self._parse_title(isbn_content)

        self._subtitle = self._parse_subtitle(isbn_content)

        self._edition = self._parse_edition(isbn_content)

        self._author = self._parse_author(isbn_content)

        self._publisher = self._parse_publisher(isbn_content)

        self._subject = self._parse_subject(isbn_content)

        self._input_isbn = isbn

        self._all_isbn_10 = self._parse_isbn_10(isbn_content)

        self._all_isbn_13 = self._parse_isbn_13(isbn_content)

        self.dictionary = isbn_content

    def title(self):
        """ The title of the book

        :return: str
        """
        return self._title

    def subtitle(self):
        """ The subtitle of the book

        :return: str
        """
        return self._subtitle

    def edition(self):
        """ The edition of the book represented as a single digit string

        :return: str
        """
        return self._edition

    def author(self):
        """ The author or authors of the book as an array of strings

        :return: [str]
        """
        return self._author

    def publisher(self):
        """ The publisher or publishers of the book as an array of strings

        :return: [str]
        """
        return self._publisher

    def subject(self):
        """ The relevant subjects of the book as an array of strings

        :return: [str]
        """
        return self._subject

    def input_isbn(self):
        """ The isbn input upon creation of the OpenLib object without the '-'

        :return: [str]
        """
        return self._input_isbn

    def all_isbn_10(self):
        """ All ISBN-10 aliases for the book as an array of strings

        :return: [str]
        """
        return self._all_isbn_10

    def all_isbn_13(self):
        """ All ISBN-13 aliases for the book as an array of strings

        :return: [str]
        """
        return self._all_isbn_13

    @staticmethod
    def _check_isbn_format(isbn):
        if not isinstance(isbn, str):
            raise ISBNFormatException('not a string')
        else:
            if not (len(isbn) == 10 or len(isbn) == 13):
                raise ISBNFormatException('length is wrong: ' + isbn)
        if not isbn.isdigit():
            raise ISBNFormatException("contains illegal characters")

    @staticmethod
    def _create_dictionary_from_isbn(isbn):
        json_details_str = requests.get("https://openlibrary.org/api/books?bibkeys=ISBN:" + isbn +
                                        "&jscmd=details&format=json").text
        if json_details_str.__eq__('{}'):
            raise ISBNNotFoundException("ISBN not found at openlibrary.org")
        json_details = json.loads(json_details_str)
        isbn_content = json_details["ISBN:" + isbn]
        return isbn_content['details']

    @staticmethod
    def _parse_isbn_13(isbn_content):
        if 'isbn_13' in isbn_content:
            all_isbn_13 = []
            all_isbn_13_content = isbn_content['isbn_13']

            for isbn in all_isbn_13_content:
                all_isbn_13.append(isbn)

            return all_isbn_13

        else:
            return None

    @staticmethod
    def _parse_isbn_10(isbn_content):
        if 'isbn_10' in isbn_content:
            all_isbn_10 = []
            all_isbn_10_content = isbn_content['isbn_10']

            for isbn in all_isbn_10_content:
                all_isbn_10.append(isbn)

            return all_isbn_10
        else:
            return None

    @staticmethod
    def _parse_subject(isbn_content):
        if 'subjects' in isbn_content:
            subject = []
            all_subjects = isbn_content['subjects']
            for sub in all_subjects:
                subject.append(sub)
            return subject
        else:
            return None

    @staticmethod
    def _parse_publisher(isbn_content):
        if 'publishers' in isbn_content:
            publisher = []
            all_publishers = isbn_content['publishers']
            for pub in all_publishers:
                publisher.append(pub)
            return publisher
        else:
            return None

    @staticmethod
    def _parse_author(isbn_content):
        if 'authors' in isbn_content:
            author = []
            authors = isbn_content['authors']
            for a in authors:
                author.append(a['name'])
            return author
        else:
            return None

    @staticmethod
    def _parse_subtitle(isbn_content):
        if 'subtitle' in isbn_content:
            return isbn_content['subtitle']
        else:
            return None

    @staticmethod
    def _parse_title(isbn_content):
        if 'title' in isbn_content:
            return isbn_content['title']
        else:
            return None

    @staticmethod
    def _parse_edition(isbn_content):
        conversion = {("first edition", "1st"): "1", ("second edition", "2nd"): "2",
                      ("third edition", "3rd"): "3", ("fourth edition", "4th"): "4",
                      ("fifth edition", "5th"): "5", ("sixth edition", "6th"): "6",
                      ("seventh edition", "7th"): "7", ("eighth edition", "8th"): "8",
                      ("ninth edition", "9th"): "9", ("tenth edition", "10th"): "10",
                      ("eleventh edition", "11th"): "11", ("twelfth edition", "12th"): "12",
                      ("thirteenth edition", "13th"): "13", ("fourteenth edition", "14th"): "14",
                      ("fifteenth edition", "15th"): "15", ("sixteenth edition", "16th"): "16",
                      ("seventeenth edition", "17th"): "17", ("eighteenth edition", "18th"): "18",
                      ("nineteenth edition", "19th"): "19", ("twentieth edition", "20th"): "20"}

        if 'edition_name' in isbn_content:
            edition = str(isbn_content['edition_name']).lower()

            for pair in conversion:
                if edition.__contains__(pair[0]) or edition.__contains__(pair[1]):
                    return conversion[pair]

        elif 'title' in isbn_content:
            title = str(isbn_content['title']).lower()
            for pair in conversion:
                if title.__contains__(pair[0]) or title.__contains__(pair[1]):
                    return conversion[pair]

        return None

    def __str__(self):
        ret = "Title: " + str(self._title) + "\n" + \
              "Subtitle: " + str(self._subtitle) + "\n" + \
              "Edition: " + str(self._edition) + "\n" + \
              "Author: " + str(self._author) + "\n" + \
              "Publisher: " + str(self._publisher) + "\n" + \
              "Subject: " + str(self._subject) + "\n" + \
              "Input ISBN: " + str(self._input_isbn) + "\n" + \
              "All ISBN-10: " + str(self._all_isbn_10) + "\n" + \
              "All ISBN-13: " + str(self._all_isbn_13) + "\n"

        return ret
