# # Zip functions in python, returning output as a tupple object of data tpes
# for item in zip([10,20,30],['x','y','z'],['X', "y", "z"]):
#     print(item)
#
# x = set(zip([10,20,30],['x','y','z'],['X', "y", "z"]))
# print(x)
#
# x = set(zip())
# print(x)
#
# for item in zip([10,20,30]):
#     print(item)
#
# # By default it will print the shortest iterations of the list only
# x = set(zip([10,20],[30,40,50,60,70,80,90,100]))
# print(x)
#
# from itertools import zip_longest as ziplong
# x = set(ziplong([10,20],[30,40,50,60,70,80,90,100]))
# print(x)
#
# # Unzippings values
# unzipvariable = zip([10,20,30],['x','y','z'],['X', "y", "z"])
# x,y,z = zip(*unzipvariable)
# print(f"x: {x}")
# print(f"y: {y}")
# print(f"z: {z}")

# Eval function - predefined function for mathematics operations
# val1 = eval("10+2")
# print(val1)
#
# val2 = eval("sum([10,20,30])")
# print(val2)
#
# val3 = eval('val2*10')
# print(val3)
#
# # This is globally defined
# val4 = eval("x+y", {'x':val1, 'y':val2})
# print(val4)
#
# # By default it will be a local variable
# val5 = eval("x+y", {}, {'x':val1, 'y':val2})
# print(val5)

# The memory view function - b for bytes
# x = b'Python Language Works With Memory'
# print(x)
# print(type(x))
#
# memoryofx = memoryview(x)
# print(type(memoryofx))
# print(memoryofx)
#
# objectofx = memoryofx.obj
# print(objectofx)
#
# # to return the ASCII Characters
# characterlist = memoryofx.tolist()
# print(characterlist)

# bytearray function
# x = bytearray("Python is very powerful", "utf-8")
# print(type(x))
#
# y = memoryview(x)
# print(y)
# print(y[4]) # to return the ASCII values
# print(chr(y[4]))
#
# z = y.tobytes()
# print(type(z))
# print(z)

# x = memoryview(b"45,50,55")
# y = x[4]
# print(y)
# print(chr(y))
# print(type(y))
#
# x = memoryview(b"Python Programmings")
# y = x[2:10]
# print(y)
#
# print(y.tobytes())
# #Alternatively
# print(bytes(y))
#
# print(y.tolist())
# # Alternatively
# print(list(y))

# The mapping functions, for iterations variables / objects
# mylist = [5,10,15,20,25]
#
# def toaddlist(n):
#     return n+1
#
# iterablevariable1 = map(toaddlist, mylist)
# print(iterablevariable1)
# for variables in iterablevariable1:
#     print(variables)
#
# def toaddstring(x,y):
#     return x + y
#
# mystringlist = map(toaddstring, (" Batman ", " Superman "), ("Beyound", "Return"))
# print(mystringlist)
# print(tuple(mystringlist))
#
# mystringlist = map(toaddstring, [" Batman ", " Superman "], ["Beyound", "Return"])
# print(mystringlist)
# print(list(mystringlist))

# The lambda functions - for iterations / iterable variables / objects
# mylist = [1,3,5,7,9]
# iterableobj1 = map(lambda x: x+1, mylist)
# print(iterableobj1)
# print(list(iterableobj1))
# this will not works
# print(tuple(iterableobj1))
# for varil in list(iterableobj1):
#     print(varil)
# for varil in iterableobj1:
#     print(varil)

# mylist1 = [10,20,30]
# mylist2 = [40,50,60]
#
# combinedlist = map(lambda x,y: x+y, mylist1, mylist2)
# print(combinedlist)
# print(list(combinedlist))
# for something in list(combinedlist):
#     print(something)

# The enumerate functions
# person = ["person1", "person2", "person3", "person4", "person5"]
# enumeratedperson = enumerate(person)
# print(type(enumeratedperson))
#
# listofenumeratedperson = list(enumeratedperson)
# print(listofenumeratedperson)
#
# for index, name in enumerate(person):
#     print(f"{index}: {name}")

# enumeratedperson = enumerate(person, start=15)
# print(type(enumeratedperson))
#
# listofenumeratedperson = list(enumeratedperson)
# print(listofenumeratedperson)
#
# for index, name in enumerate(person, start=15):
#     print(f"{index}: {name}")

# person = ["person1", "person2", "person3", "person4", "person5"]
# enumeratedperson = enumerate(person, start=10)
# print(enumeratedperson.__next__())
# print(enumeratedperson.__next__())
# print(enumeratedperson.__next__())
# print(enumeratedperson.__next__())
# print(enumeratedperson.__next__())
# try:
#     print(enumeratedperson.__next__())
# except:
#     print("No more iteration is possibles")

# Use the exce - execute function to execute the code, usually associated/come together witht he print functions prebuilt in into the python shell
# exec("print('I commanded you to print this out')") # Use the single quotation marks here
# myfunction = '''
# x = 5
# y = 10
# print('x + y = ', x+y)'''
# exec(myfunction)
#
# exec('[print(i+5) for i in [5,15,25]]') # must put single quoration marks into a string here
#
# exec('print(abs(-10))')
#
# # To print out all the available functions in exec functions
# exec('print(dir())')
#
# # Global variables
# from math import * # local variable will not works as the library is imported globally only
# codetoexec = '''
# x = sqrt(16)
# print(x)'''
# exec(codetoexec)
# # Globally
# exec(codetoexec, {'sqrt':sqrt})
# # Locally, will not work here
# # exec(codetoexec, {}, {'sqrt':sqrt})

# Module 3
# The *args function, uses when undefined parameters need to pass in
# def addition(*args):
#     result = 0
#     for x in args:
#         result = result + x
#     print(result)
#
# addition(10,22)
# addition(15,20,33,50,60)

# The **kwargs function - variable input with default parameters to be assigned, return as a dictionary
# def myrhythm(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     print('----------------------------------')
#     for key, value in kwargs.items():
#         print("{} is equal to {}".format(key,value))
#         print(f"{key} is equal to {value}")
#
# myrhythm(red = "Hibuscus", blue="Rev Volvet", green="Hulk")
