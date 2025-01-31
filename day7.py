# list
# collection of datas
# a = [11,12,13,14,15,16]
# list are ordered
# a= [1,2,3,4]
# b = [1,2,3,4]


# print(a==b)

# data = [11,'hari',5.6,True,[11,11,12,143]]
# print(a[::-1])


# a = [11,12,[100,200,['python',['hari'],'django'],300,400],13,14]


# li = [1.1,2,2,2,2,3,3,4,['ha',[11,12,['python','django'],13,14],'ri'],4,5,65,]
# print(li[8][1][2][1])

# print(a[2][2][1][0])          



# dynamic 



# a=[6,7,8,9,10,11,12,13,14]
# a[1:6]=['hari']
# print(a)


# mutable

# str immutable data type
# name= 'hari'
# name[2]='k'
# name = 'hari'


# a = [11,12,13,14]
# a[0]='hari'
# print(a)



# append(value)
# to add an element at the end of a list

# a.append('hari')
# a.append(20)


# extend(value)
# to add multiple elements at the end of a list
# a.extend('hari')
# print(a)

# insert(index,value)
# a.insert(0,'python')
# a.insert(4,'hari')
# print(a)


# pop
# a =[11,12,13,14,14,14,14,15,16,17,18]

# a.remove(14)
# print(a)
# a.pop() #removes last elements from a list
# print(a)
# # pop(index) removes an eelemenst from that index
# a.pop(0)
# print(a)

# +
# *
# in 

# itreables
# a=[1,2,3]
# print(a*2)
# b='hari'
# a+=b
# print(a)

# a ='hari'
# b='python'
# print(a*5)
# a=[11,12,13,14,15]

# if 101 in a:
#     print('yes')



# loop
# data = [11,12,13,14]
# for i in data:
#     print(i)


# a=[11,12,13,14,15,16,17]
# for i in range(0,len(a)):
#     print(a[i])










data = [0,1,2,3,-4,-7,0,10,-100,7]

for i in range(len(data)):
    if data[i] < 0:
        print(data[i],'negative')
    elif data[i]> 0:
        print(data[i],'positive')
    else:
        print(data[i],'zero')
    

# 0  zero
# 1 positive
# 2 positive