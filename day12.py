# args

# def addz(*args):
#     s=0
#     for i in args:
#         s+=i
#     return s    
# print(addz(2,3,7,3,4,5,2,5,6,7,3,23,4,5))

#kwargs

# def fullname(**kwargs):
#     s =''
#     for i in kwargs:
#         s+=kwargs[i]+' '
#     return s    
#     # return f'{fname} {mname} {lname}'

# print(fullname(fname='robert',lname='jr',mname='downie',secondname='hala',thirdname='vishnu',ninthname='yellow'))

# lambda functions

# def product(a,b):
#     return a*b

# p = lambda a,b:a*b

# sqr = lambda x :x**2

# print(sqr(5))

# print(p(7,8))

# lambda parameter1,parameter2:expression
# average of 5 numbers
# square root of a number
# full name fname lnam mname
# sum of 3 numbers
# perimeter of a circle 

# sr = lambda f : f**0.5

# print(sr(25))

# check is a person is eligible to vote or not

# vote = lambda age : True if age>=18 else False

# print(vote(9))


# if age>= 18:
#     print('you are eligible to vote')
# else:
#     print('you are not eligible to vote')



# recursion


# def hello():
#     print("Hello, World!")
#     return hello()
           

# hello()


# 10 number countdown 


def countozero(n):
    if n == 1:
        return  1
    else:
        return n * countozero(n-1)
print(countozero(5))


# fibanocci series using recursion
# 10

# scope of a variable
# modular programming
# oops
# file habdling
# exception handing

# comprehensions
# map,filter