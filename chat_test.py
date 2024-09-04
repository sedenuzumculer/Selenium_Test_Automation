
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

# Initialize undetected_chromedriver
options = uc.ChromeOptions()
driver = uc.Chrome(options=options)
options.add_argument('--start-maximized')
options.add_argument('--disable-extensions')

# Open the ChatGPT login page
driver.get('https://chatgpt.com/')

login_button = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.XPATH, '//div[contains(@class, "flex") and contains(@class, "items-center") and '
                                          'contains(@class, "justify-center")]'))
)
login_button.click()

# Locate and fill out the login form
time.sleep(5)
email_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'email-input')))
email_input.click()
email_input.send_keys('mail')

continue_button = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.CLASS_NAME, 'continue-btn'))
)

continue_button.click()
password_input = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'password')))
password_input.click()
password_input.send_keys('your password goes there')
continue_button2 = WebDriverWait(driver, 10).until(
    ec.element_to_be_clickable((By.CSS_SELECTOR, '.c15aec4ff.c49d141c8.c451ec505.ce3ec1195._button-login-password'))
)
continue_button2.click()
time.sleep(2)

time.sleep(100)
driver.quit()
