# dictionary stored data in key,value pairs,
# it is ordered,changable and doesnt allow key duplicate
# info = {
#     "name":"dipendra",
#     "address":"nepalgunj",
#     "age": 27,
#     "is_verified": True,
#
# }

#
# print(info["name"])
# print(info["name"])
# print(info)
# info["address"]= "ktm"
# print(info["address"])
# print(info)
# info.pop("is_verified")
# print(info)
# info["gender"]= "male"
# print(info)
# for key,value in info.items():
#      print(f'"key:{key}": value:{value}')

#
# info_1 = info
# print(f"Info:{info}")
# info_1["email"]="abc@gmail.com"
# print(f"Info_1{info_1}")
#nested dictionary
my_family ={
    "child1":{
        "name":"Email",
        "year": 2004

    },
   "child2": {
     "name": "dipen",
     "year": 2005

  },
   "child3": {
     "name": "Ravi",
     "year": 2009
}
}
print(my_family["child3"]["name"])
del my_family["child3"]["year"]
my_family["child3"]["gender"] = "male"
print(my_family)
