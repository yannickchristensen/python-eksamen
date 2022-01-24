import time

#Decorator
# what is a decorator

def timer(func):
    def wrapper(*args, **kwargs):
        before = time.time()
        func(*args, **kwargs)
        print("Function took:", time.time() - before, "seconds")
    return wrapper


def run():
    time.sleep(2)


run = timer(run)
run()

""" class Dad:
    @staticmethod
    def letsGo():
        print ('goodbye')


Dad.letsGo() """