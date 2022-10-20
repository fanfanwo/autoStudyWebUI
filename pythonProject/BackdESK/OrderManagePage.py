# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/admin.php?s=/index/index.html
用户名和密码都是：huace_tester
'''
import time
from random import choice
from selenium.webdriver.support.wait import WebDriverWait #导包等待的对象
from selenium.webdriver.support import expected_conditions as EC #导包的条件集合包（模块）文件
class OrderManagerPage:
    iframe = "ifcontent" #订单管理页面 左右结构的frame

    class Button:
        search = ("css selector",".am-icon-search") #订单管理页面的搜索按钮
        pay = ("xpath",'//span[text()="支付"]') #后台订单管理页面搜索 客户下的订单 的支付按钮
        pay_confirm = ("xpath",'//button[text()="确认"]')#点击支付后 的 确认按钮
        delivery = ("xpath",'//span[text()="发货"]') #点击确认后，发货按钮
        logistics_companies = ("css selector",".express-list>li") #14个 发货方式
        logistics_cofirm = ("xpath",'//button[text()="确认"]') #确认按钮

    class Input:
        searchs = ("css selector",".am-form-field.am-radius") #订单管理页面搜索输入框
        logistics_num = ("name", "express_number")  # 填写快递单号

    def __init__(self,driver):
        self.driver = driver

    def switch_to_frame(self):
        #进入到 frame
        self.driver.switch_to.frame(self.iframe)
        return self

    def search(self,text):
        #搜索框输入订单号，并点击搜索按钮
        self.driver.find_elements(*self.Input.searchs)[0].send_keys(text)
        self.driver.find_element(*self.Button.search).click()
        return self

    def click_pay(self):
        #点击支付按钮
        self.driver.find_element(*self.Button.pay).click()
        return self

    def click_pay_confirm(self):
        #点击确认支付按钮
        # pay_button = self.driver.find_elements(*self.Button.pay_confirm).click()
        WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(self.Button.pay_confirm))[-1].click()
        return self

    def click_delivery(self,logistics_number):
        #交付流程
        #点击发货按钮
        # self.driver.find_element(*self.Button.delivery).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.Button.delivery))[0].click()
        #随机选择物流公司

        ec = choice(self.driver.find_elements(*self.Button.logistics_companies))
        ec.click()
        # choice(WebDriverWait(self.driver,10).until(EC.visibility_of_any_elements_located(self.Button.logistics_companies))).click()
        #填写物流单号
        self.driver.find_element(*self.Input.logistics_num).send_keys(logistics_number)
        # WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.Input.logistics_num)).send_keys(logistics_number)
        #点击 确认按钮
        # self.driver.find_element(*self.Button.logistics_cofirm).click()
        # WebDriverWait(self.driver, 10).until(EC.visibility_of_any_elements_located(self.Button.logistics_cofirm))[-1].click()
        time.sleep(10)
        self.click_pay_confirm()
        print("------------------")
        return self
