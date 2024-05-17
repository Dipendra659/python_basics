[]
# list is mutable because we can perform operation append,insert etc.
# a=[2,3,4,5,6,7,8]
# a.append(2) # insert the elements from last index
# a.insert(3,10)
# a.remove(3)
# a.pop()
# print(a)
#
#
# b=[2, 4, 6,7, 8, 3, 9]
# print(b.index(6))
# print(b.count(4)) #element lie count garna kam garxa
# b.sort()
# print("sorted",b) #ascending  order ma sort garxa
# b.reverse()
# print("reversed",b)
# print(len(b))

# copy creates new objects and copies and only copies from references
# fruits = ["apple","pear","orange","banana"]
# c= fruits.copy()
# c.append("cherry")
# print(c)

my_list = [0]*5 #[0,0,0,0,0]
my_list2 =[1,2,3,4,5]
my_list3 = my_list + my_list2
print(my_list3)

e =[1, 2, 3, 4, 5, 6,7, 8,9]
print(e[1:5])
print(e[2:-1])
print(e[2::-2])
print(e[2::2])

