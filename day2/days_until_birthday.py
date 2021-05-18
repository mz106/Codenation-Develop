
def how_many_days_until_my_birthday():

    today = datetime.now()
    birthday = input("Please enter your birthday (YYYY-M-D): ")
    dt = datetime.strptime(birthday, '%Y-%m-%d')
    
    strp_today = today.strftime("%j")
    strp_dt = dt.strftime("%j")



    total = int(strp_dt) - int(strp_today)
    str_total = str(total)
    if total < 0:
        print("You have gone back in time! Please enter a current or future date.")
        how_many_days_until_my_birthday()
    elif str_total == "0":
        print("Happy Birthday!")    
    elif str_total == "1":
        print(f"There is {str_total} day until your birthday")
    else:
        print(f"There are {str_total} days until your birthday")
how_many_days_until_my_birthday()  
