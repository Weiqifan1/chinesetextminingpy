import pytest
import src.Controllers.appController

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

def test_appController_postendpoint():
   news = input_jsonnews()
   output = src.Controllers.appController.postendpoint(news)

   assert len(output) == 4
   firstElem = output[0]
   assert firstElem.get("sentence") == '12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验'
   assert len(firstElem.get("tokens")) == 27
   assert firstElem.get("tokens") == ['12', '月', '23', '日', ',', '中国', '铁路', '成都', '局', '集团', '公司', '组织', '媒体', '提前', '试乘', '新', '成', '昆', '铁路', ',', '感受', '即将', '到来', '的', '时空', '新', '体验']
   assert len(firstElem.get("simplified")) == 27
   assert firstElem.get("simplified") == ['12', '月', '23', '日', ',', '中国', '铁路', '成都', '局', '集团', '公司', '组织', '媒体', '提前', '试乘', '新', '成', '昆', '铁路', ',', '感受', '即将', '到来', '的', '时空', '新', '体验']
   assert len(firstElem.get("traditional")) == 27
   assert firstElem.get("traditional") == ['12', '月', '23', '日', ',', '中國', '鐵路', '成都', '侷|局', '集團', '公司', '組織', '媒體', '提前', '試乘', '新', '成', '崐|昆|崑', '鐵路', ',', '感受', '即將', '到來', '的', '時空', '新', '體驗']
   assert len(firstElem.get("pinyin")) == 27
   assert firstElem.get("pinyin") == ['12', 'Yue4', '23', 'Ri4', ',', 'Zhong1_Guo2', 'Tie3_Lu4', 'Cheng2_Du1', 'Ju2', 'Ji2_Tuan2', 'Gong1_Si1', 'Zu3_Zhi1', 'Mei2_Ti3', 'Ti2_Qian2', 'Shi4_Cheng2', 'Xin1', 'Cheng2', 'Kun1', 'Tie3_Lu4', ',', 'Gan3_Shou4', 'Ji2_Jiang1', 'Dao4_Lai2', 'Di4|Di2|Di1|De5', 'Shi2_Kong1', 'Xin1', 'Ti3_Yan4']
   assert len(firstElem.get("meaning")) == 27
   assert firstElem.get("meaning") == ['12', '/moon/month/monthly/CL:個|个[ge4],輪|轮[lun2]/', '23', '/abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/', ',', '/China/', '/railroad/railway/CL:條|条[tiao2]/', '/Chengdu subprovincial city and capital of Sichuan province 四川 in southwest China/', '/narrow/|/office/situation/classifier for games: match, set, round etc/', '/group/bloc/corporation/conglomerate/', '/company; firm; corporation/CL:家[jia1]/', '/to organize/organization/(biology) tissue/(textiles) weave/CL:個|个[ge4]/', '/media, esp. news media/', '/to shift to an earlier date/to do sth ahead of time/in advance/', '/test drive/', '/new/newly/meso- (chemistry)/|/abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/', '/surname Cheng/|/to succeed/to finish/to complete/to accomplish/to become/to turn into/to be all right/OK!/one tenth/', '/variant of 崑|昆[kun1]/|/descendant/elder brother/a style of Chinese poetry/|/used in place names, notably Kunlun Mountains 崑崙|昆仑[Kun1 lun2]/(also used for transliteration)/', '/railroad/railway/CL:條|条[tiao2]/', ',', '/to sense/perception/to feel (through the senses)/to experience/a feeling/an impression/an experience/', '/on the eve of/to be about to/to be on the verge of/', '/to arrive/arrival; advent/', "/aim/clear/|/really and truly/|/see 的士[di1 shi4]/|/of/~'s (possessive particle)/(used after an attribute)/(used to form a nominal expression)/(used at the end of a declarative sentence for emphasis)/also pr. [di4] or [di5] in poetry and songs/", '/time and place/world of a particular locale and era/(physics) space-time/', '/new/newly/meso- (chemistry)/|/abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/', '/to experience for oneself/']



