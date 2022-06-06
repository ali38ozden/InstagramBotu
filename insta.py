
from selenium import webdriver
from time import sleep

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get("https://instagram.com")
sleep(5)

# Buraya(XXXXXXXXXXXX) kendi kullanici adinizi yaziyorusunuz
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")\
    .send_keys("XXXXXXXXXXXXXXXXX")
sleep(2)
# Buraya(XXXXXXXXXXXX) kendi şifrenizi yaziyorsunuz
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")\
    .send_keys("XXXXXXXXXXXXXXXX")
sleep(2)
driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")\
    .click()
sleep(4)
driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
    .click()
sleep(4)
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]")\
    .click()
sleep(2)   
driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[3]/div[2]/div[1]/a/div")\
    .click()
sleep(2) 

for i in range(3):
    sleep(2)
    for c in  range(10):
        k=str(c+1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[2]/div/div/div["+k+"]/div[3]/button/div")\
            .click()                 
        sleep(1)                     
    driver.refresh()