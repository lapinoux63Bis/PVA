from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import csv

# Step 1) Open Firefox
timestamp = time.time()
browser = webdriver.Firefox()
WebDriverWait( browser, 8 )
# Step 2) Navigate to Facebook

browser.get("http://www.facebook.com")
# browser.find_elements(By.XPATH, "//button[contains(string(), 'Autoriser les cookies essentiels et optionnels')]")[0].click()
# # Step 3) Search & Enter the Email or Phone field & Enter Password
# username = browser.find_element(By.ID, "email")
# password = browser.find_element(By.ID, "pass")
# submit   = browser.find_element(By.NAME, "login")
# username.send_keys("YOUR EMAILID")
# password.send_keys("YOUR PASSWORD")
# # Step 4) Click Login
# submit.click()

wait = WebDriverWait(browser, 15) #.until(browser.find_element((By.CLASS_NAME, '_9ay7')))

browser.quit()
timestamp1 = time.time()

with open("registre_actions.csv", "a", newline='') as csvfile:
    write = csv.writer(csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write.writerow([timestamp, timestamp1, "", "", "", "", "", "Selenium"])

