"""Write a Python class, Flower, that has three instance variables of type str,
int, and ﬂoat, that respectively represent the name of the ﬂower, its num-
ber of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type."""

class Flower(object):
    """A class representing a flower object"""
    def __init__(self, name: str, num_petals: int, price: float):
        self._name = name
        self._num_petals = num_petals
        self._price = price

    def get_name(self) -> str:
        """get the name of flower"""
        return self._name

    def set_name(self, name: str) -> None:
        """Set a new flower name"""
        self._name = name

    def get_num_petals(self) -> int:
        """get the number of petals of flower"""
        return self._num_petals

    def set_num_petals(self, num) -> None:
        """change the number of petals of flower"""
        self._num_petals = num

    def get_price(self) -> float:
        """get the price of flower"""
        return self._price

    def set_price(self, price) -> None:
        """set a new price for flower"""
        self._price = price



#test class
if __name__ == '__main__':
    flower = Flower("Rose", 5, 0.02)

    print(flower.get_name()) #Rose
    print(flower.get_num_petals()) #5
    print(flower.get_price()) #0.02

    flower.set_name("Hibiscus")
    flower.set_num_petals(3)
    flower.set_price(0.05)

    print(flower.get_name()) # Hibiscus
    print(flower.get_num_petals()) #3
    print(flower.get_price()) #0.05
