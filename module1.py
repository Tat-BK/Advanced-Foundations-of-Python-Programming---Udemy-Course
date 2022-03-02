# # Named tuple is used when indexing tuple by name
# from collections import namedtuple
#
# mytuppleobj = namedtuple("Tupplename", ["xcoor", "ycoor"])
#
# obj1 = mytuppleobj(20,50)
#
# print(obj1)
#
# print(isinstance(obj1, mytuppleobj))
#
# print(isinstance(obj1, tuple))
#
# # mytuppleobj is a tuple
#
#
# # Unpacking tuple
# x,y = obj1
# print(f"x: {x}, y:{y}")
#
# for item in obj1:
#     print(item)
#
# x1 = obj1[0]
# print(x1)
# y1 = obj1[1]
# print(y1)
#
# obj2 = namedtuple('Tupplename2', 'xcentre, ycentre, _renamedme', rename=True)
# print(obj2._fields)

# Default dictionary
# conventionaldic = dict()
# try:
#     print(conventionaldic[5])
# except:
#     print("You do not assigned key values to it")
#
# from collections import defaultdict
# defaultdic = defaultdict(int) # integer data types
# try:
#     print(defaultdic[5]) # all position will be 0
# except:
#     print("With default values, no errors is raised")

# Dictionary can be created without values
# from collections import defaultdict
# defaultdicobj = defaultdict(set) # set is a fix
#
# defaultdicobj["keys"].add("values")
# defaultdicobj["keyswithoutvalues"]
# defaultdicobj["name"].add("John")
#
# print(dict(defaultdicobj.items()))
#
# print(type(defaultdicobj))

# For a list
# from collections import defaultdict
# defaultdicobj = defaultdict(list) # set is a fix
#
# defaultdicobj["keys"].append("values")
# defaultdicobj["keyswithoutvalues"]
# defaultdicobj["name"].append("John")
#
# print(dict(defaultdicobj.items()))
#
# print(type(defaultdicobj))

# Counter for list
# from coll

# # Ordered Dictionary
# from collections import OrderedDict
# # Create Dictionary
# mydictionary = {"Name":"John", "Age":25, "Occupation":"Python Developer"}
# print(mydictionary)
#
# # Creating empty dictionary
# myordereddictionary = OrderedDict()
# print(myordereddictionary)
#
# myordereddictionary = OrderedDict(mydictionary)
# print(myordereddictionary)
#
# # Adding item to the dictionary
# myordereddictionary["Addedkey"] = "AddedValues"
# print(myordereddictionary)
#
# # Replacing item in a dictionary
# myordereddictionary["Addedkey"] = "Added Values(with space)"
# print(myordereddictionary)
#
# # Deleting item in a dictionary
# myordereddictionary.pop("Addedkey")
# print(myordereddictionary)
#
# # Moving elements in the dictionary
# myordereddictionary.move_to_end("Name")
# print(myordereddictionary)
#
# # Reverse the iterations
# reversedmyordereddictionary = reversed(myordereddictionary)
# print(reversedmyordereddictionary)
# for item in reversedmyordereddictionary:
#     print(item)

# Queue in python - First In First Out Rule (FIFO)
# from queue import Queue
# queuelist = Queue()
# print(queuelist)
# queuelist.put("Person1")
# queuelist.put("Person2")
# queuelist.put("Person3")
# print(queuelist)
# print(queuelist.get())
# print(queuelist.get())
# print(queuelist.get())
# try:
#     print(queuelist.get())
# except:
#     print("Nothing to return already")

# Python Deque - Last In First Out (LIFO)
from collections import deque
dequelist = deque()
print(dequelist)

dequelist.append("Person1")
dequelist.append("Person2")
dequelist.append("Person3")
print(dequelist)

dequelist.popleft()
print(dequelist)

dequelist.clear()
print(dequelist)
