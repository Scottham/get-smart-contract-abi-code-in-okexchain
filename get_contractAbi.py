import json
import requests


def get_contractAbi(contract_address):
    contract_url = 'https://www.oklink.com/api/explorer/v1/okexchain/addresses/' + contract_address + '/contract'
    contract_json = requests.get(contract_url)
    contract_json_data = json.loads(contract_json.text)
    contract_json_data = contract_json_data['data']
    abiCode = contract_json_data['contractAbi']
    abiCode = json.loads(abiCode)
    return abiCode
