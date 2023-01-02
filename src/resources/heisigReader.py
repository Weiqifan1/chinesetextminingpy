from pathlib import Path

def readHeisigFile():
    base_path = Path(__file__).parent
    finpath = (base_path / "../resources/heisigReader.csv").resolve()
    loktest = open(finpath, "r").read()
    return loktest