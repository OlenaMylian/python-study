"""
calc function used for basic calculations
"""

def calc():
    stop = False
    user_input_a = 0
    user_input_b = 0
    while True:
        try:
            user_input_a = int(input("Put your number: "))
            break
        except ValueError:
            print("You need to use numbers")
            continue
    while True:
        print("Amount = ", user_input_a)
        print("Print one of the next operations",
              "\t +",
              "\t -",
              "\t *",
              "\t /",
              "\nPrint exit to quit")

        user_input_op = input()
        user_input_b = int(input("Put next number: "))
        if user_input_op == "+":
            user_input_a = sum_(user_input_a, user_input_b)
        if user_input_op == "-":
            user_input_a = diff_(user_input_a, user_input_b)
        if user_input_op == "*":
            user_input_a = mult_(user_input_a, user_input_b)
        if user_input_op == "/":
            user_input_a = separ_(user_input_a, user_input_b)
        if user_input_op == "=":
            print(user_input_a)
        if user_input_op == "exit":
            break
        else:
            print("Incorrect input")
            continue




def sum_(x, y):
    return x + y
def diff_(x, y):
    return x - y
def mult_(x, y):
    return x * y
def separ_(x, y):
    return x / y


calc()
