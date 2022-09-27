from web3 import Web3

web3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))

test_address = "0xB37a93b4925090709197c266cAE24573BadfB656"

print("isConnected:", web3.isConnected())

balance = web3.eth.getBalance(test_address)

print("balance:", web3.fromWei(balance, "ether"))
