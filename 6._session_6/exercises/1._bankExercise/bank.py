class Bank:
    # This class should contain knowledge about accounts

    def __init__(self):
        self.accounts = []


    def __str__(self):
        tmp = ""
        for element in self.accounts:
            tmp += "*----------------------------*" + '\n'
            tmp += "Name: " + element.customer.name + '\n' "Age: " + str(element.customer.age)  + '\n' + "Balance: " + str(element.balance) + '\n' + "Account number: " + str(element.acc_number) + '\n'
            tmp += "*----------------------------*" + '\n \n'
        return tmp
        