from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# Step 1) Open Firefox
browser = webdriver.Firefox()
WebDriverWait( browser, 5 )
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
browser.find_elements(By.XPATH, "//button[contains(string(), 'Autoriser les cookies essentiels et optionnels')]")[0].click()
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = browser.find_element(By.ID, "email")
password = browser.find_element(By.ID, "pass")
submit   = browser.find_element(By.NAME, "login")
username.send_keys("YOUR EMAILID")
password.send_keys("YOUR PASSWORD")
# Step 4) Click Login
submit.click()
wait = WebDriverWait( browser, 20 )

browser.quit()


# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# # Initialisation du navigateur Firefox
# driver = webdriver.Firefox()
#
# # Ouverture de google.com
# #driver.get("https://www.google.com/")
# driver.get("https://www.immoweb.be/en/search/house/for-sale?countries=BE&page=1&orderBy=relevance")
# driver.implicitly_wait(10)
#
# # Attente de l'affichage de la bannière de cookies et acceptation
#
# try:
#     WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'sc-eDvSVe cIgccM')]"))).click()
#     driver.find_element(By.CLASS_NAME, 'sc-eDvSVe cIgccM').click()
#     driver.find_element(By.XPATH, '//button[text()="ok"]').click()
#     driver.find_element_by_xpath('//*[@data-testid="uc-btn-accept-all-button"]').click()
#     #driver.find_element_by_xpath("//button[contains(text(), 'compris')]").click()
#     #driver.find_element_by_xpath("//button[contains(text(), 'refuser')]").click()
#
# except:
#     print("Impossible d'accepter les cookies.")
#
# # Recherche "python" dans Google
# search_bar = driver.find_element(By.NAME, 'q')
# search_bar.send_keys("python")
# search_bar.submit()
#
# time.sleep(15)
#
# # Fermeture du navigateur
# driver.quit()