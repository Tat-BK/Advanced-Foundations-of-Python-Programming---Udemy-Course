# Iterators in python

# numbers = [1,2,3,4,5,6,7,8,9,10]
# iteratorobj = iter(numbers)
# print(next(iteratorobj))
# print(next(iteratorobj))
# # Continue until exceed the end will raise an errors
#
# for x in range(len(numbers)):
#     print(next(iteratorobj))

# mystring = "Python Iteratbles Iterators"
# myiteratorobj = iter(mystring)
# print(next(myiteratorobj))
# print(next(myiteratorobj))

# Building own iterators objects
# def myiteratorfunc(n):
#     myiteratorobj = iter(n)
#
#     while True:
#         try:
#             print(next(myiteratorobj))
#         except StopIteration:
#             print("Breaking the operations")
#             break
#
# myiteratorfunc([1,2,3,4,5])
# myiteratorfunc("this is a string")

# Building Iterator using Object Oriented Programming Languages Concept
# This will be an infinite loops
# class Incrementclass:
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         x = self.count
#         self.count = self.count + 1
#         return x
# myiteratorobj = Incrementclass()
# myiteration = iter(myiteratorobj)
# for x in range(5):
#     print(next(myiteration))
#
# for variablename in Incrementclass():
#     print(variablename)


# class Incrementclass:
#     def __iter__(self):
#         self.count = 0
#         return self
#
#     def __next__(self):
#         if self.count <= 20:
#             x = self.count
#             self.count = self.count + 1
#             return x
#         else:
#             raise StopIteration
#
# for variablename in Incrementclass():
#     print(variablename)
