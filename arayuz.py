from tkinter import *
import insta
from threading import Thread
from time import sleep


def otoB():
    o1=Thread(target=OtoBaslaFun)
    o1.start()

def otoE():
    e1=Thread(target=ElIleGiris)
    e1.start()

def otoK():
    k1=Thread(target=Kapat)
    k1.start()

def OtoBaslaFun():
    global Ilk_Defa_Giris
    Ilk_Defa_Giris=False
    insta.BaslaIslem(Toplam_Islme1_Input.get(),Bir_Sayfada_KacKisi_Takip1_Input.get(),Begen_Yorum_Sayisi1_Input.get(),Ilk_Defa_Giris,kullaniciAdiInput.get(),sifreInput.get())
        
def ElIleGiris():
    Ilk_Defa_Giris=True
    insta.BaslaIslem(Toplam_Islme1_Input.get(),Bir_Sayfada_KacKisi_Takip1_Input.get(),Begen_Yorum_Sayisi1_Input.get(),Ilk_Defa_Giris,kullaniciAdiInput.get(),sifreInput.get())

def Kapat():
    insta.driver.close()


#############################       Arya yüz
root=Tk()
root.title("Instagram Botu")
root.geometry("1000x500")

#root.config(bg="#FF7F01")

global oto
oto =Label(root,text="Oto")
oto.place(relx=0.2,rely=0.15,relwidth=0.2,relheight=0.1)

global otoBasla
otoBasla=Button(root,text="Basla",command=otoB,width=4,height=3)
otoBasla.place(relx=0.2,rely=0.25,relwidth=0.2,relheight=0.1)

global Toplam_Islme1
Toplam_Islme1 =Label(root,text="Toplam Islem :")
Toplam_Islme1.place(relx=0.1,rely=0.5,relwidth=0.2,relheight=0.1)

global Toplam_Islme1_Input
Toplam_Islme1_Input=Entry(root,width=40,bg="#FF7F00")
Toplam_Islme1_Input.place(relx=0.29,rely=0.52,relwidth=0.03,relheight=0.05)

global Toplam_Islme2
Toplam_Islme2 =Label(root,text="//10")
Toplam_Islme2.place(relx=0.33,rely=0.5,relwidth=0.022,relheight=0.1)



global Bir_Sayfada_KacKisi_Takip1
Bir_Sayfada_KacKisi_Takip1 =Label(root,text="Bir Sayfada KacKisi Takip Edilecek :")
Bir_Sayfada_KacKisi_Takip1.place(relx=0.1,rely=0.6,relwidth=0.2,relheight=0.1)

global Bir_Sayfada_KacKisi_Takip1_Input
Bir_Sayfada_KacKisi_Takip1_Input=Entry(root,width=40,bg="#FF7F00")
Bir_Sayfada_KacKisi_Takip1_Input.place(relx=0.29,rely=0.62,relwidth=0.03,relheight=0.05)

global Bir_Sayfada_KacKisi_Takip2
Bir_Sayfada_KacKisi_Takip2 =Label(root,text="//9")
Bir_Sayfada_KacKisi_Takip2.place(relx=0.33,rely=0.6,relwidth=0.022,relheight=0.1)



global Begen_Yorum_Sayisi1
Begen_Yorum_Sayisi1 =Label(root,text="Begen Yorum Sayisi Input :")
Begen_Yorum_Sayisi1.place(relx=0.1,rely=0.7,relwidth=0.2,relheight=0.1)

global Begen_Yorum_Sayisi1_Input
Begen_Yorum_Sayisi1_Input=Entry(root,width=40,bg="#FF7F00")
Begen_Yorum_Sayisi1_Input.place(relx=0.29,rely=0.72,relwidth=0.03,relheight=0.05)

global Begen_Yorum_Sayisi2
Begen_Yorum_Sayisi2 =Label(root,text="//2")
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
elIleBasla=Button(root,text="Basla",command=otoE,width=4,height=3)
elIleBasla.place(relx=0.7,rely=0.5,relwidth=0.2,relheight=0.1)

global kapat1
kapat1=Button(root,text="Kapat",command=otoK,width=4,height=3,bg="#ff0000")
kapat1.place(relx=0.7,rely=0.7,relwidth=0.2,relheight=0.1)

#############################       Arya yüz

root.mainloop()
