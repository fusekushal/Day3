#program to implement error handling for two types of error
try:
    x = int(input("Please Enter the Numerator:"))
    y = int(input("Please Enter the Denominator:"))
    result = x / y
    print(result)
except ValueError:
    print("Error: Enter integers only.")
except ZeroDivisionError:
    print("Error: Denominator cannot be 0.")
