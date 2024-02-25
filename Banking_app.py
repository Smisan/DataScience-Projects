'''

SecureBank is a robust banking application with a user-friendly interface
designed to provide a secure and error-free banking experience. It offers 
a range of features including checking balances, transferring funds between accounts, 
depositing or withdrawing money, and ensures that transactions are secure and error-free.
Banking app with a solid user interface, which is user-friendly and robust against potential
        errors and misuse.

'''

import random as rd

#introducing custom exception errors
class InsufficientFundsError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

#defining a function to generate a random integer as current balance
def check_bal():

    current_balance = rd.randint(100, 99999)
    return current_balance

#defining a function to transfer or withdraw an amount and to raise custom errors
def move_funds(amount, current_balance):

    amount = float(amount)
    current_balance = float(current_balance)

    if amount > current_balance:
        raise InsufficientFundsError(f"Insufficient fund available. Your current balance is {current_balance}")
    elif amount <=0:
        raise InvalidAmountError("Invalid amount entered. Please enter a positive value")

#setting account limits   
MAX_TRANSFER_LIMIT = 3000
MAX_WITHDRAW_LIMIT = 1000
    
  
print("Welcome to Safebank. Please enter your credentials to continue. ")

while True:
    user_email = input("Please enter your email address: ")
    if '@' in user_email and '.' in user_email:
        print("Email exists.")
        break

    else:
        print("Please try again")


while True:
    user_pin = input("Please enter your 4 digit PIN : ")
    if user_pin.isdigit() and len(user_pin) == 4:
        print("PIN accepted.")
        break
    
    print("Invalid input. Please try again.")

#calling the function check_balance and setting it to a variable so that it can be used outside the function
current_balance = check_bal()

print('''
1. to check your balance
2. to transfer funds
3. to deposit an amount
4. to withdraw an amount
''')

#confirmation prompts to confirm PIN
def confirm_pin(user_pin):

    confirm_pin = input("Please enter your PIN to confirm action : ")

    if user_pin == confirm_pin:
        print("PIN confirmed. Proceeding with the action.")
        return True
    
    print("Wrong PIN. Action aborted.")
    return False
    

choice = input ("Please make your choice(enter a number) : ")

if choice == '1' :
    
    if confirm_pin(user_pin):
        print(f"Your current balance is : {current_balance}")


elif choice == '2':
    if confirm_pin(user_pin):

        while True:
        
            try:
                print(f"Your current balance is {current_balance}")

                transfer_amount= float(input("Please enter the amount you would like to transfer : "))

                if transfer_amount > MAX_TRANSFER_LIMIT:
                    raise InvalidAmountError (f"The transfer amount exceeds the maximum limit of {MAX_TRANSFER_LIMIT}.")
                
                result = move_funds(transfer_amount, current_balance)
        
                print (f"Transfer successful. You have transferred {transfer_amount}. Your current_balance is {current_balance-transfer_amount}")
                break

            except InvalidAmountError as e:
                print(e)

            except InsufficientFundsError as f:
                print(f)


elif choice =='3':

    if confirm_pin(user_pin):

        deposit_amount = float(input("Please enter the amount you would like to deposit : "))
        current_balance += deposit_amount
        print(f"You have deposited {deposit_amount}. Your current balance is {current_balance}")


elif choice == '4':

    if confirm_pin(user_pin):

        while True:
        
            try:
                print(f"Your current balance is {current_balance}")
                withdraw_amount= float(input("Please enter the amount you would like to withdraw : "))

                if withdraw_amount > MAX_WITHDRAW_LIMIT:
                    raise InvalidAmountError (f"The withdrawal amount exceeds the maximum limit of {MAX_WITHDRAW_LIMIT}.")
                
                result = move_funds(withdraw_amount, current_balance)

                print (f"You withdrew {withdraw_amount}. Your current_balance is {current_balance- withdraw_amount}")
                break

            except InvalidAmountError as e:
                print(e)

            except InsufficientFundsError as f:
                print(f)





    
        





        
    
        



