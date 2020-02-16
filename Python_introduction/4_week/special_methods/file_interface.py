import os
import tempfile

class File:

    def __init__(self, path):
        self.path = path
        self.f = None
    
    def write(self, to_add):
        with open(self.path, 'w') as f:
            f.write(to_add)

    def read(self):
        with open(self.path, 'r') as f:
            return f.read()

    def __iter__(self):
        self.f = open(self.path, 'r')
        return self

    def __next__(self):
        try:
            return next(self.f)
        except StopIteration:
            self.f.close()
            self.f = None
            raise

    def __str__(self):
        return self.path

    def __add__(self, second):
        file_dir = tempfile.gettempdir()
        filename1 = os.path.splitext(os.path.split(self.path)[1])[0]
        filename2 = os.path.split(second.path)[1]
        ans = File(os.path.join(file_dir, filename1 + "_" + filename2))
        ans.write(self.read() + second.read())
        return ans
