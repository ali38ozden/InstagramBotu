
from time import sleep

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()
driver.get("https://www.instagram.com") 
sleep(2)

# a=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[2]/div/div/div/div/ul/li[3]/div/button")
# print(a.accessible_name[-10:-1])  
while True:
    try:
        a=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div/div[2]/div/div/div/div/ul/li[3]/div/button")
        goldumu=a.accessible_name[-10:-1]
    except:
        print("hikaye basma geçildi")
        pass            
    if(goldumu==" görülmed"):
        print("bu hikaye daha görülmedi")
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/section/div[1]/div[2]/div/div/div/div/ul/li[4]/div/button/div[1]/span/img").click()
        except:
            print("ilk gecildi")
            pass
        try:
            bilgicek=driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/header/div[2]/div[1]/div/div/div/div/a")
            print(bilgicek.text)    
        except:
            print("2. gecildi")
            pass
        try:
            kacHikayeVar=driver.find_elements_by_css_selector("._ac3n").__len__()
            kacHikayeGecildi=driver.find_elements_by_css_selector("._ac3p").__len__()
            print(kacHikayeVar-kacHikayeGecildi)
            for i in range(kacHikayeVar-kacHikayeGecildi):
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/div[3]/div/div/div[2]/span/button").click()
                except:
                    print("beğen bulunamdı")
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]/div").click()
                except:
                    print("hikaye gec button bulunamadi")
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div/button/div/svg").click()
                except:  
                    print("bu ne bilmiyorum")                         
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[1]/div/div[3]/div").click()
                except: 
                    print("bu da ne bilimiyorum")                          
                    pass
                try:
                    driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/div[1]/div/div[5]/section/div/button[2]").click()
                except:
                    print("bir gec button daha gecildi")
                    pass

        except:
            print("burya dustu ")
            pass




#| görülmed
#|e, görüld
