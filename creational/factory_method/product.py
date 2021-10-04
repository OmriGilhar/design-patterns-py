from abc import ABC, abstractmethod


class Parser(ABC):
    """
    The Product interface declares the operations that all concrete products
    must implement.
    """

    @abstractmethod
    def parse(self, file: str) -> str:
        pass
