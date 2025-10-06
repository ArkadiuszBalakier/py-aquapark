from abc import ABC


class IntegerRange:
    def __init__(self, min_amount: int, max_amount: int) -> None:
        self.min_amount = min_amount
        self.max_amount = max_amount

    def __set_name__(self, owner, age):
        self._age = age

    def __set__(self, instance, value):
        if not hasattr(instance, '_private_data'):
            instance._private_data = {}

        if not isinstance(value, int):
            raise TypeError('Value {value} must be an integer')

        if self.min_amount < value < self.max_amount:
            instance._private_data[self._age]= value
        else:
            raise ValueError(f"Value {value} must be between {self.min_amount} and {self.max_amount}")

class Visitor:
   def __init__(self, name: str, age: int, weight: int, height: int) -> None:
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height


class SlideLimitationValidator(ABC):
    def __init__(self, age: int, weight: int, height: int) -> None:
        self.age = age
        self.weight = weight
        self.height = height


class ChildrenSlideLimitationValidator(SlideLimitationValidator):
    pass


class AdultSlideLimitationValidator(SlideLimitationValidator):
    pass


class Slide:
    pass
