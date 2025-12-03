from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    'platformName': 'Android',
    "platformVersion": "12",
    "deviceName": "JFQO7PFEU44XBIIJ",
    "automationName": "UiAutomator2",
    #if we want to open an specific app then we have no need to add these lines
#dumpsys window windows | grep -E 'mTopActivityComponent' this command is used to find out the package name
    # "appPackage": "com.qompli.app",
    # "appActivity": "com.qompli.app.MainActivity",
    # "newCommandTimeout": 300,
    # "autoGrantPermissions": True,
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Phone, 2 notifications').click()

wait = WebDriverWait(driver, 10)
el = wait.until(EC.presence_of_element_located(AppiumBy.ACCESSIBILITY_ID, "com.android.dialer:id/contactsButton"))
el.click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@content-desc="New Contact"]').click()
time.sleep(5)

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Name"]').send_keys("test Ali")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]').send_keys("123456789")

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.Button[@text="Done"]').click()
driver.close()

# driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Search among 602 contact(s)"]').send_keys("Ahmad")

driver.quit()


