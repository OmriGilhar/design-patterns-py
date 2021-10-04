import os

from creational.factory_method.creator import ParserCreator
from creational.factory_method.concrate_creator_one import YAMLParserCreator
from creational.factory_method.concrate_creator_two import JSONParserCreator

FILES_PATH = './data'


def client_code(parser: ParserCreator, file_to_parse: str) -> None:
    """
    The client code works with an instance of a concrete creator, albeit through
    its base interface. As long as the client keeps working with the creator via
    the base interface, you can pass it any creator's subclass.
    """

    print(f"{parser.parse(file_to_parse)}")


if __name__ == "__main__":
    files = [
        os.path.normpath(
            os.path.join(FILES_PATH, d)
        ) for d in os.listdir(os.path.abspath(FILES_PATH))
    ]

    for file in files:
        if file.endswith('.json'):
            print("App: Launched with the JSONParserCreator.")
            client_code(JSONParserCreator(), file)
        if file.endswith('.yaml'):
            print("App: Launched with the YAMLParserCreator.")
            client_code(YAMLParserCreator(), file)
