import json

from hex2.domain import ImportData, Loader, Parser, Importer


class JsonLoader(Loader):
    def load(self):
        return open(self.input, 'r')


class JsonParser(Parser):
    def parse(self):
        return json.load(self.data)


class IMDBScoreData(ImportData):
    model = MyDjangoIMDBScoreDataModel
    source = 'imdb'


class IMDBImporter(Importer):
    parser = JsonParser
    loader = JsonLoader

    def get_input(self):
        return 'file.json'
