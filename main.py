from client_classes import BankAccount, Client


def main ():
    client1 = Client('Alice')
    client2 = Client('Bob')
    client1.create_account(12)
    client2.create_account(13)
    client1.accounts[0].add_money(200)


if __name__ == '__main__':
    main()
