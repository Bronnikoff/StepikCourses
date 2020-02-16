import time

class Logger:
    count = 0
    def __init__(self, filename):
        self.filename = filename
    
    def __call__(self, func):
        print("init")
        def wrapper():
            self.count += 1
            print(self.count)
            func()
        return wrapper

class Iterrator:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current == self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result

class IndexItterator:
    def __init__(self, obj):
        self.obj = obj
    
    def __getitem__(self, index):
        return self.obj[index]

class open_file:
    def __init__(self, filename, mode):
        self.f = open(filename, mode)

    def __enter__(self):
        return self.f
    
    def __exit__(self, *args):
        self.f.close()

class another_manager:
    def __init__(self, exc):
        self.exc = exc
    
    def __enter__(self):
        return None
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.exc == exc_type:
            print("Nothing Happend")
            return True
        print("Noww we kill the programm! Get ready")

class time_managment:
    def __init__(self):
        self.time = 0
    
    def current_time(self):
        print("Time in manager:", time.time() - self.time)

    def __enter__(self):
        self.time = time.time()
        return self

    def __exit__(self, *args):
        print("Time in manager:", time.time() - self.time)

logger = Logger("test.txt")

@logger
def something_func():
    print("Here!")

l = list(Iterrator(1, 5))
print(l)

print("*-" * 5)
something_func()
something_func()

l = list(IndexItterator("hello"))
print(l)

with open_file("text.txt", 'w') as f:
    f.write("OpenFile Manager")

with another_manager(ZeroDivisionError):
    1 / 0

print("Im Here!")

with time_managment() as t:
    print("Go to sleep")
    time.sleep(5)
    print("Look to clocks:")
    t.current_time()
    time.sleep(3)
    print("Wake up")

