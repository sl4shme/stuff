##Links
 - https://docs.python.org/2/tutorial/classes.html
 - https://www.tutorialspoint.com/python/python_classes_objects.htm
 - https://en.wikipedia.org/wiki/C3_linearization



##To_Read
- https://docs.python.org/2/tutorial/classes.html
- https://www.python.org/download/releases/2.2.3/descrintro/
- https://docs.python.org/2/reference/datamodel.html
- https://docs.python.org/3/reference/datamodel.html
- http://www.cafepy.com/article/python_types_and_objects/python_types_and_objects.html
- http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static
- http://stackoverflow.com/questions/11949808/what-is-the-difference-between-a-function-an-unbound-method-and-a-bound-method
- https://www.programiz.com/article/python-self-why


##Basics
####Definition of a class
```python
class Car(object):
    'Base class for all cars'
    number_of_cars = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        Car.number_of_cars += 1

    def print_info(self):
        print("I'm a {} from {}.".format(self.model, self.brand))
        print("There are {} cars at the moment.".format(Car.number_of_cars))

    def accelerate(self):
        self.speed += 10
```

####Instantiation of a class
```python
car1 = Car("Renault", "Clio")
car2 = Car("Bentley", "Continental GT")

type(Car)
type(car1)
```
> type <br/>
> `__main__.Car`

####Accessing attributes and methods
```python
print(car1.brand)
print(car2.brand)
print(Car.number_of_cars)

car1.model = "Test"

car1.print_info()

car1.color = "red"
print(car1.color)
```
> Renault <br/>
> Bentley <br/>
> 2 <br/>
> I'm a Test from Renault. <br/>
> There are 2 cars at the moment. <br/>
> red

## ...attr functions
```python
hasattr(car1, 'brand') # Returns True if 'brand' attribute exists for this instance
getattr(car1, 'brand') # Returns the value of the 'brand' attribute
delattr(car1, 'brand') # Delete attribute 'brand'
setattr(car1, 'brand', 'test') # Set the attribute 'brand' to 'test'
```

## Built-In attributes

 - `__dict__`: Dictionary containing the class's namespace.
 - `__doc__`: Class docstring or none, if undefined.
 - `__name__`: Class name.
 - `__module__`: Module name in which the class is defined.
 - `__bases__`: A possibly empty tuple containing the base classes.

```python
print(Car.__doc__)
print(Car.__name__)
print(Car.__module__)
print(Car.__bases__)
print(Car.__dict__)
```
> Base class for all cars <br/>
> Car <br/>
> `__main__` <br/>
> () <br/>
> ```
{'__doc__': 'Base class for all cars',
'__init__': <function __main__.__init__>,
'__module__': '__main__',
'accelerate': <function __main__.accelerate>,
'number_of_cars': 4,
'print_info': <function __main__.print_info>}
```

## Everything is an object
```python
a = 1
a.__class__

int.__class__

a = lambda x: x
a.__class__

import sys
sys.__class__

```
> int <br/>
> type <br/>
> function <br/>
> module

## Methods TODOTODOTODOTODOTODO
```python
class Test(object):
    def __init__(self):
    
    def plop(self):

    def _plop(self):
        # By convention this method should not be accessed from outside the class.
        pass

    def __plop(self):
        https://docs.python.org/2/tutorial/classes.html#private-variables-and-class-local-references
        pass
@classmethod
@staticmethod
@property
@setter
@deleter
Class methods ad static methods and property and setter and deleter (decorator)
```

##Inheritance
###Basics
```python
class Amphibious_Car(Car):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.speed = 0
        self.on_water = self.detect_water()

    def detect_water(self):
        # here implement water detection
        return False
```
This example demonstrates:
 - inheritance from the Car class.
 - Child method creation

```python
print(Amphibious_Car.__bases__)
c = Amphibious_Car("Rinspeed", "Splash")
print(c.on_water)
c.print_info()
```
> `(<class __main__.Car at 0x7f1da93406d0>,)` <br/>
> False <br/>
> I'm a Splash from Rinspeed. <br/>
> There are 7 cars at the moment. #This was not incremented

### New style class
This is a class that inherits from `object`.
```python
Class Something(object):
```

This is done by default in Python3.

"Old-style class" is only retained for backwards compatibility and should not be used.

###Calling parent's method
```python
class Amphibious_Car(Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)
        self.on_water = self.detect_water()

    def detect_water(self):
        # here implement water detection
        return False
```

###Method overriding
```python
class Amphibious_Car(Car):
    def __init__(self, brand, model):
        Car.__init__(self, brand, model)
        self.on_water = self.detect_water()

    def detect_water(self):
        # here implement water detection
        return False

    def accelerate(self):
        if self.on_water:
            self.speed += 2
        else:
            self.speed += 10
```

###`issubclass` & `isinstance`
 - `issubclass(sub, sup)` returns True if _sub_ is a subclass of _sup_
 - `isinstance(obj, Class)` returns True if _obj_ us an instance of _Class_

###Multiple inheritance
```python
class Parent_1(object):
    def __init__(self):
        self.test_1 = True

    def say_1(self):
        print("From Parent_1")

class Parent_2(object):
    def __init__(self):
        self.test_2 = True

    def say_2(self):
        print("From Parent_2")

class Child(Parent_1, Parent_2):
    def __init__(self):
		Parent_1.__init__(self)
		Parent_2.__init__(self)

    def say(self):
        print("From Myself")

print(Child.__bases__)

c = Child()
c.say()
c.say_1()
c.say_2()
```
> `(<class '__main__.Parent_1'>, <class '__main__.Parent_2'>)` <br/>
> From Myself <br/>
> From Parent_1 <br/>
> From Parent_2

Child inherits both from Parent_1 and Parent_2

###Method Resolution Order (MRO)
Methods are resolved in this order:
- Child
- First parent (most left in the class' definition)
- First parent's parents
- Second parent
- Second parent's parents

The MRO for a specific class is accessible through the `__mro__` attribute.
```python
class Class_1(object):
    def say(self):
        print("Class_1")

class Class_2(Class_1):
    def say(self):
        print("Class_2")

class Class_3(object):
    def say(self):
        print("Class_3")

class Class_4(Class_2, Class_3):
    def say(self):
        print("Class_4")

print(Class_4.__mro__)
print(Class_4.__bases__)

c = Class_4()
c.say()
```
> `(<class '__main__.Class_4'>, <class '__main__.Class_2'>, <class '__main__.Class_1'>, <class '__main__.Class_3'>, <class 'object'>)` <br/>
> `(<class '__main__.Class_2'>, <class '__main__.Class_3'>)` <br/>
> Class_4

The sequence is ordered so that a class always appears before its parents, and if there are multiple parents, they keep the same order as the tuple of base classes.
```python
class Class_1(object):
    def say(self):
        print("Class_1")

class Class_2(Class_1):
    def say(self):
        print("Class_2")

class Class_3(Class_1):
    def say(self):
        print("Class_3")

class Class_4(Class_2, Class_3):
    def say(self):
        print("Class_4")

print(Class_4.__mro__)
```
> `(<class '__main__.Class_4'>, <class '__main__.Class_2'>, <class '__main__.Class_3'>, <class '__main__.Class_1'>, <class 'object'>)`

The computation of the MRO uses the _C3 Linearization algorithm_ and if it cannot be defined, an exception is raised.
```python
class A(object): pass
class B(object): pass
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass
```
> TypeError: Cannot create a consistent method resolution order (MRO) for bases B, A

###Super
Super allows you to call methods or get attribute of parent class.
It will locate the requested method or attribute in the parent classes checking them in the MRO order.

Python2:
```python
class base(object):
    def p(self, m):
        print("Base: {}".format(m))

class child(base):
    def p(self, m):
        print("child")
        super(child, self).p(m)

class child_child(child):
    def p(self, m):
        print("child_child")
        super(child_child, self).p(m)

c = child_child()
c.p("a")
```
> child_child <br/>
> child <br/>
> Base: a

Python3 also allows this:
```python
class Base(object):
    def __init__(self):
        print "Base created"

class Child(Base):
    def __init__(self):
        super().__init__()
```

Accessing an attribute:
```python
class base(object):
    plop = 5

class child(base):
    def __init__(self):
        print(super(child, self).plop)
```
> 5

Super also works from outside of the class definition:
```python
class Class_1(object):
    def p(self):
        print("From Class_1")

class Class_2(Class_1):
    def p(self):
        print("From Class_2")

i = Class_2()
i.p()
super(Class_2, i).p()
```
> From Class_2 <br/>
> From Class_1

## The `object`
```python
Out[36]: 
['__class__',
 '__delattr__',
 '__doc__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__']

In [37]: object.__mro__
Out[37]: (object,)

In [38]: object.__mro__
```

##Surcharching operators
