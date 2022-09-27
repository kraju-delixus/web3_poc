from web3 import Web3
#from decouple import config

infura_url = "https://mainnet.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

from web3 import Web3
from decouple import config

#infura_url = config('INFURA_URL')
print(infura_url)

# HTTPProvider:
w3 = Web3(Web3.HTTPProvider(infura_url))
res = w3.isConnected()
print(res)
#infura_url = "https://rinkeby.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

#web3 = Web3(Web3.HTTPProvider(infura_url))

#test_address = "0x00000000219ab540356cBB839Cbe05303d7705Fa"

#print("isConnected:", web3.isConnected())

#balance = web3.eth.getBalance(test_address)

#print("balance:", web3.fromWei(balance, "ether"))
latest_block = w3.eth.get_block('latest')

print(latest_block)

is_address_valid = w3.isAddress('0x6dAc6E2Dace28369A6B884338B60f7CbBF7fb9be')

print(is_address_valid)

check_sum = w3.toChecksumAddress('0xd7986a11f29fd623a800adb507c7702415ee7718')
balance = w3.eth.get_balance(check_sum)
print(balance)
address = '0xd665ce6Ef8AdA72B1CF946A6a71508bDD6D2EE04'
abi = '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"_maxTxAmount","type":"uint256"}],"name":"MaxTxAmountUpdated","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"notbot","type":"address"}],"name":"delBot","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualsend","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"manualswap","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"openTrading","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"removeStrictTxLimit","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address[]","name":"bots_","type":"address[]"}],"name":"setBots","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bool","name":"onoff","type":"bool"}],"name":"setCooldownEnabled","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"pure","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"pure","type":"function"},{"inputs":[{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address","name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}]'

contract_instance = w3.eth.contract(address=address, abi=abi)
res = contract_instance.functions.totalSupply().call()
print(res)
