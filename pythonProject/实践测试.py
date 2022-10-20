'''
1.登录商城
2.选择任意商品加入购物车
3.选择货到付款方式完成下单操作
4.登录商城后台
5.在后台完成支付的确认，并操作发货
6.选择任意物流平台进行发货
7.回到商城个人中心->订单管理->核对物流信息完成 收货，并进行评价操作
'''
from BackdESK.LoginPage import LoginPage as BackLoginPage #后台loginpage
from BackdESK.OrderManagePage import OrderManagerPage
from BackdESK.IndexPage import IndexPage

from FrontDesk.LoginPage import LoginPage as FrontLoginPage #前台loginpage
from FrontDesk.BuyPage import BuyPage
from FrontDesk.HomePage import HomePage
from FrontDesk.OrderPage import OrderPage
from FrontDesk.EvaluationPage import EvaluationPage
from FrontDesk.GoodsInfoPage import GoodsInfoPage
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(20)
home = HomePage(driver)
home.open_url(driver).click_login() #打开商城首页网址 并 首页点击登录
front_login =FrontLoginPage(driver)  #到达登录页面
front_login.login("test_fcy","test_fcy") #用户名 和 密码 完成 登录操作
home.random_choice_goods() #登录后 跳转到首页，然后随机选择商品

handles = driver.window_handles # 随机选择完商品后，新增商品页面
driver.switch_to.window(handles[-1]) #切换句柄 到商品详情页面

goods_info = GoodsInfoPage(driver)
goods_info.random_choice_format().buy_goods() # 随机选择商品规格，点击立即购买 ,到购买界面

buy = BuyPage(driver)
buy.cash_on_delivery().click_submit_orders().click_my_order() #跳转到订单管理页面

order = OrderPage(driver)
order_number = order.get_order_number() #获取订单号，然后到后台进行操作,

#新增标签页，打开后台管理页面
driver.switch_to.new_window()
back_login = BackLoginPage(driver) #实例化后台管理页面
back_login.open_url().login("huace_tester","huace_tester") #登录后台管理页面

index = IndexPage(driver) #跳转后台初始页面
index.click_level1_order_manager().click_level2_order_manager() #点击后台管理页面的订单管理

order_manage = OrderManagerPage(driver)  #跳转到订单管理页面
order_manage.switch_to_frame().search(order_number).click_pay().click_pay_confirm().click_delivery("物流单号")

handles = driver.window_handles #到前台订单管理页面
driver.switch_to.window(handles[1])

order.search(order_number).click_receive().click_comment() #在订单管理页面，点击收货，点击评论按钮

handles = driver.window_handles #点击评论按钮，新增页面 ，到评论页面
driver.switch_to.window(handles[-1])

evaluation_page = EvaluationPage(driver)
evaluation_page.evaluation("商品还好，货真价实") #在评论页面，数据评论