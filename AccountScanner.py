from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
import random
driver = webdriver.Firefox()


email = input("Enter your Email:")
print("Your email is " + email)

#Twitter

twitter_signup = "https://twitter.com/i/flow/signup"
driver.get(twitter_signup)
time.sleep(2)

link = driver.find_element_by_xpath('//span[text()="Use email instead"]/parent::div')
link.click()
time.sleep(2)

email_element = driver.find_element_by_name('email')
email_element.send_keys(email)
time.sleep(2)

try:
    notif = driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[3]/div/div/div/div/span')

    if notif.text == "Email has already been taken.":
        print("Twitter: Email found")
except:
    print("Twitter: Email not found")
        



driver.quit()

#Instagram

errors=[]
instagram_occupied = False
driver = webdriver.Firefox()
driver.get('https://www.instagram.com/')
try:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[1]/div/label/input')))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[1]/div/label/input').send_keys(email)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys('asdasdasdasd')
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[1]/div[2]/div/label/input').send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="slfErrorAlert"]')))
    alert = driver.find_element_by_xpath('//*[@id="slfErrorAlert"]')
    #print(alert.text)

    if(alert.text == "The username you entered doesn't belong to an account. Please check your username and try again."):
        instagram_occupied = False
    else:
       instagram_occupied = True

except:
    errors.append('Instagram page has changed please look at page again and refactor code.')


if instagram_occupied:
    print('Instagram: Email Found')
else:
    print('Instagram: Email Not Found')

driver.quit()

#facebook
errors2=[]
facebook_occupied = False
driver = webdriver.Firefox()
driver.get('https://www.facebook.com')
try:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="email"]')))
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="email"]').send_keys(Keys.RETURN)

   
    
    try:
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]')))
        alert = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/form/div/div[1]/div[2]')
        #print(alert.text)
        if(alert.text == "Email yang Anda masukkan tidak cocok dengan akun mana saja. Buat sebuah akun."):
            facebook_occupied = False
        

    except:
        facebook_occupied=True
        

except:
    errors2.append('facebook page has changed please look at page again and refactor code.')


if facebook_occupied:
    print('Facebook: Email Found')
else:
    print('Facebook: Email Not Found')

driver.quit()

#adobe

errors3=[]
adobe_occupied = False
driver = webdriver.Firefox()
driver.get('https://auth.services.adobe.com/en_US/deeplink.html?deeplink=ssofirst&callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FSunbreakWebUI1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Faccount.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dtrue%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=SunbreakWebUI1&scope=AdobeID%2Copenid%2Cacct_mgmt_api%2Cgnav%2Csao.cce_private%2Csao.digital_editions%2Ccreative_cloud%2Cread_countries_regions%2Csocial.link%2Cunlink_social_account%2Cadditional_info.address.mail_to%2Cclient.scopes.read%2Cpublisher.read%2Cadditional_info.account_type%2Cadditional_info.roles%2Cadditional_info.social%2Cadditional_info.screen_name%2Cadditional_info.optionalAgreements%2Cadditional_info.secondary_email%2Cadditional_info.secondary_email_verified%2Cadditional_info.phonetic_name%2Cadditional_info.dob%2Cupdate_profile.all%2Csecurity_profile.read%2Csecurity_profile.update%2Cadmin_manage_user_consent%2Cadmin_slo%2Cpiip_write%2Cmps%2Clast_password_update%2Cupdate_email%2Caccount_cluster.read%2Caccount_cluster.update%2Cadditional_info.authenticatingAccount%2Creauthenticated&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FSunbreakWebUI1%3Fredirect_uri%3Dhttps%253A%252F%252Faccount.adobe.com%252F%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%2526reauth%253Dtrue%26response_type%3Dtoken&relay=a3a531b2-295f-4a4b-b482-b692d2b03c38&locale=en_US&flow_type=token&ctx_id=accmgmt&idp_flow_type=login&reauthenticate=force#/')
try:
    email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="EmailPage-EmailField"]')))
    driver.find_element_by_xpath('//*[@id="EmailPage-EmailField"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="EmailPage-EmailField"]').send_keys(Keys.RETURN)

   
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section[2]/section/form/section[1]/label')))
        alert = driver.find_element_by_xpath('/html/body/div[1]/div/div/section/div/div/section/div/section/div/div/section[2]/section/form/section[1]/label')
        print(alert.text)
        if(alert.text == "Check your email address or create a new account"):
            adobe_occupied = False
        

    except:
        adobe_occupied=True

except:
    errors3.append('Adobe page has changed please look at page again and refactor code.')


if adobe_occupied:
    print('Adobe: Email Found')
else:
    print('Adobe: Email Not Found')



#github
error4=[]
delay = 3
github_occupied = False
driver.get('https://github.com/join')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.XPATH, '//*[@id="user_email"]')))
    email_input = driver.find_element_by_xpath('//*[@id="user_email"]').send_keys(email)
    driver.find_element_by_xpath('//*[@id="user_password"]').click()
    driver.find_element_by_xpath('//*[@id="user_email"]').click()
except TimeoutException:
    errors.append('Github page has changed please look at page again and refactor code.')
try:
    WebDriverWait(driver, delay).until(EC.presence_of_element_located(
        (By.CLASS_NAME, 'error')))
    github_elmnt = driver.find_element_by_class_name('error')
    github_occupied = True
except TimeoutException:
    github_occupied = False
    errors.append('Github Timeout/ Element cannot be found anymore.')
if github_occupied:
    print('Github: Email Found')
else:
    print('Github: Email Not Found')
