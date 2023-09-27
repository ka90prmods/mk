print(".gg/kVV2mCtsZb << pobierz token gen / download token gen")
import os
os.system("title mk market - server invite: kVV2mCtsZb")
import tkinter
from tkinter import ttk
import random
import requests


import sv_ttk

char = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789'

def gentokens():
    entered_text = entry.get()
    print("started:", entered_text)
    for i in range(100* 1000* 10):

        frist = ''.join((random.choice(char) for i in range(24)))

        sec = ''.join((random.choice(char) for i in range(6)))

        endR = ''.join((random.choice(char) for i in range(26)))

        result = frist + '.' + sec + '.' + endR

        output = open('tokens.txt', 'a')
        output.write(result + '\n')

        print(f'' + result)
        payload = {
            'content': result
        }

        response = requests.post(entered_text, json=payload)

root = tkinter.Tk()

entry = ttk.Entry(root, width=45)
entry.pack(pady=10)
button = ttk.Button(root, text="start", command=gentokens)
button2 = ttk.Button(root, text="Toggle theme (dark / light)", command=sv_ttk.toggle_theme)
button.pack()
button2.pack()

sv_ttk.set_theme("dark")

root.mainloop()
