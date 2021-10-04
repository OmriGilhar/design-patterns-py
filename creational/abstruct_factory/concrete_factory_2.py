from creational.abstruct_factory.abs_factory import AbstractFactory
from creational.abstruct_factory.abstract_product_a import AbstractProductA
from creational.abstruct_factory.abstract_product_b import AbstractProductB
from creational.abstruct_factory.concrete_product_a2 import ConcreteProductA2
from creational.abstruct_factory.concrete_product_b2 import ConcreteProductB2


class ConcreteFactory2(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()
