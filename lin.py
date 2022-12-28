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
        os.system("apt-get install python2")
        os.system("cd data")
        os.system("python2 Bobur1c.py")

def li(*a):
    print("Linux\n[1] TGddos\n[2] DDoS\n[99] Restore factory settings")
    a = input("\n=>")
    mainlin(a)
