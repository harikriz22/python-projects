# functions
# block of code  which are executed when they are called


# def functioname():
    # code to be executed when function is called


# def myname(name):
#     print(f'my name is {name}')


# myname('assim')

# def addz(a=0,b=0,c=0): #former parameters
#     print(a,b,c)
#     # print(a+b)

# # positional arguments
# # ctrl + c/
# addz(1,2,3)

#keyword arguments

# addz(b=2,a=1,c=70)

# arguments
#values to be passed to a fucntions







# myname()
# myname()

# myname()

# DRY 


# def addz(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
    
# if addz(10):
#     print('even')
# else:
#     print('odd')




# 2 numbers

# basic 
# +
# -
# *
# /


# first-
# second -

# 1.add
# 2.sub
# 3.mul
# 4.div





def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def mul(a,b):
    return a * b
def div(a,b):
    return a / b


num1 = int(input('enter your first number: ---')) 
num2 = int(input('enter your second number: ---')) 
choice = int(input(
    'choose the operation you want \n1.Addition \n2.Subtraction \n3.multiplication \n4.Division \n :----------'
))
if choice == 1:
    print('sum is ' ,add(5,2))
elif choice == 2:
    print('difference is ' ,sub(num1,num2))
elif choice == 3:
    print('product is ' ,mul(num1,num2))
elif choice == 4:
    print('result is ' ,div(num1,num2))
else:
    print('invalid choice')