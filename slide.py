import cv2
import time
import requests
from selenium import webdriver
import urllib.request
import distance2
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://qzone.qq.com/")
driver.switch_to.frame("login_frame")
driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
driver.find_element_by_xpath('//*[@id="u"]').send_keys("1230000000")
driver.find_element_by_xpath('//*[@id="p"]').send_keys('123456789')
driver.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(10)
print(driver.page_source)
driver.switch_to.frame("tcaptcha_iframe")
#driver.find_element_by_xpath('//*[@id="slideBg"]').screenshot('123.png')
url1 = driver.find_element_by_xpath('//*[@id="slideBg"]').get_attribute("src")
url2 = driver.find_element_by_xpath('//*[@id="slideBlock"]').get_attribute("src")
urllib.request.urlretrieve( url1,'Bg.jpg')
urllib.request.urlretrieve( url2,'Block.png')
'''
计算移动距离
'''
image = cv2.imread('Bg.jpg')
dis = distance2.get_pos(image)
h,w,t = image.shape#(h,w,3)
#获取移动距离,原始图像是w*h 展示图像是280*163 按比例缩放
dis = dis*280/w - 31
print("滑动距离=",dis)

#滑动验证

from selenium.webdriver.common.action_chains import ActionChains
element = driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
ActionChains(driver).click_and_hold(element).perform() #点击不放
ActionChains(driver).move_by_offset(xoffset=dis,yoffset=0).perform() #拖动
ActionChains(driver).release(element).perform() #释放鼠标

