##Links
 - https://docs.python.org/2/tutorial/classes.html
 - https://www.tutorialspoint.com/python/python_classes_objects.htm
 - https://en.wikipedia.org/wiki/C3_linearization



##To_Read
 - https://docs.python.org/2/tutorial/classes.html
 - https://www.google.co.uk/search?q=python+new+style+class&ie=utf-8&oe=utf-8&gws_rd=cr&ei=VXs4WO-pIoWJmQHIgYP4CQ
 - https://learnpythonthehardway.org/book/ex44.html#
 - https://www.programiz.com/python-programming/inheritance

Super (new style class) Maybe super and MRO in another article
 - https://docs.python.org/2/library/functions.html#super
 - https://fuhm.net/super-harmful/
 - https://rhettinger.wordpress.com/2011/05/26/super-considered-super/
 - http://www.artima.com/weblogs/viewpost.jsp?thread=236275
 - http://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods



##Basics
####Definition of a class
```python
class Car():
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
```

####Accessing attributes and methods
```python
print(car1.brand)
print(car2.brand)
print(Car.number_of_cars)

car1.model = "Test"

car1.print_info()
```
> Renault <br/>
> Bentley <br/>
> 2 <br/>
> I'm a Test from Renault. <br/>
> There are 2 cars at the moment.


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

If any class is duplicated in the MRO, it will be place after all the class that inherit from it.
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

Reality is a bit more complex that this and uses the _C3 Linearization algorithm_.
If the MRO cannot be defined, an exception is raised.
```python
class A(object): pass
class B(object): pass
class X(A, B): pass
class Y(B, A): pass
class Z(X, Y): pass
```
> TypeError: Cannot create a consistent method resolution order (MRO) for bases B, A

####Super

## Private, _ __ ,  ... hiding ...

## New style class
This is a class that inherits from `object`.
```python
Class Something(object):
```

This is done by default in Python3.

"Old-style class" is only retained for backwards compatibility and should not be used.


Here is what is inherithed from the base object

------ > If too much put in another file







## Class methods and static methods and property and setter and deleter (decorator)











-------- MMEMEMOP






# python classes
import datetime
class Employee(object):

    """This is a base class to define employees    as a structure    """

    """Class variables are shared among all instances of this class    """

    company_name = 'HPE'
    number_of_employees = 0
    raise_amount = 1.4

    def __init__(self, first_name, last_name):
        """Initial attributes for the class        """
        self.first_name = first_name
        self.last_name = last_name

        Employee.number_of_employees += 1

    def email(self):
        """This a public function for a class,        we can access this when the class gets        initialized.
        self is the parameter need it to manage instance states
        Returns: email for employee        """
        return "{}.{}@hpe.com".format(self.first_name,
                                      self._compose_last_name())

    def _compose_last_name(self):
        """This is a private method, python doesn't actually enforce it with language constrains        but using a single underscore is the standard by the community
        Returns: last_name separated by "-" in case there are more than 1
        """
        last_name = self.last_name
        if ' ' in last_name:
            last_name = "-".join(last_name.split())
        return last_name

    def __protected_method(self):
        """This is something called mangling and it allows you to avoid naming clashing between classes        and subclasses
        at runtime it gets represented as _classname__protected_method        Returns:
        """
        return self

    def role(self):
        raise NotImplementedError('implement this')


    def company(self):
        return self.company_name

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, employee_string):
        """Class methods takes as a first parameter a class        there is no need to instantiate the class to use this methods.
        and they can be used to construct a class themselves
        Args:            employee_string:
        Returns:
        """
        first, last = employee_string.split('-')
        return cls(first_name=first, last_name=last)

    @staticmethod
    def is_work_day(day):
        """Static methods are like regular methods, they don't accept        self or cls as a parameter, but make sense to include them in the class        if they share some sort of logic.        Args:            day:
        Returns:
        """
        if day.weekday == 5 or day.weekday == 6:
            return False
        return True

class Engineer(Employee):
    """    This is a class that inherits from our base Employee class
    """

    def __init__(self, first_name, last_name, projects):
        """Note that __init__ is not required because python looks on the chain        of inheritance, this is call resolution order.
        type help(Engineer)
        unfortunately we need to write again the same __init__ arguments from the parent class        """
        super(self.__class__, self).__init__(first_name, last_name)
        self.projects = projects

    def role(self):
        return 'Engineer'


class Manager(Employee):
    def role(self):
        return 'Manager'

    def team(self):
        return []

print(Employee.number_of_employees)
# every instance of a class becomes a unique objectemployee_1 = Employee(first_name='juana', last_name='la cubana')employee_2 = Employee(first_name='pepe', last_name='el toro')
print(employee_1)print(employee_2)
print(Employee.number_of_employees)
enginer_1 = Engineer('memo', 'garcia', projects='lol')print(enginer_1.company())
employee_1.company_name = 'Cisco'print(employee_1.company())
print(Employee.number_of_employees)
emp_string_1 = 'memo-garcia'memo = Employee.from_string(emp_string_1)

my_day = datetime.date(2016, 10, 4)print(Employee.is_work_day(my_day))
print(help(Engineer))

# Abstract classesfrom abc import ABCMeta, abstractmethod

class BaseClass(object):
    """When using an abstract class, all of its methods must be used.
    an abstract class cannot be instantiated, just inherit    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def hello(self):
        return 'world!'

#b = BaseClass()#print(b.hello())
class InheritBaseClass(BaseClass):
    def hello(self):
        return 'lol!'
i = InheritBaseClass()print(i.hello())
