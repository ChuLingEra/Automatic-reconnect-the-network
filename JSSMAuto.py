# Date:2022.4.23
# Author:ChuLingEr
# Tip:nothing

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

option = webdriver.ChromeOptions()
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
wb = webdriver.Chrome(options=option)  # 配置浏览器

wb.get('http://172.17.207.11/')  # 校园网登录页面IP地址
wb.implicitly_wait(5)  # 隐式等待(秒),为了防止网页加载不完全

wb.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/form/input[2]').send_keys('')  # 输入你的账号
wb.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/form/input[3]').send_keys('')  # 输入你的密码

ipt_tag = wb.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/select')  # 获取下拉框
options = Select(ipt_tag).options  # 获取下拉框的所有选项
options_selected = Select(ipt_tag).all_selected_options  # 合并下拉框的所有选项
Select(ipt_tag).select_by_index(1)  # 本部举例，1为校园网，2为中国移动，3为中国电信，4为中国联通,根据实际情况修改

wb.find_element(By.XPATH, '/html/body/div/div/div[2]/div[4]/form/input[3]').send_keys(
    Keys.ENTER)  # 点击登录，在自动输入密码后自动键入回车达到登录的目的

sleep(2)  # 等待2s自动关闭浏览器以及WebDriver相关进程
wb.quit()
print('登录成功')
