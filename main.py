import json
from web3 import Web3

url = ""
web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())
web3.eth .defaultAccount = web3.eth.accounts[0]

abi = json.loads()
address = web3.toChecksumAddress()
ehr = web3.eth.contract(address=address, abi=abi)

def func():
    tx_hash = ehr.functions.transaction().transact()