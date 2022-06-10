
from tkinter import *

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import random

text=["takip edermisiniz","takipe takip ","nice post","gt","takip edebilirmisiniz","beni geri takip edermisiniz","yeni bir şeyler deniyorum beni takip edermisiniz","sevdim inkar edemem yaşadım isyan edemem",\
    "umdum cenneten ","zaman öylede geçiyor","hayat böylede bitiyor","bu yourmu okuyosan okumuş oluyosun sdfhasdfaf","güzel post","yazlım ile uğraşan varmı","bir takip ederseniz sevinirim be","yazlim oğrenmek istyenler buyursun efendim"]


#-----------------bizim belirlediğimiz



global Ilk_Defa_Giris
Ilk_Defa_Giris=False





def OtoBaslaFun():
    Ilk_Defa_Giris=False
    BaslaIslem()

def ElIleGiris():
    Ilk_Defa_Giris=True
    BaslaIslem()

def Kapat():
    driver.close()
    

    




#############################       Arya yüz
root=Tk()
root.title("Instagram Botu")
root.geometry("1000x500")
#root.config(bg="#FF7F01")

global oto
oto =Label(root,text="Oto")
oto.place(relx=0.2,rely=0.15,relwidth=0.2,relheight=0.1)

global otoBasla
otoBasla=Button(root,text="Basla",command=OtoBaslaFun,width=4,height=3)
otoBasla.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.1)

global Toplam_Islme1
Toplam_Islme1 =Label(root,text="Toplam Islem :")
Toplam_Islme1.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.1)

global Toplam_Islme1_Input
Toplam_Islme1_Input=Entry(root,width=40,bg="#FF7F00")
Toplam_Islme1_Input.place(relx=0.29,rely=0.52,relwidth=0.03,relheight=0.05)

global Toplam_Islme2
Toplam_Islme2 =Label(root,text="//15")
Toplam_Islme2.place(relx=0.33,rely=0.5,relwidth=0.022,relheight=0.1)

global Bir_Sayfada_KacKisi_Takip1
Bir_Sayfada_KacKisi_Takip1 =Label(root,text="Bir Sayfada KacKisi Takip Edilecek :")
Bir_Sayfada_KacKisi_Takip1.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.1)

global Bir_Sayfada_KacKisi_Takip1_Input
Bir_Sayfada_KacKisi_Takip1_Input=Entry(root,width=40,bg="#FF7F00")
Bir_Sayfada_KacKisi_Takip1_Input.place(relx=0.29,rely=0.62,relwidth=0.03,relheight=0.05)

global Bir_Sayfada_KacKisi_Takip2
Bir_Sayfada_KacKisi_Takip2 =Label(root,text="//15")
Bir_Sayfada_KacKisi_Takip2.place(relx=0.33,rely=0.6,relwidth=0.022,relheight=0.1)

global Begen_Yorum_Sayisi1
Begen_Yorum_Sayisi1 =Label(root,text="Begen Yorum Sayisi Input :")
Begen_Yorum_Sayisi1.place(relx=0.1,rely=0.7,relwidth=0.2,relheight=0.1)

global Begen_Yorum_Sayisi1_Input
Begen_Yorum_Sayisi1_Input=Entry(root,width=40,bg="#FF7F00")
Begen_Yorum_Sayisi1_Input.place(relx=0.29,rely=0.72,relwidth=0.03,relheight=0.05)

global Begen_Yorum_Sayisi2
Begen_Yorum_Sayisi2 =Label(root,text="//4")
Begen_Yorum_Sayisi2.place(relx=0.33,rely=0.7,relwidth=0.02,relheight=0.1)



global urlLabel1
urlLabel1 =Label(root,text="El İle")
urlLabel1.place(relx=0.4,rely=0.15,relwidth=0.6,relheight=0.1)

global kullaniciAdi
kullaniciAdi =Label(root,text="Kullanici Adi: ")
kullaniciAdi.place(relx=0.5,rely=0.3,relwidth=0.2,relheight=0.05)

global kullaniciAdiInput
kullaniciAdiInput=Entry(root,width=40,bg="#FF7F00")
kullaniciAdiInput.place(relx=0.7,rely=0.3,relwidth=0.2,relheight=0.05)

global sifre
sifre =Label(root,text="Şifre: ")
sifre.place(relx=0.5,rely=0.4,relwidth=0.2,relheight=0.05)

global sifreInput
sifreInput=Entry(root,width=40,bg="#FF7F00")
sifreInput.place(relx=0.7,rely=0.4,relwidth=0.2,relheight=0.05)

global elIleBasla
elIleBasla=Button(root,text="Basla",command=ElIleGiris,width=4,height=3)
elIleBasla.place(relx=0.7,rely=0.5,relwidth=0.2,relheight=0.1)

global kapat1
kapat1=Button(root,text="Kapat",command=Kapat,width=4,height=3,bg="#ff0000")
kapat1.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.1)
#############################       Arya yüz




def BaslaIslem():
    #sistem
    kacKereGecildi=0
    kacKisiTakipEdildi=0
    postbulundu=True
    
    
    if Toplam_Islme1_Input.get()!="":
        Toplam_Islme=Toplam_Islme1_Input.get()
    else:
        Toplam_Islme=15                                                                    #burda default degiscek
    if Bir_Sayfada_KacKisi_Takip1_Input.get()!="":
        Bir_Sayfada_KacKisi_Takip=Bir_Sayfada_KacKisi_Takip1_Input.get()
    else:
        Bir_Sayfada_KacKisi_Takip=0
    if Begen_Yorum_Sayisi1_Input.get()!="":
        Begen_Yorum_Sayisi=Begen_Yorum_Sayisi1_Input.get()
    else:
        Begen_Yorum_Sayisi=4
    

    global driver
    options = webdriver.ChromeOptions()
    options.add_argument('--user-data-dir=C:\\Users\\ali\\AppData\\Local\\Google\\Chrome\\User Data')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get("https://www.instagram.com")
    driver.maximize_window()

    if Ilk_Defa_Giris==True:
        kullaniciAdi=kullaniciAdiInput.get()
        kullaniciSifre=sifreInput.get()
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
            postbulundu=False

        if postbulundu==False:
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[2]/div/a/div/div[2]").click()                                                  # ilk posta tıklamak
                postbulundu=True
            except:
                postbulundu=False

        if postbulundu==False:
            try:
                driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/div[1]/div/div[1]/div[1]/div/a/div[1]/div[2]").click()                                                  # ilk posta tıklamak
                postbulundu=True
            except:
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
    driver.close()
    print("Bitti")
root.mainloop()