from demo_lib.client import Account, Client

if __name__ == '__main__':
    clients = list()
    clients.append(Account(Client(name='Dmitry', second_name='Morozov'), 125000000))
    clients.append(Account(Client(name='Irina', second_name='Zvereva')))
    for person in clients:
        print(person)
