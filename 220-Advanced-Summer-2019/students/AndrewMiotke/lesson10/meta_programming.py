"""
Meta programming with class
"""


class Foo:
    pass

f = Foo()

print(type(f))
print(type(Foo)) # returns a type


class D:
    pass


d = D()
setattr(D, "name", "Jane")
getattr(d, "name") # returns "Jane"
