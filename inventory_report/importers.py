from inventory_report.product import Product
from abc import ABC, abstractmethod
from typing import Dict, List, Type
import json
import csv


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> List[Product]:
        pass


class CsvImporter(Importer):
    def import_data(self) -> List[Product]:
        novo_arquivo = list()

        with open(self.path) as arquivo:
            pdt = csv.DictReader(arquivo)

            for x in pdt:
                novo_arquivo.append(Product(**x))

        return novo_arquivo


class JsonImporter(Importer):
    def import_data(self) -> List[Product]:
        novo_arquivo = list()

        with open(self.path) as arquivo:
            pdt = json.load(arquivo)

        for x in pdt:
            novo_arquivo.append(Product(**x))

        return novo_arquivo


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
