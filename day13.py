# # time
# # random
# # os
# # sys

# import time

# # print(time.time())
# # print(time.ctime(1737611653.6907043)) #epoch
# a= time.time()
# for i in range(1,4):
#     print(i)
#     time.sleep(2)
# b = time.time()

# print(b-a)



# quiz with timer 

import random

values = ['rock','paper','scissor']

user=''

while user not in values:
    user = input("Enter rock, paper or scissor: ").lower()



comp = random.choice(values)
print('user choose',user)
print('computer choose',comp)

if user == comp:
    print('tie')
elif user == 'rock':
    if comp == 'scissor':
        print('user win')
    else:
        print('computer win')

elif user =='paper':
    if comp == 'rock':
        print('user win')
    else:
        print('computer win')

elif user =='scissor':
    if comp == 'paper':
        print('user win')
    else:
        print('computer wins')    

# print(random.randint(1,10))
# a = ['apple','orange','grape','pineapple','lemon','blueberry','mango']

# print(random.choice(a))

# coin toss 

# a = random.randint(0,1)
# if a == 1:
#     print('heads')
# else:
#     print('tails')


# a=['heads','tails']
# print(random.choice(a))

# rock paper scissor


# recursion using  fn-1 f n-2





