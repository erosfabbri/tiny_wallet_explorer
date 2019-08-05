# v 1.5
import requests
import signal
import time
import os
from tkinter import *
from tkinter.ttk import *
import subprocess
window = Tk()
refresher = subprocess.Popen(['python', 'bgr.py'])
# 0x99F6da169610943538205Be87F4135774E8BAb83
# PLEASE DONATE (ETH) IF YOU LIKE THIS TINY PROGRAM


def me_close():
    refresher.send_signal(signal.CTRL_BREAK_EVENT)
    window.destroy()


time.sleep(5)
while 1:
    tmpfile = open("temp")
    in_data = tmpfile.readline()
    data = in_data.split(",")
    storj_balance_str = data[0]
    stj_value_in_usd = data[1]
    eth_balance = data[2]
    n2 = int(data[3])
    tmpfile.close()
    # definizione e proprietà ogetti

    stj_bal_label = Label(window, justify=LEFT, text="STORJ BALANCE: "+storj_balance_str[:n2]+"."+storj_balance_str[n2:]
                          , background='white')
    stj_bal_label.pack(anchor=W)
    stj_value_label = Label(window, justify=LEFT, text="STORJ VALUE: " + stj_value_in_usd + " USD", background='white')
    stj_value_label.pack(anchor=W)
    eth_bal_label = Label(window, justify=LEFT, text="ETH BALANCE: " + eth_balance, background='white')
    eth_bal_label.pack(anchor=W)
    last_refresh_label = Label(window, justify=LEFT, text="LAST REFRESH: " + time.strftime("%H:%M:%S"),
                               background='white')
    last_refresh_label.pack(anchor=W)
    frame = Frame(window)
    frame.pack()
    button = Button(frame, text="Exit", command=me_close)
    button.pack()
    # proprietà finestrad
    window.configure(background='white')
    window.overrideredirect(1)
    window.geometry("200x100+1324+748")
    window.update_idletasks()
    window.update()
    window.attributes('-topmost', True)
