# Main class
from bank import Bank
from customer import Customer
from account import Account

def make_customer(choice):
    if choice == 1:
        customer_name = input("Insert name: ")
        customer_age = input("Insert age: ")
        return Customer(customer_name, customer_age)

    elif choice == 2:
        customer_name = input("Insert name: ")
        return Customer(customer_name)

    else:
        print("Invalid choice")
        pass

def make_account(customer):
    account_balance = input("Insert balance: ")
    account_number = input("Insert account number: ")
    return Account(customer, account_balance, account_number)
    
#Instantiate bank
bank = Bank()

while(True):

    #Get inputs for creating a customer
    user_choice_of_customer = int(input("Press 1. for default customer (name & age) or 2. for just name: "))

    #Create customer
    customer_created = make_customer(user_choice_of_customer)

    #Create account & add to bank
    #bank.add_account(make_account(customer_created))
    bank.accounts.append(make_account(customer_created))
        
    print(bank)





    