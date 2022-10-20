# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/admin.php?s=/index/index.html
用户名和密码都是：huace_tester
'''

class IndexPage:

    class Button:
        order_manages = ("xpath",'//span[text()="订单管理"]') #订单管理有两个层级

    class Input:
        pass

    def __init__(self,driver):
        self.driver = driver

    def click_level1_order_manager(self):
        #点击层级一的订单管理按钮
        self.driver.find_elements(*self.Button.order_manages)[0].click()
        return self

    def click_level2_order_manager(self):
        #点击层级二的订单管理按钮
        self.driver.find_elements(*self.Button.order_manages)[1].click()
        return self