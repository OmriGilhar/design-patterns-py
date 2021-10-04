from creational.factory_method.product import Parser
import yaml
import json


class YAMLParser(Parser):
    def parse(self, file: str) -> str:
        with open(file, "r") as stream:
            data = yaml.safe_load(stream)
        return json.dumps(data, indent=3)
