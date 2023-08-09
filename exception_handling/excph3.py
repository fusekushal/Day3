"""Program to implement exception handling """
try:
    x = input("Enter something:")
    y = int(float(x))
    print(f'the integer value is {y}')
except ValueError:
    print("Error: Cannot convert to integer")