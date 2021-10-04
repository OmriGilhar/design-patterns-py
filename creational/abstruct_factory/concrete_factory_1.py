from creational.abstruct_factory.abs_factory import AbstractFactory
from creational.abstruct_factory.abstract_product_a import AbstractProductA
from creational.abstruct_factory.abstract_product_b import AbstractProductB
from creational.abstruct_factory.concrete_product_a1 import ConcreteProductA1
from creational.abstruct_factory.concrete_product_b1 import ConcreteProductB1


class ConcreteFactory1(AbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible. Note
    that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()
