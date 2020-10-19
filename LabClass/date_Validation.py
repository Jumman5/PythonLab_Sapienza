"""
    Write a function that gets three integers as an input d, m, a (
    it is assumed that a is always an odd number to avoid leap years) 
    and returns True or False depending on whether the three numbers form
    a valid date in the "d/m/a" format. Ex: 30/2/2017 False, 1/1/1111 True.

"""
def UserInput():
    while True:
        try:
            Variable_name = int(input("Enter your value as integer:" ))
            return Variable_name
            break
        except:
            print("Oops! that was not valid number. Try again...")

x = UserInput()
print("your value: ", x)