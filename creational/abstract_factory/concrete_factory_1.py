from creational.abstract_factory.abs_factory import FoodAbstractFactory
from creational.abstract_factory.abstract_product_a import \
    AbstractProductGreasy
from creational.abstract_factory.abstract_product_b import AbstractProductLight
from creational.abstract_factory.concrete_product_a1 import \
    ConcreteProductGreasyPizza
from creational.abstract_factory.concrete_product_b1 import \
    ConcreteProductLight


class ConcreteDominosFactoryFood(FoodAbstractFactory):
    """
    Concrete Factories produce a family of products that belong to a single
    variant. The factory guarantees that resulting products are compatible.
    Note that signatures of the Concrete Factory's methods return an abstract
    product, while inside the method a concrete product is instantiated.
    """

    def create_product_greasy(self) -> AbstractProductGreasy:
        return ConcreteProductGreasyPizza()

    def create_product_light(self) -> AbstractProductLight:
        return ConcreteProductLight()
