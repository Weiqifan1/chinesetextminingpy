import pytest
import src.Services.textAnalysisDictToMiningDictConverter as Converter
import src.Controllers.appController


def input_jsonSimpNews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "script": "simplified",
      "text": cntext
   }
   return jsondict

def createTestData():
    news = input_jsonSimpNews()
    outputDict = src.Controllers.appController.postendpoint(news)
    output = outputDict["output"]
    return output

def test_convertAnalysisDictToMiningDict():
    analysisDict = createTestData()
    analysisDict = {}
    res = Converter.convertAnalysisDictToMiningDict(analysisDict)
    assert res == {}










