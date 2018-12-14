# driver.find_element(By.XPATH,"//*[contains(@text,'xxx')]")
import os
from selenium.webdriver.common.by import By

loc = (By.XPATH,"//*[contains(@text,'xxx')]")


# print("loc类型：",type(loc))
#
# print("解包前：",loc)
# # 解包
# print("解包后：",*loc)

# lac = By.XPATH,"//*[contains(@text,'xxx')]"
#
# print("类型：", type(lac))
# print("解包前：", lac)
# print("解包后：", *lac)

filename="data_login.yaml"
print(os.getcwd()+os.sep+"data"+os.sep+filename)