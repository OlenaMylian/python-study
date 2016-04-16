"""
calc function used for basic calculations
"""

def calc():
    user_input_a = 0
    user_input_b = 0
    last_dig = 0
    valid_chr = ["+", "-", "*", "/", "exit", "=", "_", "help", "c"]
    ## Cheking for digits in first number
    user_input_a = int_check(user_input_a, "first?")
    while True:
        ## We are cheking for invalid char's in operant.
        user_input_op = valid_check(valid_chr)
        if user_input_op == "=":
                print(user_input_a)
        elif user_input_op == "help":
            print("List of available actions: ")
            print(valid_chr)
        elif user_input_op == "c":
            user_input_a = 0
            user_input_b = 0
            print(user_input_a)
            user_input_a = int_check(user_input_a, "first?")
        else:
            ## Takes input from user for new number, if operant == "_" - it's return
            ## previous number that was input by user.
            user_input_b = last_num(last_dig)
            last_dig = user_input_b
            if user_input_op == "+":
                user_input_a = sum_(user_input_a, user_input_b)
            elif user_input_op == "-":
                user_input_a = diff_(user_input_a, user_input_b)
            elif user_input_op == "*":
                user_input_a = mult_(user_input_a, user_input_b)
            ## Cheking for ZeroDevision error
            elif user_input_op == "/":
                    if user_input_b == 0:
                        print("ZeroDivision:")
                    else:
                        user_input_a = separ_(user_input_a, user_input_b)
            elif user_input_op == "exit":
                        exit()


def sum_(x, y):
    return x + y
def diff_(x, y):
    return x - y
def mult_(x, y):
    return x * y
def separ_(x, y):
    return x / y


## Takes input from user for new number, if operant == "_" - it's return
## previous number that was input by user.
def last_num(last_dig):
    while True:
        x = input("dig?")
        if x == "_":
            x = last_dig
            return x
        else:
             try:
                x = int(x)
                return x
             except ValueError:
                print("You need to use digits")
                continue


## We are cheking for invalid char's in operant.
def valid_check(l):
    while True:
        x = input("op?")
        count = 0
        for i in l:
           if x == i:
               return x
           else:
               count += 1
               if count > len(l) - 1:
                   print("Invalid character")
                   continue
               else:
                   continue

## Cheking for digits in first number
def int_check(x, y = ""):
    while True:
        try:
            x = int(input(y))
        except ValueError:
            print("You need to use numbers")
        else:
            return x

calc()
