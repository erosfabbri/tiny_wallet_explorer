import requests
from time import sleep
# ADD HERE YOUR ADDRESS!
address = "0x99F6da169610943538205Be87F4135774E8BAb83"



def del_tmp():
    a = 1


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


def truncate(f, n):
    # Truncates/pads a float f to n decimal places without rounding
    s = '%.12f' % f
    i, p, d = s.partition('.')
    return '.'.join([i, (d + '0' * n)[:n]])


position = search_token()

while True:
    tempfile = open("temp", "w")
    response = requests.get('http://api.ethplorer.io/getAddressInfo/'+address+'?apiKey=freekey')
    storj_balance_str = str(response.json()['tokens'][position]['balance'])
    eth_balance = response.json()['ETH']['balance']
    n1 = len(storj_balance_str)
    n2 = n1 - 8
    stj_balance = truncate(float(storj_balance_str[:n2] + "." + storj_balance_str[n2:]), 2)
    stj_rate = response.json()['tokens'][0]['tokenInfo']['price']['rate']
    stj_value_in_usd = str(truncate(float(stj_balance) * stj_rate, 2))
    tempfile.write(str(storj_balance_str)+","+str(stj_value_in_usd)+","+str(eth_balance)+","+str(n2))
    tempfile.close()
    sleep(300)








