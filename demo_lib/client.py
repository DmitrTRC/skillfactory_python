class Client:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.second_name = kwargs.get('second_name', '')
        self.status = kwargs.get('status', '')
        self.location = kwargs.get('location', '')
        self.birthday = kwargs.get('birthday', None)


class Guest(Client):
    def __init__(self, **kwargs):
        super(Guest, self).__init__(**kwargs)
        self.is_invited = kwargs.get('invited', False)

    def __str__(self):
        return f'{self.name:15} {self.second_name:15} , {self.location:20} status: {self.status:20}'


class Account:
    def __init__(self, client: Client, initial_balance=0):
        self.client = client
        self.__balance = initial_balance
        self.creditable = False

    def withdraw_money(self, amount):
        if amount > self.balance and not self.creditable:
            print(f'Insufficient money on your account for this operation ! {self.balance} RUB.  remains')
        else:
            self.__balance -= amount

    def put_money(self, amount):
        self.__balance += amount

    @property
    def balance(self):
        return self.__balance

    def __str__(self):
        return f'Client : {self.client.name} {self.client.second_name} Actual balance : {self.balance} RUB.'
