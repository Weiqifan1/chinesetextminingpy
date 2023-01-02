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
   return my_json_string

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
   assert firstElem.get("traditional") == ['12', '月', '23', '日', ',', '中國', '鐵路', '成都', '侷|局', '集團', '公司', '組織', '媒體', '提前', '試乘', '新', '成', '昆|崑|崐', '鐵路', ',', '感受', '即將', '到來', '的', '時空', '新', '體驗']
   assert len(firstElem.get("pinyin")) == 27
   assert firstElem.get("pinyin") == ['12', 'Yue4', '23', 'Ri4', ',', 'Zhong1Guo2', 'Tie3Lu4', 'Cheng2Du1', 'Ju2', 'Ji2Tuan2', 'Gong1Si1', 'Zu3Zhi1', 'Mei2Ti3', 'Ti2Qian2', 'Shi4Cheng2', 'Xin1', 'Cheng2', 'Kun1', 'Tie3Lu4', ',', 'Gan3Shou4', 'Ji2Jiang1', 'Dao4Lai2', 'De5', 'Shi2Kong1', 'Xin1', 'Ti3Yan4']
   assert len(firstElem.get("meaning")) == 27
   assert firstElem.get("meaning") == ['12', '/moon/month/monthly/CL:個|个[ge4],輪|轮[lun2]/', '23', '/abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/', ',', '/China/', '/railroad/railway/CL:條|条[tiao2]/', '/Chengdu subprovincial city and capital of Sichuan province 四川 in southwest China/', '/narrow/|/office/situation/classifier for games: match, set, round etc/', '/group/bloc/corporation/conglomerate/', '/company; firm; corporation/CL:家[jia1]/', '/to organize/organization/(biology) tissue/(textiles) weave/CL:個|个[ge4]/', '/media, esp. news media/', '/to shift to an earlier date/to do sth ahead of time/in advance/', '/test drive/', '/new/newly/meso- (chemistry)/|/abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/', '/surname Cheng/|/to succeed/to finish/to complete/to accomplish/to become/to turn into/to be all right/OK!/one tenth/', '/descendant/elder brother/a style of Chinese poetry/|/used in place names, notably Kunlun Mountains 崑崙|昆仑[Kun1 lun2]/(also used for transliteration)/|/variant of 崑|昆[kun1]/', '/railroad/railway/CL:條|条[tiao2]/', ',', '/to sense/perception/to feel (through the senses)/to experience/a feeling/an impression/an experience/', '/on the eve of/to be about to/to be on the verge of/', '/to arrive/arrival; advent/', "/aim/clear/|/see 的士[di1 shi4]/|/really and truly/|/of/~'s (possessive particle)/(used after an attribute)/(used to form a nominal expression)/(used at the end of a declarative sentence for emphasis)/also pr. [di4] or [di5] in poetry and songs/", '/time and place/world of a particular locale and era/(physics) space-time/', '/new/newly/meso- (chemistry)/|/abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/', '/to experience for oneself/']
   assert len(firstElem.get("heisigSimplified")) == 27
   assert firstElem.get("heisigSimplified") == ['', '13 月 month', '', '12 日 day', '', '38 中 middle 549 国 country', '730 铁 iron 1053 路 path', '368 成 turn into 1383 都 metropolis', '893 局 bureau', '538 集 gather 622 团 troupe', '696 公 public 1391 司 take charge of', '1347 组 group 1082 织 weave', '2732 媒 matchmaker 813 体 body', '598 提 bring up 303 前 in front', '360 试 test 1706 乘 hitch a ride', '1191 新 new', '368 成 turn into', '457 昆 descendants', '730 铁 iron 1053 路 path', '', '576 感 feel 667 受 accept', '1148 即 immediately 244 将 General', '680 到 arrive 783 来 come', "70 的 'bull''s eye'", '168 时 time 1075 空 empty', '1191 新 new', '813 体 body 1457 验 check']
   assert len(firstElem.get("heisigSimpInt")) == 27
   assert firstElem.get("heisigSimpInt") == [set(), {13}, set(), {12}, set(), {549, 38}, {730, 1053}, {368, 1383}, {893}, {538, 622}, {696, 1391}, {1082, 1347}, {2732, 813}, {598, 303}, {360, 1706}, {1191}, {368}, {457}, {730, 1053}, set(), {576, 667}, {1148, 244}, {680, 783}, {70}, {168, 1075}, {1191}, {1457, 813}]
   assert len(firstElem.get("heisigTraditional")) == 27
   assert firstElem.get("heisigTraditional") == ['', '13 月 month', '', '12 日 day', '', '36 中 middle 516 國 country', '339 鐵 iron 976 路 path', '341 成 turn into 1340 都 metropolis', '829 局 bureau', '502 集 gather 1471 團 troupe', '643 公 public 1348 司 take charge of', '1299 組 group 1020 織 weave', '2665 媒 matchmaker 1070 體 body', '563 提 bring up 277 前 in front', '334 試 test 1678 乘 hitch a ride', '1123 新 new', '341 成 turn into', '423 昆 descendants', '339 鐵 iron 976 路 path', '', '540 感 feel 617 受 accept', '1087 即 immediately 920 將 General', '628 到 arrive 789 來 come', "66 的 'bull''s eye'", '156 時 time 998 空 empty', '1123 新 new', '1070 體 body 1419 驗 check']
   assert len(firstElem.get("heisigTradInt")) == 27
   assert firstElem.get("heisigTradInt") == [set(), {13}, set(), {12}, set(), {36}, {976}, {1340, 341}, {829}, {502}, {643, 1348}, set(), {2665}, {563, 277}, {1678}, {1123}, {341}, {423}, {976}, set(), {617, 540}, {1087}, {628}, {66}, {998}, {1123}, set()]


