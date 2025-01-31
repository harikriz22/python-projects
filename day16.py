# # class Car:
# #     def __init__(self):
# #         self.name ='maruthi 800'
# #         self.color='red'
        

# #     def start(self):
# #         print('car has started')

# #     def run(self):
# #         print('car is running')

# # car1 = Car()
# # car1.start()
# # car2 = Car()
# # car2.run()

# # print(car2.color)
# # # constructor 

# # # initialize

# # #magic functions
# # # __init__()


class Mobile:

    def __init__(self,b,p):
        
        self.brand = b
    
        self.price = p

    def showvalues(self):
        print(f'{self.brand}  {self.model} with a price of rs {self.price}')
        
    def compare(self,obj):
        if self.price > obj.price:
            print(f'{self.brand} has higher price')
        else:
            print(f'{obj.brand} has higher price')



m1 = Mobile('iphone',75000)
m2 = Mobile('samsung',65000)

m2.compare(m1)

# student class
    
#     name
#     roll
#     m1
#     m2
#     m3
#     m4 
#     m5

#     sum(

#     )
#     average()

#     percentage()


#     result(

#     )


# class Student:
#     def __init__(self,name,roll,m1,m2,m3,m4,m5):
#         self.name = name
#         self.roll = roll
#         self.mark1 = m1
#         self.mark2 = m2
#         self.mark3 = m3
#         self.mark4 = m4
#         self.mark5 = m5



#     def msum(self):
#         return self.mark1+self.mark2+self.mark3+self.mark4+self.mark5      

#     def average(self):
#         return s1.msum()/5
    
#     def percentage(self):
#         return (s1.msum()/250)*100
    
#     def result(self):
#         print(f'{self.name} has a total mark of {self.msum()} average of {self.average()} and has a cgpa of {self.percentage()}')


# s1= Student('assim',24,40,41,42,43,44)

# s1.result()


# emplooyeee

# name 
# emp_id

# 40000


