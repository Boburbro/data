if __name__ == '__main__':
    print("Siz 'BoburBro.py' faylini ishga tushirishingiz kerak!")
    from tgddos import tgddos
    import os, sys
    from web import webb
else:
    from data.tgddos import tgddos
    import os, sys
    from data.web import webb

clear = "cls"


def mainwin(a):
    if a == 1 or a == "1" or a == "01":
        tgddos()
    if a == 99 or a == "99":
        with open("data/name.txt", "w") as file:
            c = ""
            v = file.write(c)
            os.system(clear)
    if a == "2":
        webb()
    if a == 3:
        url = input("url manzilni kiriting \n->")
        os.system(f"python data/xss.py -u {url}")
    else:
        exit()



def ru(*a):
    print("Windows shell\n[1] TGddos\n[2] WebHack\n[3] Xss-scan\n[99] Restore factory settings")
    a = input("\n=>")
    mainwin(a)