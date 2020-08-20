import tkinter
from numpy import place
import random
n = ""
a = ""
g = ""
def グー_click():
    global b
    b = random.choice(["グー", "チョキ", "パー"])
    global n
    global a
    a = "グー"
    n = a + b
    click()
    
def パー_click():
    global b
    b = random.choice(["グー", "チョキ", "パー"])
    global n
    global a
    a = "パー"
    n = a + b
    click()
    
    
def チョキ_click():
    global b
    b = random.choice(["グー", "チョキ", "パー"])
    global n
    global a
    a = "チョキ"
    n = a + b
    click()

def click():
    b = random.choice(["グー", "チョキ", "パー"])
    global a
    global g
    global n
    if a == b:
        g = "アイコ"
    else:
        if b == "チョキ":
            if a == "グー":
                g = "勝ち"
            else:
                g = "負け"
        elif b == "グー":
            if a == "パー":
                g = "勝ち"
            else:
                    g = "負け"
        elif b == "チョキ":
            if a == "グー":
                g = "勝ち"
            else:
                    g = "負け"
    
    処理 = tkinter.Tk()
    処理.geometry("300x300")
    処理.title("勝ち負け")
    ttt = tkinter.Label(処理, text=g)
    ttt.pack()
    ccc = tkinter.Label(処理, text="相手は" + b)
    ccc.pack()
    yyy = tkinter.Label(処理, text="ジブンは" + a)
    yyy.pack()
    処理.mainloop()
    

tki = tkinter.Tk()
tki.geometry("300x300")
tki.title("じゃんけん")

タイトル = tkinter.Label(tki, text="じゃんけん")
タイトル.place(x=110, y=10)

グー = tkinter.Button(tki, text="グー", command=グー_click)
グー.place(x=40, y=200)

パー = tkinter.Button(tki, text="パー", command=パー_click)
パー.place(x=130, y=200)
    
チョキ = tkinter.Button(tki, text="チョキ", command=チョキ_click)
チョキ.place(x=220, y=200)



    
