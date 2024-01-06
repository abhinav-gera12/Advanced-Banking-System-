'''
Creating a virtual bank system which holds the information of a customer account details
if a customer wants to deposit, withdrawal, transfer the funds then the customer can do it easily while inputing the infromation
'''

class BankAccount():
    number_of_customers = 0                                         #it tracks the number of customers who opened the account
    account_number = 12345                                          #it provides the account number to that particular customer who opened the account
    
    def __init__(self,name,phone_number,age,gender,pin,initial_deposit):       #constructor with the main parameters
        self.name = name                                            #name of the customer
        self.phone_number = phone_number                            #phone number of the cusomter
        self.age = age
        self.gender = gender
        self.account_balance = initial_deposit                      #account balance is initialized using the initial deposit parameter
        self.pin = pin                                              #customer account pin number
        self.customer_account_number = BankAccount.account_number   #customer account number is initialized using the BankAccount class attribute
        
        BankAccount.account_number += 1                             #BankAccount class attribute is incremented by 1 cuz if any customer adds another account then it will automatically added into BankAccount details
        BankAccount.number_of_customers += 1                        #keep track of number of customers via incrementation
        

    def show_details(self):                                         #class method -1 which provides the information of the customer
        print(f'''\n\t\t Personal Details \n
                Name : {self.name}
                Age: {self.age}
                Gender: {self.gender}
                Account Number: {self.customer_account_number}
                Balance: {self.account_balance}''')
        
    def deposit(self):                                              #class method-2 which deposit the amount to the customer account
        amount = int(input("Enter the deposit amount: "))
        if amount > 0:
            self.account_balance = self.account_balance + amount
            print(f"The transaction is successful")
            print(f"Current Balance: {self.account_balance}")
        else:
            print(f"Invalid amount")
            print(f"The trasaction is failed. Please try agian!")
            
    def withdraw(self):                                             #class method-2 which withdrawal the amount from the customer's account
        amount = int(input("Enter the withdrawal amount: "))
        if amount <= self.account_balance and amount > 0:
            self.account_balance = self.account_balance - amount
            print(f"Transaction Successfully Completed!")
            print(f"The account balance has been upadted | Current Balance : {self.account_balance}")
        else:
            print(f"Transaction Failed!")
            print(f"Insuffient Funds | Current Balance: {self.account_balance}")
            
    def transfer(self,other):                                       #class method-3 which transfer the amount to the another account
        amount = int(input("Enter the transfer amount: "))
        if amount <= self.account_balance and amount > 0:
            self.account_balance = self.account_balance - amount
            other.account_balance = other.account_balance + amount
            print(f"Transaction Successfully Completed!")
            print(f"The account balance has been upadted")
            print(f"Current Balance of {customer1.name} : {self.account_balance}")
        else:
            print(f"Transaction Failed!")
            print(f"Insuffient Funds | Current Balance: {self.account_balance}")
            

#customer1 = BankAccount(name="Abhinav Gera",phone_number = 9876543210,age = 21,gender="Male",pin=1234,initial_deposit=1000)
#customer2 = BankAccount(name="Arun Gera",phone_number = 9876543211,age = 29,gender="Male",pin=5678,initial_deposit=3000)

# print(f"Number of customers: {BankAccount.number_of_customers}")

# print(customer1.show_details())
# print(customer2.show_details())

# customer1.deposit()
# print(customer1.show_details())

# customer1.withdraw()
# print(customer1.show_details())

# customer1.transfer(customer2)
# print(customer1.show_details())
# print(customer2.show_details())

customer_details = {}                 # use account no. as key and class object (customer account) as value (KEY:VALUE)
mobile_link = {}                      # use mobile no. as key and store account no. as value, for linking purpose
def new_customer():
    name = input('Enter the name of customer: ')
    mobile_number = int(input("Mobile Number must be of 6 digits. Enter mobile number: "))
    if mobile_number != 6:
        print('Invalid Number')
        return
    age = int(input("Enter the age: "))
    gender = input("Enter your gender: ")
    initial_deposit = int(input('Enter the initial deposit amount: '))
    if initial_deposit <= 0:
        print('Invalid Amount')
        return
    pin = int(input('Pin must be of 3 digits. Create PIN: '))
    if pin != 3:
        print('Invalid Pin')
        return
    
    customer = BankAccount(name=name, phone_number=mobile_number, age=age, gender=gender, pin = pin, initial_deposit = initial_deposit)
    customer_details[customer.customer_account_number] = customer                   # account. no. stored as key and oject as value
    mobile_link[customer.phone_number] = customer.customer_account_number           # mobile number linked
    print('New User Created!')
    print(f'Welcome {customer.name} to Bank. {customer.customer_account_number} is your account number')

def login():
    account_number = int(input('Enter your Account Number: '))
    account_pin = int(input('Enter your Account PIN: '))
    if account_number in customer_details.keys() and account_pin == customer_details[account_number].pin :
        print(f'\n{customer_details[account_number].name} Logged in')
        customer_details[account_number].show_details()
    else:
        print('Account either not exist or the pin is wrong')
        return
    while True:
        user_input1 = input('''
                            Press 1 for deposit:
                            Press 2 for withdrawl:
                            Press 3 for money transfer:
                            Press 4 to log out
                            ''')
        if user_input1 == '1':
            customer_details[account_number].deposit()
        elif user_input1 == '2':
            customer_details[account_number].withdrawl()
        elif user_input1 == '3':
            mobile = int(input('Enter the pin number of recepient: '))
            if mobile in mobile_link.keys():
                secondary = mobile_link[mobile]             # use mobile no. to get acct. no.
                customer_details[account_number].payment(customer_details[secondary])
            else:
                print('The mobile number you have enter does not have an account associated with it')
        elif user_input1 == '4':
            print('Logged Out')
            return
        else:
            print('Invalid input try again')
        print('\n#############################################################\n')
        customer_details[account_number].show_details()


while True:
    user_input1 = input('''
                        Press 1 for creating a new customer:
                        Press 2 for logging in as an existing customer:
                        Press 3 for displaying number of customers:
                        Press 4 for exit\n''')

    if user_input1 == '1':
        print("Create user")
        new_customer()
    elif user_input1 == '2':
        login()
    elif user_input1 == '3':
        print(f"There currently {BankAccount.number_of_customers} customers in Corporate bank.")
    elif user_input1 == '4':
        print('Exited')
        break
    else:
        print('Invalid input try again')
    print('\n*************************************************************\n')
