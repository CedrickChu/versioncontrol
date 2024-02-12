def number():
    try:
        a = int(input("Enter a First Number: "))
        b = int(input("Enter Second Number: "))
    except ValueError:
        print("That's not a valid number!")
        return None, None
    else:
        return a, b


a, b = number()
if a is not None and b is not None:
    try:
        divide = a / b
        print(f"The division of {a} by {b} is {divide}")
    except ZeroDivisionError:
        print("You cannot divide by zero!")
