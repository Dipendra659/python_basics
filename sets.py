#set stores multiple item in single variables
# set items are unordered, unchangable and does not allow duplicate values.
#
#
# my_set = {1,2,3,4,5,6,1,2,}
# print(my_set)
#
# This_set = {"apple","banana","true",1,2}
# print(This_set)
#
# This_set1 = {"apple","banana","false",0,2}
# print(This_set1)
#
#
# a = {"npj","ktm"}
# a.add("btl")
# print(a)

# set_1 = {1, 2, 3, 4, 5, 6}
# set_2 = {7, 5, 6, 4, 8, 9}
# set_3 = set_1.union(set_2)
# set_4 = set_1.intersection(set_2)
# print(f"union:{set_3}")
# print(f"intersection :{set_4}")

#multiple set union
# set_5 = {1, 2, 3, 4}
# set_6 = {1, 2, 3, 4, 5}
# set_7 = {4, 5}
# set_8 = set_5.intersection(set_6)
# set_9 = set_5.intersection(set_7)
# print(set_9)

#
# set_10 = {"google","apple"}
# set_11 = {"apple","microsoft"}
# set_12 = set_10.difference(set_11)
# print(set_12)

#python frozenset()
# a frozenset is an unordered and unindex collection of unique elements.
#since the elements are fixed , unliked sets you can't add or remove elements.

fruits = {"apple","banana", "cherry", "apple","kiwi"}
basket = frozenset(fruits)
print("unique elements:",basket)

#add new fruit throws an error
# basket.add("orange")
print("after adding new element:",basket)

city = {"npj", "ktm","dha"}
y = frozenset(city)
x = fruits.union(y)
print(x)