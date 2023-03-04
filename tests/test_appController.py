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

def test_appController_texttovocab_info_traditional():
   news = input_jsonTradNews()
   outputDict = src.Controllers.appController.texttovocabinfo(news)
   testdata = getDataForVocabInfoTest()
   outp = outputDict["output"]
   assert outp == testdata

def test_appController_texttovocab_raw_traditional():
   news = input_jsonTradNews()
   outputDict = src.Controllers.appController.texttovocabraw(news)
   outp = outputDict["output"]
   testdata = getDataForVocabRawTest()
   assert outp == testdata

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

def getDataForVocabRawTest():
   return """多
的
在
是
月
會
號

到
日
出
所以

為
被
作業

以
經濟
通過
表示
當
接受
條件
符合
困

所
方
媒體
朝
資格
取消

衝擊

竹北
但
前
市
未
金
即
帶來
辦
大量
戶
若
聯
含
牌
設
抽
條例
訪
民眾
碼
發放
移
領取
於
務
鄭
籍
提案
設定
疫情
門檻
民生
自治
戶籍
減緩
湧入
紓
人潮
遷入
政事"""

def getDataForVocabInfoTest():
   return """all words: 71
hsk1: 7 of 150
hsk2: 4 of 151
hsk3: 3 of 300
hsk4: 9 of 600
hsk5: 6 of 1300
hsk6: 1 of 2500
non hsk: 41

多 hsk1 0 Duo1 /many/much/often/a lot of/numerous/more/in excess/how (to what extent)/multi-/Taiwan pr. [duo2] when it means "how"/
的 hsk1 2 Di4|Di1|Di2|De5 /aim/clear/|/see 的士[di1 shi4]/|/really and truly/|/of/~'s (possessive particle)/(used after an attribute)/(used to form a nominal expression)/(used at the end of a declarative sentence for emphasis)/also pr. [di4] or [di5] in poetry and songs/
在 hsk1 4 Zai4 /(located) at/(to be) in/to exist/in the middle of doing sth/(indicating an action in progress)/
是 hsk1 5 Shi4 /is/are/am/yes/to be/
月 hsk1 32 Yue4 /moon/month/monthly/CL:個|个[ge4],輪|轮[lun2]/
會 hsk1 33 Kuai4|Hui4 /to balance an account/accountancy/accounting/|/can (i.e. have the skill, know how to)/likely to/sure to/to meet/to get together/meeting/gathering/union/group/association/a moment (Taiwan pr. for this sense is [hui3])/
號 hsk1 254 Hao2|Hao4 /roar/cry/CL:個|个[ge4]/|/ordinal number/day of a month/mark/sign/business establishment/size/ship suffix/horn (wind instrument)/bugle call/assumed name/to take a pulse/classifier used to indicate number of people/

到 hsk2 25 Dao4 /to (a place)/until (a time)/up to/to go/to arrive/(verb complement denoting completion or result of an action)/
日 hsk2 29 Ri4 /abbr. for 日本[Ri4 ben3], Japan/|/sun/day/date, day of the month/
出 hsk2 65 Chu1 /to go out/to come out/to occur/to produce/to go beyond/to rise/to put forth/to happen/(used after a verb to indicate an outward direction or a positive result)/classifier for dramas, plays, operas etc/
所以 hsk2 192 Suo3Yi3 /therefore/as a result/so/the reason why/

為 hsk3 20 Wei4|Wei2 /because of/for/to/|/as (in the capacity of)/to take sth as/to act as/to serve as/to behave as/to become/to be/to do/by (in the passive voice)/
被 hsk3 43 Bei4 /quilt/by/(indicates passive-voice clauses)/(literary) to cover/to meet with/(coll.) (since c. 2009) used before a verb that does not accurately represent what actually happened, to describe with black humor how sb or sth was dealt with by the authorities (as in 被自殺|被自杀[bei4 zi4 sha1])/
作業 hsk3 2507 Zuo4Ye4 /school assignment/homework/work/task/operation/CL:個|个[ge4]/to operate/

以 hsk4 51 Yi3 /abbr. for Israel 以色列[Yi3 se4 lie4]/|/to use/by means of/according to/in order to/because of/at (a certain date or place)/
經濟 hsk4 124 Jing1Ji4 /economy/economic/
通過 hsk4 143 Tong1Guo4 /to pass through; to get through/to adopt (a resolution); to pass (legislation)/to pass (a test)/by means of; through; via/
表示 hsk4 154 Biao3Shi4 /to express/to show/to say/to state/to indicate/to mean/
當 hsk4 160 Dang4|Dang1 /at or in the very same.../suitable/adequate/fitting/proper/to replace/to regard as/to think/to pawn/(coll.) to fail (a student)/|/to be/to act as/manage/withstand/when/during/ought/should/match equally/equal/same/obstruct/just at (a time or place)/on the spot/right/just at/
接受 hsk4 472 Jie1Shou4 /to accept/to receive/
條件 hsk4 497 Tiao2Jian4 /condition; circumstance; term; factor/requirement; prerequisite; qualification/situation; state; condition/CL:個|个[ge4]/
符合 hsk4 1231 Fu2He2 /in keeping with/in accordance with/tallying with/in line with/to agree with/to accord with/to conform to/to correspond with/to manage/to handle/
困 hsk4 1920 Kun4 /to trap/to surround/hard-pressed/stranded/destitute/

所 hsk5 108 Suo3 /actually/place/classifier for houses, small buildings, institutions etc/that which/particle introducing a relative clause or passive/CL:個|个[ge4]/
方 hsk5 408 Fang1 /surname Fang/|/square/power or involution (math.)/upright/honest/fair and square/direction/side/party (to a contract, dispute etc)/place/method/prescription (medicine)/just when/only or just/classifier for square things/abbr. for square or cubic meter/
媒體 hsk5 568 Mei2Ti3 /media, esp. news media/
朝 hsk5 1412 Zhao1|Chao2|Chao2 /morning/|/abbr. for 朝鮮|朝鲜[Chao2 xian3] Korea/|/imperial or royal court/government/dynasty/reign of a sovereign or emperor/court or assembly held by a sovereign or emperor/to make a pilgrimage to/facing/towards/
資格 hsk5 2102 Zi1Ge2 /qualifications/seniority/
取消 hsk5 2238 Qu3Xiao1 /to cancel/cancellation/

衝擊 hsk6 3094 Chong1Ji1 /to attack/to batter/(of waves) to pound against/shock/impact/

竹北  0 Zhu2Bei3 /Zhubei or Chupei city in Hsinchu County 新竹縣|新竹县[Xin1 zhu2 Xian4], northwest Taiwan/
但  46 Dan4 /but/yet/however/only/merely/still/
前  84 Qian2 /front/forward/ahead/first/top (followed by a number)/future/ago/before/BC (e.g. 前293年)/former/formerly/
市  146 Shi4 /market/city/CL:個|个[ge4]/
未  339 Wei4 /not yet/did not/have not/not/8th earthly branch: 1-3 p.m., 6th solar month (7th July-6th August), year of the Sheep/ancient Chinese compass point: 210°/
金  462 Jin1 /surname Jin/surname Kim (Korean)/Jurchen Jin dynasty (1115-1234)/|/gold/chemical element Au/generic term for lustrous and ductile metals/money/golden/highly respected/one of the eight categories of ancient musical instruments 八音[ba1 yin1]/
即  466 Ji2 /namely/that is/i.e./prompt/at once/at present/even if/prompted (by the occasion)/to approach/to come into contact/to assume (office)/to draw near/
帶來  634 Dai4Lai2 /to bring/to bring about/to produce/
辦  736 Ban4 /to do/to manage/to handle/to go about/to run/to set up/to deal with/
大量  842 Da4Liang4 /great amount/large quantity/bulk/numerous/generous/magnanimous/
戶  947 Hu4 /a household/door/family/
若  971 Ruo4 /to seem/like/as/if/
聯  1038 Lian2 /to ally/to unite/to join/(poetry) antithetical couplet/
含  1413 Han2 /to keep/to contain/to suck (keep in your mouth without chewing)/
牌  1436 Pai2 /mahjong tile/playing card/game pieces/signboard/plate/tablet/medal/CL:片[pian4],個|个[ge4],塊|块[kuai4]/
設  1572 She4 /to set up/to arrange/to establish/to found/to display/
抽  1779 Chou1 /to draw out/to pull out from in between/to remove part of the whole/(of certain plants) to sprout or bud/to whip or thrash/
條例  2814 Tiao2Li4 /regulations; rules; code of conduct; ordinances; statutes/
訪  3053 Fang3 /(bound form) to visit/to call on/to seek/to inquire/to investigate/
民眾  3175 Min2Zhong4 /populace/masses/the people/
碼  3271 Ma3 /weight/number/code/to pile/to stack/classifier for length or distance (yard), happenings etc/
發放  3276 Fa1Fang4 /to provide/to give/to grant/
移  3312 Yi2 /to move/to shift/to change/to alter/to remove/
領取  3570 Ling3Qu3 /to receive/to draw/to get/
於  4283 Wu1|Yu1|Yu2 /(literary) Oh!/Ah!/|/surname Yu/Taiwan pr. [Yu2]/|/in/at/to/from/by/than/out of/
務  4450 Wu4 /affair/business/matter/to be engaged in/to attend to/by all means/
鄭  4618 Zheng4 /bound form used in 鄭重|郑重[zheng4 zhong4] and 雅鄭|雅郑[ya3 zheng4]/|/Zheng state during the Warring States period/surname Zheng/abbr. for 鄭州|郑州[Zheng4 zhou1]/
籍  5027 Ji2 /surname Ji/|/book or record/registry/roll/place of one's family or ancestral records/membership/
提案  5135 Ti2An4 /proposal/draft resolution/motion (to be debated)/to propose a bill/to make a proposal/
設定  5438 She4Ding4 /to set/to set up/to install/setting/preferences/
疫情  5810 Yi4Qing2 /epidemic situation/
門檻  6355 Men2Kan3 /doorstep/sill/threshold/fig. knack or trick (esp. scheme to get sth cheaper)/
民生  7105 Min2Sheng1 /people's livelihood/people's welfare/
自治  8168 Zi4Zhi4 /autonomy/
戶籍  9053 Hu4Ji2 /census register/household register/
減緩  11902 Jian3Huan3 /to slow down/to retard/
湧入  12236 Yong3Ru4 /to come pouring in/influx/
紓  20712 Shu1 /abundant/ample/at ease/relaxed/to free from/to relieve/
人潮  21235 Ren2Chao2 /a tide of people/
遷入  21898 Qian1Ru4 /to move in (to new lodging)/
政事  23396 Zheng4Shi4 /politics/government affairs/
"""