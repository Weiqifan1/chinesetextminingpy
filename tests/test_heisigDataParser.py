
from src.libraryInterface import HeisigParser

def test_wordToSimplifiedTrad():
    #given
    HeisigParser.initHeisigParser()
    #when
    trad = HeisigParser.getHeisigTradDict()
    simp = HeisigParser.getHeisigSimpDict()
    kanji = HeisigParser.getHeisigKanjiDict()
    #then
    assert len(trad) == 3035
    assert len(simp) == 3018
    assert len(kanji) == 3030
    assert trad['蓉'] == {'ordinal': 3035, 'char': '蓉', 'meaning': 'cottonrose hibiscus (B)'}
    assert simp['菇'] == {'ordinal': 2996, 'char': '菇', 'meaning': 'mushroom (stem)'}
    assert kanji['廻'] == {'ordinal': 2886, 'char': '廻', 'meaning': 'circling'}





















