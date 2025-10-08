'''
Magic methods. Task 3 
 Description 
Implement class Currency and inherited classes Euro, Dollar, Pound. Course is 1 EUR == 2 USD == 100 GBP 
You need to implement the following methods: 
course - classmethod which returns string in the following pattern: {float value} {currency to} for 1 {currency for} 
>>> print(
f"Euro.course(Pound) ==> {Euro.course(Pound)}\n"
f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
f"Pound.course(Euro) ==> {Pound.course(Euro)}\n"
)
Euro.course(Pound) ==> 100.0 GBP for 1 EUR
Dollar.course(Pound) ==> 50.0 GBP for 1 USD
Pound.course(Euro) ==> 0.01 EUR for 1 GBP
 to_currency - method transforms currency from one currency to another. Method should return instance of a required currency. 
>>> e = Euro(100)
>>> r = Pound(100)
>>> d = Dollar(200)
  >>> print(
f"e = {e}\n"
f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
f"e.to_currency(Euro) = {e.to_currency(Euro)}\n"
)
e = 100 EUR
e.to_currency(Dollar) = 200.0 USD # Dollar instance printed
e.to_currency(Pound) = 10000.0 GBP # Pound instance printed
e.to_currency(Euro) = 100.0 EUR # Euro instance printed
  >>> print(
f"r = {r}\n"
f"r.to_currency(Dollar) = {r.to_currency(Dollar)}\n"
f"r.to_currency(Euro) = {r.to_currency(Euro)}\n"
f"r.to_currency(Pound) = {r.to_currency(Pound)}\n"
)
r = 100 GBP
r.to_currency(Dollar) = 2.0 USD # Dollar instance printed
r.to_currency(Euro) = 1.0 EUR # Euro instance printed
r.to_currency(Pound) = 100.0 GBP # Pound instance printed
 + - returns an instance of a new value 
>>> e = Euro(100)
>>> r = Pound(100)
>>> d = Dollar(200)
>>> print(
f"e + r => {e + r}\n"
f"r + d => {r + d}\n"
f"d + e => {d + e}\n"
)
e + r => 101.0 EUR # Euro instance printed
r + d => 10100.0 GBP # Pound instance printed
d + e => 400.0 USD # Dollar instance printed
 other comparison methods: > < == 
'''
from __future__ import annotations
from typing import Type


class Currency:
    # conversion base in EUR equivalents
    _to_eur = {
        "EUR": 1.0,
        "USD": 0.5,   # 1 USD = 0.5 EUR
        "GBP": 0.01   # 1 GBP = 0.01 EUR
    }

    _code_map = {
        "Euro": "EUR",
        "Dollar": "USD",
        "Pound": "GBP",
    }

    def __init__(self, value: float):
        self.value = float(value)

    @classmethod
    def _get_code(cls) -> str:
        """Return ISO code for the class."""
        return cls._code_map[cls.__name__]

    @property
    def code(self) -> str:
        return self.__class__._get_code()

    def __str__(self):
        return f"{self.value} {self.code}"

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        from_code = cls._get_code()
        to_code = other_cls._get_code()
        value_in_eur = 1 * cls._to_eur[from_code]
        result = value_in_eur / cls._to_eur[to_code]
        return f"{result} {to_code} for 1 {from_code}"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        from_code = self.code
        to_code = other_cls._get_code()
        value_in_eur = self.value * self._to_eur[from_code]
        converted_value = value_in_eur / self._to_eur[to_code]
        return other_cls(converted_value)

    def __add__(self, other: Currency) -> Currency:
        if not isinstance(other, Currency):
            return NotImplemented
        other_converted = other.to_currency(self.__class__)
        return self.__class__(self.value + other_converted.value)

    def __eq__(self, other: Currency) -> bool:
        return self._to_eur[self.code] * self.value == self._to_eur[other.code] * other.value

    def __lt__(self, other: Currency) -> bool:
        return self._to_eur[self.code] * self.value < self._to_eur[other.code] * other.value

    def __gt__(self, other: Currency) -> bool:
        return self._to_eur[self.code] * self.value > self._to_eur[other.code] * other.value


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass


