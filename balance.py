from web3 import Web3

#infura_url = "https://mainnet.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

infura_url = "https://rinkeby.infura.io/v3/02212b331661455b8408a8a887c0c4b2"

web3 = Web3(Web3.HTTPProvider(infura_url))

test_address = "0xcFe95817aC44C3f8CE75F1EE6EC1431F586AB5A3"

print("isConnected:", web3.isConnected())

balance = web3.eth.getBalance(test_address)

print("balance:", web3.fromWei(balance, "ether"))
