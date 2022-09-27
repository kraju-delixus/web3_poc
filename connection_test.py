from web3 import Web3
from decouple import config

infura_url = "https://mainnet.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

print(infura_url)

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(infura_url))
res = w3.isConnected()
print(res)