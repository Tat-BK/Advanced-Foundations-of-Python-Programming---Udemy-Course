# Decorators
# def addition(num):
#     return num + 5
#
# addbyfive = addition
# print(addbyfive(10))
# print(addbyfive(15))

# Multiple functions
# def addition(num):
#     def additionbyfive(num):
#         return num + 5
#
#     total = additionbyfive(num)
#     return total
#
# print(addition(5))
# print(addition(15))

# def func1():
#     def func2():
#         return "I am function 2"
#     return "I am function 1"
# print(func1())
#
# var1 = func1()
# print(var1)

# Functions calling another functions
# def additionbyfive(num):
#     return num + 5
#
# def callingfunction(executefunc):
#     constantnum = 10
#     return executefunc(constantnum)
#
# print(callingfunction(additionbyfive))

# Closure
# def func1(text):
#     "Return Message 1"
#     def func2():
#         "Return Message 2"
#         print(text)
#     # Calling the function
#     func2()
# func1("I want to say something")

# This is the decorating functions
def func1(func2):
    def func3():
        myfunction = func2()
        uppercase = myfunction.upper()
        return uppercase
    return func3

def inputtext():
    return "This is my text"

decorating = func1(inputtext)
print(decorating())

# Alternatively
#@decorators functions
@func1

def inputtext2():
    return "This is my another text"

print(inputtext2())
