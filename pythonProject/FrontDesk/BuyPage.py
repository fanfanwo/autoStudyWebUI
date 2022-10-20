# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''
from random import choice
class BuyPage:

    class Button:
        # buy_pattern = ("xpath",'//span[text()="货到付款"]') #货到付款购买方式
        buying_patterns = ("css selector",'.payment-list>li') #三种付款方式
        submit_orders = ("css selector",".btn-go.btn-loading-example") #提交订单按钮
        my_order = ("css selector",".am-btn.am-btn-primary.am-radius") #我的订单按钮

    class Input:
        pass

    def __init__(self,driver):
        self.driver = driver

    # def click_buy_pattern(self):
    #     #选择货到付款
    #     self.driver.find_element(*self.Button.buy_pattern).click()

    def choice_buy_pattern(self,value):
        #选择货到付款方式
        #有两n方式确定我们使用什么付款方式
        """
        选择货到付款方式
        :param value: > 0 -->支付宝  1-->微信  3-->货到付款
        :return:
        """
        #方式一--使用下标获取
        self.driver.find_elements(*self.Button.buying_patterns)[value].click()

        #方式二--li元素定位
        # ele_s = self.driver.find_elements(*self.Button.buying_patterns)
        # for i in ele_s:
        #     if i.find_element("tag name","span").text == value:
        #         i.click()

        return self

    def cash_on_delivery(self):
        #选择货到付款
        self.choice_buy_pattern(2)
        return self

    def click_submit_orders(self):
        #点击提交订单
        self.driver.find_element(*self.Button.submit_orders).click()
        return self

    def click_my_order(self):
        #点击我的订单
        self.driver.find_element(*self.Button.my_order).click()
        return self