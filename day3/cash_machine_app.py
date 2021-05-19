pin = 1234
balance = 100

# # entered_pin = 0
# # amount = 0



def cash_machine(arg1, arg2):
    
    if arg1 == pin and arg2 <= balance:
        print("Dispensing cash... brrrrrrrrrr")
    elif arg1 == pin and arg2 > balance:
        print("You don't have enough funds")
    elif arg1 != pin:
        print("You have entered an incorrect pin")

def info_input():
    entered_pin = input("Please enter your pin: ")
    if entered_pin.isnumeric() == False:
        print("Please enter a number")
        info_input()
    # else:
    #     return int(entered_pin)    
    amount = input("Please enter the amount: ")
    if amount.isnumeric() == False: 
        print("Please enter a number: ")
        info_input()
    else:
        return int(amount)    
    cash_machine(int(entered_pin), int(amount))
