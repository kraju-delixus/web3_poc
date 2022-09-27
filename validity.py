from web3 import Web3
from decouple import config

infura_url = "https://mainnet.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(infura_url))

#checking an eth address is valid with the is_address method
is_address_valid = w3.isAddress('0x6dAc6E2Dace28369A6B884338B60f7CbBF7fb9be')

print(is_address_valid)