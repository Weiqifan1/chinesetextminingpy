from src.libraryInterface import HskParser

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





