# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''

class LoginPage:
    url = "http://shop-xo.hctestedu.com/"

    class Button:
        login = ("xpath", '//button[text()="登录"]')

    class Input:
        username = ("name", "accounts")
        password = ("name", "pwd")

    def __init__(self,driver):
        self.driver = driver

    def login(self,username,password):
        self.driver.find_element(*self.Input.username).send_keys(username)
        self.driver.find_element(*self.Input.password).send_keys(password)
        self.driver.find_element(*self.Button.login).click()
        return self