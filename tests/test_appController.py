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
   json_chinese_hagrid = """{
       "text": "轰！ 又是捶门声。 达力惊醒了。 ‘什么地方打抢?’ 达力迷迷糊糊地说。 他们背后又是哗啦一声响。弗农
       姨父抢着一支来复枪连滚带爬地跑进屋， 这时他们才明白他那细长的包裹里原来是什么东西。 ‘门外是什么人？’ 
       他喊道，‘ 我警告你—-我有枪！’ 外面静了一会儿。 然后—咔嚓门从合页上脱落下来， 震耳欲聋的哗啦一声， 门板摔在地上。"
   }"""
   return json_chinese_hagrid #json.loads(json_chinese_hagrid)

#@pytest.fixture
def input_jsonnews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   json_chinese_newsparagraph = """{
       "text": "12月23日
       ，中国铁路成都局集团公司组织媒体提前试乘新成昆铁路，感受即将到来的时空新体验。记者在现场获悉，
       新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘，这也是该车型首次正式亮相。 据介绍，
       第三代C型CR200J'复兴号'动车组为9节车厢，较第二代'绿巨人'增加了商务座、旋转座椅等，
       外形涂装为绿白相间。此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组，将全部用于新成昆铁路开行。"
   }"""
   return json_chinese_newsparagraph #json.loads(json_chinese_newsparagraph)

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0

def test_divisible_by_6(input_value):
   assert input_value % 6 == 3

def test_appController_postendpoint():
   news = input_jsonnews()#input_defaultjson()#input_jsonnews()
   output = src.appController.postendpoint(news)

   booleanTrue = output == news
   assert booleanTrue


#def test_appController_postendpoint():


#def test_correct():
#    assert src.appController.postendpoint(to_python) == to_python