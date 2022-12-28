if __name__ == '__main__':
    print("Siz 'BoburBro.py' faylini ishga tushirishingiz kerak!")
    from tgddos import tgddos
    import os,sys
else:
    from data.tgddos import tgddos
    import os,sys

clear = "clear"

def mainlin(a):
    if a == 1 or a == "1" or a == "01":
        tgddos()
    if a == 99 or a == "99":
        with open("data/name.txt", "w") as file:
            c = ""
            v = file.write(c)
            os.system(clear)
    if a == 2:
        os.system("sudo apt-get install python2")
        os.system("python2 data/Bobur1c.py")
    if a == 3:
        os.system("bash data/Bobur2c")
def li(*a):
    p = input()
    if p == "y":
        os.system("pip install requests")
        os.system("pip install smtp")
        os.system("pip install telethon")
    print("Linux\n[1] TGddos\n[2] DDoS\n[3] Admin hack \n[99] Restore factory settings\n[0] exit")
    a = input("\n=>")
    if a == 0 or a == "0":
        exit()
    try:
        a = int(a)
    except:
        pass
    mainlin(a)
