from enum import Enum


class EmailCategory(str, Enum):
    PRODUCTIVE = "Produtivo"
    UNPRODUCTIVE = "Improdutivo"