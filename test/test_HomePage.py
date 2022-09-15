from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj=Service("C:/chromedriver.exe")
driver=webdriver.Chrome(service=service_obj)
driver.get("https://kalaguragampa.com/")
driver.implicitly_wait(5)
driver.maximize_window()
driver.get_screenshot_as_png()
assert driver.title =="Kalagura Gampa Store - Home"
print("Successfully landed in Homepage")
driver.close()