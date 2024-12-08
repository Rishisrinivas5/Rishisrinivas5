user = {
    'pin': 1234,
    'balance': 100000
}

def withdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you want to withdraw: "))
        pin = int(input("Please enter your PIN to confirm the withdrawal: "))
        if pin == user['pin']:
            if amount > user['balance']:
                print("You don't have sufficient balance to make this withdrawal")
            else:
                user['balance'] -= amount
                print(f"{amount} Rupees successfully withdrawn. Your remaining balance is {user['balance']} Rupees")
                print('')
                return False
        else:
            print("Incorrect PIN. Withdrawal cancelled.")
            return False

def balance_enquiry():
    pin = int(input("Please enter your PIN to check your balance: "))
    if pin == user['pin']:
        print(f"Total balance: {user['balance']} Rupees")
        print('')
    else:
        print("Incorrect PIN. Balance enquiry cancelled.")
        print('')

def change_pin():
    pin = int(input("Please enter your current PIN: "))
    if pin == user['pin']:
        new_pin = int(input("Enter your new PIN: "))
        confirm_new_pin = int(input("Confirm your new PIN: "))
        if new_pin == confirm_new_pin:
            user['pin'] = new_pin
            print("PIN successfully changed.")
        else:
            print("PINs do not match. PIN change cancelled.")
    else:
        print("Incorrect current PIN. PIN change cancelled.")

is_quit = False

print('')
print("*************WELCOME**************")

pin = int(input('Please enter your four-digit PIN: '))

if pin == user['pin']:
    while not is_quit:
        print("What do you want to do?")
        print(" Enter 1 to Withdraw Cash \n Enter 2 for Balance Enquiry \n Enter 3 to Change PIN \n Enter 4 to Quit")

        query = int(input("Enter the number corresponding to the activity you want to do: "))

        if query == 1:
            withdraw_cash()
        elif query == 2:
            balance_enquiry()
        elif query == 3:
            change_pin()
        elif query == 4:
            is_quit = True
        else:
            print("Please enter a correct value shown")
else:
    print("Entered wrong PIN")
