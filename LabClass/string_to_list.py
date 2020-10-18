""" Write a function that gets as an input a string of words separated
    by spaces and returns a list with the lengths of words in the string.
"""

def string_to_list(any_String):
    try:
        
        my_list =  list(any_String.split(" "))
        # my_final_list = [i for i in my_list]
        return my_list
    except:
        print("Invalid data type.Try again....")

x="a b c d e e f g i"

print("My list", string_to_list(x))