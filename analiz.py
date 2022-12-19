def anal1(*a):
    try:
        with open("data/name.txt", "r") as file:
            v = file.read()
            if v == "linux" or v == "termux" or v == "shell":
                pass
            else:
                6%0
    except:
        print("Siz qaysi sitemadan foydalanyabsiz\n[1]Linux\n[2]Termux\n[3]Windows shell")
        a = input("=>")
        if a == "1":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("linux")
                exit()

        if a == "2":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("termux")
                exit()
        if a == "3":
            print("Aktivatsya tugadi qayta ishga tushiring!")
            with open("data/name.txt", "w") as file:
                file.write("shell")
                exit()


if __name__ == '__main__':
    print("Nimadur xato")
    exit()