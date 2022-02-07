from brownie import network, SimpleStorage, accounts, config


def read_contract():
    print(SimpleStorage[0])


def main():
    read_contract()
