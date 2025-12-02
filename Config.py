from appium.webdriver.common.appiumby import AppiumBy
from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    "platformVersion": "12",
    "deviceName": "JFQO7PFEU44XBIIJ",
    "automationName": "UiAutomator2",
    #if we want to open an specific app then we have no need to add these lines
    # "appPackage": "com.qompli.app",
    # "appActivity": "com.qompli.app.MainActivity",
    # "newCommandTimeout": 300,
    # "autoGrantPermissions": True,
}

url = 'http://127.0.0.1:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Contacts, 0 notifications')
el.click()

driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Search among 602 contact(s)"]').send_keys("Mama G")

# driver.quit()


