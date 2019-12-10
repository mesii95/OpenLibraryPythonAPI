# OpenLibraryPythonAPI
A Python API to obtain Book information from OpenLibrary.org


For educational and research purposes I have created this API to obtain book data from OpenLibrary.org using
their provided REST API.


Example use case:

  valid_isbn = 978-0486404530
  
  book = OpenLib(valid_isbn)
  
  print(book)
