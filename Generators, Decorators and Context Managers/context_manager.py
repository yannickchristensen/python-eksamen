from contextlib import contextmanager

f = open("test.txt", "r")
s = f.readline()
f.close()

class File:
    def __init__(self, filename, method):
        self.file = open(filename, method)

    def __enter__(self):
        print('Enter')
        return self.file

    def __exit__(self, *args):
        print('Exit')
        self.file.close()
        if args[0] == FileNotFoundError:
            return True
        
with File("test.txt", "w") as file:
    file.write('hello world')
    print('doing stuff')
    raise FileNotFoundError

""" @contextmanager
def file(filename, method):
    print('enter')
    file = open(filename, method)
    yield file
    file.close()
    print('exit')

with file("test.txt", "w") as f:
    f.write("hello")
    print('doing stuff') """