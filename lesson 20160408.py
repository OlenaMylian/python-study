## Test for

grn1 = kop50 = kop25 = kop5 = kop1 = 0.00

money_list = [100, 50, 25, 5, 1]
answer_list = ["1 grn", "50 kop", "25 kop", "5 kop", "1 kop"]

try:
    amount = float(input("Input amount of your money: "))*100
    if amount < 0:
        raise ValueError
except:
    print("Error! Wrong input.")
else:
    for i, x in enumerate(money_list):
        if amount // x and amount > 0:
                print("Amount of coins you need of", "\t", answer_list[i],"is\t", int(amount))
        amount %= x


##Exercise!!!!!!!!!!!!!!

import random

low_int = 1
up_int = 10
answer = 0
guess = 0

while answer != 1:
    
    
    
    try:
        guess = random.randint(low_int,up_int)
        print("Is that number equal", str(guess), "?")
        print("Choose one of three variants",
              "\n1. Your guess is right.",
              "\n2. It's bigger.",
              "\n3. It's less.",
              "\nPress one of three buttons 1, 2, 3.")
        answer = int(input())

    except ValueError:
          print("You need to input digits")
          continue
    else:
              
        if answer == 1:
                print("I'm the winer now! What the smartass I am! =)")
                break
        if answer == 2:
                low_int = guess + 1
                continue
        if answer == 3:
                up_int = guess - 1
                continue
        else:
                print("You need to input only numbers 1, 2, 3.")
                continue
    
                
       
print(" GAME OVER")



##### Exercise 3

import random

guess = random.randint(1,10)
answer = 0
low_int = 1
up_int = 10



while answer != 1:
    try:
        
        print("Is that number equal", str(guess), "?")
        print("Choose one of three variants",
              "\n1. Your guess is right.",
              "\n2. It's bigger.",
              "\n3. It's less.",
              "\nPress one of three buttons 1, 2, 3.")
        answer = int(input())

    except ValueError:
          print("You need to input digits")
          continue
    else:
              
        if answer == 1:
                print("I'm the winer now! What the smartass I am! =)")
                break
        if answer == 2:
                guess = random.randint(low_int + 1, up_int)
                continue
        if answer == 3:
                guess = random.randint(low_int, up_int - 1)
                continue
        if guess > 10 or guess < 0:
                print("you are lying... Your head will collapse")
                break
                
        else:
                print("You need to input only numbers 1, 2, 3.")
                continue
print(" GAME OVER")



