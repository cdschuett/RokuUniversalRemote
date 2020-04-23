#! python3

import tkinter as tk
import requests

# TODO: Enter text in fields

# TODO: Return Handler

# TODO: Options Handler

# TODO: Rewind Handler

# TODO: Fast Forward Handler

# TODO: Pause/Play Handler

# TODO: Back button and handler

# TODO: Install Handler
# TODO: Install Field
# TODO: Pictures on buttons
# TODO: single event hhandler for keypress where keypress value is passed

url = 'http://192.168.50.5:8060/keypress/home'

payload = '/keypress/up'

def handle_up():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/up')

def handle_down():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/down')

def handle_left():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/left')

def handle_right():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/right')

def handle_ok():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/select')

def handle_home():
    res = requests.post('http://' + ipr.get() + ':8060/keypress/home')
    
window = tk.Tk()
greeting = tk.Label(text="Roku Universal Remote")

ipr = tk.Entry(window, width=25)
upr = tk.Button(window, text="Up", width=10, height=2, command=handle_up)
dnr = tk.Button(window, text="Down", width=10, height=2, command=handle_down)
ltr = tk.Button(window, text="Left", width=10, height=2, command=handle_left)
rtr = tk.Button(window, text="Right", width=10, height=2, command=handle_right)
okr = tk.Button(window, text="OK", width=10, height=2, command=handle_ok)
homer = tk.Button(window, text="Home", width=10, height=2, command=handle_home)

greeting.grid(row=0, column = 0, columnspan=3)
ipr.grid(row=1, column = 0, columnspan=3)
upr.grid(row=2, column = 1)
ltr.grid(row=3, column = 0)
rtr.grid(row=3, column = 2)
okr.grid(row=3, column = 1)
dnr.grid(row=4, column = 1)
homer.grid(row=5, column = 2)
  
window.mainloop()

