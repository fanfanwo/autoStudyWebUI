import json
import unittest
import ddt

# from ddt import ddt, data
"""
ddt  的使用有三种方式：
1.data
2.unpack #解包
3.file_data 
"""

'''
内存存储
'''
'''
data = {
    "username": "huace_tester",
    "password": "huace_tester"
}
for value in data.items():  #循环读取data的每一项
    print(value)
'''

'''
ddt的data
'''
'''
@ddt.ddt
class Test(unittest.TestCase):

    @ddt.data((1,2,3))
    def test_data(self,a):
        print(a)

    @ddt.unpack
    @ddt.data((1,2,3,4,5,6,7))
    def test_data_unpack(self,*a):
        print(a)

'''

'''
json文件存储并读取
json文件中的数据要放在列表里
'''
'''
@ddt.ddt
class Test(unittest.TestCase):

    @ddt.unpack  # 一次性接受两个值 分别给两个属性时，需要加解包装饰器    
    @ddt.file_data("test1.json") #打开test.json文件 ,没有指定遍历类型时，默认打印value值
    def test_01(self,username,password):  #username,password为json文件中的key
        print(username,password)

'''

'''
yaml文件的读取方式
读取yaml文件不需要unpack解包
yaml文件中 第一行要加-
'''
'''
@ddt.ddt
class Test(unittest.TestCase):

    @ddt.file_data("test.yaml")
    def test_01(self,username,password):
        print(username,password)
'''

'''
ddt excel的操作
使用注意事项：
首先Excel 有两种后缀名：xls 、xlsx
xlrd == 1.2.0 以上的不支持xlsx
所以尽量指定Pip install xlrd== 1.2.0
'''
import xlrd

excel_object = xlrd.open_workbook("testexcel.xlsx")
sheet_object = excel_object.sheets()
# print(sheet_object[0].__dict__)
# 获取sheet表格内容
# data = sheet_object[1].cell(rowx=0,colx=2)
# print(data)
# data_row = sheet_object[1].row(0)
# print(data_row)
# data_row_value = sheet_object[1].row_values(0)
# print(data_row_value)
data_nrows = sheet_object[1].nrows
# print(data_nrows)
data_ncols = sheet_object[1].ncols
# print(data_ncols)
keys = sheet_object[1].row_values(0)
data = []
for i in range(1, data_nrows):
    values = sheet_object[1].row_values(i)
    # print("keys:", keys)
    # print("values:", values)
    data.append(dict(zip(keys, values)))
print("data的类型：",type(data))
ckeys = sheet_object[0].col_values(0)
data1 = []
for i in range(1,data_ncols):
    values= sheet_object[0].col_values(i)
    # print("ckeys:",ckeys)
    # print("values: ",values)
    data1.append(dict(zip(ckeys,values)))
# print(data1)
# print(json.dumps(data1))
# 组合使用，获取文件中的所有数据，
#解包后 数据data1变为字典，元组的解包和字段的解包
@ddt.ddt()
class Test(unittest.TestCase):
    # @ddt.unpack #data1解包后变成 dict字典
    # @ddt.data(data1)
    # def test_execl1(self,*value_):
    #     print(value_)

    # @ddt.data(data)
    # def test_excel2(self,value_):
    #     # print("test_excel2的传参类型",type(value_))
    #     print("test_excel2的值",value_)

    @ddt.data(data1)
    def test_excel3(self,*value_):
        print("test_excel3参数的类型：",type(value_))
        print("test_excel3的值",*value_)  #value是列表类型

    # @ddt.unpack
    # @ddt.data(*data)
    # def test_excel3(self,**value_):
    #     print(value_)

"""
ddt 和 excel的使用
第二层
思考ddt里面是不是有直接打开json文件和yaml文件的方法
是否可以构建一个打开Excel的方式在ddt里 
"""