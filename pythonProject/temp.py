a = ([{"name":"fcy"},{"name":"fcy"}],)

def fun(*args,**kwargs):
    print(type(*args))
    print(args)
fun(a)