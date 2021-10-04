from creational.factory_method.creator import ParserCreator
from creational.factory_method.product import Parser
from creational.factory_method.concrate_product_two import JSONParser


class JSONParserCreator(ParserCreator):
    def parser_factory(self) -> Parser:
        return JSONParser()
