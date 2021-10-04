from abc import ABC, abstractmethod


class ParserCreator(ABC):
    """
    The Creator class declares the factory_method method that is supposed to return an
    object of a Product class. The Creator's subclasses usually provide the
    implementation of this method.
    """

    @abstractmethod
    def parser_factory(self):
        """
        Note that the Creator may also provide some default implementation of
        the factory_method method.
        """
        pass

    def parse(self, file: str) -> str:
        """
        Also note that, despite its name, the Creator's primary responsibility
        is not creating products. Usually, it contains some core business logic
        that relies on Product objects, returned by the factory_method method.
        Subclasses can indirectly change that business logic by overriding the
        factory_method method and returning a different type of product from it.
        """

        # Call the factory_method method to create a Product object.
        parser = self.parser_factory()

        # Now, use the product.
        return parser.parse(file)
