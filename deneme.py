from time import sleep
from threading import Thread
def tekrarla(ne, bekleme):
    while True:
        sleep(bekleme)
        print(ne)
def bekleycekmi():
    print("bekleemdi")

if __name__ == '__main__':
    dum = Thread(target = tekrarla, args = ("dum",1))
    dum1 = Thread(target = bekleycekmi)
    dum.start()
    dum1.start()

