def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
celsius = input("Please input a number: ")
if isfloat(celsius):
    fahrenheit = ((float(celsius))*9/5)+32
    print(f"the result is: {fahrenheit}.")
else:
    print("Your input is not a valid number. ")