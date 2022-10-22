import ddt
import unittest
"""
ddt 和 excel的使用
第二层
思考ddt里面是不是有直接打开json文件和yaml文件的方法
是否可以构建一个打开Excel的方式在ddt里 
"""

@ddt.ddt()
class Test2(unittest.TestCase):
    @ddt.excel_data("testexcel.xlsx","Sheet2")
    def test_excel5(self,**value_):
        print(value_)