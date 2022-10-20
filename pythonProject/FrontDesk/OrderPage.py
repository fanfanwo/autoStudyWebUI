# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''
from selenium.webdriver.support.wait import WebDriverWait #导包等待的对象
from selenium.webdriver.support import expected_conditions as EC #导包的条件集合包（模块）文件
class OrderPage:

    class Button:
        order_numbers = ("css selector",".am-icon-bookmark-o") #订单管理页面的 订单号
        receive = ("xpath", '//span[text()="收货"]')  # 收货按钮 --货到付款方式，后台点击发货，后 等客户点击收货按钮
        confirm_receive = ("xpath",'//span[text()="确定"]') #确定收货按钮
        comment = ("xpath",'//span[text()="评论"]') #收货后 评论按钮
        search = ("xpath",'//button[text()=" 搜索"]') #搜索按钮

    class Input:
        search = ("name","f0p") #搜索订单号

    def __init__(self,driver):
        self.driver = driver

    def get_order_number(self):
        #获取订单
        order_num = self.driver.find_element(*self.Button.order_numbers).text.lstrip() # 20221012204950277936订单号前面会有个空格
        return order_num

    def search(self,ordernum):
        #搜索订单号
        self.driver.find_element(*self.Input.search).send_keys(ordernum)
        self.driver.find_element(*self.Button.search).click()
        return self

    def click_receive(self):
        #收货按钮
        self.driver.find_element(*self.Button.receive).click()
        #收货确定确定按钮
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.Button.confirm_receive)).click()
        # self.driver.find_element(*self.Button.confirm_receive).click()
        return self

    def click_comment(self):
        #评论按钮
        self.driver.find_element(*self.Button.comment).click()
        return self