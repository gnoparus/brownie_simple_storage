from brownie import network, SimpleStorage, accounts, config


def read_contract():
    print(SimpleStorage[-1])


def main():
    read_contract()
