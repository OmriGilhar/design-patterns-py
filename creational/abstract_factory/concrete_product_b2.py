from creational.abstract_factory.abstract_product_a import \
    AbstractProductGreasy
from creational.abstract_factory.abstract_product_b import AbstractProductLight


class ConcreteProductLight(AbstractProductLight):
    def useful_function_b(self) -> str:
        return "The result of the product B2."

    def another_useful_function_b(self, collaborator: AbstractProductGreasy):
        """
        The variant, Product B2, is only able to work correctly with the
        variant, Product A2. Nevertheless, it accepts any instance of
        AbstractProductA as an argument.
        """
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with the ({result})"
