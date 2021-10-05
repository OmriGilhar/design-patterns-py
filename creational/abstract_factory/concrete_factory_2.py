from creational.abstract_factory.abs_factory import AbstractFactory
from creational.abstract_factory.abstract_product_a import AbstractProductGreasy
from creational.abstract_factory.abstract_product_b import AbstractProductLight
from creational.abstract_factory.concrete_product_a2 import \
    ConcreteProductGreasyPasta
from creational.abstract_factory.concrete_product_b2 import \
    ConcreteProductLight


class ConcreteHutFactory(AbstractFactory):
    """
    Each Concrete Factory has a corresponding product variant.
    """

    def create_product_greasy(self) -> AbstractProductGreasy:
        return ConcreteProductGreasyPasta()

    def create_product_light(self) -> AbstractProductLight:
        return ConcreteProductLight()
