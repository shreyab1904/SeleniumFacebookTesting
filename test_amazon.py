import time

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager

driver=webdriver.Chrome(ChromeDriverManager().install())

print("Test case Started")
driver.maximize_window()
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fhomepage.html%3F_encoding%3DUTF8%26ref_%3Dnavm_em_signin%26action%3Dsign-out%26path%3D%252Fgp%252Fhomepage.html%253F_encoding%253DUTF8%2526ref_%253Dnavm_em_signin%26signIn%3D1%26useRedirectOnSuccess%3D1%26ref_%3Dnav_em_signout_0_1_1_32&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
time.sleep(1)
driver.find_element_by_name("email").send_keys("")
time.sleep(1)
driver.find_element_by_id("continue").click()
driver.find_element_by_name("password").send_keys("")
time.sleep(1)
driver.find_element_by_id("signInSubmit").click()
driver.find_element_by_id("twotabsearchtextbox").send_keys("Samsung A52")
driver.find_element_by_id("nav-search-submit-text").click()

time.sleep(60)
print("test case has successfully completed")