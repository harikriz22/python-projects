# # # # class A():
# # # # 	def run(a,b):
# # # # 		pass

# # # # 	def run(a,b,c):
# # # # 		pass
	
# # # # a=A
# # # # a.run(1,2)
# # # # a.run(3,4,5)    



# # # class A():
# # # 	def eat():
# # # 		print('a')


# # # class B(A):
# # # 	pass

# # # b=B
# # # b.eat()


# # # abstraction 

# # import random
# # from abc import ABC,abstractmethod

# # class Vehicle(ABC):
# #     def __init__(self):
# #         pass
    
# #     def generate(self):
# #         z=f'VH{random.randint(2000,30000)}'
# #         print(z)

# #     @abstractmethod
# #     def run(self):
# #         print('runs on petrol')


# # class Car(Vehicle):

# #     def __init__(self):
# #         pass

# #     def run(self):
# #         print('hello')

# # c=Car()
# # c.generate()




# # exception handling



# try:

#     a=int(input('enter a number'))
#     b=0
#     c=a/b
#     print(c)

# except ZeroDivisionError:
#     print('you cannot divide a number with zero try again')
    

# except ValueError:
#     print('invalid input')

# else:

#     print('hari',c)


# finally:
#     print('this will always execute')


# class Myerror(Exception):
#     pass


# a= 10
# if a> 5:
#     raise Myerror('wrong')




# list comprehension
# lambda function

a=[]
for i in range(10):
    a.append(i*i)

print(a)

# data = [expression]

sqr=[i*i for i in range(1,11)]
print(sqr)


# 1000  even numbers
even=[i for i in range(1,1000) if i%2==0 ]
print(even)


a=[1,0,9,11,-6,2,-1,87,7,-1]

result = ['positive' if i > 0  else 'negative' for i in a] 
print(result)



six = [i for i in range(1,1001) if '6' in str(i)]
print(six)
# multiple of 3 and 5
# from first 1000 numbers print numbers that has digit 6 in them
from day18 import Student
