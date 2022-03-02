# Meta class / Meta programming
# class Foo:
#     pass
# x = Foo()
# print(x.__class__)
# print(type(x))
# print(type(Foo))
#
# myvar1 = 5
# mydictionary = {'x':1,'y':2}
# class Foo:
#     pass
# x = Foo()
# for objects in (myvar1, mydictionary,x):
#     print(type(objects))
#
# for typing in int, float, dict, list, tuple:
#     print(type(typing))

# Defining class dynamically
# print(type(3))
# print(type(['something','in','the','list']))
# print(type((1,2,3,4,5)))
# class myclass:
#     pass
# print(type(myclass()))
# print(type(myclass))

# myclass = type('classname',(),{})
# x = myclass()
# print(x)
# print(type(x))
#
# class myclass:
#     pass
# x = myclass()
# print(x)
# print(type(x))
#___________________________________________
# class Foo:
#     pass
#
# Bar = type('Bar', (Foo,), dict(attr=100))
#
# x = Bar()
# print(x.attr)
# print(x.__class__)
# print(x.__class__.__bases__)

#______________________________
# class Foo:
#     pass
# class Bar(Foo):
#     attr=100
#
# x = Bar()
# print(x.attr)
# print(x.__class__)
# print(x.__class__.__bases__)

#_____________________________________
# Foo = type('Foo', (), {
#                         'attr':100,
#                         'attr_val': lambda x:x.attr
#                         })
# x = Foo()
# print(x.attr)
# print(x.attr_val())
#________________________________________________
# class Foo:
#     attr = 100
#     def attr_val(self):
#         return self.attr
#
# x = Foo()
# print(x.attr)
# print(x.attr_val())
#____________________________________________
# def f(obj):
#     print('attr = ', obj.attr)
# Foo = type(
#             'Foo',
#             (),
#             {
#                 'attr':100,
#                 'attr_val':f
#             }
# )
# x = Foo()
# print(x.attr)
# print(x.attr_val)
# print(x.attr_val())
#______________________________________
# def f(obj):
#     print('attr = ',obj.attr)
# class Foo:
#     attr = 100
#     attr_val = f
#
# x = Foo()
# print(x.attr)
# print(x.attr_val())
#________________________________________________
Many mores to come
https://realpython.com/python-metaclasses/#defining-a-class-dynamically
