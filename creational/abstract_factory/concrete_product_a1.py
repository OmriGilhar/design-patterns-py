from creational.abstract_factory.abstract_product_a import AbstractProductGreasy


class ConcreteProductGreasyPizza(AbstractProductGreasy):
    def useful_function_a(self) -> str:
        return "The result of the product A1."
