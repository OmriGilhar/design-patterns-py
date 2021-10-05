from abc import ABC, abstractmethod
from creational.abstract_factory.abstract_product_a import \
    AbstractProductGreasy


class AbstractProductLight(ABC):
    """
    Here's the the base interface of another product. All products can interact
    with each other, but proper interaction is possible only between
    products of the same concrete variant.
    """
    @abstractmethod
    def useful_function_b(self) -> None:
        """
        Product B is able to do its own thing...
        """
        pass

    @abstractmethod
    def another_useful_function_b(
            self,
            collaborator: AbstractProductGreasy
    ) -> None:
        """
        ...but it also can collaborate with the ProductA.

        The Abstract Factory makes sure that all products it creates are of the
        same variant and thus, compatible.
        """
        pass
