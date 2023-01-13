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

def input_jsonSimpNews_missingScript():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "text": cntext
   }
   return jsondict



def input_jsonSimpNews_missingText():
   jsondict = {
      "script": "simplified"
   }
   return jsondict


def input_jsonSimpNews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "script": "simplified",
      "text": cntext
   }
   return jsondict
#skriv en test der tester at det ikke er markeret om undertekster er simplificerede eller traditionelle

def input_jsonTradNews():
   # https://www.taiwannews.com.tw/ch/news/4779971
   cntext = """竹北市戶政事務所12日湧入大量人潮，碼牌抽到1297號，多是為辦遷入戶籍作業。

鄭朝方12日接受媒體聯訪表示，民生紓困金是為減緩疫情帶來的經濟衝擊，所以未設定門檻條件，12日通過提案的自治條例，是以1月12日（含當日）前設籍於竹北市，即符合領取資格，但民眾若在發放紓困金前移出，會被取消資格。"""
   jsondict = {
      "script": "traditional",
      "text": cntext
   }
   return jsondict

def test_appController_postendpoint_traditional():
   news = input_jsonTradNews()
   outputDict = src.Controllers.appController.postendpoint(news)
   output = outputDict["output"]
   assert len(output) == 2
   firstElem = output[0]
   assert firstElem.get("sentence") == '竹北市戶政事務所12日湧入大量人潮，碼牌抽到1297號，多是為辦遷入戶籍作業'
   assert len(firstElem.get("tokens")) == 26
   assert firstElem.get("tokens") == ['竹北', '市', '戶', '政事', '務', '所', '12', '日', '湧入', '大量', '人潮', '，', '碼', '牌', '抽', '到', '1297', '號', '，', '多', '是', '為', '辦', '遷入', '戶籍', '作業']
   assert len(firstElem.get("simplified")) == 26
   assert firstElem.get("simplified") == ['竹北', '市', '户', '政事', '务', '所', '12', '日', '涌入', '大量', '人潮', '，', '码', '牌', '抽', '到', '1297', '号', '，', '多', '是', '为', '办', '迁入', '户籍', '作业']
   assert len(firstElem.get("traditional")) == 26
   assert firstElem.get("traditional") == ['竹北', '市', '戶', '政事', '務', '所', '12', '日', '湧入', '大量', '人潮', '，', '碼', '牌', '抽', '到', '1297', '號', '，', '多', '是', '為', '辦', '遷入', '戶籍', '作業']
   assert len(firstElem.get("pinyin")) == 26
   assert firstElem.get("pinyin") == ['Zhu2Bei3', 'Shi4', 'Hu4', 'Zheng4Shi4', 'Wu4', 'Suo3', '12', 'Ri4', 'Yong3Ru4', 'Da4Liang4', 'Ren2Chao2', '，', 'Ma3', 'Pai2', 'Chou1', 'Dao4', '1297', 'Hao2|Hao4', '，', 'Duo1', 'Shi4', 'Wei4|Wei2', 'Ban4', 'Qian1Ru4', 'Hu4Ji2', 'Zuo4Ye4']
   assert len(firstElem.get("meaning")) == 26
   assert firstElem.get("meaning") == ['/Zhubei or Chupei city in Hsinchu County 新竹縣|新竹县[Xin1 zhu2 Xian4], northwest Taiwan/', '/market/city/CL:個|个[ge4]/', '/a household/door/family/', '/politics/government affairs/', '/affair/business/matter/to be engaged in/to attend to/by all means/', '/actually/place/classifier for houses, small buildings, institutions etc/that which/particle introducing a relative clause or passive/CL:個|个[ge4]/', '12', '/abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/', '/to come pouring in/influx/', '/great amount/large quantity/bulk/numerous/generous/magnanimous/', '/a tide of people/', '，', '/weight/number/code/to pile/to stack/classifier for length or distance (yard), happenings etc/', '/mahjong tile/playing card/game pieces/signboard/plate/tablet/medal/CL:片[pian4],個|个[ge4],塊|块[kuai4]/', '/to draw out/to pull out from in between/to remove part of the whole/(of certain plants) to sprout or bud/to whip or thrash/', '/to (a place)/until (a time)/up to/to go/to arrive/(verb complement denoting completion or result of an action)/', '1297', '/roar/cry/CL:個|个[ge4]/|/ordinal number/day of a month/mark/sign/business establishment/size/ship suffix/horn (wind instrument)/bugle call/assumed name/to take a pulse/classifier used to indicate number of people/', '，', '/many/much/often/a lot of/numerous/more/in excess/how (to what extent)/multi-/Taiwan pr. [duo2] when it means "how"/', '/is/are/am/yes/to be/', '/because of/for/to/|/as (in the capacity of)/to take sth as/to act as/to serve as/to behave as/to become/to be/to do/by (in the passive voice)/', '/to do/to manage/to handle/to go about/to run/to set up/to deal with/', '/to move in (to new lodging)/', '/census register/household register/', '/school assignment/homework/work/task/operation/CL:個|个[ge4]/to operate/']
   assert len(firstElem.get("hskLevel")) == 26
   assert firstElem.get("hskLevel") == ['', '', '', '', '', 'hsk5', '', 'hsk2', '', '', '', '', '', '', '', 'hsk2', '', 'hsk1', '', 'hsk1', 'hsk1', 'hsk3', '', '', '', 'hsk3']
   assert len(firstElem.get("bcluFrequency")) == 26
   assert firstElem.get("bcluFrequency") == [None, 146, 947, 23396, 4450, 108, None, 29, 12236, 842, 21235, None, 3271, 1436, 1779, 25, None, 254, None, None, 5, 20, 736, 21898, 9053, 2507]
   assert len(firstElem.get("heisigSimplified")) == 26
   assert firstElem.get("heisigSimplified") == ['786 竹 bamboo 454 北 north', '419 市 market', '896 户 door', '389 政 politics 953 事 matter', '752 务 tasks', '926 所 place', '', '12 日 day', '2442 涌 gush 693 入 enter', '113 大 large 180 量 quantity', '793 人 person 149 潮 tide', '', '2893 码 numeral', '1497 牌 brand', '914 抽 take out', '680 到 arrive', '', '1027 号 appellation', '', '116 多 many', '394 是 be', '746 为 act', '743 办 manage', '1618 迁 resituate 693 入 enter', '896 户 door 2851 籍 records', '940 作 do 1351 业 profession']
   assert len(firstElem.get("heisigSimpInt")) == 26
   assert firstElem.get("heisigSimpInt") == [[{'竹': 786}, {'北': 454}], [{'市': 419}], [{'户': 896}], [{'政': 389}, {'事': 953}], [{'务': 752}], [{'所': 926}], [], [{'日': 12}], [{'涌': 2442}, {'入': 693}], [{'大': 113}, {'量': 180}], [{'人': 793}, {'潮': 149}], [], [{'码': 2893}], [{'牌': 1497}], [{'抽': 914}], [{'到': 680}], [], [{'号': 1027}], [], [{'多': 116}], [{'是': 394}], [{'为': 746}], [{'办': 743}], [{'迁': 1618}, {'入': 693}], [{'户': 896}, {'籍': 2851}], [{'作': 940}, {'业': 1351}]]
   assert len(firstElem.get("heisigTraditional")) == 26
   assert firstElem.get("heisigTraditional") == ['728 竹 bamboo 420 北 north', '388 市 market', '830 戶 door', '363 政 politics 878 事 matter', '934 務 tasks', '857 所 place', '', '12 日 day', '2378 湧 gush 638 入 enter', '106 大 large 170 量 quantity', '736 人 person 139 潮 tide', '', '2848 碼 numeral', '1492 牌 brand', '846 抽 take out', '628 到 arrive', '', '1493 號 appellation', '', '109 多 many', '368 是 be', '1385 為 act', '1119 辦 manage', '2542 遷 resituate 638 入 enter', '830 戶 door 2798 籍 records', '868 作 do 1304 業 profession']
   assert len(firstElem.get("heisigTradInt")) == 26
   assert firstElem.get("heisigTradInt") == [[{'竹': 728}, {'北': 420}], [{'市': 388}], [{'戶': 830}], [{'政': 363}, {'事': 878}], [{'務': 934}], [{'所': 857}], [], [{'日': 12}], [{'湧': 2378}, {'入': 638}], [{'大': 106}, {'量': 170}], [{'人': 736}, {'潮': 139}], [], [{'碼': 2848}], [{'牌': 1492}], [{'抽': 846}], [{'到': 628}], [], [{'號': 1493}], [], [{'多': 109}], [{'是': 368}], [{'為': 1385}], [{'辦': 1119}], [{'遷': 2542}, {'入': 638}], [{'戶': 830}, {'籍': 2798}], [{'作': 868}, {'業': 1304}]]

def test_appController_postendpoint_simplified():
   news = input_jsonSimpNews()
   outputDict = src.Controllers.appController.postendpoint(news)
   output = outputDict["output"]
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
   assert len(firstElem.get("hskLevel")) == 27
   assert firstElem.get("hskLevel") == ['', 'hsk1', '', 'hsk2', '', 'hsk1', '', '', '', 'hsk6', 'hsk2', 'hsk5', 'hsk5', 'hsk4', '', 'hsk2', '', '', '', '', 'hsk5', 'hsk6', '', 'hsk1', '', 'hsk2', 'hsk5']
   assert len(firstElem.get("bcluFrequency")) == 27
   assert firstElem.get("bcluFrequency") == [None, 32, None, 29, None, 52, 1916, 1939, 584, 825, 85, 256, 568, 1685, None, 70, 165, 8306, 1916, None, 1456, 1622, 3080, 2, 8041, 70, 1700]
   assert len(firstElem.get("heisigSimplified")) == 27
   assert firstElem.get("heisigSimplified") == ['', '13 月 month', '', '12 日 day', '', '38 中 middle 549 国 country', '730 铁 iron 1053 路 path', '368 成 turn into 1383 都 metropolis', '893 局 bureau', '538 集 gather 622 团 troupe', '696 公 public 1391 司 take charge of', '1347 组 group 1082 织 weave', '2732 媒 matchmaker 813 体 body', '598 提 bring up 303 前 in front', '360 试 test 1706 乘 hitch a ride', '1191 新 new', '368 成 turn into', '457 昆 descendants', '730 铁 iron 1053 路 path', '', '576 感 feel 667 受 accept', '1148 即 immediately 244 将 General', '680 到 arrive 783 来 come', "70 的 'bull''s eye'", '168 时 time 1075 空 empty', '1191 新 new', '813 体 body 1457 验 check']
   assert len(firstElem.get("heisigSimpInt")) == 27
   assert firstElem.get("heisigSimpInt") == [[], [{'月': 13}], [], [{'日': 12}], [], [{'中': 38}, {'国': 549}], [{'铁': 730}, {'路': 1053}], [{'成': 368}, {'都': 1383}], [{'局': 893}], [{'集': 538}, {'团': 622}], [{'公': 696}, {'司': 1391}], [{'组': 1347}, {'织': 1082}], [{'媒': 2732}, {'体': 813}], [{'提': 598}, {'前': 303}], [{'试': 360}, {'乘': 1706}], [{'新': 1191}], [{'成': 368}], [{'昆': 457}], [{'铁': 730}, {'路': 1053}], [], [{'感': 576}, {'受': 667}], [{'即': 1148}, {'将': 244}], [{'到': 680}, {'来': 783}], [{'的': 70}], [{'时': 168}, {'空': 1075}], [{'新': 1191}], [{'体': 813}, {'验': 1457}]]
   assert len(firstElem.get("heisigTraditional")) == 27
   assert firstElem.get("heisigTraditional") == ['', '13 月 month', '', '12 日 day', '', '36 中 middle 516 國 country', '339 鐵 iron 976 路 path', '341 成 turn into 1340 都 metropolis', '829 局 bureau', '502 集 gather 1471 團 troupe', '643 公 public 1348 司 take charge of', '1299 組 group 1020 織 weave', '2665 媒 matchmaker 1070 體 body', '563 提 bring up 277 前 in front', '334 試 test 1678 乘 hitch a ride', '1123 新 new', '341 成 turn into', '423 昆 descendants', '339 鐵 iron 976 路 path', '', '540 感 feel 617 受 accept', '1087 即 immediately 920 將 General', '628 到 arrive 789 來 come', "66 的 'bull''s eye'", '156 時 time 998 空 empty', '1123 新 new', '1070 體 body 1419 驗 check']
   assert len(firstElem.get("heisigTradInt")) == 27
   assert firstElem.get("heisigTradInt") == [[], [{'月': 13}], [], [{'日': 12}], [], [{'中': 36}, {'國': 516}], [{'鐵': 339}, {'路': 976}], [{'成': 341}, {'都': 1340}], [{'侷': 829}], [{'集': 502}, {'團': 1471}], [{'公': 643}, {'司': 1348}], [{'組': 1299}, {'織': 1020}], [{'媒': 2665}, {'體': 1070}], [{'提': 563}, {'前': 277}], [{'試': 334}, {'乘': 1678}], [{'新': 1123}], [{'成': 341}], [{'昆': 423}], [{'鐵': 339}, {'路': 976}], [], [{'感': 540}, {'受': 617}], [{'即': 1087}, {'將': 920}], [{'到': 628}, {'來': 789}], [{'的': 66}], [{'時': 156}, {'空': 998}], [{'新': 1123}], [{'體': 1070}, {'驗': 1419}]]

def test_appController_postendpoint_missingScript():
   news = input_jsonSimpNews_missingScript()
   outputDict = src.Controllers.appController.postendpoint(news)
   output = outputDict["output"]
   assert len(output) == 0

def test_appController_postendpoint_missingText():
   news = input_jsonSimpNews_missingText()
   outputDict = src.Controllers.appController.postendpoint(news)
   output = outputDict["output"]
   assert len(output) == 0