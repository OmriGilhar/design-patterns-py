from creational.factory_method.creator import ParserCreator
from creational.factory_method.product import Parser
from creational.factory_method.concrate_product_one import YAMLParser

"""
Concrete Creators override the factory_method method in order to change the resulting
product's type.
"""


class YAMLParserCreator(ParserCreator):
    """
    Note that the signature of the method still uses the abstract product type,
    even though the concrete product is actually returned from the method. This
    way the Creator can stay independent of concrete product classes.
    """
    def parser_factory(self) -> Parser:
        return YAMLParser()
