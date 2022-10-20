import unittest


class Test(unittest.TestCase):
    def test_01(self):
        """
        构造一个根据a的数据的不同而得到不同的结果的测试用例
        本质可以理解为，根据不同的a的值执行不同的测试用例
        :return:
        """
        print(self.a)
    # pass

a = (1,2,3,4,5,6,7)
"""
构造一个函数，
遍历a 运行用例
"""
setattr(Test,"a",a)
def test_11111(self):
    # print(self.a)
    pass
for i in a:
    setattr(Test,f"test_custom_{i}",test_11111)
# print(Test.__dict__)
setattr(Test.test_custom_1,"b",123)
print(getattr(Test.test_custom_1,"b"))

"""
为函数添加一个测试数据的方法
"""
'''
for i in a:
    def func(self):
        print(self.a)
    setattr(Test,f"test_custom_{i}",func) #为Test 构建了一个函数 , 循环构造了8个测试用例 =每个测试用例函数都是test开头（test_custom_1 - test_custom_8），-->为类添加测试用例的方法
    setattr(Test,"a",i) #为Test 构建了变量
'''

'''
for i in a:
    def func(self):
        print(self.id())
    setattr(Test,f"test_{i}",func)
    # print(Test.__dict__) #打印类中的所有函数
'''

'''
推理理解
测试用例需要执行，有两点要求：
1.Test对象里面的函数名必须是test开头
2.Test对象里面的用例主体，必须是函数
'''

