

class ISBNNotFoundException(Exception):
    def __call__(self, msg):
        self.msg = msg
