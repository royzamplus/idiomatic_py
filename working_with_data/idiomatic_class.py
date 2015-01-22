#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Use the isinstance function to determine the type of an object
def get_size(some_object):
    if isinstance(some_object, (list, dict, str, tuple)):
        return len(some_object)
    elif isinstance(some_object, (bool, type(None))):
        return 1
    elif isinstance(some_object, (int, float)):
        return int(some_object)

print(get_size('hello'))
print(get_size([1, 2, 3, 4, 5]))
print(get_size(10.0))

# Use leading underscores in function and variable names to denote ''private'' data
class Foo(object):
    def __init__(self):
        """Since 'id' is of vital importance to us, we don't
        want a derived class accidentally overwriting it. We'll
        prepend with double underscores to introduce name
        mangling.
        """
        self.__id = 8
        self.value = self.__get_value()  # Call our 'private copy'

    def get_value(self):
        pass

    def should_destroy_earth(self):
        return self.__id == 42

    # Here, we're storing a 'private copy' of get_value,
    # and assigning it to '__get_value'. Even if a derived
    # class overrides get_value in a way incompatible with
    # ours, we're fine
    __get_value = get_value

class Baz(Foo):
    def get_value(self, some_new_parameter):
        pass

class Qux(Foo):
    def __init__(self):
        """Now when we set 'id' to 42, it's not the same 'id'
        that 'should_destroy_earth' is concerned with. In fact,
        if you inspect a Qux object, you'll find it doesn't
        have an __id attribute. So we can't mistakenly change
        Foo's __id attribute even if we wanted to.
        """
        self.id = 42
        # No relation to Foo's id, purely coincidental
        super(Qux, self).__init__()

q = Qux()
b = Baz()  # Works fine now
q.should_destroy_earth()  # returns False
q.id == 42  # returns True

# Use properties to ''future-proof'' your class implementation
class Product(object):
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        # now if we need to change how price is calculated, we can do it
        # here (or in the "setter" and __init__)
        return self._price * TAX_RATE

    @price.setter
    def price(self, value):
        # The "setter" function must have the same name as the property
        self._price = value

# Use __repr__ for a machine-readable representation of a class
class Foo(object):
    def __init__(self, bar=10, baz=12, cache=None):
        self.bar = bar
        self.baz = baz
        self._cache = cache or {}

    def __str__(self):
        return '{}, {}'.format(self.bar, self.baz)
    
    def __repr__(self):
        return 'Foo({}, {}, {})'.format(self.bar, self.baz, self._cache)

def log_to_console(instance):
    print(instance)

log_to_console([Foo(), Foo(cache={'x': 'y'})])

# Define __str__ in a class to show a human-readable representation
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '{0}, {1}'.format(self.x, self.y)

p = Point(1, 2)
print(p)
