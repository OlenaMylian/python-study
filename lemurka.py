# Exercise №1
# We need to compare three numbers that user will input.
x=int(input("x?"))
y=int(input("y?"))
z=int(input("z?"))

if x>y:
    if x>z:
        print(x)
    else:
        print (z)
else:
    if y>z:
        print (y)
    else:
        print (z)


# Exercise №2
# We need to catch the Error in user input. 
# If there error >> Catch it.
# If all fine >> Print the area value S.
try:
    a = int(input("a?"))
    b = int(input("b?"))
    c = int(input("c?"))
    if not ((a+b)>c and (b+c)>a and (c+a)>b):
        raise NameError("OMG")
except NameError as MyError:
    print(MyError)
except ValueError:
    print ("No number")
else:
    p = (a+b+c)/2
    print (p)
    S = (p*(p-a)*(p-b)*(p-c))**0.5
    

# Exercise №3
# The user input some number in float format, it will be a money amount.
# For example 123.45 ro 512.22
# We need to output how much coins of max nominal we need.
number = float(input("floatnumber?"))

grn1 = number // 1
number = number % 1

kop50 = number*100 // 50
number = number*100 % 50

kop25 = number // 25
number = number % 25

kop5 = number // 5
number = number % 5

kop1 = number // 1


if grn1 != 0:
    print("grn1 = ", int(grn1))
if kop50 != 0:
    print(int(kop50))
if kop25 != 0:
    print(int(kop25))
if kop5 != 0:
    print(int(kop5))
if kop1 != 0:
    print(int(kop1))
    



# Exercise №4
# 


# Exercise №5
# 
