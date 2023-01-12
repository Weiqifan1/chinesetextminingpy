from src.libraryInterface import BcluParser

def test_initBcluDictionary():
    BcluParser.initBCLUDictionary()
    bclu = BcluParser.getBCLUdict()
    assert len(bclu) == 74099
    assert bclu['第'] == ['第', 1, '2002074595']
    assert bclu["踆"] == ['踆', 74099, '25']
