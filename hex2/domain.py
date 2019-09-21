from django.db import models


class ImportData:
    model: models.Model
    source: str


class Loader:
    def __init__(self, input):
        self.input = input

    def load(self):
        return self.input


class Parser:
    def __init__(self, data):
        self.data = data

    def parse(self):
        return self.data


class Importer:
    parser = None
    loader = None

    def create_instance_from_data(self, import_data):
        loader = self.loader(self.get_input())
        raw_data = loader.load()
        parser = self.parser(raw_data)
        data = parser.parse()
        return self.import_data.model(**data)

    def get_input(self):
        raise NotImplementedError