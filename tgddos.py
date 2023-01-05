if __name__ == '__main__':
    from clear import clearr
    import time
    import pyautogui
else:
    from data.clear import clearr
    import time
    import pyautogui

def tgddos(*a):
    clearr()

    message = input("Xabarni kiriting->")
    n = int(input("Sonni kiriting->"))
    s = int(input("Necha soniyadan keyin boshlansin ->"))
    print("Boshlandi")
    count = 5
    while count!=5:
        time.sleep(1)

    count-=1

    for i in range(0, n):
        pyautogui.typewrite(message+"\n")