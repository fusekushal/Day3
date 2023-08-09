#program to implement filename
filename = input("Enter the name of the file:")
try:
    with open(filename, "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"Something went wrong: {e}")