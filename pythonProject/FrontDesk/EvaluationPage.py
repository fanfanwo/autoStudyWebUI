# -*- coding: utf-8 -*-
'''
登录网址：http://shop-xo.hctestedu.com/
用户名和密码都是：test_fcy
'''
from random import choice
class EvaluationPage:

    class Button:
        commit = ("xpath",'//button[text()="提交"]') #提交按钮
        anonimity = ("css selector",".am-switch-label") #匿名按钮
        level = ("css selector",".rating>li") #级别 有6个元素，但实际上页面只需要5个

    class Input:
        comment = ("name","content[]") #评价输入框

    def __init__(self,driver):
        self.driver = driver

    def evaluation(self,content):
        #评论流程
        choice(self.driver.find_elements(*self.Button.level)[:5]).click() #list切片获取前5个,随机选中1个点击
        self.driver.find_element(*self.Input.comment).send_keys(content) #输入评论内容
        self.driver.find_element(*self.Button.anonimity).click() #点击匿名按钮
        self.driver.find_element(*self.Button.commit).click()
        return self
