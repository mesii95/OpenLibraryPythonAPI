# OpenLibraryPythonAPI
A Python API to obtain Book information from OpenLibrary.org


For educational and research purposes I have created this API to obtain book data from OpenLibrary.org using
their provided REST API.

The data is stored in a Python object dictionary with the following fields. Each field has the conventional 
getter. ex: object.title()

    _title = None
    _subtitle = None
    _edition = None
    _author = None
    _publisher = None
    _subject = None
    _input_isbn = None
    _all_isbn_10 = None
    _all_isbn_13 = None
    

#Example use case:
  
  from BookMeta.OpenLibrary import *
  
  valid_isbn = '978-0486404530'
  
  book = OpenLib(valid_isbn)
  
  print(book)

#Output:

  Title: Calculus
  Subtitle: an intuitive and physical approach
  Edition: 2
  Author: ['Morris Kline']
  Publisher: ['Dover Publications']
  Subject: ['Calculus']
  Input ISBN: 9780486404530
  All ISBN-10: ['0486404536']
  All ISBN-13: None
  
