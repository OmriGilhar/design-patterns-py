from creational.abstract_factory.abstract_product_a import AbstractProductGreasy


class ConcreteProductGreasyPasta(AbstractProductGreasy):
    def useful_function_a(self) -> str:
        return "The result of the product A2."
