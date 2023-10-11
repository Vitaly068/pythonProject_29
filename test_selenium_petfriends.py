import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_petfriends(web_browser):
    # Open PetFriends base page:
    web_browser.get("https://petfriends.skillfactory.ru/")

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # click on the new user button
    btn_newuser = web_browser.find_element(By.XPATH, "/html/body/div/div/div[2]/button")
    btn_newuser.click()

    # click existing user button
    btn_exist_acc = web_browser.find_element(By.XPATH, "/html/body/div/div/form/div[4]/a")
    btn_exist_acc.click()

    # add email
    field_email = web_browser.find_element(By.ID, "email")
    field_email.clear()
    field_email.send_keys("totena@fexbox.org")

    # add password
    field_pass = web_browser.find_element(By.ID, "pass")
    field_pass.clear()
    field_pass.send_keys("totena")

    # click submit button
    # btn_submit = web_browser.find_element_by_xpath("//button[@type='submit']")
    btn_submit = web_browser.find_element(By.XPATH, "/html/body/div/div/form/div[3]/button")
    btn_submit.click()

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
    # click submit my pets
    btn_submit = web_browser.find_element(By.XPATH, "/html/body/nav/div[1]/ul/li[1]/a")
    btn_submit.click()



    # Make the screenshot of browser window:
    web_browser.save_screenshot('my_pets.png')

    assert web_browser.current_url == 'https://petfriends.skillfactory.ru/my_pets', "login error"
