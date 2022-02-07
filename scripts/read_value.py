from brownie import network, SimpleStorage, accounts, config


def read_contract():
    last_contract = SimpleStorage[-1]
    print(last_contract)

    print(last_contract.retrieve())


def main():
    read_contract()
