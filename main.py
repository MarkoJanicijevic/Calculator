def add (x, y):
    return x + y
def subtract (x, y):
    return x - y
def multiply (x, y):
    return x * y
def divide (x, y):
    return x / y

def choose_an_operation ():
    operation = input("Choose an operation by entering one of the symbols above: ")
    return operation




def calculation (x):
    print("+ \n - \n * \n / \n")
    operation = choose_an_operation()
    y = float(input("What is your second number? "))
    operation_dictionary = {
        "+":add(x, y),
        "-":subtract(x, y),
        "*":multiply(x, y),
        "/":divide(x, y),
    }
    result = operation_dictionary[operation]
    print(f" {x}  {operation}  {y}  =  {result}")
    choice = input("Do you want to continue with this result or start new calculation? Enter 'c' or 'n'. ")
    if choice == "c":
        print(f"Your result so far is {result}: ")
        calculation(result)
    else:
        calculation(float(input("What is your first number? ")))



calculation(float(input("What is your first number? ")))

