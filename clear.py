if __name__ == '__main__':
    import os, sys
    from analiz import anal1
else:
    import os, sys
    from data.analiz import anal1

def clearr(*a):
    try:
        with open("data/name.txt", "r") as file:
            v = file.read()
            if v == "linux" or v == "termux":
                clear = 'clear'
            if v == "shell":
                clear = "cls"
        return clear
    except:
        anal1(1)
    os.system(clear)

