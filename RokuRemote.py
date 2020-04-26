#! python3

import tkinter as tk
from tkinter import ttk
import requests
import socket
import sys
import re

def updtlist(event):
    srr['bg'] = 'red'
    srr['state'] = 'disabled'
    # Search string for IP address
    roku = re.compile(r'Roku')
    #ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}')
    ip = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('239.255.255.250', 1900)
    sock.settimeout(15)

    message = \
        'M-SEARCH * HTTP/1.1\r\n' \
        'Host: 239.255.255.250:1900\r\n' \
        'ST: upnp:rootdevice\r\n' \
        'MAN: "ssdp:discover"\r\n' \
        'MX: 3\r\n' \
        '\r\n'

    try:

        # Send data
        print('sending {!r}'.format(message))
        sent = sock.sendto(message.encode('utf-8'), server_address)

        capture = []

        while True:
            data, server = sock.recvfrom(4096)
            capture.append(data.decode('utf-8'))

    except(socket.timeout):
        print('closing socket')
        sock.close()


    #for i in capture:
    #    match = roku.search(i)
        
    foundlist = list(filter(roku.search, capture))
    iplist = ip.findall("".join(foundlist))
    ipr.config(values=iplist)
    srr['state'] = 'normal'
    srr['bg'] = 'green'


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


def handle_keypress(event, arg):
    res = requests.post('http://' + ipr.get() + ':8060/keypress/' + arg)

window = tk.Tk()
window.title('Roku Remote')
greeting = tk.Label(text="Roku Universal Remote")

srr = tk.Button(window, text="Search", width=10, height=1)
ipr = ttk.Combobox(window, width=25, height=1)
upr = tk.Button(window, text="Up", width=10, height=1)
dnr = tk.Button(window, text="Down", width=10, height=1)
ltr = tk.Button(window, text="Left", width=10, height=1)
rtr = tk.Button(window, text="Right", width=10, height=1)
okr = tk.Button(window, text="OK", width=10, height=1)
homer = tk.Button(window, text="Home", width=10, height=1)
backr = tk.Button(window, text="<-", width=10, height=1)
revr = tk.Button(window, text="<<", width=10, height=1)
ffr = tk.Button(window, text=">>", width=10, height=1)

greeting.grid(row=0, column = 0, columnspan=3)
srr.grid(row=1, column = 0)
ipr.grid(row=2, column = 0, columnspan=3)
backr.grid(row=3, column = 0)
homer.grid(row=3, column = 2)
upr.grid(row=4, column = 1)
ltr.grid(row=5, column = 0)
rtr.grid(row=5, column = 2)
okr.grid(row=5, column = 1)
dnr.grid(row=6, column = 1)
revr.grid(row=7, column = 0)
ffr.grid(row=7, column = 2)

srr.bind("<Button-1>", updtlist)
upr.bind("<Button-1>", lambda event, arg='up': handle_keypress(event, arg))
dnr.bind("<Button-1>", lambda event, arg='down': handle_keypress(event, arg))
ltr.bind("<Button-1>", lambda event, arg='left': handle_keypress(event, arg))
rtr.bind("<Button-1>", lambda event, arg='right': handle_keypress(event, arg))
okr.bind("<Button-1>", lambda event, arg='select': handle_keypress(event, arg))
homer.bind("<Button-1>", lambda event, arg='home': handle_keypress(event, arg))
backr.bind("<Button-1>", lambda event, arg='back': handle_keypress(event, arg))
revr.bind("<Button-1>", lambda event, arg='rev': handle_keypress(event, arg))
ffr.bind("<Button-1>", lambda event, arg='fwd': handle_keypress(event, arg))

window.mainloop()

