

class ISBNFormatException(Exception):
    def __call__(self, msg):
        self.msg = msg
