# string
# sequence of chrs " "
# name = 'hari'
# location = "lochi"
# email = ''' sghuiajld@j.com'''
# a = '''hari once said that "life is great" '''
# print(a)
# \
# \'   --- >  '
#\" -----> "
#\n - newline
#\t - tabspace
#\b backspace
# name = 'hari\bshi'
# # a = 'hari\'s resume'
# # b = "hari\b \tonce said that\n \"life is great\""
# print(name)




# typecasting typeconversion
# ctrl +z

# a= '5'
# a = int(a)
# b = 5
# print(a+b)

#statically typed

# int a = 5
# name = 'hari'

# python is a dynamically typed language
# implicit
# explicit


# a = 5
# print(type(a))




    #  0 1 2 3 4 5 6 7 8 9 10 11 12
# a = 'python django'
            #   -5 -4  -3  -2 -1

# [start:stop:step]
#indexed datatype
# index starts at 0
# print(a[1:5])
# print(a[1:])
# print(a[:5])
# print(a[::-1])

# operations


# 1.concatination addition

# a = 'hari'
# b = 'python'
# c= a+' '+b
# print(type(c),c)

# 2.multiplication

# a = 4
# b = 'hari'
# print(a*b)

# in operator membership operator

# name = 'hari'
# if 'hr' in name:
#     print('a is present in name')





# loop 
# 2 type
# name = 'harikrishnan'

# for i in name:
#     print(i)

# a=len(name)

# for i in range(a):
#     print(i,name[i])



a = 'harikrishnan'
# 'a' at position 1
# 'i' at position 3

# for i in range(len(a)):
#     # print(a[i])
#     if a[i] =='a' or a[i]=='e' or a[i]=='i' or a[i] =='o' or a[i] =='u':
#         print(a[i],'at index ',i)

a='hari'
for i in range(len(a)):
    if a[i] in 'aeiou':
        print(a[i],i)
# fibanoccii series

# 0 1 1 2 3 5 8 13 21 

# 2 . palaindrome
# 131 --> 131 

# 3 . reverse of a string [::-1]

