from pathlib import Path

def readHeisigFile():
    base_path = Path(__file__).parent
    finpath = (base_path / "../resources/heisigReader.csv").resolve()
    loktest = open(finpath, "r", encoding="utf8").read()
    return loktest