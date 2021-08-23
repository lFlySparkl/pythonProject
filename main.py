from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path="C:\\Users\\dmitr\\PycharmProjects\\pythonProject\\chromedriver\\chromedriver.exe")

url = "https://netpeak.ua/"

try:
    browser.get(url = url)
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[1]/ul/li[3]").click()
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[3]/div/div[2]/ul[1]/li[3]/div/a").click()
    time.sleep(2)

    href = browser.find_element_by_xpath("/html/body/div[1]/div[9]/div/div/div[10]/a").get_attribute("href")
    browser.get(href)
    time.sleep(2)

    s_button = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[5]/div/a")

    if s_button:
        print("Found button")
        s_button.click()
    else:
        print("Button not found")
    time.sleep(2)

    browser.get(url=url)
    time.sleep(2)

    login_link = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[1]/div/nav/div[1]/div[2]/ul/li[1]/a").get_attribute("href")
    browser.get(login_link)
    time.sleep(2)

    u_login = "qwerty"
    u_password = "qwerty123"

    user_input = browser.find_element_by_id("login")
    user_input.send_keys(u_login)

    user_input = browser.find_element_by_id("password")
    user_input.send_keys(u_password)

    login_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/button")

    if login_button.is_enabled():
        print("Button active.")
        login_button.click()
    else:
        print("Button isn't active")
    time.sleep(2)

    browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[4]/div/md-checkbox/div[1]").click()

    login_button = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[5]/button")

    if login_button.is_enabled():
        print("Button active.")
        login_button.click()
    else:
        print("Button isn't active")
    time.sleep(2)

    found_alert = browser.find_element_by_xpath("/html/body/md-toast/div/span")
    if found_alert:
        print("Alert found")
    else:
        print("Alert not found")

    l_border = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[1]/md-input-container/input").value_of_css_property('border-color')

    p_border = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[2]/div/form/div[2]/md-input-container/input").value_of_css_property('border-color')

    if l_border and p_border == "rgb(221, 44, 0)":
        print("Alert color change to Red")
    else:
        print("Alert color not change")

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()