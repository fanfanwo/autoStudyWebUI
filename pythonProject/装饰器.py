# -*- coding: utf-8 -*-

# 不带参数的装饰器
'''
def log(func): #func接受被装饰的函数的引用
    print(func) #打印结果：<function a at 0x0180C0B8>
    return func

@log
def a():
    print(1111)
    return 111
a()

'''

# 被装饰的函数有参数 怎么办
'''
def log(func): #func接受被装饰的函数的引用
    def wrap(*args):  #闭包函数
        return func(*args)
    return wrap
@log
def b(args):
    print(args)
    return 111
b(123)
'''

'''
# 如果装饰器要有参数 怎么办？
def log(value1, value2):
    def wrapper(func):
        setattr(func, value1, "value1")
        setattr(func, value2, "value2")
        return func
    return wrapper

@log("value1", "value2")  # == wrapper 是一个引用 +() 是调用 wrapper(c)
def c():
    print("执行了c")
    return 111

print(getattr(c, "value1"))
'''

#如果被装饰的函数需要参数，，装饰器函数也要参数 怎么办？
def log(value1,value2):
    # print(value1,value2)
    def wrapper(func):
        # print(value1, value2)
        def wrap(*args,**kwargs):
            setattr(func,value1,args[0])
            setattr(func,value2,args[1])
            return func(*args,**kwargs)
        return wrap
    return wrapper

@log("参数1","参数2")
def d(*args,**kwargs):
    print(args,kwargs)

# d("a","b","c","v",name = 1,nickname=123)
# d("a","b")
d("account","passwd",name=1)
if hasattr(d,"参数1"):
    print(111)
