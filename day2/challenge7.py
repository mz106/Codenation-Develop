
#Challenge 7 checks if an input (integer or string) is a palindrome 

def palindrome_checker(par):

    
    par_reversed = par[:: -1]

    if par == par_reversed:
        print("It's a palindrome!")
    else:
        print("It's not a palindrome.")    

def palindrome_input():
    integer_or_string = input("Are you inputting a string or an integer? ")
    if integer_or_string == "integer":
        integer_input = int(input("Please enter an integer: "))
        palindrome_checker(integer_input)
    elif integer_or_string == "string":
        integer_input = input("Please enter a string: ")
        palindrome_checker(integer_input)

palindrome_input()