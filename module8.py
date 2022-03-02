# List comprehensions/inheritance
# # Regular Way
# mylist = ["superman", "batman", "spiderman", "ironman", "HULK"]
# mylist2 = []
# for hero in mylist:
#     if "man" in hero:
#         mylist2.append(hero)
# print(mylist2)
#
# # Using list comprehensiosn
# mylist2 = [hero for hero in mylist if "man" in hero]
# print(mylist2)

# # Iterate over the regular way
# mylist = []
# for characters in "List Comprehensiosn":
#     if characters == " ":
#         pass #break
#     else:
#         mylist.append(characters)
# print(mylist)
#
# # Alternatively
# mylist = [characters for characters in "List Comprehensiosn" if characters != " "]
# print(mylist)

# # For matrix
# mylist = []
# for x in range(3):
#     mylist.append([])
#
#     for y in range(5):
#         mylist[x].append(y)
# print(mylist)
#
# # Alternatively
# mylist = [[y for y in range(5)]for x in range(3)]
# print(mylist)

# Dictionary Comprehensions
# age = [20,22,25,26,28]
# name = ["John", "Alex", "Elvin", "Tom", "Jack"]
# mydictionary = {x:y for (x,y) in zip(name, age)}
# print(mydictionary)
#
# numbers = [1,5,10,23,252,2010]
# mydictionary = {x:x*2 for x in numbers if x%2==0}
# print(mydictionary)

# Set Comprehensions
# numbers = [10,20,30,40,50]
# mysets = {x for x in numbers}
# print(mysets)
#
# mysets = {y * 2 for y in numbers}
# print(mysets)
# print(type(mysets))
#
# val2 = {n * 3 for n in range(5)}
# print(val2)
#
# numbers = [2,5,6,7,8,9]
# mysets = {val for val in numbers if val%2}
# print(mysets)
# mysets = {val for val in numbers if val%2==1} # Means true
# print(mysets)
# mysets = {val for val in numbers if val%2==0} # Means False
# print(mysets)

# Tuple comprehensions by generators expressions
# mytuple  = tuple(val for val in (1,2,3,4,5))
# print(mytuple)
#
# numbers = [1,2,3,4,5,6,7,8,9,10]
# mytuple = tuple(evennumbers for evennumbers in numbers if evennumbers%2==0)
# print(mytuple)
