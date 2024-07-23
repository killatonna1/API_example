class MyBaseClass:
    pass

class MyClass(MyBaseClass):
    def __init__(self):
        pass
    
    def __str__(self):
        pass
    
    def __add__(self, other):
        pass
    
    def __getitem__(self, key):
        pass
    
    # Other magic methods...

# Get all magic methods of MyClass
magic_methods = [method for method in dir(MyClass) if method.startswith('__') and method.endswith('__')]

print("Magic methods of MyClass:")
for method in magic_methods:
    print(method)

# Print the method resolution order
print("Method Resolution Order of MyClass:", MyClass.__mro__)
