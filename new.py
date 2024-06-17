def find_short_long_word(x):
    shortest = x[0]
    longest = x[0]
    for i in x:
        if len(i)<len(shortest):
         shortest = i
        elif len(i)>len(longest):
         longest=i
    return shortest, longest
a= find_short_long_word(['hi', 'hello', 'd','address'])
print(a)
