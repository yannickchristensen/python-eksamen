# List, Tuple, Set and Dictionary

#List

list = ["apple", "pear", "banana", "pear"] 
list2 = [1,2,3]

list2[0] = 'a'
print(list2[0])

for x in list:
    print(x)

list.append("pineapple")
print(list)
list.remove("pineapple")
print(list.count("pear"))
list.reverse()
print(list)


#Tuple

tuple = ("Yannick", "Brot", "Christensen")

print(tuple[0])

for x in tuple:
    print(x)



#Set

set = {4, 5, 6, 7, 8}

for x in set:
    print(x)

set2 = {1, 2, 3, 4, 5, 6}


set3 = set.difference(set2)
print(set3)
set4 = set.intersection(set2)
print(set4)


#Dictionary

dict = {
    "France": "Paris", 
    "Germany": "Berlin", 
    "Denmark": "Copenhagen"}

for key in dict:
    print(key, '->', dict[key])


dict.update({"Spain": "Barcelona"})
dict["Spain"] = "Madrid"

print(dict)

dict.get("Denmark")
print(dict["Denmark"])

dict.pop("Denmark")
del dict["Spain"]

print(dict.keys())
print(dict.values())


print(len(dict))
print(len(tuple))
print(len(set))
print(len(set))


[(15,23), {15, 18}, {12: 1.2, 13: 1.3, 14: 1.4}]