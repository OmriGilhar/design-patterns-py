from creational.abstract_factory.abstract_product_a import \
    AbstractProductGreasy
from creational.abstract_factory.abstract_product_b import AbstractProductLight


class ConcreteProductLight(AbstractProductLight):
    def useful_function_b(self) -> str:
        return "The result of the product B1."

    """
    The variant, Product B1, is only able to work correctly with the variant,
    Product A1. Nevertheless, it accepts any instance of AbstractProductA as an
    argument.
    """

    def another_useful_function_b(
            self,
            collaborator: AbstractProductGreasy
    ) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with the ({result})"
