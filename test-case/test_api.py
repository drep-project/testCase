import requests
import json
import pytest


#  生成测试报告 : pytest test_quick_start.py --junit-xml=report.xml
#  https://www.jianshu.com/p/8fa34a3c82bd
#  HTML测试报告   py.test test_class.py --html=./report.html

def getVoteCreditDetails(url, jsonDataStr):
    headers = {
        'Content-Type': "application/json",
        }
    response = requests.request("POST", url, data=jsonDataStr, headers=headers)
    return response.text

def test_createAccount():
    url = "http://127.0.0.1:15645"

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_createAccount",
        "params": [],
        "id": 3
    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    #print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果
    assert response == successData


'''列出所有本地地址'''


def test_listAddress():
    url = "http://127.0.0.1:15645"

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [],
        "id": 3

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData

    '''查询地址余额'''


def test_getBalance():
    url = "http://127.0.0.1:15645"
    address = '0x45fdbcde02aad7a438052a7f4e74594c22245dd9'

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [address],
        "id": 3

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData

    '''投票'''


def test_VoteCredit():
    url = "http://127.0.0.1:15645"
    seAddress = '0x45fdbcde02aad7a438052a7f4e74594c22245dd9'
    reAddress = '0x75a45fb9e16b44e8c0b595d18c657f54b7300c3d'
    amount = '0x111'
    gasPrice = '0x110'
    gasOnline = '0x30000'

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [seAddress, reAddress, amount, gasPrice, gasOnline],
        "id": 1

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 1,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData

    '''取消投票'''


def CancelVoteCredit():
    url = "http://127.0.0.1:15645"

    seAddress = '0x45fdbcde02aad7a438052a7f4e74594c22245dd9'
    reAddress = '0x75a45fb9e16b44e8c0b595d18c657f54b7300c3d'
    amount = '0x111'
    gasPrice = '0x110'
    gasOnline = '0x30000'

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [seAddress, reAddress, amount, gasPrice, gasOnline],
        "id": 1

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 1,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData

    '''候选投票'''


def test_CandidateCredit():
    url = "http://127.0.0.1:15645"

    seAddress = '0x45fdbcde02aad7a438052a7f4e74594c22245dd9'
    reAddress = '0x7ccef5ca5d8ee76781974d019a919c9887639811'
    amount = '0x111'
    gasPrice = '0x110'
    gasOnline = '0x30000'
    usermsg = '{\"Pubkey\":\"0x7ccef5ca5d8ee76781974d019a919c9887639811\",\"Node\":\"192.168.31.51:55555\"}'  # 用户pubkey ip等信息

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [seAddress, reAddress, amount, gasPrice, gasOnline, usermsg],
        "id": 1

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData

    #    '''取消候选'''

def test_CancelCandidateCredit():

    url = "http://127.0.0.1:15645"
    seAddress = '0x45fdbcde02aad7a438052a7f4e74594c22245dd9'
    amount = '0x111'
    gasPrice = '0x110'
    gasOnline = '0x30000'

    jsonStr =   {
    "jsonrpc": "2.0",
    "method": "account_listAddress",
    "params": [seAddress,amount,gasPrice,gasOnline,""],
    "id": 3

    }
    #print(jsonStr)


    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    #print(jsonData)



    response = getVoteCreditDetails(url, jsonData)

    response = json.loads(response)


    # success data
    successData ={
    "jsonrpc":"2.0",
    "id":3,
    "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4":"0x3641100"}
    }
    print(successData)   # 预期结果
    print(response)      # 测试结果

    assert response == successData


''' 根据地址获取stake 所有细节信息'''


def test_getVoteCreditDetails():
    url = "http://127.0.0.1:15645"

    address = ''

    jsonStr = {
        "jsonrpc": "2.0",
        "method": "account_listAddress",
        "params": [address],
        "id": 3

    }
    # print(jsonStr)

    jsonData = json.dumps(jsonStr, sort_keys=True, indent=4)
    # print(jsonData)

    response = test_getVoteCreditDetails(url, jsonData)
    response = json.loads(response)

    # success data
    successData = {
        "jsonrpc": "2.0",
        "id": 3,
        "result": {"0x300fc5a14e578be28c64627c0e7e321771c58cd4": "0x3641100"}
    }

    # test
    print(successData)  # 预期结果
    print(response)  # 测试结果

    assert response == successData


#if __name__ == '__main__':


#     /*
#  name: getVoteCreditDetails
#  usage: 根据地址获取stake 所有细节信息
#  params:
#     1. 地址
#  return: bytecode
#  example: curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getVoteCreditDetails","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
#  response:
#    {"jsonrpc":"2.0","id":3,"result":"{\"0x300fc5a14e578be28c64627c0e7e321771c58cd4\":\"0x3641100\"}"}
# */
#
#
#
# /*
#  name: GetCancelCreditDetails
#  usage: 根据地址获取stake 所有细节信息
#  params:
#     1. 地址
#  return: bytecode
#  example: curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCancelCreditDetails","params":["0x8a8e541ddd1272d53729164c70197221a3c27486"], "id": 3}' -H "Content-Type:application/json"
#  response:
#    {"jsonrpc":"2.0","id":3,"result":"{\"0x300fc5a14e578be28c64627c0e7e321771c58cd4\":\"0x3641100\"}"}
# */
#
# /*
#  name: GetCandidateAddrs
#  usage: 根据地址获取所有候选节点
#  params:
#     1. 地址
#  return: bytecode
#  example: curl http://localhost:15645 -X POST --data '{"jsonrpc":"2.0","method":"chain_getCandidateAddrs","params":[""], "id": 3}' -H "Content-Type:application/json"
#  response:
#    {"jsonrpc":"2.0","id":3,"result":"{\"0x300fc5a14e578be28c64627c0e7e321771c58cd4\":\"0x3641100\"}"}
# */
