from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

text=["takip edermisiniz","takipe takip ","nice post","gt","takip edebilirmisiniz","beni geri takip edermisiniz","yeni bir şeyler deniyorum beni takip edermisiniz","sevdim inkar edemem yaşadım isyan edemem",\
    "umdum cenneten ","zaman öylede geçiyor","hayat böylede bitiyor","bu yourmu okuyosan okumuş oluyosun sdfhasdfaf","güzel post","yazlım ile uğraşan varmı","bir takip ederseniz sevinirim be","yazlim oğrenmek istyenler buyursun efendim"]

#sistem
kacKereGecildi=0
kacKisiTakipEdildi=0
postbulundu=True

#-----------------bizim belirlediğimiz
Toplam_Islme=15             #15
Bir_Sayfada_KacKisi_Takip=0      #15
Begen_Yorum_Sayisi=3        #3

Ilk_Defa_Giris=False

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.instagram.com")
driver.maximize_window()



if Ilk_Defa_Giris==True:
    kullaniciAdi=input("KULLANICI ADI: ")
    kullaniciSifre=input("KULLANICI SİFRE: ")
    sleep(5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input")\
        .send_keys(kullaniciAdi)
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input")\
        .send_keys(kullaniciSifre)
    sleep(0.5)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]")\
        .click()
    sleep(4)
    try:
        driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")\
            .click()
    except:
        pass

driver.get("https://www.instagram.com/explore/people/")

for i in range(Toplam_Islme): # toplam islem tekrar sayisi
    sleep(2)
    for c in  range(Bir_Sayfada_KacKisi_Takip): #Takip etme dondgusu
        k=str(c+1)
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[2]/div/div/div["+k+"]/div[3]/button/div")\
             .click() 
            kacKisiTakipEdildi=kacKisiTakipEdildi+1; 
        except:
            kacKereGecildi=kacKereGecildi+1
            print("Button: "+str(k)+" gecildi                SimdiyeKadarGecilen: "+str(kacKereGecildi)+"            Kac kisi takip ediliyor: "+str(kacKisiTakipEdildi))
            pass               
        sleep(1)                     
    driver.refresh()
    print("SimdiyeKadarGecilen: "+str(kacKereGecildi)+"            Kac kisi takip ediliyor: "+str(kacKisiTakipEdildi))

    driver.get("https://www.instagram.com/explore/")                                                         # kesif ete girmek
    sleep(5)

    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div[1]/div[2]").click()                                                  # ilk posta tıklamak
        postbulundu=True
    except:
        print("\n\nilk post konum bulunamadı baska deneneiyor 1\n\n")
        postbulundu=False

    if postbulundu==False:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]").click()                                                  # ilk posta tıklamak
            postbulundu=True
        except:
            print("\n\nilk post konum bulunamadı baska deneneiyor 2\n\n")
            postbulundu=False

    if postbulundu==False:
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[1]/div/a/div[1]/div[2]").click()                                                  # ilk posta tıklamak
            postbulundu=True
        except:
            print("\n\nilk post konum bulunamadı baska deneneiyor 3\n\n")
            postbulundu=False

    sleep(random.randint(1,2))

    for a in range(Begen_Yorum_Sayisi): # döngü 5 kere çalışacak
 
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button")\
               .click()                                                                                                                                                                                                             # post beğen                     
        except:
           print("hata 1")
           input("baklım neymis")
        
        sleep(random.randint(0,2))

        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea")\
                .send_keys(str(random.randint(0,10))+text[random.randint(0,text.__len__()-1)]+str(random.randint(0,99))) #burdaki amacim yazın sonunua sayi atıyım da sdfasadsf23 dsafasdfsaf22 gibi yani her bir yorum birbirinden farklı olsun diye
        except:
            print("yorum geçilidi")
           
        sleep(random.randint(0,2))
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button/div").click()           # paylaşa basldı
        except:
            print("payaş geçildi")

        sleep(random.randint(3,7))
       
        try:
            driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div/button").click()                                                          # sonraki posta gecti
        except:
            print("sonraki posta gecemedi")
        sleep(random.randint(3,7))
          

    driver.get("https://www.instagram.com/explore/people/")
    sleep(random.randint(50,70))

#driver.back
                    
print("Bitti")