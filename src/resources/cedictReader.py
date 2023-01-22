import os
from pathlib import Path


def readCedictFile():
    base_path = Path(__file__).parent
    finpath = (base_path / "../resources/cedict20221227.txt").resolve()
    loktest = open(finpath, "r", encoding="utf8").read()
    return loktest