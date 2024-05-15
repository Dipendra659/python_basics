# course = "python for Beginners"
# print(course[-3])
# print(course[0:9])
# print(course[0:])
#
#
#
# # print(course[:50]) # returns 0 to 4th index
# # print(course[50])
#
# print(course[1:-1])
# print(len(course))
# place= "Nepalgunj bikasnagar "
# print(place.capitalize())
# print(place.upper())
# print(place.find('g'))
#
#
# print(place.count("c"))
# # print(place.replace( "d","a")),
# txt="hello, welcome to my world."
# x= txt.endswith(".")
# print(x)
#
# x = "hello ,its me dipendra"
# x = txt.startswith("h")
# print(x)
# text= "98657777659"
# x= text.zfill(16)
# print(x)

address ="Nepalgunj"#wednesday day 3
print(address[::2]) # print every second character
print(address[::-1]) # print reverse

#strip,split,join
#strip removes trailing whitespaces.
#split returns a list
#join it concatenates string with another string.
string_example =" hello Dipendra  "
print(string_example)
print(string_example.strip())
print(string_example.split())
a = string_example.split()
print(a[0])

# jwt_token = "Dipendra.shahi.thakurii"
# b = jwt_token.split(".")
# print(b[1])
# print(b[2])
# print(b)
place = " nepalgunj bikasnagar"
c = (place.strip())
d = "hello".join(c)
print(d)
e= place.split()
f= "".join(e)
print(f)