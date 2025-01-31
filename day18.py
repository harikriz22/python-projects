# # 3 types

# # single level inhertence
# # multi level inheritence
# # multiple inheritence


# class Person1:
#     def __init__(self):
#         print('person 1')

#     def run(self):
#         print("Person is running")
    
#     def jump(self):
#         print("Person is jumping")

    
#     def speak(self):
#         print("Person1 is speaking")    

# class Person2(Person1):
#     def __init__(self):
#         print('person 2')
#         super().__init__()

#     def swim(self):
#         print("Person is swimming")

#     def fly(self):
#         print("Person is flying")

#     def speak(self):
#         super().speak()
#         print("Person2 is speaking")

# class Person3:
#     def eat():
#         print("Person is eating")

#     def sleep():
#         print("Person is sleeping")

    
#     def speak():
#         print("Person3 is speaking")    

# class Person4(Person1,Person2,Person3):
#     def sing():
#         print("Person is singing")

#     def dance():
#         print("Person can dance")

    # MRO - method resolution order
    


# p2=Person2()

# p2.speak()

# polymorphism
# poly - many
# morph - forms

# duck typing
# operator overloading
# method loading
# methos overriding


# duck typing
# if it looks like a duck and quacks like a duck, it is a duck


# class Chicken:

#     def coocoo():
#         print("cluck cluck")

#     def walks() :
#         print("chicken is walking")
# class Duck:   
#     def quack():
#         print("quack quack")
    
#     def walks():
#         print("duck is walking")
# class Farmer:

#     def catches(bird):
#         bird.walks()

# c= Chicken
# d= Duck

# f= Farmer
# f.catches(c)



# a = 5
# b = 7

# print(a+b)

# print(int.__add__(a,b))

# + ---> __add__

# __init__

# - __sub__


class Student:
    def __init__(self,m1,m2):
        # self.name = name
        self._m1 = m1
        self.__m2 = m2


    def __add__(self,otr):
    
        return (self.m1+otr.m1  ,self.m2+otr.m2)
    




s1=Student(7,6)
s2=Student(6,8)        
s1.m1
print(s1+s2)

# __sub__
# __mul__
# __truediv__

# (13,14)
