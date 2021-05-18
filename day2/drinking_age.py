
import time

def are_you_old_enough_to_drink():
    time.sleep(1)
    print("""
    Want a pint? Gotta be 18! ...and British!""")
    time.sleep(2)
    age = int(input("""
    Enter you age: """))
    time.sleep(3)
    country = input("""
    Are you from the UK, yes or no:   """)
    time.sleep(3)
    if age >= 18 and country == "yes":
        print(f"""
    You are {age} and from the UK. So... gin?""")
    elif age < 18 and country == "yes":
        print(f"""
    So, you've got the right passport, but you are only {age}. Come back in {18 - age} years.""")
    elif age >= 18 and country != "yes":
        print(f"""
    Well, you are of age, but you might be French. Sooooooo... no gin!""")
    else:
        print(f"""
    NO! NO! NO! No gin for you!!!""")                 

are_you_old_enough_to_drink()   
