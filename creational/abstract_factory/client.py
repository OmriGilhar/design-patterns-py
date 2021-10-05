from creational.abstract_factory.abs_factory import FoodAbstractFactory
from creational.abstract_factory.concrete_factory_1 import \
    ConcreteDominosFactoryFood
from creational.abstract_factory.concrete_factory_2 import \
    ConcreteHutFactoryFood


def client_code(pizza_provider: FoodAbstractFactory) -> None:
    """
    The client code works with factories and products only through abstract
    types: AbstractFactory and AbstractProduct. This lets you pass any factory
    or product subclass to the client code without breaking it.
    """
    greasy_product = pizza_provider.create_product_greasy()
    light_product = pizza_provider.create_product_light()

    print(f"{light_product.useful_function_b()}")
    print(f"{light_product.another_useful_function_b(greasy_product)}", end="")


if __name__ == "__main__":
    """
    The client code can work with any concrete factory class.
    """
    print("Client: Testing client code with the first factory type:")
    client_code(ConcreteDominosFactoryFood())

    print("\n")

    print("Client: Testing the same client code with the second factory type:")
    client_code(ConcreteHutFactoryFood())
