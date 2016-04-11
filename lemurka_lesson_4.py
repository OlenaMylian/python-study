##import random
##
##secret = random.randint(1,10)
##count = 0
##is_win = False
##
##while count < 5:
##    try:
##        guess = int(input(str(count) + "?"))
##    except ValueError:
##        continue
##    count+=1
##    if secret == guess:
##        print("You win")
##        is_win = True
##        break
##    if secret < guess:
##        print("<")
##    else:
##        print(">")
##
##
##        
##if not is_win:
##    print("You are looser")
##



##import random

##l = [random.randint(1, 99) for x in range(5)]







## List
l = [62,54,78,44,27]
a_min = l[0]
counter_min = 0
counter_max = 0

for x in l:
    if a_min > x:
       a_min = x


b_max = l[0]

for x in l:
    if b_max < x:
       b_max = x

print(a_min)
print(b_max)
print(l)


for x in l:
    
        if x == a_min:
                break
        counter_min += 1
        

for x in l:
        if x == b_max:
                break
        counter_max += 1


l[counter_min], l[counter_max] = l[counter_max], l[counter_min]

print(l)
                

