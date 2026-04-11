def add_money(amount, client, client_balance):
    client_balance += amount
    print(f'Client {client} added {amount}. balance is {client_balance}')
    return client_balance

def payment(amount, client, client_balance):
    if client_balance >= amount:
        client_balance -= amount
        print(f'Client {client} added {amount}. balance is {client_balance}')
    else:
        print(f'not enough money')
    return client_balance


if __name__=='__main__':
    client_1= 'Alice'
    client_1_balance = 1000
    client_2= 'Bob'
    client_2_balance = 500
    clint_1_balance = add_money(400, client_1, client_1_balance)
    clint_2_balance = add_money(500, client_2, client_2_balance)
    client_1_balance = payment( 200, client_1, client_1_balance)
    client_2_balance = payment( 300, client_2, client_2_balance)