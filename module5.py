# Generators function
def mygeneratorfunction():
    x = 0
    print("First point is ")
    yield x + 1 # analogous only to return
    x += 1
    print("Second point is ")
    yield x + 1 # analogous only to return
    x += 1
    print("Third point is ")
    yield x + 1 # analogous only to return

generatorobj = mygeneratorfunction()
print(generatorobj)
print(type(generatorobj))

print(f"The current value of x is {next(generatorobj)}")
print(f"The current value of x is {next(generatorobj)}")
print(f"The current value of x is {next(generatorobj)}")
try:
    print(f"The current value of x is {next(generatorobj)}")
except:
    print("No more iterations are possible now")
for i in generatorobj:
    print(f"The current value of x is {i}")

# Generators
mylist = [x*x for x in range(0,10)]
print(mylist)
mygenerator = (x * x for x in range(0,10))
print(mygenerator)

for number in mygenerator:
    print(number)
