list_amount = 100
l_0 = [" " + str(i) for i in range(0, list_amount + 1)]
for i in range(0, list_amount):
    if len(str(l_0[i])) < len(str(list_amount)) and i == 0:
        space = len(str(list_amount)) - len(str(l_0[i]))
        l_0[i] = " " * space + str(l_0[i])
        if i > 10:
            l_0[i] = l_0[i][1:]
    if len(str(l_0[i])) > len(str(list_amount))  or i == 0:
        space = len(str(l_0[i])) - len(str(list_amount))
        l_0[i] = l_0[i][space:]

for i in range(1, list_amount + 1):
    l_x = []
    y = i
    l_x.append(i)
    if len(str(l_x[0])) < len(str(list_amount)):
        space = len(str(list_amount)) - len(str(l_x[0]))
        l_x[0] = " " * space + str(l_x[0])
    for x in range(0, list_amount):
        l_x.append(" *")

        if len(l_x) == list_amount + 1:

            globals()['l_%d' % y] = l_x

for i in range(0, list_amount + 1):
    print(*globals()['l_%d' % i])







def var_generator():
    for X in range(0, list_amount + 1):
       globals()['l_%d' % X] = l_generator()



#if len(str(l_x[0])) < len(str(list_amount)):
#    space = len(str(list_amount)) - len(str(l_x[0]))
#    l_x[0] = " " * space + str(l_x[0])