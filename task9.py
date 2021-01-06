from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from selenium import webdriver
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element_by_tag_name('button').click()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)

    select = browser.find_element_by_css_selector("input#answer")
    select.send_keys(y)

    browser.find_element_by_css_selector('button[type="submit"]').click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()    

    #new_window = browser.window_handles[1]
    #browser.switch_to.window(new_window)

