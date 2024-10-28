name_and_age = {"Bill":21, "Jane": 34, "Sam": 56}

name =  input("Enter name:")
age = int(input("Enter age: "))

name_and_age[name] = age
print(name_and_age)


# print(name_and_age)
# print(name_and_age.keys())
# print(name_and_age.values())
# print(name_and_age.items())
# print(max(name_and_age.values()))
#
# for name,age in name_and_age.items():
#     print(name, age)
#
# for name,age in name_and_age.items():
#     if age == 56:
#         print(name, age)
#
# print(list(name_and_age.items()))
# print(tuple(name_and_age.items()))

# print(name_and_age["Jane"])
# print(len(name_and_age))
# name_and_age["Lukas"]=20
# print(name_and_age)
# name_and_age["Lukas"]="ten"
# print(name_and_age)
# name_and_age["Lukas"]=10
# print(name_and_age)
#
# del name_and_age["Lukas"]
# print (name_and_age)
#
# print(name_and_age.pop("Bill"))
# print(name_and_age)
#
# name_and_age["Jane"] =name_and_age["Sam"]
# print(name_and_age)
#
# for name in name_and_age:
#     print(name, name_and_age[name])
#
# for i in range(len(name_and_age)):
#     print(i)