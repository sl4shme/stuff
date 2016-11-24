##Links
 -

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
> (\<class __main__.Car at 0x7f1da93406d0>,) <br/>
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

###Multiple inheritance

####`issubclass` & `isinstance`

####Super

## The `object` base class

## Private, _ __ ,  ... hiding ...
