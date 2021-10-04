from creational.abstruct_factory.abstract_product_a import AbstractProductA


class ConcreteProductA1(AbstractProductA):
    def useful_function_a(self) -> str:
        return "The result of the product A1."
