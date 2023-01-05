import os

if __name__ == '__main__':
    from win import ru
    from lin import li
    from ter import te
    from clear import clearr
    from analiz import anal1
    from pips import pips
else:
    from data.analiz import anal1
    from data.clear import clearr
    from data.win import ru
    from data.lin import li
    from data.ter import te
    from data.pips import pips



def anal(*a):
    try:

        with open("data/name.txt", "r") as file:
            v = file.read()
            if v == "linux" or v == "termux" or v == "shell":
                pass
            else:
                6%0
        return v
    except:
        print("Siz qaysi sitemadan foydalanyabsiz\n[1]Linux\n[2]Termux\n[3]Windows shell")
        aa = input("=>")
        if aa == "1":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("linux")


        if aa == "2":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("termux")

        if aa == "3":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("shell")




def run1(*a):
    anal1()
    clearr()
    anal()
    s = anal()
    upgrade()
    if s == "termux":
        try:
            while True:
                anal1()
                te()
        except Exception as e:
            print(e, "error nomi")
            pass

    if s == "linux":
        try:
            while True:
                anal1()
                li()
        except Exception as e:
            print(e, "error nomi")
            pass


    if s == "shell":
        try:
            while True:
                anal1()
                ru()
        except Exception as e:
            print(e ,"error nomi")
            pass



def upgrade(*a):
    try:
        with open("data/dir.txt" , "r"):
            pass
    except:
        for txt in pips:
            print("pip yuklanmoqda...")
            os.system(f"pip install {txt}")

            with open("data/dir.txt", "w"):
                pass
            exit()