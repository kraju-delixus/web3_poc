from web3 import Web3
from decouple import config

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
res = w3.isConnected()
print(res)