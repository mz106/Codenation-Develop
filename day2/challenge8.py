
# This function prints the index of the last vowel in a string

long_string = """jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuh
gtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"""

def last_vowel_index():
    reversed_long_string = long_string[:: -1]
    
    for i in reversed_long_string:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            print((len(long_string) -1 ) - reversed_long_string.index(i))
            break
       
last_vowel_index()
