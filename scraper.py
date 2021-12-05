"""import requests
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent"""
from tkinter import *
import random
import time

yazılacak_liste = []


def window():
    global inp1
    global inp2
    global root

    root = Tk()
    root.config(bg="yellow")
    root.title("Sahibinden.com")
    root.resizable(0, 0)
    root.geometry("400x300")

    txt1 = Label(text="Kategori:", bg="yellow", fg="black", font=("Calibri", 18))
    txt1.place(x=15, y=10)

    inp1 = Entry(font=("Calibri", 13))
    inp1.place(x=98 + 15, y=17)

    txt2 = Label(text="Şehir:", bg="yellow", fg="black", font=("Calibri", 18))
    txt2.place(x=15, y=50)

    inp2 = Entry(font=("Calibri", 13))
    inp2.place(x=70 + 13, y=57)

    txt3 = Label(text="--------------------İşlem Seçiniz.--------------------",
                 fg="black", bg="white", font=("Calibri", 17))
    txt3.place(x=0, y=100)

    btn1 = Button(text="Not Defterine Yaz.", bg="black", fg="white", command=deftere_yaz, font=("Calibri", 14))
    btn1.place(x=20, y=150)

    btn2 = Button(text="Rastgele Numara Ver.", bg="red", fg="white", font=("Calibri", 14))
    btn2.place(x=197, y=150)

    root.mainloop()


def deftere_yaz():
    kategori = inp1.get()
    sehir = inp2.get() 
    kategori = kategori.lower()
    sehir = sehir.lower()

    #txt4 = Label(text="Bu Biraz Zaman Alabilir.\nLütfen Bekleyiniz...", fg="black", bg="red", font=("Calibri", 13))
    #txt4.place(x=25, y=220)

    islem(kategori, sehir)

    #txt4.config(text="Yazma İşlemi Bitti !")
    #txt4.place(x=25, y=220)

    print("İşlem bitti.")
    print(yazılacak_liste)

    #txt4.config(text="Not Defterine Numaralar:\nYazıldı.", bg="green", fg="white")
    #txt4.place(x=25, y=220)


def islem(kategori, sehir):
    ua = UserAgent()
    headers = {"User-agent": ua.random}
    sayfa = 0
    say2 = 0
    say = 0
    for sayfa in range(0, 981, 20):
        time.sleep(1.5)
        url = "https://www.sahibinden.com/" + str(kategori) + "/" + str(sehir) + "?pagingOffset=" + str(
            sayfa) + "&query_text_mf=" + str(sehir)
        # sahibinden kriterli sayfaya gittik
        print(url)
        r = requests.get(url, headers=headers)
        print("Sayfa sayısı:",say2)
        say+=1
        print("Kod:",r.status_code)
        soup = bs(r.content, "lxml")

        print(url)
            

        for link in soup.find_all("a", {"class": "classifiedTitle"}, href=True):
            ua = UserAgent()
            headers = {"User-agent": ua.random}
            print("Ben geldim")
            url = "https://www.sahibinden.com" + str(link["href"])
            
            time.sleep(1)
            print(url)
            r = requests.get(url, headers=headers)

            soup = bs(r.content, "lxml")
            print(soup)
            
            number = soup.find("dd",class_="user-info-phones").text.strip()
            print(number)
            try:
                print(number.text)
            except:
                print(number.string)
            break
            yazılacak = "----"

            #yazılacak_liste.append(yazılacak)
            say += 1
            print(say)
            print(yazılacak)
            
        

        

                
    print(yazılacak_liste)
    #with open("Numaralar.txt", "w") as f:
        #for i in yazılacak_liste:

            #f.write(i+"\n")


window()
