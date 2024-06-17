# python Decorator allows to change the behaviour of a function without modifying the function itself and take another function as parameter.
# def decorator_function(orginal_function):
#     def wrapper_function(*args,**kwargs):
#         print("start.....")
#         result = orginal_function (*args, **kwargs)
#         print(result)
#         print("End....")
#         return result
#     return wrapper_function
# @decorator_function
# def name(a):
#     return a
# @decorator_function
# def place(b):
#     return b
# x = name("dipendra")
# print(x)
# y = place("butwal")
# print(y)
#









def decorator_function( orginal_function):
    def wrapper_function(*args,**kwargs):
        print("start...")
        result = orginal_function(*args, **kwargs)
        print(result)
        print("End.........")
        return result
    return wrapper_function()
@decorator_function
def place(a):
    return a
@decorator_function
def age(x):
    return x
S = place("surkhet")
print(a)
b= age(26)
print(b)