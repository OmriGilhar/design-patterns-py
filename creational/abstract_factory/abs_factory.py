from abc import ABC, abstractmethod
from creational.abstract_factory.abstract_product_a import \
    AbstractProductGreasy
from creational.abstract_factory.abstract_product_b import AbstractProductLight


class FoodAbstractFactory(ABC):
    """
    The Abstract Factory interface declares a set of methods that return
    different abstract products. These products are called a family and are
    related by a high-level theme or concept. Products of one family are
    usually able to collaborate among themselves. A family of products may
    have several variants, but the products of one variant are incompatible
    with products of another.
    """
    @abstractmethod
    def create_product_greasy(self) -> AbstractProductGreasy:
        pass

    @abstractmethod
    def create_product_light(self) -> AbstractProductLight:
        pass
