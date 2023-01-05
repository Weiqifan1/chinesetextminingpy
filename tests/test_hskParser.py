import pytest
from src.libraryInterface import CedictParser
from src.libraryInterface import HskParser
from src.resources import hskReader
import json

def test_initBcluDictionary():
    bclu = HskParser.init_bcluDictionary()
    assert len(bclu) == 74099
    assert bclu['第'] == ['第', 1, '2002074595']
    assert bclu["踆"] == ['踆', 74099, '25']

def test_initHskParser():
    #given
    HskParser.initHskParser()
    #when
    simp = HskParser.getHskSimpDict()

    #then
    assert len(simp) == 6
    assert len(simp.get('hsk1')) == 150
    assert len(simp.get('hsk2')) == 151
    assert len(simp.get('hsk3')) == 300
    assert len(simp.get('hsk4')) == 600
    assert len(simp.get('hsk5')) == 1300
    assert len(simp.get('hsk6')) == 2500
    assert '殖民地' in simp.get('hsk6')





