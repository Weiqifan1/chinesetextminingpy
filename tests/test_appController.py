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
      "deckName": "testDeckName",
      "deckInfo": "testDeckInfo",
      "script": "simplified"
   }
   return jsondict

def input_jsonSimpNews():
   # http://cn.chinadaily.com.cn/a/202212/23/WS63a58ed9a3102ada8b2281d8.html
   cntext = """12月23日, 中国铁路成都局集团公司组织媒体提前试乘新成昆铁路, 感受即将到来的时空新体验。 记者在现场获悉, 新成昆铁路将采用第三代C型CR200J'复兴号'动车组值乘, 这也是该车型首次正式亮相。 据介绍, 第三代C型CR200J'复兴号'动车组为9节车厢, 较第二代'绿巨人'增加了商务座, 旋转座椅等, 外形涂装为绿白相间。 此次中国铁路成都局集团公司迎接回6组最新型'复兴号'动车组, 将全部用于新成昆铁路开行。"""
   jsondict = {
      "deckName": "testDeckName",
      "deckInfo": "testDeckInfo",
      "script": "simplified",
      "cardOrder": "chronological",
      "textType": "rawText",
      "vocab": [],
      "sentencenames": [],
      "text": cntext
   }
   return jsondict

def input_jsonTradNews():
   # https://www.taiwannews.com.tw/ch/news/4779971
   cntext = """竹北市戶政事務所12日湧入大量人潮，碼牌抽到1297號，多是為辦遷入戶籍作業。

鄭朝方12日接受媒體聯訪表示，民生紓困金是為減緩疫情帶來的經濟衝擊，所以未設定門檻條件，12日通過提案的自治條例，是以1月12日（含當日）前設籍於竹北市，即符合領取資格，但民眾若在發放紓困金前移出，會被取消資格。"""
   jsondict = {
      "deckName": "testDeckName",
      "deckInfo": "testDeckInfo",
      "script": "traditional",
      "cardOrder": "chronological",
      "textType": "rawText",
      "vocab": [],
      "sentencenames": [],
      "text": cntext
   }
   return jsondict

def input_jsonTradNews_textTypeOrdered2Line():
   # https://www.taiwannews.com.tw/ch/news/4779971
   cntext4 = """
   竹北市戶政事務所12日湧入大量人潮， 碼牌抽到1297號， 多是為辦遷入戶籍作業。
   
   
   line2
   鄭朝方12日接受媒體聯訪表示，
   
   line3
   民生紓困金是為減緩疫情帶來的經濟衝擊，
   
   所以未設定門檻條件，
   """
   cntext3 = "Thank you for the music\nWelcome to the jungle"
   cntext2 = '竹北市戶政事務所12日湧入大量人潮， 碼牌抽到1297號， 多是為辦遷入戶籍作業。\n\n\n\
   line2\n鄭朝方12日接受媒體聯訪表示，\n\nline3\n民生紓困金是為減緩疫情帶來的經濟衝擊，\n\n\
   所以未設定門檻條件，'
   testnewline = ord("\n")
   testcarriage = ord("\r")

   cntext = "作業。\r\n\r\n\r\nline2\n方12日，\n\n\n\nline3\n民生，\n\n所以，"
   listOfUni = [ord(x) for x in cntext]
   jsondict = {
      "deckName": "testDeckName",
      "deckInfo": "testDeckInfo",
      "script": "traditional",
      "cardOrder": "chronological",
      "textType": "ordered2Line",
      "vocab": [],
      "sentencenames": [],
      "text": cntext
   }
   return jsondict

def test_appController_texttovocab_traditional():
   news = input_jsonTradNews()
   outputDict = src.Controllers.appController.texttovocab(news)
   assert outputDict["output"] == getDataForVocabTest()

def test_appController_postendpoint_traditional_vocabAndOrdered2Line():
   news = input_jsonTradNews_textTypeOrdered2Line()
   outputDict = src.Controllers.appController.postendpoint(news)
   assert outputDict["deckName"] == "testDeckName"
   assert outputDict["deckInfo"] == "testDeckInfo"
   assert outputDict["script"] == "traditional"
   assert outputDict["cardOrder"] == "chronological"
   output = outputDict["output"]
   assert len(output) == 4
   firstElem = output[0]
   assert firstElem.get("sentence") == '作業。'
   assert len(firstElem.get("tokens")) == 2
   assert firstElem.get("tokens") == ['作業', '。']
   assert len(firstElem.get("simplified")) == 2
   assert firstElem.get("simplified") == ['作业', '。']
   assert len(firstElem.get("traditional")) == 2
   assert firstElem.get("traditional") == ['作業', '。']
   assert len(firstElem.get("pinyin")) == 2
   assert firstElem.get("pinyin") == ['Zuo4Ye4', '。']
   assert len(firstElem.get("meaning")) == 2
   assert firstElem.get("meaning") == ['/school assignment/homework/work/task/operation/CL:個|个[ge4]/to operate/', '。']
   assert len(firstElem.get("hskLevel")) == 2
   assert firstElem.get("hskLevel") == ['hsk3', '']
   assert len(firstElem.get("blcuFrequency")) == 2
   assert firstElem.get("blcuFrequency") == [2507, None]
   assert len(firstElem.get("heisigSimplified")) == 2
   assert firstElem.get("heisigSimplified") == ['940 作 do 1351 业 profession', '']
   assert len(firstElem.get("heisigSimpInt")) == 2
   assert firstElem.get("heisigSimpInt") == [[{'作': 940}, {'业': 1351}], []]
   assert len(firstElem.get("heisigTraditional")) == 2
   assert firstElem.get("heisigTraditional") == ['868 作 do 1304 業 profession', '']
   assert len(firstElem.get("heisigTradInt")) == 2
   assert firstElem.get("heisigTradInt") == [[{'作': 868}, {'業': 1304}], []]

def test_appController_postendpoint_traditional_vocab():
   news = input_jsonTradNews()
   outputDict = src.Controllers.appController.postendpoint(news)
   assert outputDict["deckName"] == "testDeckName"
   assert outputDict["deckInfo"] == "testDeckInfo"
   assert outputDict["script"] == "traditional"
   assert outputDict["cardOrder"] == "chronological"
   output = outputDict["output"]
   assert len(output) == 11
   firstElem = output[0]
   assert firstElem.get("sentence") == '竹北市戶政事務所12日湧入大量人潮，'
   assert len(firstElem.get("tokens")) == 12
   assert firstElem.get("tokens") == ['竹北', '市', '戶', '政事', '務', '所', '12', '日', '湧入', '大量', '人潮', '，']
   assert len(firstElem.get("simplified")) == 12
   assert firstElem.get("simplified") == ['竹北', '市', '户', '政事', '务', '所', '12', '日', '涌入', '大量', '人潮', '，']
   assert len(firstElem.get("traditional")) == 12
   assert firstElem.get("traditional") == ['竹北', '市', '戶', '政事', '務', '所', '12', '日', '湧入', '大量', '人潮', '，']
   assert len(firstElem.get("pinyin")) == 12
   assert firstElem.get("pinyin") == ['Zhu2Bei3', 'Shi4', 'Hu4', 'Zheng4Shi4', 'Wu4', 'Suo3', '12', 'Ri4', 'Yong3Ru4', 'Da4Liang4', 'Ren2Chao2', '，']
   assert len(firstElem.get("meaning")) == 12
   assert firstElem.get("meaning") == ['/Zhubei or Chupei city in Hsinchu County 新竹縣|新竹县[Xin1 zhu2 Xian4], northwest Taiwan/', '/market/city/CL:個|个[ge4]/', '/a household/door/family/', '/politics/government affairs/', '/affair/business/matter/to be engaged in/to attend to/by all means/', '/actually/place/classifier for houses, small buildings, institutions etc/that which/particle introducing a relative clause or passive/CL:個|个[ge4]/', '12', '/abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/', '/to come pouring in/influx/', '/great amount/large quantity/bulk/numerous/generous/magnanimous/', '/a tide of people/', '，']
   assert len(firstElem.get("hskLevel")) == 12
   assert firstElem.get("hskLevel") == ['', '', '', '', '', 'hsk5', '', 'hsk2', '', '', '', '']
   assert len(firstElem.get("blcuFrequency")) == 12
   assert firstElem.get("blcuFrequency") == [None, 146, 947, 23396, 4450, 108, None, 29, 12236, 842, 21235, None]
   assert len(firstElem.get("heisigSimplified")) == 12
   assert firstElem.get("heisigSimplified") == ['786 竹 bamboo 454 北 north', '419 市 market', '896 户 door', '389 政 politics 953 事 matter', '752 务 tasks', '926 所 place', '', '12 日 day', '2442 涌 gush 693 入 enter', '113 大 large 180 量 quantity', '793 人 person 149 潮 tide', '']
   assert len(firstElem.get("heisigSimpInt")) == 12
   assert firstElem.get("heisigSimpInt") == [[{'竹': 786}, {'北': 454}], [{'市': 419}], [{'户': 896}], [{'政': 389}, {'事': 953}], [{'务': 752}], [{'所': 926}], [], [{'日': 12}], [{'涌': 2442}, {'入': 693}], [{'大': 113}, {'量': 180}], [{'人': 793}, {'潮': 149}], []]
   assert len(firstElem.get("heisigTraditional")) == 12
   assert firstElem.get("heisigTraditional") == ['728 竹 bamboo 420 北 north', '388 市 market', '830 戶 door', '363 政 politics 878 事 matter', '934 務 tasks', '857 所 place', '', '12 日 day', '2378 湧 gush 638 入 enter', '106 大 large 170 量 quantity', '736 人 person 139 潮 tide', '']
   assert len(firstElem.get("heisigTradInt")) == 12
   assert firstElem.get("heisigTradInt") == [[{'竹': 728}, {'北': 420}], [{'市': 388}], [{'戶': 830}], [{'政': 363}, {'事': 878}], [{'務': 934}], [{'所': 857}], [], [{'日': 12}], [{'湧': 2378}, {'入': 638}], [{'大': 106}, {'量': 170}], [{'人': 736}, {'潮': 139}], []]

def test_appController_postendpoint_simplified_noVocab():
   news = input_jsonSimpNews()
   outputDict = src.Controllers.appController.postendpoint(news)
   assert outputDict["deckName"] == "testDeckName"
   assert outputDict["deckInfo"] == "testDeckInfo"
   assert outputDict["script"] == "simplified"
   assert outputDict["cardOrder"] == "chronological"
   output = outputDict["output"]
   assert len(output) == 13
   secondElement = output[1]
   assert secondElement.get("sentence") == '中国铁路成都局集团公司组织媒体提前试乘新成昆铁路,'
   assert len(secondElement.get("tokens")) == 15
   assert secondElement.get("tokens") == ['中国', '铁路', '成都', '局', '集团', '公司', '组织', '媒体', '提前', '试乘', '新', '成', '昆', '铁路', ',']
   assert len(secondElement.get("simplified")) == 15
   assert secondElement.get("simplified") == ['中国', '铁路', '成都', '局', '集团', '公司', '组织', '媒体', '提前', '试乘', '新', '成', '昆', '铁路', ',']
   assert len(secondElement.get("traditional")) == 15
   assert secondElement.get("traditional") == ['中國', '鐵路', '成都', '侷|局', '集團', '公司', '組織', '媒體', '提前', '試乘', '新', '成', '昆|崑|崐', '鐵路', ',']
   assert len(secondElement.get("pinyin")) == 15
   assert secondElement.get("pinyin") == ['Zhong1Guo2', 'Tie3Lu4', 'Cheng2Du1', 'Ju2', 'Ji2Tuan2', 'Gong1Si1', 'Zu3Zhi1', 'Mei2Ti3', 'Ti2Qian2', 'Shi4Cheng2', 'Xin1', 'Cheng2', 'Kun1', 'Tie3Lu4', ',']
   assert len(secondElement.get("meaning")) == 15
   assert secondElement.get("meaning") == ['/China/', '/railroad/railway/CL:條|条[tiao2]/', '/Chengdu subprovincial city and capital of Sichuan province 四川 in southwest China/', '/narrow/|/office/situation/classifier for games: match, set, round etc/', '/group/bloc/corporation/conglomerate/', '/company; firm; corporation/CL:家[jia1]/', '/to organize/organization/(biology) tissue/(textiles) weave/CL:個|个[ge4]/', '/media, esp. news media/', '/to shift to an earlier date/to do sth ahead of time/in advance/', '/test drive/', '/new/newly/meso- (chemistry)/|/abbr. for Xinjiang 新疆[Xin1 jiang1] or Singapore 新加坡[Xin1 jia1 po1]/surname Xin/', '/surname Cheng/|/to succeed/to finish/to complete/to accomplish/to become/to turn into/to be all right/OK!/one tenth/', '/descendant/elder brother/a style of Chinese poetry/|/used in place names, notably Kunlun Mountains 崑崙|昆仑[Kun1 lun2]/(also used for transliteration)/|/variant of 崑|昆[kun1]/', '/railroad/railway/CL:條|条[tiao2]/', ',']
   assert len(secondElement.get("hskLevel")) == 15
   assert secondElement.get("hskLevel") == ['hsk1', '', '', '', 'hsk6', 'hsk2', 'hsk5', 'hsk5', 'hsk4', '', 'hsk2', '', '', '', '']
   assert len(secondElement.get("blcuFrequency")) == 15
   assert secondElement.get("blcuFrequency") == [52, 1916, 1939, 584, 825, 85, 256, 568, 1685, None, 70, 165, 8306, 1916, None]
   assert len(secondElement.get("heisigSimplified")) == 15
   assert secondElement.get("heisigSimplified") == ['38 中 middle 549 国 country', '730 铁 iron 1053 路 path', '368 成 turn into 1383 都 metropolis', '893 局 bureau', '538 集 gather 622 团 troupe', '696 公 public 1391 司 take charge of', '1347 组 group 1082 织 weave', '2732 媒 matchmaker 813 体 body', '598 提 bring up 303 前 in front', '360 试 test 1706 乘 hitch a ride', '1191 新 new', '368 成 turn into', '457 昆 descendants', '730 铁 iron 1053 路 path', '']
   assert len(secondElement.get("heisigSimpInt")) == 15
   assert secondElement.get("heisigSimpInt") == [[{'中': 38}, {'国': 549}], [{'铁': 730}, {'路': 1053}], [{'成': 368}, {'都': 1383}], [{'局': 893}], [{'集': 538}, {'团': 622}], [{'公': 696}, {'司': 1391}], [{'组': 1347}, {'织': 1082}], [{'媒': 2732}, {'体': 813}], [{'提': 598}, {'前': 303}], [{'试': 360}, {'乘': 1706}], [{'新': 1191}], [{'成': 368}], [{'昆': 457}], [{'铁': 730}, {'路': 1053}], []]
   assert len(secondElement.get("heisigTraditional")) == 15
   assert secondElement.get("heisigTraditional") == ['36 中 middle 516 國 country', '339 鐵 iron 976 路 path', '341 成 turn into 1340 都 metropolis', '829 局 bureau', '502 集 gather 1471 團 troupe', '643 公 public 1348 司 take charge of', '1299 組 group 1020 織 weave', '2665 媒 matchmaker 1070 體 body', '563 提 bring up 277 前 in front', '334 試 test 1678 乘 hitch a ride', '1123 新 new', '341 成 turn into', '423 昆 descendants', '339 鐵 iron 976 路 path', '']
   assert len(secondElement.get("heisigTradInt")) == 15
   assert secondElement.get("heisigTradInt") == [[{'中': 36}, {'國': 516}], [{'鐵': 339}, {'路': 976}], [{'成': 341}, {'都': 1340}], [{'侷': 829}], [{'集': 502}, {'團': 1471}], [{'公': 643}, {'司': 1348}], [{'組': 1299}, {'織': 1020}], [{'媒': 2665}, {'體': 1070}], [{'提': 563}, {'前': 277}], [{'試': 334}, {'乘': 1678}], [{'新': 1123}], [{'成': 341}], [{'昆': 423}], [{'鐵': 339}, {'路': 976}], []]

def test_appController_postendpoint_missingScript():
   news = input_jsonSimpNews_missingScript()
   outputDict = src.Controllers.appController.postendpoint(news)
   assert outputDict["deckInfo"] == 'text json is missing either of the following: [deckName, deckInfo, script, cardOrder, textType, text, vocab, sentencenames]'

def test_appController_postendpoint_missingText():
   news = input_jsonSimpNews_missingText()
   outputDict = src.Controllers.appController.postendpoint(news)
   assert outputDict["deckInfo"] == 'text json is missing either of the following: [deckName, deckInfo, script, cardOrder, textType, text, vocab, sentencenames]'

def getDataForVocabTest():
   return """all words: 71
hsk1: 7 of 150
hsk2: 4 of 151
hsk3: 3 of 300
hsk4: 9 of 600
hsk5: 6 of 1300
hsk6: 1 of 2500
non hsk: 41

竹北
市
戶
政事
務
所
日
湧入
大量
人潮
碼
牌
抽
到
號
多
是
為
辦
遷入
戶籍
作業
鄭
朝
方
接受
媒體
聯
訪
表示
民生
紓
困
金
減緩
疫情
帶來
的
經濟
衝擊
所以
未
設定
門檻
條件
通過
提案
自治
條例
以
月
含
當
前
設
籍
於
即
符合
領取
資格
但
民眾
若
在
發放
移
出
會
被
取消"""