import re

data = """!how()where()*mul(527,340)?why()^?mul(168,100)!^#mul(390,111)>'when()'select())((from()how()mul(412,526)/@what()from()when()-mul(500,980)#&[}]mul(887,503)%,$mul(699,805)what()select())>mul(292,305),'-{,@,how()who()mul(213,633)when()?@who()mul(652,4)*&'what()mul(177,237)&who()why()(@{+;why()<mul(23,321)what()when();from()-do()who() {&}-:(mul(844,162)~from()/mul(77,769)%,how()@%(?who()]<mul(694,833)^from()how()> &mul(193,679),)&mul(565,339)?}what()!who(){mul(705,313)mul(294,50)+mul(201,534) )~how()mul(659,49)!mul(871,788)select()where()from()mul(346,618) *&@'why()&}#mul(483,765)!#select()^*+[what()when()mul(448,525)]>:where()&^who()&mul(611,331):!)*/]}mul(37,42)>mul(538,106)when()why()mul(36,120)~where()-{+from()$'mul(950,456))mul(28,237)what()when(479,124)mul(697,976)):**/]&#how()#mul(424,841)why()'!;~mul(108,859)~%{?!mul(40,521)do()[^when()/%$+ [where()mul(187,953)who()where()select()(select()what()mul(984,77)<@)(/where()from()~;mul(163,398)/who()who()~mul(445,94))what()what()][how(),mul(115,245)--}/#how()what()!mul(366,981)'$why()do()what(565,96)who()mul(128,999):mul(858,772)[,,mul(796,864)why()what()^(mul(136,980)when()?!when()}mul(142,552)(mul(354,328)[(@how() (/~#mul(159,715)where()&mul(567,560)from()$^'$&&+!when()mul(582,489);where();select(),mul(306,841)? ,)how()mul(274,549)@~what()~?*mul(448,441);&<'select()when()when()#select()from()mul(404,209)^/ @who()who()'mul(400,15)';^&&when():{mul(199,543)[from()~+mul(452,787)([select()>/]$!/mul(840,165)when()>^why()~>when()(mul(830,125)from():mul(433,238);%why(){';$mul(494,781),-mul(139,401)&&&+who()>/^select()]do()mul(116,181)+$*[:who() do()how()<what()+mul(392,879)()what()don't()~)&?#*}mul(909,275)mul(695,234):],from()++^how()>;mul(514,117)$who()*)~%mul(859,857)}mul(837,844)>{@-what())-@@mul(574,73)]<[[why(608,495)how()who()when()mul(937,176)(%mul(471,325){'+)?:}mul(695,347)mul(56,888)where()##;#>who()+mul(157,650)mul(847,72):,[(how(144,703):mul(294,627)})>@mul(74,230)@)+what()mulhow()><<,$!(;why()mul(635,532)-select()mul(171,737)?select()[why()&^mul(587,686)$how()from())when()>;where()&mul(600,336)}@&{mul(651,690)from()?->&%mul(454,745)mul(387,378)mul(142,934)]mul(820,891)@#why()&how();;why()mul(337,723)&]from()when(894,39) ,>( mul/%(mul(271,558)#}']what()$-<^(mul(234 [what()when()select()($)+!don't()/ %<?%!]^mul(752,478)]how()mul(719,540)'when() why():(&'from(59,581)~mul(921,696)who()@,**%from(918,170))mul(224,391),where(104,159)do()from(339,837)}<<where()?{&how()mul(329,298)<who()what(937,474)&]@?mul(920,516);mul(438,991);{why()!]~'from()>mul(927,106)why()<%{{&~'<from()mul(950,746)'mul(240,649)?what(827,689)(mul(750,353)select(720,6)^mul(663,218)<,(why()<who()^>%why()mul(617?from()select()<what()mul(873,278)&^where(86,235)mul(170,108)!select()mul(66,5)@$^,~%from()mul(785,826): ~who(){mul(383,166):!![:~}+-'mul(554,291)@^)(^#when()when()why()mul(330,699)[:how(888,93)who()how(863,345)who()mul{how()-why()who()]$^mul(512,474)^@:mul(728,970)%mul(779,946)&& mul(216,667) where()^'%mul(788,642)how()>from()}$mul(915,977)& &mul(477,287){# mul(798,930)]mul(111select()*^@@/what()mul(518,86):('({&~{why()mul(991,855)*%^who()who()$/:{$mul(827,700)-'(mul(377,585)#&mul(171,537)when()@/>{< ,*:mul(349,478)!&^{-/mul(448,750)mul(868,546)mul(893,203)
;?++how()$mul(218,402){mul(52,837)&{what()<who()[}<{don't()!mulwhen()!mul(323,214)$-]?'from(443,779)when()~how()mul(394,217)<who()do()# {+$#why()mul(873,360)mul(971,135)*^mul(131,811)/}@:mul(59,937)~select() #mul(657,749)[)mul(982,524)mul(602,483)?*mul(218,526)@{*where(){mul(164,992):what()why()]!*$mul(581,601)what()(#]%when()(how(){]mul(448,35)@^-mul(334,228):/$]<]&]:;mul(719,850)when()*!mul(724,214) from()select(264,396)mul(849,228))what()~;>#$% <mul(968,167);mul(603,611)mul(766,876)&why()mul(693,810)<)&!don't()/;what()+%%mul(666,136)mul(76,902)<how()}where()}select()select()<,mul(886,504)from()'{from()mul(398,932)%~,-)mul(948,141)<,!<*mul(51,426)?)/what()~why()++mul(775,745)from()+,(select())why()when()%%mul(987,730)![when()}!(how()do():%/(+mul(656,106):who()*&mul(599,486),(?*select(842,61)<^!mul(400,798) @[]*/@mul(808,934)]-,mul(542,49)mul(262,237)why()<what()how()$who()&?mul(151,471:from()*&%mul(252,481):select()-}mul(364,841)[~mul(656,650)@'^<^what();do();~from()(!;'mul(837,565) what()mul(695,312){-;^&<when()mul(562,683*/select()select()-%(#^mul(792,201)@@)mul(934,213),when(365,302)&}*'when()mul{>{>%when()mul(997,771)/select()!mul(88,621)when();mul(120,538)&what(592,500)#:*,how()#mul(745,304)$;:&*mul(276,817)/select()'how()'{when()mul(422,988)mul(386,816)what(87,832)-${mul(43,620)mul(271,338)+;why()why()-#*don't()where():],]what()-mul(4,311)' why()?don't()/~from()~select()<[why()mul(37,622)select()^]select()#where()<{mul(910,54,don't(),#^+{mul(153,137))[mul(348,234)::+{mul(710,502)'}'do()~where(722,741)why()!]mul(810,172)@[{from()where())why(230,249)<who()mul(734,174)$<when()what()?mul(729,870)$why()<who()-*>*^+mul(439,248)(?/#how():mul(559,154)!+from(26,260),)!'mul(67,900){>where()select()#~who()#%what()mul(194,100){<[,'(;-mul(421,329'what()@$$?when()<',mul(410,915)]who(672,22)-:*mul(722,311) select()how()~how()!*'mul(114,108)%($$#what(728,367)do()from(),*mul(159,172)>%]mul(358,684)who()&~]when()$mul(791,993)who()++$why()how()&$mul(913,73)-!mul(53,114))([{ select()@]from()(mul(89,340);^-$>?from() mul(184,541)+-%:(# mul(43,872)? # -[mul(984,77)&<+]when()(#;!mul(22,759)how()<how()/,;mul(156,529)-mul(377,400)%@select()^&mul(19,833)mul(68,933)mul:^;what()-@%,>{select()mul(264,832)>/$mul(78,759)]mul(645,838)select()<$& mul(665,217)mul(332,96)where()##mul(410,119)mul(614,640)}-%who()/why()what()mul(514,395)!<+{:%#how()+#mul(169,935)/+who()where()select()*mul(298,793)&@how()?!(who(191,903)when()?mul(492,499)) % $^{when(779,320)select()mul(631,153) ';[from()/^-+mul(669,90)what();^/[mul(275,626)why()&&where()mul(647,52)[ /(;[{[mul(522,127)-)mul(477,645)what(998,194)%:{when()[%%mul(32,779)/from()why();mul(665how()'mul(856,294)%how()*$how(372,599)when()<@  don't()mul(46,719)^where()>+: }(when()@mul:from(393,669)!+;how()[%)how()mul(317,228):!who()/mul(998,368); }mul(156,743)@;'^;$<#[mul(317,438)how()[{)#-why()(+?mul(230,66)!?{:@select()}/mul-:when()@$&mul(575,563)!what(){&$}^^%mul(821,423);@@select(815,842))/?>[mul(838,244)where()/[>mul(299,138){%(-mul(476,161)mul(286,551)~;from()%${mul(479,12)%&&;how()mul(867,436)];mul(742,138)select(205,272)where()from(628,468)mul(284,644)@when()<!how()why()don't()[;)$,mul(420,782)'$;select()why()^?']mul(124,908)#mul(256,912)mul(255,378):'from():who()$><~^mul(254,513)who()@where()-[! mul(458,892)how()'['{mul(875,437)(#^from()mul(431>/}<{#how()mul(453,206)
where()]mul(385,96)^~){what()mul(879,45)/-){mul(115,393)!mul(257,133)&<;'mul(35,453);(mul(213,735)*+don't()~['select()?mul(761,741)]:)&from()?mul(648,940)+what()?mul(297,466);what()!mul(232,28)+/-who()%;where()?)mul(305,615)(*$^who()+&!select()mul(538,332)!@how() <${how(){?mul(357,604~when()what()why()~mul(543,859)when()do() mul(129,114),mul(182,648)#]/how()%$mul(974,606) #@)mul(841,177)how()[,from()-]^/mul(91,282)who()}where()+when()&$;why()mul*when()#mul(480,245):what()from()$~mul(885,960)@*what()]mul(656,115) select()select()how(737,324)~* ?mul(108,370);?$(!mul(428,835)+why()>/)mul(863,986)%&mul(840,769when(),{mul(463,323):?:mul(521,574)/when()(mul(362,622)~+'(-mul(904>$@]>?select()mul(511,354))mul(873,772),[,mul(492,786)^mul(113,58),(who()when()who()&</,mul(252,375)}+}what()select(384,157))&mul(257,777)(mul(934,832)how()-<~where()]who()>mul(949,323@when()@)~?mul(913,84)when()-}?<how()(>$+mul(82,683)where()how()->>who()]don't()!{mul(520,514)~+>mul(570,919);from()@!-*+]+where()mul(14,350)mul(577,453))/when()@?{select()%@mul(904,10)%&:>/,mul(632,748)&/#mul(919,899)@>don't()when()?<mul(923,825)-mul(773,944$~' $%:how(){don't() ~]-<]select();>]mul(183*how()select()~what()~+ #mul(301,159)from()(do()#@[who()>{(what(258,705)mul(844,738)mul(412,928)why()&how()}#-}~when()mul(949,165)mul(607,272)~who(931,656)do()&how();mul(594,752){~mul(695,972)<{}#mul(270,571)/,*from(447,32)'&>[mul(924,945),-!mul(539,419what()+<*what(885,804)<$~}~*mul(144,590)what()^<where(420,327){+mul(956,54)^+&'mul(799,92)$mul(939,70):how()select(){mul(414,359)'mul(649,366){+<how(140,173)what():#mul(503,754){*<who()}@*#what()mul(946,836)don't()','when()mul(460,355)where()select())mul(993,832)why() }'from()(~who()?mul(441{]select()?who():where()(mul(950,523) how()from(),::/^mul(382,457)how():what()~how()[:mul(104,980)~%why()what()*#mul(361,914)where()mul(310,662)@@from()from()%@>what()mul(989,595)who(),from(196,894)when(655,793)'*mul(375,733)how()-when()^*mul(272,881)why()mul(570,456)@@how()why())*mul(357&mul(844,880)<mul(348,758)?~{mul(454,846)what()why()'%}*mul(693,537)where()how()*-what()]{):mul(825,136)why()~/how()'mul(952,811)when():select();where()&&select()mul(846,735)mul(333,612)>mul(881,330)]select()~mul(236,135)'where(){why()+{mul(520,254)(:do()mul(645,835[&~from()why() what(){^select()]mul(892,641)@mul(814,94)& ,*how()who()why()&mul(61,560)@$%'mul(599,707)what(439,650)$-[():$!mul(73when()[#<mul(825,421)mul(426,176)@-^where()select()who()why()when()?mul(453,39),mul(724,707)]#@where();mul(925,260):($(;>don't()mul(538,792)<what()*when()~select(){~mul(326,892)@(;}do()when()?when()how()mul(100,121>> #from()why()/mul(460,218)mul(319,652))mul(290,239)%*how()why()(>@where()mul(591,728)@#select()when() )mul(184,663)!]<mul(34,388)%, -* mul(979,738)mul(178,487)))mul(429,189)]mul(820,475)<when()# what(),)where(),when()mul(245,395) mul(97,635)who()-}don't()<from()~:>%<mul(662,837)mul(460,812)mul(856,752):mul(324,499), *]/how(725,450)~when()what())mul(864,735)when()}$mul(49,227)what()where()#mul(576^!@:@+~mul(919,52)]/? how()^mul(383,37))#*mul(631,513)!'~@from()>}}mul(747,180)when()/~why()<,!select()mul(252,522)%*mul(690,254)+'!from()mul?(where()where()&)<!mul(801,852)%};{select(){ what()mul(42,685)<^;;*]!what()don't()>]when();mul(118,112)*?}where(544,721)#mul(721,220)@mul(190,918)+>how()#!/usr/bin/perl)where()]mul(548,120)where()mul(150,935)
;?!where()'who()$select()why()&mul(55,883){:+mul(220,196)where()-('from()?select()who()mul(504,565))#mul(745,347)<where()when()mul%'from()#</?*mul(149,109))from()select()'&*%^,mul(986,752)><++/mul(635,120)]~mul(791,406)-mul(724,781),when(144,428) [[mul(718,565)who()why() %mul(328,251)who()+]&mul(707,742)!how()]{from()]'--(mul(96,818)@-(-$how()mul(767,105)^-mul(250,160):}where()mul(966,869)mul(878,876)!;),mul(874,72)why()+#who() )why()where()mul(896,845))?'#mul(585,579)$?~from()]!mulwho()%~select(757,508)'&^?mul(244,631)'how()$}mul(995,939)&why()@from())(+(do()^who()what()$mul(166,376)when(866,717)mul(419,53))]%>}{&{%select()do()from()&/*!'why(443,390))mul(397,885)when()how()who()what()mul(99,988)?,what()&mul(836,347)mul(692 mul(724,602)(mul(250,6)*how()how()'!how()mul(639,245)]mul(81,785)&+~mul(101,124)mul(984,435)what()[,}*mul(347,607)select()<mul^where(393,801)-,when()*$>;&where()mul(80,544){#~&mul(934,254):#+!who()<[mul(357,513)?:>what()~?when()({mul(937,208)]>?who()'when()select()'how()'mul(608,880)do();%:>select();]what();mul(978,885)!+select(195,899)~@*+mul(668when()'how(){>!#~}mul(449,440) !:]mul(908,330)mul(425,622)why()>[where()^**;,mul(373,419)from()%&'how()^,,^who()don't()@?&%select(491,38)mul(162+]*!:#^/ *+mul(390,994)select()#mul(244,23)@from()';where()mul (}when() )mul(16,801)/~^when()+)&-;when()mul(987,488)~@)mul(132,925)mul(959,924)@select(351,211)how()(-^}[mul(398,876)>,mul(492,208)how()what()?{who()where()'+mul(407,996)-)?where():mul(911,656);}/when()&mul(683,608)/why(574,363)mul(771,125)how()who()-~-#*?{&mul(832,987)mul(443*}+$mul(609,538)mul(949,408)how()mul(322,393)!$/&where()'mul(599,249)}#@ mul(858,751)why()+#what()>/-<from()mul(713,3)?why(482,825)&?&/*!*mul(256,486)select()<what()@mul(652,369)?{<select()why(),mul(836,865))<mul(454,939)%>:how()/how()?don't()when()when(){~/]mul(253,448)^^))mul(84>mul(85,415) ]})+why(40,365)}how()mul(11,381)how()%%who()where()why()mul(906,336)how()~where()-who():]where()select(239,576)why()mul(912,508)mul(24 ~^from(718,313)-@mul(517,16)@%mul(55,215) !what();*^/@mul(880,672)where(522,916)mul(804who()what()[(where(286,361)<select():(what()mul(155,258){!+!^mul(423,458)$how(615,130)'&select()don't()^{:$mul(326,138)^#(!mul(932,531)^?select()from()##who()how()who()mul+({<]#who()'{@mul(226,273)~/^why()<*why()mul(689,562)*mul(446,724)why()/when()when(869,266)do())why()mul(812,183)~from()%mul(971,441)when()%+?+^]mul(30,805))why()how()[from()mul(822,234),[?-%&](:$mul(440,835))when()&where()mul(12,352)])& ]-[{({mul(555,778)+mul(882,447)}:[!select()'mul(787,318)mul(539,118)$from()mul(511,100)+'~;+^^when()[mul(916,562)#+select()?]:~mul(506,622)]mul(778,105)(>@}^$:mul(51,378)({${,[from()}mul(543,793)}(}:[select()]mul(772,432)mul(253,865)(from()::?mul(150,306)<mul(62,389)who()#?when()~%/(!mul(146,73) -&#what()mul(114,144)<*&:{when()@how()from()]do(),>+< when()]when(78,385)]what()mul(681,911)}>what()mul(385,561)mul(97,729)$@mul(293,50):-@-mul(471,695)}where()-:^:}mul(566,792)&++[how()#mul(287,219)why()!mul(373,971)when()how()mul(154,605) ^mul(93,56)!@)@from()who(416,376)%$'[mul(472,481)^')select()when() {&mul(303,563)[;;@}~mul(167,624)mul(550,339{mul(626,174)'$;when()-[mul(11,151)how()select()&<when()!$where()<$mul(485,546)who()/(+,,who()#??mul(760,654)'when()why())when()%^do()?>-select())when()mul(951,26)mul(988[[/select()what(195,189)-mul(991,661)([}from()~:[why()^!mul(558,565)select()+*}mul(525,81)
?select()mul(457,497)from()who()[how()who()select(){:(>mul(273,631):)' )mul(433,659)/select()$ ??mul(996,214);'&>:(#!don't();<mul(720,546)when(827,349)<#<mul(143,489)mul(674,877)+&!what()'#mul(44})'from()+&where(){!~select(840,430)mul(212,347)why()@@~who()mul(969,631)why()where()select(887,765)%why()~/}}mul(519,309)'@}mulselect(606,267)~don't()'mul(216,53);^who()mul(71,582)[why()select())from()]%>from()mul(806,472)$;why()<who()&:){~mul}{ )! mul(143,398)mul(447,376)](> what()^,?don't()+-#what(220,900)]-from()mul(672,653)where()why()select(){why()*mul(394,630)mul(214,535)}(from()'from()!mul(304,752)who()'{from()from()%;@from(471,425)from()mul(431,414)?from(536,612)*don't()[<mul(679,373)]when()^mul(959,511)where()<[%mul(505,852)from()$!#do()++>mul(494,757),{@mul(864,136)why()%$ mul(901,770)(?how()! !mul(389,250)>:mul(107,240)how()+how(),mul(402,117)^:#,why(432,943)~mul(764,768)</-why()when()],why()$mul(300,720)->%/) mul(486,61)[from()% ~^}how(){mul(436,252))'mul(314,683)what()$@&)mul^what()(how()mul(356,528)+?] %)#mul(945,995);when(336,103)mul(904,121)'),mulwhy()why();why()@<*%+mul(173,177)mul(552,612);,select()%@mul(824,863)@from()mul(151,472)select()when()^}mul(381,33)mul(987,66)mul)+from()]]'mul(484,944),<how()~where()mul(904,715)mul(254,934)from())?!&^$,~mul(95,795)mul(317,265)~why()$;mul(964,988)##@mul(602,81)~from(){,mul(927,985</[+##mul(544,556)~(/how()~mul(816,799)when()[from()why()],mul(357,945)?%,(mul(513,777)from(104,28);>} mul(79,219)mul(645,343)+#select()#what()#>#mul(962,402)^,mul(170,849)+$/[],{ how()*mul!select()#how()do() ~[!{mul(132,291)from()when()^{mul(876,121);@&>?mul(14,405)select()}'why()^!mul(701,908)^]+what()how()%when(),{mul(163,570)why(),where(802,334)from()^mul(203,784)^select()who()^*@when()~/)mul(457,821)how()*!how()%#>[mul(911,205)*}];/]*!select()mul(209,380)why():*@*where()what()]who()mul(158,681)select()from()mul(913,623)select()?,>mul(692,963)>}mul(641,525)why()mul(107,645)from()(+mul(948,423)mul(497,166)from()%'mul(972,376)when()where()[[don't()~}/what()$*what()mul(205,460)</:#@*how()mul(541,537)]mul(974,76)[{)^ {(mul(985,506)(#@why()mul(105,151)from()how():{select()mul(726,399))#(how()mul(166,283);+([~-!,don't()-how()mul(814,281),who(244,221)<^:%:^)how()mul(46,257), @mul(620,932)>,-%:-mul(212,248)when()select()mul(511,961)who()who(694,88)>mul(725,998(<]mul(881,682)select()select()mul(392,740)$>)mul(794,79),;$mul/:};#(>/)mul(60,633)['!~how())who(){$mul(757,172)%how()what()how(),mul(19,116)-'?who();where()when()who():mul(201!]how()-'{#where()<+what()mul(848,314)->from()mul(366,508;^[%why(10,776){~mul(403,696)(~{))why()/mul(61,507),+ }mul(771,565)-}@)mul(726,28)*;when()-$!:,[&mul(672,226)}?]*do()when()[mul(749,250)(mul(514,431)~*when()%what()'how(204,98)how()where()mul(529[]}~mul(204,564)what()++<]}&select()mul(459,244)what()mul(687,827)?when()<~,]<?~<mul(448,423)%mul(660,452)what()mul(111,31),/mul(485,116)select();*>%$+<<*mul(403,7)how()what()^mul(433,321)}%do()where(436,974)^/,+what()who() mul(338,162):(mul(876,575)%why()!+;/^why()mul(588,29)(how()select(350,689)+'^-:-&mul(694,2)what()mul(997,566)from()!]%'?;<-why()mul(540,192)^from()*<):~do()what()from()/{/mul(236,520)#>when()*#)(mul(243,137)mul(483,202)('who()do()when(){>$$what()&)']mul(763,83)>who(744,412)*^who()*) don't()mul(948,448)(:mul(867,155)^^***,+}-^mul(510,656),,;:[^[!mul(37,392where()[mul(67,386)'(^!,~mul+~(+ how(321,247)}$*mul(632,944)
{how()mul,how()when()+when()}what()mul(900,270)^:,where()mul(489,842){!what()when()#!mul(243,646)!where()*when();who()mul(67,231)select()*select()do()how()$(**,+how();mul(472,391)select()@'how(630,875)who()>mul(83,172);+$where()+~~mul(163,367)<mul(788,607)from()?&]what() mul(780,691)/@when()((who()+~?mul(323,888)mul(67,878),,):>mul(10,776) ({select()select()~*[mul(216,443)-)select()::(-?@select()mul(938,86)mul(238,475)where() }<(don't() +>;mul(491,189)~[/#;mul(687,66)$+]'-don't()+when()&+$;-]mul(605,671)?;mul(8,465)when()<~:^(what(549,164)[mul(253,71)([?where()from()why()?when()$mul(885,722)~~>what()select()]@%>mul(12,734)(/)[where()select(649,213)from(945,849)(*%mul(948/when()mul(490,837)(@where()'what()}what()why()mul(906,59)when()how()#select(),:}do():#mulwhat(918,618);mul(290,290)mul(894,51)?mul(230,518)*,;select()mul(366,247)[]from(946,647)&!^where()where()how(),mul(94,114)mul(275,889)when(){$#[<?<$when()mul(172,248)$)where()what()mul(292,19)<why()/@@[$@mul(715,134))why()~}'how()~mul(405,534)mul(827,178)when()-mul(349,293){},${[;from()(what()mul(851,954)mul(384,35)$#/mul?+%&,mul(334,901)why()~~(&from()[]mul(497,387)select()!{)]select()when():!mul(57,56)~$**}^how()mul(952,706)~+!what()#$@}]don't()]mul(884,597)+[&(^{what()where()~mul(617,23)what(806,100)where(660,881);)}!don't()$<}mul(630,77))*+mul(366,51,%%:*^+mul(128,254)why()-what()!'where()+%mul(356,640)('(mul(366,919),,how()!why()when()who()%]mul(414,493)&from()?[mul(810,596)>mul(892,356)&[-mul(303,485)*select()how()''mul(738,220)!@mul(371,794)where()mul(380,261)mul(210,796): *{$]why()how()?mul(615,74)select()from()do()from()*how()/'mul(507,36)what()when()#]?#{-mul(398,229)select()}mul(844,299)!<;#^%]+,when()mul(4,527)#when()##!%]when()(mul(708,803)}/when()why(514,182)({mul(336,134);,[}/:mul(899,874)select()how()]#mul(548,253)>^~mul(294,767)#^* mul(444,302)where()how()]{]select()!where()!mul(906,663)mul(656,596){[ & ;^+%-mul(108,609)who()+(why()/how()(@don't()'{-from() mul(364,848),^$ ?]  +:mul(889,175)mul(660,583)*!@mul(423,213)mul(311,390)%how()?!{mul(738,520)mul(97,84)?mul(423,763)<'?mul(15,141)mul(300,197)>select()%when()mul(640,732)^}mul(919,588)(}<!select()&}select()select()mul(655,724)),mul(271,552)don't()from()mul(364,12)(%[why(): ]when()mul(106,517)((select()mul(800,445)@when()']mul(325,316)>how(),-]how(),<don't()/+who()<,select(){mul(292,951)mul(966,75)@@?}{+~from();mul(472,867) :*&?/mul(408,687)!+[][[!?$mul(211,912)who()<}mul(826,742)/mul(362,601))mul(823,393)when()~select()!what()mul(144,414)~mul(743,461)*~who()]select()mul(579,413)why(),,?mul(690,917)]<)where()@]%%mul(774,571){!*@don't()^from()how();@~$mul(317,142)select(161,55)mul(636,392)}mul(538,552) when()'#$#mul(580,654){when(46,367)'}]select())mul(775,934)who()%%>select()!select()what()from()mul(231,907)where(799,691)-,:)@]mul(336,972)<what()~* {#-:;mul(500,188)$$%]&!$mul(938,24)*^?)mul(576,582),($how()/when() !mul(701,946)~#^<don't())mul(982,103)?how()* ^from(507,869)'who()select()mul(107,848)why() ')when()when()select(903,770)#who()mul(367,164)}how()mul(869,254)mul(993,910);;mul(969,393)who()<select() :select()?&'[mul(273,219)who());%%^!!-mul(464,515)&;{why()<<)'*mul(73,753)],-/mul(263,676)what()"""

mul_pattern = r"mul\((\d+),(\d+)\)"  
state_pattern = r"(do\(\)|don't\(\))"  

instructions = re.findall(f"{mul_pattern}|{state_pattern}", data)

enabled = True 
total_sum = 0

for instruction in instructions:
    if instruction[2]:
        if instruction[2] == "do()":
            enabled = True
        elif instruction[2] == "don't()":
            enabled = False
    elif instruction[0] and instruction[1]:  
        x, y = int(instruction[0]), int(instruction[1])
        if enabled:
            total_sum += x * y

print("Sum of enabled multiplications:", total_sum)