import requests
import time

while True:
    url = "http://127.0.0.1:15645"

    payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_transfer\",\n\t\"params\":[\"0xcb8d95912384bb8e0455775368c49c5f5b8b19b1\",\"0xde4541def39ca2393d159f6f407d225dfb653c22\",\"0x16800000\",\"0x110\",\"0x30000\",\"\"],\n\t\"id\":1\n\t\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6616a7d2-3705-4d37-b779-ef595abde465"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)




from datetime import datetime
import requests
from time import sleep


def creat_account(num):
    url = "http://127.0.0.1:15645"

    payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_createAccount\",\n\t\"params\":[], \n\t\"id\": 3\n\t\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "27a29181-18f4-4549-80c2-d23196a7df15"
    }

    response = requests.request("POST", url, data=payload, headers=headers)
    account = eval(response.text)
    print(account['result'])
    print("num: {}".format(num))
    return account


def privkey_api(count):

    url = "http://127.0.0.1:15645"

    payload = "{\n\t\"jsonrpc\":\"2.0\",\n\t\"method\":\"account_transfer\",\n\t\"params\":[\"0xaD3dC2D8aedef155eabA42Ab72C1FE480699336c\",\"0xde4541def39ca2393d159f6f407d225dfb653c22\",\"0x16800000\",\"0x110\",\"0x30000\",\"\"],\n\t\"id\":1\n\t\n}"
    headers = {
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "6616a7d2-3705-4d37-b779-ef595abde465"
    }

    response = requests.request("POST", url, data=payload, headers=headers)

    print(response.text)

    print("count: {}".format(count))


# 1s 12

num = 0
count = 1
while True:
    if num == 100:
        break
    if count % 120 == 0:
        sleep(3)
    creat_account(num)
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 创建账户")
    num = num + 1

    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "- 发起交易")
    privkey_api(count)
    count = count + 1
    sleep(1 / 12)