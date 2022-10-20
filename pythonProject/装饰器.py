
def log(func):
    def wrap(*args):
        
        return func(args)
    return wrap

@log
def a(args):
    b = 1
    return b
print(a(2))