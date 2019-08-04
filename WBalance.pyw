# v 1.0
import requests
import time
from tkinter import *
from tkinter.ttk import *
# ADD HERE YOUR ADDRESS!
address = "0x99F6da169610943538205Be87F4135774E8BAb83"
# PLEASE DONATE IF YOU LIKE THI TINY PROGRAM


def search_token():
    whl_run = True
    x = 0
    while whl_run:
        r = requests.get('http://api.ethplorer.io/getAddressInfo/0x99F6da169610943538205Be87F4135774E8BAb83?apiKey'
                         '=freekey')
        result = r.json()['tokens'][x]['tokenInfo']['name']
        if result == "STORJ":
            whl_run = False
        x = x+1
    return x - 1


def close_window(root):
    root.destroy()


def truncate(f, n):
    # Truncates/pads a float f to n decimal places without rounding
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


position = search_token()
while 1:
    response = requests.get('http://api.ethplorer.io/getAddressInfo/'+address+'?apiKey=freekey')
    storj_balance_str = str(response.json()['tokens'][position]['balance'])
    eth_balance = response.json()['ETH']['balance']
    n1 = len(storj_balance_str)
    n2 = n1 - 8
    stj_balance = truncate(float(storj_balance_str[:n2] + "." + storj_balance_str[n2:]), 2)
    stj_rate = response.json()['tokens'][0]['tokenInfo']['price']['rate']
    stj_value_in_usd = str(truncate(float(stj_balance) * stj_rate, 2))
    # definizione e proprietà ogetti
    window = Tk()
    stj_bal_label = Label(window, justify=LEFT, text="STORJ BALANCE: "+storj_balance_str[:n2]+"."+storj_balance_str[n2:]
                          , background='white')
    stj_bal_label.pack(anchor=W)
    stj_value_label = Label(window, justify=LEFT, text="STORJ VALUE: " + stj_value_in_usd + " USD", background='white')
    stj_value_label.pack(anchor=W)
    eth_bal_label = Label(window, justify=LEFT, text="ETH BALANCE: " + str(eth_balance), background='white')
    eth_bal_label.pack(anchor=W)
    last_refresh_label = Label(window, justify=LEFT, text="LAST REFRESH: " + time.strftime("%H:%M:%S"),
                               background='white')
    last_refresh_label.pack(anchor=W)
    # proprietà finestra
    window.configure(background='white')
    window.overrideredirect(1)
    window.geometry("200x75+1324+748")
    window.update_idletasks()
    window.update()
    window.attributes('-topmost', True)
    time.sleep(300)
