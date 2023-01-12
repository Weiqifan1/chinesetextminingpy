import pytest
from src.libraryInterface import ChineseLibParser

def test_sentenceToTokens():
   ChineseLibParser.initChineseLibParser()
   sent = "记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相"
   basicTokens = ChineseLibParser.getTokenToPinyinTuplesFromSentence(sent)
   assert basicTokens == [('记者', 'jìzhě'), ('在', 'zài'), ('现场', 'xiànchǎng'), ('获悉', 'huòxī'), (',', ','),
                          ('新', 'Xīn'), ('成', 'Chéng'), ('昆', 'kūn'), ('铁路', 'tiělù'), ('将', 'jiāng'),
                          ('采用', 'cǎiyòng'), ('第', 'dì'), ('三代', 'sāndài'), ('C', 'C'), ('型', 'xíng'),
                          ('CR200J', 'CR200J'), ("'", "'"), ('复兴', 'Fùxīng'), ('号', 'háo'), ("'", "'"),
                          ('动车', 'dòngchē'), ('组', 'Zǔ'), ('值', 'zhí'), ('乘', 'Chéng'), (',', ','), ('这', 'zhè'),
                          ('也', 'Yě'), ('是', 'shì'), ('该', 'gāi'), ('车', 'Chē'), ('型', 'xíng'), ('首次', 'shǒucì'),
                          ('正式', 'zhèngshì'), ('亮相', 'liàngxiàng')]



