# print(dic)
# print(dictionary.items())
# print(dictionary['address'])
# print(dictionary['asdfsadfsadf'])
# print(dictionary.get('address'))
# print(dictionary.keys())
# print(dictionary.values())
# for dic in dictionary.values():
#     print(dic)
# for key in dictionary.keys():
#     print(f'the value corresponding to the key {key} is {dictionary[key]}')

# for key, values in dictionary.items():
#     print(f'the value corresponding to the key {key} is {values}')
dictionary = {
    "name":"bharat",
    "address":"lalitpur",
    "phone_no":"9818742324",
    1:1,
    "stutus": False
}
# print(len(dictionary))
# x = dictionary.pop('name')
# print(x)
# print(dictionary)

# dictionary.popitem()
# # print(y)
# print(dictionary)

abc = {
    1: "sno",
    2: "name",
    3: "address",
    4: "abc"
}
# abc[4] = "phone"
# print(abc)
# abc.clear()
# print(abc)

# abc.update(dictionary)
# print(abc)

# dictionary["name"] = ['abc', 'xssdfsdf']
# print(dictionary)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily["child2"]["name"])
print(myfamily)


