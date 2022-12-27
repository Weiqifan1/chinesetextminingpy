import pytest
import json
import src.appController

@pytest.fixture
def input_value():
   input = 39
   return input


def input_defaultjson():
   my_json_string = """{
       "text": "lykke"
   }"""
   return my_json_string#json.loads(my_json_string)

#@pytest.fixture
def input_jsonhagrid():
   # https://mychinesereading.com/hagrids-introduction/
   cntext = """轰！ 又是捶门声。 达力惊醒了。 ‘什么地方打抢?’ 达力迷迷糊糊地说。 他们背后又是哗啦一声响。弗农姨父抢着一支来复枪连滚带爬地跑进屋， 这时他们才明白他那细长的包裹里原来是什么东西。 ‘门外是什么人？’ 他喊道，‘ 我警告你—-我有枪！’ 外面静了一会儿。 然后—咔嚓门从合页上脱落下来， 震耳欲聋的哗啦一声， 门板摔在地上。"""
   jsondict = {
      "text": cntext
   }
   return jsondict


#@pytest.fixture
def input_jsonnews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "text": cntext
   }
   return jsondict

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 3

def test_appController_postendpoint():
   news = input_jsonnews()
   output = src.appController.postendpoint(news)

   res = ['12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验',
          "记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相",
          "据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间",
          "此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行"]

   assert len(output) == 4
   firstElem = output[0]
   assert firstElem.get("sentence") == '12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验'
   assert firstElem.get("rawTokens") == ['12', '月', '23', '日', ',', ' ', '中国', '铁路', '成都', '局', '集团公司', '组织', '媒体', '提前', '试乘', '新', '成昆铁路', ',', ' ', '感受', '即将', '到来', '的', '时空', '新体验']
   assert firstElem.get("wordToPinyinTuples") == [('12', '12'), ('月', 'yuè'), ('23', '23'), ('日', 'Rì'), (',', ','),
                                                  ('中国', 'Zhōngguó'), ('铁路', 'tiělù'), ('成都', 'Chéngdū'), ('局', 'jú'),
                                                  ('集团', 'jítuán'), ('公司', 'gōngsī'), ('组织', 'zǔzhī'), ('媒体', 'méitǐ'),
                                                  ('提前', 'tíqián'), ('试乘', 'shìchéng'), ('新', 'Xīn'), ('成', 'Chéng'),
                                                  ('昆', 'kūn'), ('铁路', 'tiělù'), (',', ','), ('感受', 'gǎnshòu'), ('即将', 'jíjiāng'),
                                                  ('到来', 'dàolái'), ('的', 'de'), ('时空', 'shíkōng'), ('新', 'Xīn'), ('体验', 'tǐyàn')]
   thirdElem = output[2]
   assert thirdElem.get("sentence") == " 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间"
   assert thirdElem.get("rawTokens") == [' ', '据介绍', ',', ' ', '第三代', 'C', '型', 'CR200J', "'", '复兴号', "'", '动车组', '为', '9', '节车厢', ',',
                                         ' ', '较', '第二代', "'", '绿巨人', "'", '增加', '了', '商务', '座', ',', ' ', '旋转', '座椅', '等', ',', ' ', '外形', '涂装', '为', '绿白', '相间']
   assert thirdElem.get("wordToPinyinTuples") == [('据', 'jù'), ('介绍', 'jièshào'), (',', ','), ('第', 'dì'), ('三代', 'sāndài'),
                                                  ('C', 'C'), ('型', 'xíng'), ('CR200J', 'CR200J'), ("'", "'"), ('复兴', 'Fùxīng'),
                                                  ('号', 'háo'), ("'", "'"), ('动车', 'dòngchē'), ('组', 'Zǔ'), ('为', 'wéi'),
                                                  ('9', '9'), ('节', 'jiē'), ('车厢', 'chēxiāng'), (',', ','), ('较', 'jiào'),
                                                  ('第二', 'dìèr'), ('代', 'dài'), ("'", "'"), ('绿', '绿'), ('巨人', 'jùrén'),
                                                  ("'", "'"), ('增加', 'zēngjiā'), ('了', 'le'), ('商务', 'shāngwù'), ('座', 'zuò'),
                                                  (',', ','), ('旋转', 'xuánzhuǎn'), ('座椅', 'zuòyǐ'), ('等', 'děng'), (',', ','),
                                                  ('外形', 'wàixíng'), ('涂装', 'túzhuāng'), ('为', 'wéi'), ('绿', '绿'), ('白', 'Bái'), ('相间', 'xiāngjiàn')]


