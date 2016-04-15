"""
calc function used for basic calculations
"""

def calc():
    stop = False
    user_input_a = 0
    user_input_b = 0
    user_input_a = int(input("Put your number: "))
    last_dig = 0
    while True:
        print("Amount = ", user_input_a)
        print("Print one of the next operations",
              "\t +",
              "\t -",
              "\t *",
              "\t /",
              "\nPrint exit to quit")
                           
        user_input_op = input()
        user_input_b = last_num(last_dig)
        
        if user_input_op == "+":
            user_input_a = sum_(user_input_a, user_input_b)
        if user_input_op == "-":
            user_input_a = diff_(user_input_a, user_input_b)
        if user_input_op == "*":
            user_input_a = mult_(user_input_a, user_input_b)
        if user_input_op == "/":
                if user_input_b == 0:
                    print("ZeroDivision:")
                else:
                    user_input_a = separ_(user_input_a, user_input_b)
        if user_input_op == "exit":
            break
        
            
        last_dig = user_input_a
        
        



def sum_(x, y):
    return x + y
def diff_(x, y):
    return x - y
def mult_(x, y):
    return x * y
def separ_(x, y):
    return x / y

def last_num(last_dig):
    
    while True:
        x = input()
        print(x)
        if x == "_":
            
            x = last_dig
            return x
        
        else:
             try:
                x = int(x)
                return x
             except ValueError:
                continue
            
    
                        
calc()
