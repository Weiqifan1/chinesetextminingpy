from src.libraryInterface import BlcuParser

def test_initBlcuDictionary():
    BlcuParser.initBLCUDictionary()
    blcu = BlcuParser.getBLCUdict()
    assert len(blcu) == 74099
    assert blcu['第'] == ['第', 1, '2002074595']
    assert blcu["踆"] == ['踆', 74099, '25']
