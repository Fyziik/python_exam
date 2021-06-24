class Account:
    # This class should contain the link between an account and a customer

    def __init__(self, customer, balance, acc_number):
        self.customer = customer
        self.balance = balance
        self.acc_number = acc_number
