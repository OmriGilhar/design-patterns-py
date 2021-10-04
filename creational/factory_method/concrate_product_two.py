from creational.factory_method.product import Parser
import json


class JSONParser(Parser):
    def parse(self, file: str) -> str:
        with open(file, 'r') as stream:
            data = json.load(stream)
        return json.dumps(data, indent=3)
