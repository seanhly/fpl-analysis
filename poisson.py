from math import e, factorial
from re import sub, match
from unicodedata import normalize
from numpy import random

def fake_to_actual(fake_p):
    """
    a = -0.01146
    b = 0.99901
    c = 1.06076
    return a + b * fake_p ** c;
    """
    return fake_p

PLAYERS = [
	[15157, "MID", "james milner", "brighton"],
	[17761, "DEF", "james tarkowski", "everton"],
	[21205, "GKP", "tom heaton", "man utd"],
	[37096, "GKP", "lukasz fabianski", "west ham"],
	[44699, "FWD", "ashley barnes", "burnley"],
	[49262, "GKP", "jason steele", "brighton"],
	[50175, "FWD", "danny welbeck", "brighton"],
	[51943, "GKP", "václav hladký", "burnley"],
	[54469, "DEF", "adam smith", "bournemouth"],
	[56979, "MID", "jordan henderson", "brentford"],
	[57328, "DEF", "nathaniel clyne", "crystal palace"],
	[58621, "DEF", "kyle walker", "burnley"],
	[59735, "GKP", "karl darlow", "leeds"],
	[59859, "MID", "ilkay gündoğan", "man city"],
	[59949, "DEF", "séamus coleman", "everton"],
	[60689, "FWD", "chris wood", "nott'm forest"],
	[61256, "MID", "carlos henrique casimiro", "man utd"],
	[67089, "GKP", "martin dúbravka", "burnley"],
	[69752, "GKP", "norberto murara neto", "bournemouth"],
	[72147, "GKP", "marco bizot", "aston villa"],
	[74854, "GKP", "simon moore", "sunderland"],
	[75115, "FWD", "callum wilson", "west ham"],
	[76357, "MID", "tom cairney", "fulham"],
	[77794, "DEF", "kieran trippier", "newcastle"],
	[78916, "DEF", "dan burn", "newcastle"],
	[79602, "GKP", "daniel bentley", "wolves"],
	[80201, "GKP", "bernd leno", "fulham"],
	[80801, "MID", "idrissa gana gueye", "everton"],
	[81441, "GKP", "mark gillespie", "newcastle"],
	[82143, "GKP", "wes foderingham", "west ham"],
	[83299, "DEF", "lewis dunk", "brighton"],
	[84182, "GKP", "alphonse areola", "west ham"],
	[84450, "MID", "granit xhaka", "sunderland"],
	[85633, "GKP", "matz sels", "nott'm forest"],
	[85971, "MID", "son heung-min", "spurs"],
	[86873, "GKP", "benjamin lecomte", "fulham"],
	[87835, "DEF", "matt doherty", "wolves"],
	[88248, "GKP", "stefan ortega moreno", "man city"],
	[88894, "MID", "ross barkley", "aston villa"],
	[90585, "DEF", "willy boly", "nott'm forest"],
	[91651, "MID", "mateo kovačić", "man city"],
	[91889, "FWD", "niclas füllkrug", "west ham"],
	[95658, "DEF", "harry maguire", "man utd"],
	[97032, "DEF", "virgil van dijk", "liverpool"],
	[97299, "DEF", "john stones", "man city"],
	[97846, "GKP", "alex cairns", "leeds"],
	[98747, "GKP", "nick pope", "newcastle"],
	[98980, "GKP", "emiliano martínez romero", "aston villa"],
	[101148, "DEF", "jamaal lascelles", "newcastle"],
	[101178, "MID", "james ward-prowse", "west ham"],
	[101188, "DEF", "lucas digne", "aston villa"],
	[101982, "GKP", "sam johnstone", "wolves"],
	[102057, "FWD", "raúl jiménez rodríguez", "fulham"],
	[105717, "DEF", "arthur masuaku", "sunderland"],
	[106468, "DEF", "álex moreno lopera", "aston villa"],
	[106611, "DEF", "michael keane", "everton"],
	[106617, "FWD", "patrick bamford", "leeds"],
	[106760, "DEF", "luke shaw", "man utd"],
	[107265, "GKP", "angus gunn", "nott'm forest"],
	[108413, "MID", "will hughes", "crystal palace"],
	[109345, "MID", "solly march", "brighton"],
	[109533, "DEF", "emerson palmieri dos santos", "west ham"],
	[109646, "DEF", "tosin adarabioyo", "chelsea"],
	[109745, "GKP", "kepa arrizabalaga revuelta", "arsenal"],
	[110504, "MID", "bertrand traoré", "sunderland"],
	[110735, "DEF", "adam webster", "brighton"],
	[111234, "GKP", "jordan pickford", "everton"],
	[111317, "MID", "david brooks", "bournemouth"],
	[111452, "GKP", "odysseas vlachodimos", "newcastle"],
	[111478, "DEF", "joël veltman", "brighton"],
	[111773, "DEF", "emil krafth", "newcastle"],
	[113564, "DEF", "sam byram", "leeds"],
	[114243, "MID", "jacob murphy", "newcastle"],
	[114283, "MID", "jack grealish", "everton"],
	[115556, "DEF", "ben davies", "spurs"],
	[116216, "MID", "leandro trossard", "arsenal"],
	[116535, "GKP", "alisson becker", "liverpool"],
	[118748, "MID", "mohamed salah", "liverpool"],
	[119471, "DEF", "fabian schär", "newcastle"],
	[121160, "GKP", "ederson santana de moraes", "man city"],
	[121709, "GKP", "walter benítez", "crystal palace"],
	[122074, "GKP", "marcus bettinelli", "man city"],
	[122798, "DEF", "andrew robertson", "liverpool"],
	[122806, "MID", "john mcginn", "aston villa"],
	[124165, "MID", "patrick roberts", "sunderland"],
	[126184, "DEF", "nathan aké", "man city"],
	[128295, "MID", "christian nørgaard", "arsenal"],
	[135720, "DEF", "kevin danso", "spurs"],
	[138001, "GKP", "tom king", "everton"],
	[141746, "MID", "bruno borges fernandes", "man utd"],
	[149065, "GKP", "josé malheiro de sá", "wolves"],
	[149484, "DEF", "tyrone mings", "aston villa"],
	[149519, "MID", "maxwel cornet", "west ham"],
	[151589, "MID", "leander dendoncker", "aston villa"],
	[152551, "MID", "jefferson lerma solís", "crystal palace"],
	[153127, "MID", "isaac hayden", "newcastle"],
	[153133, "MID", "alex iwobi", "fulham"],
	[153366, "MID", "harrison reed", "fulham"],
	[153682, "MID", "harry wilson", "fulham"],
	[154296, "MID", "joão maria lobo alves palhares costa palhinha gonçalves", "spurs"],
	[154561, "GKP", "david raya martín", "arsenal"],
	[154566, "FWD", "dominic solanke-mitchell", "spurs"],
	[155405, "MID", "kalvin phillips", "man city"],
	[155408, "MID", "lewis cook", "bournemouth"],
	[155503, "GKP", "freddie woodman", "liverpool"],
	[156074, "DEF", "rob holding", "crystal palace"],
	[156689, "MID", "andreas hoelgebaum pereira", "fulham"],
	[158499, "MID", "ryan christie", "bournemouth"],
	[158534, "DEF", "kyle walker-peters", "west ham"],
	[158983, "MID", "endo wataru", "liverpool"],
	[159506, "DEF", "ola aina", "nott'm forest"],
	[159533, "MID", "adama traoré diarra", "fulham"],
	[165809, "MID", "bernardo mota veiga de carvalho e silva", "man city"],
	[166477, "DEF", "timothy castagne", "fulham"],
	[166989, "MID", "youri tielemans", "aston villa"],
	[167074, "DEF", "kenny tete", "fulham"],
	[167512, "DEF", "luke o'nien", "sunderland"],
	[167887, "MID", "josh laurent", "burnley"],
	[168636, "FWD", "enes ünal", "bournemouth"],
	[168991, "MID", "philip billing", "bournemouth"],
	[169359, "DEF", "matt targett", "newcastle"],
	[169528, "DEF", "antonee robinson", "fulham"],
	[169593, "GKP", "remi matthews", "crystal palace"],
	[171287, "DEF", "joe gomez", "liverpool"],
	[171314, "DEF", "rúben dos santos gato alves dias", "man city"],
	[171422, "MID", "alan browne", "sunderland"],
	[172567, "MID", "josh cullen", "burnley"],
	[172649, "GKP", "dean henderson", "crystal palace"],
	[172780, "MID", "james maddison", "spurs"],
	[174592, "MID", "marcus edwards", "burnley"],
	[174594, "FWD", "lukas nmecha", "leeds"],
	[174874, "DEF", "joachim andersen", "fulham"],
	[176297, "MID", "marcus rashford", "man utd"],
	[177815, "FWD", "dominic calvert-lewin", "leeds"],
	[178186, "FWD", "jarrod bowen", "west ham"],
	[178301, "FWD", "ollie watkins", "aston villa"],
	[179268, "DEF", "marc cucurella saseta", "chelsea"],
	[179458, "MID", "jacob bruun larsen", "burnley"],
	[180135, "MID", "sean longstaff", "leeds"],
	[180736, "DEF", "trevoh chalobah", "chelsea"],
	[180804, "DEF", "axel tuanzebe", "burnley"],
	[180974, "MID", "joelinton cássio apolinário de lira", "newcastle"],
	[181284, "MID", "gonçalo manuel ganchinho guedes", "wolves"],
	[183656, "MID", "josh dasilva", "brentford"],
	[183751, "MID", "manuel benson hedilazio", "burnley"],
	[184029, "MID", "martin ødegaard", "arsenal"],
	[184254, "GKP", "guglielmo vicario", "spurs"],
	[184341, "MID", "mason mount", "man utd"],
	[184349, "MID", "ryan sessegnon", "fulham"],
	[184667, "DEF", "victor lindelöf", "aston villa"],
	[184754, "MID", "hwang hee-chan", "wolves"],
	[191866, "DEF", "kristoffer ajer", "brentford"],
	[192290, "DEF", "connor roberts", "burnley"],
	[194010, "DEF", "rico henry", "brentford"],
	[195384, "MID", "mikel merino zazón", "arsenal"],
	[195546, "MID", "emiliano buendía stati", "aston villa"],
	[197024, "MID", "guido rodríguez", "west ham"],
	[198869, "DEF", "benjamin white", "arsenal"],
	[199598, "MID", "ethan ampadu", "leeds"],
	[199670, "FWD", "odsonne édouard", "crystal palace"],
	[199796, "DEF", "matty cash", "aston villa"],
	[199798, "DEF", "ezri konsa ngoyo", "aston villa"],
	[200089, "MID", "joe willock", "newcastle"],
	[200617, "MID", "daniel james", "leeds"],
	[200641, "MID", "reiss nelson", "brentford"],
	[200720, "GKP", "caoimhín kelleher", "brentford"],
	[200785, "MID", "tyler adams", "bournemouth"],
	[200834, "DEF", "nordi mukiele", "sunderland"],
	[201595, "GKP", "lucas estella perri", "leeds"],
	[201658, "MID", "marcus tavernier", "bournemouth"],
	[201666, "MID", "harvey barnes", "newcastle"],
	[201895, "DEF", "omar alderete", "sunderland"],
	[202641, "GKP", "andré onana", "man utd"],
	[202993, "MID", "rodrigo bentancur", "spurs"],
	[204120, "DEF", "olivier boscagli", "brighton"],
	[204214, "DEF", "pervis estupiñán tenorio", "brighton"],
	[204480, "MID", "declan rice", "arsenal"],
	[204580, "MID", "vitaly janelt", "brentford"],
	[204646, "MID", "donyell malen", "aston villa"],
	[204716, "DEF", "ibrahima konaté", "liverpool"],
	[204822, "DEF", "omar richards", "nott'm forest"],
	[204936, "GKP", "gianluigi donnarumma", "man city"],
	[204968, "MID", "ryan yates", "nott'm forest"],
	[205533, "FWD", "eddie nketiah", "crystal palace"],
	[205651, "FWD", "gabriel fernando de jesus", "arsenal"],
	[206325, "DEF", "oleksandr zinchenko", "nott'm forest"],
	[206915, "MID", "curtis jones", "liverpool"],
	[207189, "MID", "sander berge", "fulham"],
	[207283, "MID", "mathias jensen", "brentford"],
	[208706, "MID", "bruno guimarães rodriguez moura", "newcastle"],
	[208912, "DEF", "joe worrall", "burnley"],
	[209036, "DEF", "marc guéhi", "crystal palace"],
	[209046, "MID", "callum hudson-odoi", "nott'm forest"],
	[209243, "MID", "jadon sancho", "aston villa"],
	[209244, "MID", "phil foden", "man city"],
	[209288, "GKP", "tom mcgill", "brighton"],
	[209289, "MID", "emile smith rowe", "fulham"],
	[209365, "DEF", "matthijs de ligt", "man utd"],
	[209400, "MID", "daichi kamada", "crystal palace"],
	[210156, "FWD", "taiwo awoniyi", "nott'm forest"],
	[210462, "MID", "ibrahim sangaré", "nott'm forest"],
	[210494, "DEF", "nayef aguerd", "west ham"],
	[211975, "DEF", "manuel akanji", "man city"],
	[212314, "MID", "saša lukić", "fulham"],
	[212319, "FWD", "richarlison de andrade", "spurs"],
	[213198, "MID", "christopher nkunku", "chelsea"],
	[213999, "MID", "edson álvarez velázquez", "west ham"],
	[214048, "DEF", "maximilian kilman", "west ham"],
	[214225, "DEF", "joe rodon", "leeds"],
	[214285, "DEF", "konstantinos tsimikas", "liverpool"],
	[214572, "GKP", "brandon austin", "spurs"],
	[214590, "DEF", "aaron wan-bissaka", "west ham"],
	[215059, "GKP", "robert lynch sánchez", "chelsea"],
	[215136, "DEF", "neco williams", "nott'm forest"],
	[215379, "MID", "elliot anderson", "nott'm forest"],
	[215413, "MID", "kiernan dewsbury-hall", "everton"],
	[215439, "MID", "tomáš souček", "west ham"],
	[215460, "MID", "ian poveda-ocampo", "sunderland"],
	[215711, "MID", "leon bailey", "aston villa"],
	[216051, "DEF", "diogo dalot teixeira", "man utd"],
	[216055, "MID", "florentino ibrain morris luís", "burnley"],
	[216094, "DEF", "jeremie frimpong", "liverpool"],
	[216646, "FWD", "yoane wissa", "newcastle"],
	[218328, "MID", "samuel chukwueze", "fulham"],
	[218364, "DEF", "borna sosa", "crystal palace"],
	[219168, "FWD", "alexander isak", "liverpool"],
	[219249, "MID", "matt o'riley", "brighton"],
	[219847, "FWD", "kai havertz", "arsenal"],
	[219924, "DEF", "issa diop", "fulham"],
	[219937, "DEF", "rhys williams", "liverpool"],
	[220237, "DEF", "sven botman", "newcastle"],
	[220566, "MID", "rodrigo 'rodri' hernandez cascante", "man city"],
	[220598, "FWD", "michael obafemi", "burnley"],
	[220627, "DEF", "james justin", "leeds"],
	[220684, "DEF", "aji alese", "sunderland"],
	[220695, "MID", "paris maghoma", "brentford"],
	[221389, "GKP", "john victor maciel furtado", "nott'm forest"],
	[221399, "MID", "jack harrison", "leeds"],
	[221466, "DEF", "marcos senesi barón", "bournemouth"],
	[221632, "DEF", "cristian romero", "spurs"],
	[221820, "DEF", "lisandro martínez", "man utd"],
	[222531, "MID", "morgan gibbs-white", "nott'm forest"],
	[222683, "MID", "justin kluivert", "bournemouth"],
	[222690, "DEF", "tyrell malacia", "man utd"],
	[222694, "DEF", "pascal struijk", "leeds"],
	[223094, "FWD", "erling haaland", "man city"],
	[223336, "MID", "dan neil", "sunderland"],
	[223340, "MID", "bukayo saka", "arsenal"],
	[223434, "DEF", "igor julio dos santos de paulo", "west ham"],
	[223541, "MID", "federico chiesa", "liverpool"],
	[223827, "DEF", "daniel ballard", "sunderland"],
	[223911, "DEF", "chris mepham", "bournemouth"],
	[224024, "MID", "lucas tolentino coelho de lima", "west ham"],
	[224068, "GKP", "matt turner", "nott'm forest"],
	[224117, "FWD", "viktor gyökeres", "arsenal"],
	[224967, "DEF", "vitalii mykolenko", "everton"],
	[224995, "MID", "luis sinisterra lucumí", "bournemouth"],
	[225321, "GKP", "aaron ramsdale", "newcastle"],
	[225796, "DEF", "reece james", "chelsea"],
	[226182, "DEF", "jayden bogle", "leeds"],
	[226597, "DEF", "gabriel dos santos magalhães", "arsenal"],
	[226944, "MID", "boubacar kamara", "aston villa"],
	[226956, "DEF", "mads roerslev rasmussen", "brentford"],
	[227127, "MID", "yves bissouma", "spurs"],
	[227444, "DEF", "nikola milenković", "nott'm forest"],
	[229384, "MID", "andy irving", "west ham"],
	[229600, "GKP", "mark travers", "everton"],
	[230001, "DEF", "noussair mazraoui", "man utd"],
	[230046, "MID", "douglas luiz soares de paulo", "nott'm forest"],
	[230376, "MID", "jhon arias", "wolves"],
	[231057, "MID", "jean-ricner bellegarde", "wolves"],
	[231065, "DEF", "ethan pinnock", "brentford"],
	[231416, "DEF", "ferdi kadıoğlu", "brighton"],
	[231480, "DEF", "santiago ignacio bueno", "wolves"],
	[231747, "FWD", "jean-philippe mateta", "crystal palace"],
	[232112, "MID", "manuel ugarte ribeiro", "man utd"],
	[232185, "MID", "ismaïla sarr", "crystal palace"],
	[232413, "MID", "eberechi eze", "arsenal"],
	[232571, "GKP", "anthony patterson", "sunderland"],
	[232653, "MID", "jacob ramsey", "newcastle"],
	[232792, "DEF", "tariq lamptey", "brighton"],
	[232820, "DEF", "joe anderson", "sunderland"],
	[232826, "MID", "anthony gordon", "newcastle"],
	[232859, "DEF", "djed spence", "spurs"],
	[232892, "DEF", "calvin bassey", "fulham"],
	[232928, "MID", "james garner", "everton"],
	[233963, "DEF", "konstantinos mavropanos", "west ham"],
	[235448, "GKP", "ellery balcombe", "brentford"],
	[235674, "MID", "manor solomon", "spurs"],
	[235826, "FWD", "joël piroe", "leeds"],
	[240299, "MID", "joe hodge", "wolves"],
	[240514, "GKP", "kjell scherpen", "brighton"],
	[241231, "DEF", "jordan beyer", "burnley"],
	[242880, "DEF", "benoît badiashile mukinayi", "chelsea"],
	[242882, "DEF", "bafodé diakité", "bournemouth"],
	[242898, "MID", "brennan johnson", "spurs"],
	[243016, "MID", "alexis mac allister", "liverpool"],
	[243298, "MID", "cody gakpo", "liverpool"],
	[243345, "MID", "lewis o'brien", "nott'm forest"],
	[243526, "DEF", "gabriel gudmundsson", "leeds"],
	[243571, "DEF", "nathan patterson", "everton"],
	[244042, "FWD", "rodrigo muniz carvalho", "fulham"],
	[244723, "DEF", "tyrick mitchell", "crystal palace"],
	[244731, "MID", "luis díaz marulanda", "liverpool"],
	[244850, "MID", "morgan rogers", "aston villa"],
	[244851, "MID", "cole palmer", "chelsea"],
	[244858, "MID", "fábio freitas gouveia carvalho", "brentford"],
	[244954, "DEF", "pau torres", "aston villa"],
	[246301, "DEF", "jorge cuenca barreno", "fulham"],
	[247245, "DEF", "hannes delcroix", "burnley"],
	[247348, "DEF", "daniel muñoz mejía", "crystal palace"],
	[247412, "FWD", "jørgen strand larsen", "wolves"],
	[247632, "MID", "pedro lomba neto", "chelsea"],
	[247693, "FWD", "randal kolo muani", "spurs"],
	[247955, "DEF", "lutsharel geertruida", "sunderland"],
	[248056, "MID", "tanaka ao", "leeds"],
	[248857, "MID", "noni madueke", "arsenal"],
	[248875, "MID", "jérémy doku", "man city"],
	[248937, "MID", "sam greenwood", "leeds"],
	[249231, "DEF", "keane lewis-potter", "brentford"],
	[250199, "MID", "nicolás domínguez", "nott'm forest"],
	[250735, "MID", "darko churlinov", "burnley"],
	[424044, "MID", "hamed traorè", "bournemouth"],
	[424876, "MID", "dominik szoboszlai", "liverpool"],
	[427623, "DEF", "chris richards", "crystal palace"],
	[427637, "MID", "brenden aaronson", "leeds"],
	[428580, "MID", "frank onyeka", "brentford"],
	[428971, "GKP", "steven benda", "fulham"],
	[429414, "FWD", "saša kalajdžić", "wolves"],
	[430871, "MID", "matheus santos carneiro da cunha", "man utd"],
	[431248, "DEF", "ladislav krejcí", "wolves"],
	[431639, "FWD", "zian flemming", "burnley"],
	[432422, "MID", "sandro tonali", "newcastle"],
	[432714, "MID", "james mcatee", "nott'm forest"],
	[432720, "GKP", "james trafford", "man city"],
	[432830, "DEF", "nathan collins", "brentford"],
	[433036, "MID", "tijjani reijnders", "man city"],
	[433154, "MID", "dwight mcneil", "everton"],
	[433312, "MID", "marshall munetsi", "wolves"],
	[433952, "MID", "largie ramazani", "leeds"],
	[434399, "DEF", "reinildo mandava", "sunderland"],
	[434752, "DEF", "jaka bijol", "leeds"],
	[435973, "FWD", "lyle foster", "burnley"],
	[435997, "MID", "noah okafor", "leeds"],
	[436234, "MID", "bryan gil salvatierra", "spurs"],
	[436893, "DEF", "julián araujo zúñiga", "bournemouth"],
	[437495, "GKP", "illan meslier", "leeds"],
	[437499, "DEF", "maxence lacroix", "crystal palace"],
	[437505, "FWD", "wilson isidor", "sunderland"],
	[437730, "MID", "antoine semenyo", "bournemouth"],
	[437738, "DEF", "sebastiaan bornauw", "leeds"],
	[437742, "MID", "albert sambi lokonga", "arsenal"],
	[437748, "MID", "mike trésor ndayishimiye", "burnley"],
	[438098, "MID", "fábio ferreira vieira", "arsenal"],
	[438234, "MID", "omar marmoush", "man city"],
	[438464, "MID", "cheick doucouré", "crystal palace"],
	[439135, "DEF", "eiran cashin", "brighton"],
	[440089, "MID", "mikkel damsgaard", "brentford"],
	[440148, "MID", "tyler morton", "liverpool"],
	[440323, "FWD", "armando broja", "burnley"],
	[440854, "DEF", "jakub kiwior", "arsenal"],
	[440955, "FWD", "nazarii rusyn", "sunderland"],
	[440993, "MID", "iliman ndiaye", "everton"],
	[441024, "DEF", "harrison ashby", "newcastle"],
	[441164, "DEF", "pedro porro sauceda", "spurs"],
	[441191, "DEF", "tino livramento", "newcastle"],
	[441192, "MID", "jeremy sarmiento morante", "brighton"],
	[441240, "MID", "romain faivre", "bournemouth"],
	[441264, "FWD", "brian brobbey", "sunderland"],
	[441266, "MID", "ryan gravenberch", "liverpool"],
	[441271, "DEF", "ki-jana hoever", "wolves"],
	[441302, "DEF", "ian maatsen", "aston villa"],
	[444102, "FWD", "francisco evanilson de lima barbosa", "bournemouth"],
	[444145, "MID", "gabriel martinelli silva", "arsenal"],
	[444172, "GKP", "will dennis", "bournemouth"],
	[444180, "MID", "jaidon anthony", "burnley"],
	[444463, "DEF", "wesley fofana", "chelsea"],
	[444765, "DEF", "sepp van den berg", "brentford"],
	[444884, "MID", "harvey elliott", "aston villa"],
	[445044, "MID", "dejan kulusevski", "spurs"],
	[445122, "DEF", "jurriën timber", "arsenal"],
	[446008, "MID", "bryan mbeumo", "man utd"],
	[447203, "FWD", "darwin núñez ribeiro", "liverpool"],
	[447325, "GKP", "harry tyrer", "everton"],
	[447715, "MID", "aaron ramsey", "burnley"],
	[448047, "MID", "enzo fernández", "chelsea"],
	[448089, "MID", "joão victor gomes da silva", "wolves"],
	[448104, "DEF", "piero hincapié", "arsenal"],
	[448514, "DEF", "rayan aït-nouri", "man city"],
	[449027, "GKP", "giorgi mamardashvili", "liverpool"],
	[449434, "MID", "anthony elanga", "newcastle"],
	[449871, "MID", "amadou onana", "aston villa"],
	[449988, "FWD", "fábio soares silva", "wolves"],
	[450070, "MID", "crysencio summerville", "west ham"],
	[450072, "DEF", "shurandy sambo", "burnley"],
	[450535, "MID", "malcolm ebiowei", "crystal palace"],
	[450539, "MID", "myles peart-harris", "brentford"],
	[450542, "MID", "jesurun rak-sakyi", "crystal palace"],
	[451302, "GKP", "altay bayındır", "man utd"],
	[451340, "MID", "mitoma kaoru", "brighton"],
	[451432, "DEF", "david mota veiga teixeira do carmo", "nott'm forest"],
	[456512, "MID", "dan ndoye", "nott'm forest"],
	[457569, "GKP", "đorđe petrović", "bournemouth"],
	[458249, "FWD", "joshua zirkzee", "man utd"],
	[458297, "MID", "pierre ekwah elimby", "sunderland"],
	[460028, "DEF", "levi samuels colwill", "chelsea"],
	[460842, "MID", "mohammed kudus", "spurs"],
	[461188, "DEF", "bashir humphreys", "burnley"],
	[461195, "DEF", "dennis cirkin", "sunderland"],
	[461199, "MID", "romaine mundle", "sunderland"],
	[461421, "MID", "lewis dobbin", "aston villa"],
	[461446, "MID", "tyler onyango", "everton"],
	[461484, "MID", "joe white", "newcastle"],
	[461537, "GKP", "dermot mee", "man utd"],
	[461567, "DEF", "owen dodgson", "burnley"],
	[462116, "DEF", "jean-clair todibo", "west ham"],
	[462381, "GKP", "filip marschall", "aston villa"],
	[462424, "DEF", "william saliba", "arsenal"],
	[462492, "GKP", "joe gauci", "aston villa"],
	[462635, "MID", "joe gelhardt", "leeds"],
	[463034, "FWD", "liam delap", "chelsea"],
	[463067, "MID", "georginio rutter", "brighton"],
	[463748, "GKP", "karl hein", "arsenal"],
	[463936, "MID", "jamie bynoe-gittens", "chelsea"],
	[463981, "DEF", "james hill", "bournemouth"],
	[465247, "GKP", "senne lammens", "man utd"],
	[465351, "DEF", "matheus nunes", "man city"],
	[465527, "MID", "hannibal mejbri", "burnley"],
	[465642, "DEF", "malick thiaw", "newcastle"],
	[465680, "FWD", "arnaud kalimuendo", "nott'm forest"],
	[465694, "MID", "nico gonzález iglesias", "man city"],
	[465702, "DEF", "timothée pembélé", "sunderland"],
	[465730, "DEF", "maxim de cuyper", "brighton"],
	[465920, "MID", "mykhailo mudryk", "chelsea"],
	[466052, "MID", "rayan cherki", "man city"],
	[466075, "DEF", "riccardo calafiori", "arsenal"],
	[466117, "MID", "naouirou ahamada", "crystal palace"],
	[466525, "MID", "anton stach", "leeds"],
	[467169, "MID", "antony dos santos", "man utd"],
	[467189, "GKP", "mads hermansen", "west ham"],
	[467779, "MID", "mats wieffer", "brighton"],
	[469142, "DEF", "jan paul van hecke", "brighton"],
	[469247, "MID", "samuel iling-junior", "aston villa"],
	[469272, "MID", "loum tchaouna", "burnley"],
	[470294, "MID", "darko gyabi", "leeds"],
	[470313, "FWD", "nick woltemade", "newcastle"],
	[471798, "GKP", "gabriel słonina", "chelsea"],
	[472713, "DEF", "aaron hickey", "brentford"],
	[472739, "GKP", "carl rushworth", "brighton"],
	[472769, "DEF", "nico o'reilly", "man city"],
	[474120, "MID", "julio enciso espínola", "brighton"],
	[474907, "DEF", "reece welch", "everton"],
	[475123, "GKP", "carlos miguel dos santos pereira", "nott'm forest"],
	[475168, "FWD", "joão pedro junqueira de jesus", "chelsea"],
	[476502, "MID", "boubacar traoré", "wolves"],
	[476887, "MID", "dilane bakwa", "nott'm forest"],
	[477064, "DEF", "rico lewis", "man city"],
	[477424, "DEF", "joško gvardiol", "man city"],
	[477547, "DEF", "leo fuhr hjelde", "sunderland"],
	[477555, "MID", "oscar bobb", "man city"],
	[477580, "DEF", "illia zabarnyi", "bournemouth"],
	[477717, "DEF", "maxime estève", "burnley"],
	[477851, "MID", "abdoullah ba", "sunderland"],
	[478969, "DEF", "hjalmar ekdal", "burnley"],
	[480455, "DEF", "jarrad branthwaite", "everton"],
	[481283, "GKP", "james wright", "aston villa"],
	[481655, "MID", "martín zubimendi ibáñez", "arsenal"],
	[482442, "MID", "pape matar sarr", "spurs"],
	[482609, "DEF", "malo gusto", "chelsea"],
	[482973, "FWD", "igor jesus maciel da cruz", "nott'm forest"],
	[483081, "DEF", "rodrigo martins gomes", "wolves"],
	[483364, "GKP", "krisztián hegyi", "west ham"],
	[484420, "MID", "enzo le fée", "sunderland"],
	[485047, "DEF", "felipe rodrigues da silva", "nott'm forest"],
	[485055, "GKP", "antonín kinský", "spurs"],
	[485337, "MID", "evann guessand", "aston villa"],
	[485711, "FWD", "benjamin sesko", "man utd"],
	[486385, "FWD", "norberto bercique gomes betuncal", "everton"],
	[486520, "MID", "ilia gruev", "leeds"],
	[486672, "MID", "moisés caicedo corozo", "chelsea"],
	[487053, "DEF", "destiny udogie", "spurs"],
	[487117, "FWD", "evan ferguson", "brighton"],
	[487676, "DEF", "trai hume", "sunderland"],
	[487702, "MID", "luca koleosho", "burnley"],
	[487838, "DEF", "lewis hall", "newcastle"],
	[488024, "MID", "yéremy pino santos", "crystal palace"],
	[488213, "FWD", "tolu arokodare", "wolves"],
	[489571, "GKP", "etienne green", "burnley"],
	[489580, "DEF", "calvin ramsay", "liverpool"],
	[489639, "GKP", "bart verbruggen", "brighton"],
	[489706, "MID", "justin devenny", "crystal palace"],
	[489888, "MID", "amine adli", "bournemouth"],
	[490000, "GKP", "blondy nna noukeu", "sunderland"],
	[490094, "MID", "tim iroegbunam", "everton"],
	[490142, "MID", "freddie potts", "west ham"],
	[490145, "FWD", "dane scarlett", "spurs"],
	[490721, "DEF", "hugo bueno lópez", "wolves"],
	[490881, "MID", "toby collyer", "man utd"],
	[490885, "MID", "george earthy", "west ham"],
	[491007, "MID", "dário luís essugo", "chelsea"],
	[491012, "FWD", "youssef ramalho chermiti", "everton"],
	[491279, "DEF", "micky van de ven", "spurs"],
	[491287, "MID", "enzo barrenechea", "aston villa"],
	[491501, "MID", "james mcconnell", "liverpool"],
	[491557, "MID", "jenson metcalfe", "everton"],
	[491745, "DEF", "elijah campbell", "everton"],
	[492066, "DEF", "niall huggins", "sunderland"],
	[492368, "DEF", "isaac schmidt", "leeds"],
	[492777, "DEF", "conor bradley", "liverpool"],
	[492831, "FWD", "zeki amdouni", "burnley"],
	[492859, "MID", "wilfried gnonto", "leeds"],
	[493105, "MID", "alejandro garnacho ferreyra", "chelsea"],
	[493125, "DEF", "radu drăgușin", "spurs"],
	[493250, "MID", "amad diallo", "man utd"],
	[493362, "MID", "xavi simons", "spurs"],
	[493837, "MID", "jay matete", "sunderland"],
	[494521, "DEF", "adrien truffert", "bournemouth"],
	[494595, "MID", "florian wirtz", "liverpool"],
	[494960, "DEF", "quilindschy hartman", "burnley"],
	[495145, "GKP", "alex paulsen", "bournemouth"],
	[495161, "MID", "marko stamenić", "nott'm forest"],
	[496178, "DEF", "roman dixon", "everton"],
	[496208, "MID", "ben gannon-doak", "bournemouth"],
	[496221, "MID", "adam wharton", "crystal palace"],
	[496279, "MID", "isaac heath", "everton"],
	[496661, "MID", "tyler dibling", "everton"],
	[497606, "MID", "tawanda chirewa", "wolves"],
	[497894, "FWD", "rasmus højlund", "man utd"],
	[497949, "DEF", "david møller wolfe", "wolves"],
	[498016, "GKP", "robin roefs", "sunderland"],
	[499167, "DEF", "josh nichols", "arsenal"],
	[499169, "DEF", "myles lewis-skelly", "arsenal"],
	[499175, "MID", "ethan nwaneri", "arsenal"],
	[499300, "DEF", "adam aznou", "everton"],
	[499309, "FWD", "marc guiu paz", "chelsea"],
	[499716, "DEF", "james rowswell", "spurs"],
	[499717, "DEF", "jayden meghoma", "brentford"],
	[499721, "MID", "mikey moore", "spurs"],
	[499726, "MID", "callum olusesi", "spurs"],
	[500040, "DEF", "cristhian mosquera", "arsenal"],
	[500058, "FWD", "jayden danns", "liverpool"],
	[500151, "DEF", "nicolò savona", "nott'm forest"],
	[500696, "MID", "nectarios triantis", "sunderland"],
	[501837, "DEF", "yerson mosquera valdelamar", "wolves"],
	[502500, "FWD", "igor thiago nascimento rodrigues", "brentford"],
	[502697, "MID", "carlos alcaraz durán", "everton"],
	[503139, "MID", "alex scott", "bournemouth"],
	[503300, "GKP", "matthew cox", "brentford"],
	[503301, "MID", "omari hutchinson", "nott'm forest"],
	[503714, "MID", "lesley ugochukwu", "burnley"],
	[504296, "MID", "coby ebere", "everton"],
	[507433, "GKP", "hákon rafn valdimarsson", "brentford"],
	[508395, "MID", "yehor yarmoliuk", "brentford"],
	[508479, "GKP", "filip jörgensen", "chelsea"],
	[509291, "MID", "andré trindade da costa neto", "wolves"],
	[509416, "MID", "yasin ayari", "brighton"],
	[510281, "MID", "sávio moreira de oliveira", "man city"],
	[510362, "DEF", "toti gomes", "wolves"],
	[510500, "MID", "joão pedro ferreira da silva", "nott'm forest"],
	[510663, "FWD", "hugo ekitiké", "liverpool"],
	[511499, "MID", "mathys tel", "spurs"],
	[512462, "DEF", "jake o'brien", "everton"],
	[513418, "MID", "kevin schade", "brentford"],
	[513433, "MID", "brajan gruda", "brighton"],
	[513466, "MID", "merlin röhl", "everton"],
	[513834, "MID", "andrew moran", "brighton"],
	[514254, "MID", "diego gómez amarilla", "brighton"],
	[514315, "DEF", "lino da cruz sousa", "aston villa"],
	[514356, "MID", "roméo lavia", "chelsea"],
	[514613, "DEF", "zak johnson", "sunderland"],
	[515024, "MID", "luke harris", "fulham"],
	[515597, "DEF", "lamare bogarde", "aston villa"],
	[515621, "DEF", "chadi riad dnanou", "crystal palace"],
	[516211, "MID", "abdallah sima", "brighton"],
	[516895, "MID", "kobbie mainoo", "man utd"],
	[516939, "DEF", "emmanuel agbadou", "wolves"],
	[517052, "FWD", "nicolas jackson", "chelsea"],
	[517179, "DEF", "alfie pond", "wolves"],
	[518030, "GKP", "max weiß", "burnley"],
	[518438, "DEF", "kaelan casey", "west ham"],
	[518442, "MID", "lewis orford", "west ham"],
	[518906, "DEF", "owen bevan", "bournemouth"],
	[519634, "DEF", "jenson seelt", "sunderland"],
	[519895, "DEF", "oliver sonne", "burnley"],
	[523705, "DEF", "jackson tchatchoua", "wolves"],
	[530121, "MID", "zain silcott-duberry", "bournemouth"],
	[530318, "MID", "kaden rodney", "crystal palace"],
	[531363, "FWD", "nathan fraser", "wolves"],
	[531989, "MID", "david ozoh", "crystal palace"],
	[532529, "MID", "jack hinshelwood", "brighton"],
	[532605, "MID", "andrey nascimento dos santos", "chelsea"],
	[533463, "MID", "dango ouattara", "brentford"],
	[533710, "FWD", "iwan morgan", "brentford"],
	[534836, "DEF", "travis patterson", "aston villa"],
	[535017, "GKP", "julian eyestone", "brentford"],
	[535301, "MID", "carlos baleba", "brighton"],
	[535818, "MID", "simon adingra", "sunderland"],
	[535928, "MID", "stefan bajčetić maquieira", "liverpool"],
	[536109, "DEF", "ollie scarles", "west ham"],
	[536119, "MID", "charlie crew", "leeds"],
	[536241, "FWD", "martin sherif", "everton"],
	[536694, "MID", "matheus frança de oliveira", "crystal palace"],
	[536916, "MID", "facundo buonanotte", "chelsea"],
	[537403, "MID", "kadan young", "aston villa"],
	[538207, "FWD", "william osula", "newcastle"],
	[541462, "DEF", "matai akinmboni", "bournemouth"],
	[543295, "MID", "antoni milambo", "brentford"],
	[544877, "DEF", "milos kerkez", "liverpool"],
	[545477, "DEF", "alex murphy", "newcastle"],
	[547027, "MID", "habib diarra", "sunderland"],
	[547037, "MID", "jack fletcher", "man utd"],
	[547410, "MID", "harrison jones", "sunderland"],
	[547676, "DEF", "tyler fredricson", "man utd"],
	[547701, "MID", "archie gray", "spurs"],
	[547719, "MID", "lewis miley", "newcastle"],
	[547720, "DEF", "charlie tasker", "brighton"],
	[547801, "MID", "callum bates", "everton"],
	[548308, "DEF", "ashley phillips", "spurs"],
	[549067, "DEF", "zach abbott", "nott'm forest"],
	[549074, "MID", "tom watson", "brighton"],
	[549329, "DEF", "lucas pires silva", "burnley"],
	[549912, "MID", "chemsdine talbi", "sunderland"],
	[549939, "GKP", "mike penders", "chelsea"],
	[550090, "DEF", "diego coppola", "brighton"],
	[550141, "MID", "adrian mazilu", "brighton"],
	[550596, "MID", "dominic sadi", "bournemouth"],
	[550615, "MID", "tyrique george", "chelsea"],
	[550839, "MID", "wilson odobert", "spurs"],
	[550864, "DEF", "leny yoro", "man utd"],
	[551153, "FWD", "luís hemir silva semedo", "sunderland"],
	[551206, "MID", "jaydon banel", "burnley"],
	[551210, "DEF", "jorrel hato", "chelsea"],
	[551221, "GKP", "tommy setford", "arsenal"],
	[551226, "MID", "mateus gonçalo espanha fernandes", "west ham"],
	[551483, "DEF", "álex jiménez sánchez", "bournemouth"],
	[552427, "FWD", "will lankshear", "spurs"],
	[553299, "DEF", "takai kōta", "spurs"],
	[554197, "MID", "chris rigg", "sunderland"],
	[556637, "MID", "nehemiah oriola", "brighton"],
	[556639, "MID", "jayce fitzgerald", "man utd"],
	[559684, "MID", "jack moorhouse", "man utd"],
	[559962, "MID", "jamaldeen jimoh-aloba", "aston villa"],
	[560248, "DEF", "bastien meupiyou menadjou", "wolves"],
	[560262, "FWD", "junior kroupi", "bournemouth"],
	[560441, "DEF", "luis eduardo soares da silva", "nott'm forest"],
	[560552, "MID", "kevin santos lopes de macedo", "fulham"],
	[563324, "DEF", "brayden clarke", "arsenal"],
	[564406, "FWD", "eliezer mayenda dossou", "sunderland"],
	[564505, "GKP", "sam proctor", "aston villa"],
	[564510, "MID", "garang kuol", "newcastle"],
	[564940, "MID", "soungoutou magassa", "west ham"],
	[565297, "FWD", "mateo joseph fernández-regatillo", "leeds"],
	[565431, "FWD", "callum marshall", "west ham"],
	[566164, "MID", "sverre nypan", "man city"],
	[566213, "DEF", "stephen mfuni", "man city"],
	[567121, "MID", "joe knight", "brighton"],
	[568791, "GKP", "callan mckenna", "bournemouth"],
	[569014, "MID", "eric da silva moreira", "nott'm forest"],
	[569577, "DEF", "triston rowe", "aston villa"],
	[570241, "DEF", "kim ji-soo", "brentford"],
	[570526, "MID", "lucas bergvall", "spurs"],
	[573062, "MID", "martial godo", "fulham"],
	[574398, "MID", "franco umeh-chibueze", "crystal palace"],
	[574458, "DEF", "mamadou sarr", "chelsea"],
	[575034, "FWD", "ethan wheatley", "man utd"],
	[575204, "MID", "claudio echeverri", "man city"],
	[575458, "DEF", "jair paula da cunha filho", "nott'm forest"],
	[575476, "DEF", "murillo costa dos santos", "nott'm forest"],
	[575901, "DEF", "julio soler barreto", "bournemouth"],
	[576323, "MID", "oluwaseun adewumi", "burnley"],
	[576756, "FWD", "zépiqueno redmond", "aston villa"],
	[576980, "FWD", "zach marsh", "crystal palace"],
	[577016, "DEF", "josh acheampong", "chelsea"],
	[577114, "MID", "luis guilherme lira dos santos", "west ham"],
	[577669, "MID", "noah sadiki", "sunderland"],
	[577725, "MID", "josh king", "fulham"],
	[577731, "MID", "ben broggio", "aston villa"],
	[577974, "DEF", "harry amass", "man utd"],
	[578153, "DEF", "abdukodir khusanov", "man city"],
	[578512, "DEF", "miodrag pivaš", "newcastle"],
	[578614, "MID", "enock agyei", "burnley"],
	[579075, "MID", "asher agbinone", "crystal palace"],
	[586268, "GKP", "ármin pécsi", "liverpool"],
	[586309, "FWD", "thierno barry", "everton"],
	[587178, "DEF", "yasin özcan", "aston villa"],
	[588555, "GKP", "elyh harrison", "man utd"],
	[588793, "DEF", "maldini kacurri", "arsenal"],
	[588796, "MID", "ismeal kabia", "arsenal"],
	[589100, "DEF", "jacob slater", "brighton"],
	[589507, "FWD", "leon chiwome", "wolves"],
	[590012, "DEF", "caleb kporha", "crystal palace"],
	[590014, "MID", "rio cardines", "crystal palace"],
	[590035, "MID", "yusuf akhamrich", "spurs"],
	[590039, "MID", "divine mukasa", "man city"],
	[590760, "FWD", "daniel adu-adjei", "bournemouth"],
	[591357, "MID", "ryan trevitt", "brentford"],
	[591385, "DEF", "samuel amissah", "fulham"],
	[591386, "MID", "trey nyoni", "liverpool"],
	[592031, "MID", "yankuba minteh", "brighton"],
	[593001, "MID", "enso gonzález medina", "wolves"],
	[596042, "MID", "kieran morrison", "liverpool"],
	[596047, "FWD", "chido obi", "man utd"],
	[596054, "MID", "tom edozie", "wolves"],
	[596777, "DEF", "patrick dorgu", "man utd"],
	[599303, "FWD", "sean neave", "newcastle"],
	[600882, "FWD", "harry gray", "leeds"],
	[602903, "DEF", "ezra mayers", "west ham"],
	[606689, "MID", "romelle donovan", "brentford"],
	[606745, "DEF", "ayden heaven", "man utd"],
	[606774, "MID", "remy rees-dottin", "bournemouth"],
	[606775, "MID", "ben winterburn", "bournemouth"],
	[606798, "DEF", "andrés garcía", "aston villa"],
	[606921, "MID", "romain esse", "crystal palace"],
	[607464, "DEF", "michael kayode", "brentford"],
	[608181, "FWD", "stefanos tzimas", "brighton"],
	[609873, "MID", "harrison armstrong", "everton"],
	[610799, "DEF", "luka vušković", "spurs"],
	[611134, "MID", "kendry páez andrade", "chelsea"],
	[611695, "MID", "malick yalcouyé", "brighton"],
	[611912, "MID", "landon emenalo", "chelsea"],
	[611922, "MID", "rio ngumoha", "liverpool"],
	[611926, "DEF", "amara nallo", "liverpool"],
	[611975, "FWD", "ahmed abdullahi", "sunderland"],
	[612534, "DEF", "benjamin fredrick", "brentford"],
	[613804, "DEF", "el hadji malick diouf", "west ham"],
	[616077, "MID", "max dowman", "arsenal"],
	[616222, "DEF", "vitor de oliveira nunes dos reis", "man city"],
	[616288, "MID", "ryan mcaidoo", "man city"],
	[618873, "MID", "sékou koné", "man utd"],
	[620487, "DEF", "veljko milosavljevic", "bournemouth"],
	[622536, "DEF", "benjamin arthur", "brentford"],
	[622758, "DEF", "aarón anselmino", "chelsea"],
	[623095, "MID", "yang min-hyeok", "spurs"],
	[623110, "MID", "seung-soo park", "newcastle"],
	[624773, "MID", "estêvão almeida de oliveira gonçalves", "chelsea"],
	[626464, "MID", "gustavo nunes fernandes gomes", "brentford"],
	[626844, "MID", "milan aleksić", "sunderland"],
	[628204, "MID", "yunus emre konak", "brentford"],
	[631786, "FWD", "jonah kusi-asare", "fulham"],
	[640108, "MID", "antoñito cordero campillo", "newcastle"],
	[640419, "DEF", "jun'ai byfield", "spurs"],
	[641221, "DEF", "pedro cardoso de lima", "wolves"],
	[643135, "MID", "fer lópez gonzález", "wolves"],
	[643473, "DEF", "airidas golambeckis", "west ham"],
	[645618, "MID", "bradley burrowes", "aston villa"],
	[646243, "MID", "andre harriman-annous", "arsenal"],
	[647671, "FWD", "mateus mané", "wolves"],
	[647681, "DEF", "giovanni leoni", "liverpool"],
	[647850, "FWD", "charalampos kostoulas", "brighton"],
	[651426, "DEF", "jaydee canvot", "crystal palace"],
	[660392, "FWD", "christantus uche", "crystal palace"],
	[661712, "DEF", "diego león blanco", "man utd"],
]

def name_template(name):
    name = normalize("NFD", name).lower()
    return " ".join(
        sorted(sub("[^a-z ]", "", sub("[-]", " ", name)).split())
    )
PLAYERS_BY_NAME = {
    name_template(name): [pid, name_template(name), position, team]
    for pid, position, name, team in PLAYERS
}
PLAYERS_BY_ID = {
    pid: [pid, name_template(name), position, team]
    for pid, position, name, team in PLAYERS
}

"""
DATA = [
    {
        "player_stats": {
            "jan paul van hecke": {
                "goal": 0.058823529411764705,
                "assist": 0.034482758620689655,
                "no_assist": 0.9960159362549801
            },
            "lewis dunk": {
                "goal": 0.07692307692307693,
                "assist": 0.034482758620689655,
                "no_assist": 0.9960159362549801
            },
            "freddie simmonds": {
                "goal": 0.07692307692307693,
                "assist": 0.038461538461538464,
                "no_assist": 0.9950248756218906
            },
            "diego coppola": {
                "goal": 0.06666666666666667,
                "assist": 0.038461538461538464,
                "no_assist": 0.9950248756218906
            },
            "ferdi kadioglu": {
                "goal": 0.07692307692307693,
                "assist": 0.05263157894736842,
                "no_assist": 0.9876543209876543
            },
            "carlos baleba": {
                "goal": 0.09090909090909091,
                "assist": 0.05263157894736842,
                "no_assist": 0.9876543209876543
            },
            "ibrahima konate": {
                "goal": 0.07692307692307693,
                "assist": 0.05263157894736842,
                "no_assist": 0.9876543209876543
            },
            "joel veltman": {
                "goal": 0.047619047619047616,
                "assist": 0.058823529411764705,
                "no_assist": 0.9876543209876543
            },
            "olivier boscagli": {
                "goal": 0.047619047619047616,
                "assist": 0.05263157894736842,
                "no_assist": 0.9876543209876543
            },
            "charlie tasker": {
                "goal": 0.07692307692307693,
                "assist": 0.05263157894736842,
                "no_assist": 0.9876543209876543
            },
            "yasin ayari": {
                "goal": 0.1111111111111111,
                "assist": 0.06666666666666667,
                "no_assist": 0.9803921568627451
            },
            "danny welbeck": {
                "goal": 0.2857142857142857,
                "assist": 0.06666666666666667,
                "no_assist": 0.9803921568627451
            },
            "jack hinshelwood": {
                "goal": 0.08695652173913043,
                "assist": 0.06666666666666667,
                "no_assist": 0.9803921568627451
            },
            "joe gomez": {
                "goal": 0.07692307692307693,
                "assist": 0.06666666666666667,
                "no_assist": 0.9803921568627451
            },
            "stefanos tzimas": {
                "goal": 0.2777777777777778,
                "assist": 0.09090909090909091,
                "no_assist": 0.9705882352941176
            },
            "virgil van dijk": {
                "goal": 0.1111111111111111,
                "assist": 0.09090909090909091,
                "no_assist": 0.9705882352941176
            },
            "wataru endo": {
                "goal": 0.08,
                "assist": 0.09090909090909091,
                "no_assist": 0.9705882352941176
            },
            "james milner": {
                "goal": 0.09090909090909091,
                "assist": 0.1111111111111111,
                "no_assist": 0.9615384615384616
            },
            "trey nyoni": {
                "goal": 0.2,
                "assist": 0.1,
                "no_assist": 0.9615384615384616
            },
            "maxim de cuyper": {
                "goal": 0.10526315789473684,
                "assist": 0.1111111111111111,
                "no_assist": 0.9615384615384616
            },
            "charalampos kostoulas": {
                "goal": 0.22727272727272727,
                "assist": 0.1111111111111111,
                "no_assist": 0.9615384615384616
            },
            "mats wieffer": {
                "goal": 0.07692307692307693,
                "assist": 0.14285714285714285,
                "no_assist": 0.9523809523809523
            },
            "diego gomez": {
                "goal": 0.19047619047619047,
                "assist": 0.125,
                "no_assist": 0.9523809523809523
            },
            "curtis jones": {
                "goal": 0.125,
                "assist": 0.125,
                "no_assist": 0.9523809523809523
            },
            "milos kerkez": {
                "goal": 0.08,
                "assist": 0.125,
                "no_assist": 0.9523809523809523
            },
            "joe knight": {
                "goal": 0.14285714285714285,
                "assist": 0.14285714285714285,
                "no_assist": 0.9523809523809523
            },
            "tom watson": {
                "goal": 0.15384615384615385,
                "assist": 0.125,
                "no_assist": 0.9523809523809523
            },
            "brajan gruda": {
                "goal": 0.15384615384615385,
                "assist": 0.125,
                "no_assist": 0.9523809523809523
            },
            "alexis mac allister": {
                "goal": 0.15384615384615385,
                "assist": 0.14285714285714285,
                "no_assist": 0.9411764705882353
            },
            "kaoru mitoma": {
                "goal": 0.19047619047619047,
                "assist": 0.15384615384615385,
                "no_assist": 0.9411764705882353
            },
            "ryan gravenberch": {
                "goal": 0.11764705882352941,
                "assist": 0.14285714285714285,
                "no_assist": 0.9411764705882353
            },
            "nehemiah oriola": {
                "goal": 0.2,
                "assist": 0.15384615384615385,
                "no_assist": 0.9411764705882353
            },
            "andrew robertson": {
                "goal": 0.0625,
                "assist": 0.11764705882352941,
                "no_assist": 0.9333333333333333
            },
            "calvin ramsay": {
                "goal": 0.14285714285714285,
                "assist": 0.16666666666666666,
                "no_assist": 0.9333333333333333
            },
            "georginio rutter": {
                "goal": 0.2222222222222222,
                "assist": 0.16666666666666666,
                "no_assist": 0.9333333333333333
            },
            "yankuba minteh": {
                "goal": 0.18518518518518517,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "rio ngumoha": {
                "goal": 0.25,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "jayden danns": {
                "goal": 0.36363636363636365,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "alexander isak": {
                "goal": 0.425531914893617,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "jeremie frimpong": {
                "goal": 0.14285714285714285,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "federico chiesa": {
                "goal": 0.2777777777777778,
                "assist": 0.18181818181818182,
                "no_assist": 0.9230769230769231
            },
            "cody gakpo": {
                "goal": 0.3225806451612903,
                "assist": 0.2,
                "no_assist": 0.9090909090909091
            },
            "hugo ekitike": {
                "goal": 0.38461538461538464,
                "assist": 0.20833333333333334,
                "no_assist": 0.9
            },
            "florian wirtz": {
                "goal": 0.2564102564102564,
                "assist": 0.25,
                "no_assist": 0.8888888888888888
            },
            "dominik szoboszlai": {
                "goal": 0.23076923076923078,
                "assist": 0.25,
                "no_assist": 0.8888888888888888
            },
            "mohamed salah": {
                "goal": 0.45454545454545453,
                "assist": 0.2857142857142857,
                "no_assist": 0.875
            },
        },
        "game_stats": {
            "liverpool": {
                "goals": {
                    "0": 0.15384615384615385,
                    "1": 0.29411764705882354,
                    "2": 0.3076923076923077,
                    "3+": 0.36363636363636365
                },
                "clean_sheet": 0.3125
            },
            "brighton": {
                "goals": {
                    "0": 0.3333333333333333,
                    "1": 0.4,
                    "2": 0.25,
                    "3+": 0.125
                },
                "clean_sheet": 0.15384615384615385
            }
        }
    },
    {
	"player_stats": {
		"santiago bueno": {
			"goal": 0.024390243902439025,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"yerson mosquera": {
			"goal": 0.034482758620689655,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"emmanuel agbadou": {
			"goal": 0.024390243902439025,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ladislav krejci": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joao gomes": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ki-jana hoever": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"toti gomes": {
			"goal": 0.027777777777777776,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"matt doherty": {
			"goal": 0.034482758620689655,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"toluwalase arokodare": {
			"goal": 0.14285714285714285,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"andre trindade": {
			"goal": 0.024390243902439025,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"marli salmon": {
			"goal": 0.14285714285714285,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"rodrigo gomes": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"hugo bueno": {
			"goal": 0.024390243902439025,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"marshall munetsi": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"david wolfe": {
			"goal": 0.027777777777777776,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"mateus mane": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"william saliba": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"hee-chan hwang": {
			"goal": 0.1111111111111111,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tawanda chirewa": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"jackson tchatchoua": {
			"goal": 0.02857142857142857,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jorgen larsen": {
			"goal": 0.14285714285714285,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"fernando lopez": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"jeanricner bellegarde": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"cristhian mosquera": {
			"goal": 0.125,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jhon arias": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jurrien timber": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"viktor gyokeres": {
			"goal": 0.5405405405405406,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ben white": {
			"goal": 0.08333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"piero hincapie": {
			"goal": 0.10526315789473684,
			"assist": 0.10526315789473684,
			"no_assist": 0.9411764705882353
		},
		"myles lewis-skelly": {
			"goal": 0.1,
			"assist": 0.11764705882352941,
			"no_assist": 0.9333333333333333
		},
		"martin zubimendi": {
			"goal": 0.125,
			"assist": 0.16,
			"no_assist": 0.9230769230769231
		},
		"max dowman": {
			"goal": 0.3333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel martinelli": {
			"goal": 0.35714285714285715,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"gabriel jesus": {
			"goal": 0.5121951219512195,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"ethan nwaneri": {
			"goal": 0.29411764705882354,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"mikel merino": {
			"goal": 0.4,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"noni madueke": {
			"goal": 0.3448275862068966,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"eberechi eze": {
			"goal": 0.37735849056603776,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"leandro trossard": {
			"goal": 0.38461538461538464,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"declan rice": {
			"goal": 0.2,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"martin odegaard": {
			"goal": 0.23809523809523808,
			"assist": 0.2857142857142857,
			"no_assist": 0.8333333333333334
		},
		"bukayo saka": {
			"goal": 0.45454545454545453,
			"assist": 0.38095238095238093,
			"no_assist": 0.8
		}
	},
	"game_stats": {
		"arsenal": {
			"goals": {
				"0": 0.09090909090909091,
				"1": 0.21052631578947367,
				"2": 0.2777777777777778,
				"3+": 0.5454545454545454
			},
			"clean_sheet": 0.6451612903225806
		},
		"wolverhampton": {
			"goals": {
				"0": 0.6451612903225806,
				"1": 0.3333333333333333,
				"2": 0.08333333333333333,
				"3+": 0.024390243902439025
			},
			"clean_sheet": 0.08333333333333333
		}
	}
},
{
	"player_stats": {
		"ruben dias": {
			"goal": 0.05555555555555555,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nathan ake": {
			"goal": 0.0625,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"rio cardines": {
			"goal": 0.2222222222222222,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.08,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"john stones": {
			"goal": 0.0625,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"abduqodir khusanov": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"josko gvardiol": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chrisantus uche": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"jean-philippe mateta": {
			"goal": 0.37777777777777777,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tyrick mitchell": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nico oreilly": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.07142857142857142,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"adam wharton": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"daichi kamada": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"erling haaland": {
			"goal": 0.5555555555555556,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"rico lewis": {
			"goal": 0.05555555555555555,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"eddie nketiah": {
			"goal": 0.23809523809523808,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nico gonzalez": {
			"goal": 0.08,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"romain esse": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"borna sosa": {
			"goal": 0.047619047619047616,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.125,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"rayan ait nouri": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"justin devenny": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kalvin phillips": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"tijjani reijnders": {
			"goal": 0.21052631578947367,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ismaila sarr": {
			"goal": 0.2564102564102564,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bernardo silva": {
			"goal": 0.14814814814814814,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"yeremy pino": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"oscar bobb": {
			"goal": 0.22727272727272727,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"phil foden": {
			"goal": 0.2777777777777778,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"divine mukasa": {
			"goal": 0.18181818181818182,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"rayan cherki": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"jeremy doku": {
			"goal": 0.20833333333333334,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"omar marmoush": {
			"goal": 0.30303030303030304,
			"assist": 0.21739130434782608,
			"no_assist": 0.9
		},
		"matheus nunes": {
			"goal": 0.07142857142857142,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"de oliveira savio": {
			"goal": 0.21052631578947367,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
	},
	"game_stats": {
		"crystal palace": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.2
		},
		"man city": {
			"goals": {
				"0": 0.2,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.3225806451612903
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jair cunha": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.09523809523809523,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ben davies": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jack thompson": {
			"goal": 0.2,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joao palhinha": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.0625,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"yves bissouma": {
			"goal": 0.125,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"felipe morato": {
			"goal": 0.05,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"neco williams": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"archie gray": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ibrahim sangare": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"ryan yates": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.05,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"dominic solanke": {
			"goal": 0.30303030303030304,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nicolas dominguez": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"chris wood": {
			"goal": 0.3333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nicolo savona": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.2857142857142857,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.36363636363636365,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.23255813953488372,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"arnaud kalimuendo": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"randal muani": {
			"goal": 0.30303030303030304,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"callum hudson-odoi": {
			"goal": 0.21739130434782608,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"igor jesus": {
			"goal": 0.3333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"dan ndoye": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jimmy sinclair": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"omari giraud-hutchinson": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"richarlison": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.21052631578947367,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"morgan gibbs-white": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mohammed kudus": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"elliot anderson": {
			"goal": 0.125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dilane bakwa": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"willy boly": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"pape matar sarr": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
	},
	"game_stats": {
		"nottingham forest": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.29411764705882354
		},
		"tottenham": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.2631578947368421
		}
	}
},
{
	"player_stats": {
		"konstantinos mavropanos": {
			"goal": 0.05,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"jean-clair todibo": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"victor lindelof": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"max kilman": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"pau torres": {
			"goal": 0.07142857142857142,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"yeimar mosquera": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"soungoutou magassa": {
			"goal": 0.038461538461538464,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ezra mayers": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"airidas golambeckis": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"guido rodriguez": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"freddie potts": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"oliver scarles": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"tomas soucek": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"aaron wan-bissaka": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"callum marshall": {
			"goal": 0.23529411764705882,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"lamare bogarde": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"george hemmings": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"callum wilson": {
			"goal": 0.3125,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"amadou onana": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"kyle walker-peters": {
			"goal": 0.05,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"andres garcia": {
			"goal": 0.08695652173913043,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"luis guilherme lira": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mohamadou kante": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"el hadji diouf": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"travis patterson": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jamaldeen jimoh": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"andrew irving": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"niclas fullkrug": {
			"goal": 0.2631578947368421,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"crysencio summerville": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas paqueta": {
			"goal": 0.21052631578947367,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james ward-prowse": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"george earthy": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"john mcginn": {
			"goal": 0.19047619047619047,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"donyell malen": {
			"goal": 0.3333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ben broggio": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"mateus fernandes": {
			"goal": 0.11764705882352941,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"ian maatsen": {
			"goal": 0.125,
			"assist": 0.10526315789473684,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.15384615384615385,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"lucas digne": {
			"goal": 0.058823529411764705,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"evann guessand": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ollie watkins": {
			"goal": 0.425531914893617,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"jarrod bowen": {
			"goal": 0.3125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey elliott": {
			"goal": 0.2,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"emiliano buendia": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"jadon sancho": {
			"goal": 0.16,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"de paulo igor": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
	},
	"game_stats": {
		"west ham": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.21739130434782608
		},
		"aston villa": {
			"goals": {
				"0": 0.21739130434782608,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.3333333333333333
		}
	}
},
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.09523809523809523,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"luke onien": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"omar alderete": {
			"goal": 0.08695652173913043,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"alex murphy": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"fabian schar": {
			"goal": 0.11764705882352941,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"reinildo mandava": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"lutsharel geertruida": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan burn": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jamaal lascelles": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan neil": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"arthur masuaku": {
			"goal": 0.05,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"noah sadiki": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nordi mukiele": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"daniel ballard": {
			"goal": 0.11764705882352941,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"eliezer mayenda": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.2777777777777778,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"wilson isidor": {
			"goal": 0.3225806451612903,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"brian brobbey": {
			"goal": 0.23809523809523808,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"trai hume": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.2894736842105263,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jacob ramsey": {
			"goal": 0.17391304347826086,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chris rigg": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yoane wissa": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"harrison jones": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"chemsdine talbi": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"enzo le fee": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"nick woltemade": {
			"goal": 0.37777777777777777,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"granit xhaka": {
			"goal": 0.125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"simon adingra": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.13333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"bertrand traore": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony gordon": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony elanga": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"romain mundle": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
	},
	"game_stats": {
		"sunderland": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.23809523809523808,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.23809523809523808
		},
		"newcastle": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.3225806451612903
		}
	}
},
{
	"player_stats": {
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"sebastiaan bornauw": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"joe rodon": {
			"goal": 0.07142857142857142,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"jaka bijol": {
			"goal": 0.0625,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ethan ampadu": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sam byram": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ethan pinnock": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"aaron hickey": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sepp van den berg": {
			"goal": 0.09523809523809523,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.08,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"james justin": {
			"goal": 0.07142857142857142,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"gabriel gudmundsson": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.26666666666666666,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"ilia gruev": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lukas nmecha": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"rico henry": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.2222222222222222,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kristoffer ajer": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"anton stach": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ao tanaka": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.29411764705882354,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.07692307692307693,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.14814814814814814,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jack harrison": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"frank onyeka": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"degnand gnonto": {
			"goal": 0.20833333333333334,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.20833333333333334,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"mathias jensen": {
			"goal": 0.125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"reiss nelson": {
			"goal": 0.23809523809523808,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.4166666666666667,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"dango ouattara": {
			"goal": 0.2857142857142857,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mikkel damsgaard": {
			"goal": 0.16,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
	},
	"game_stats": {
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.35714285714285715
		},
		"leeds": {
			"goals": {
				"0": 0.35714285714285715,
				"1": 0.4,
				"2": 0.2222222222222222,
				"3+": 0.1
			},
			"clean_sheet": 0.23076923076923078
		}
	}
},
{
	"player_stats": {
		"lisandro martinez": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"tyler fredricson": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"veljko milosavljevic": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"marcos senesi": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ayden heaven": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"leny yoro": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"harry maguire": {
			"goal": 0.11764705882352941,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tyler adams": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"julio soler": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"adam smith": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"alejandro jimenez": {
			"goal": 0.0625,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"tyrell malacia": {
			"goal": 0.11764705882352941,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"diego leon": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"matthijs de ligt": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"malcom dacosta": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"noussair mazraoui": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"bafode diakite": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jack fletcher": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"julian araujo": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"evanilson": {
			"goal": 0.2631578947368421,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"manuel ugarte": {
			"goal": 0.08,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"alex scott": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kobbie mainoo": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"luke shaw": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"james hill": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"eli junior kroupi": {
			"goal": 0.2777777777777778,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"amine adli": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"enes unal": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"shea lacey": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"adrien truffert": {
			"goal": 0.0625,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"benjamin sesko": {
			"goal": 0.4166666666666667,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"diogo dalot": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joshua zirkzee": {
			"goal": 0.3448275862068966,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"marcus tavernier": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ryan christie": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mason mount": {
			"goal": 0.23255813953488372,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"casemiro": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"justin kluivert": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"patrick dorgu": {
			"goal": 0.11764705882352941,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"antoine semenyo": {
			"goal": 0.3225806451612903,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"david brooks": {
			"goal": 0.19047619047619047,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"amad diallo": {
			"goal": 0.3225806451612903,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"bryan mbeumo": {
			"goal": 0.4,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"bruno fernandes": {
			"goal": 0.36363636363636365,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"matheus cunha": {
			"goal": 0.38095238095238093,
			"assist": 0.25,
			"no_assist": 0.8571428571428571
		}
	},
	"game_stats": {
		"man utd": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3225806451612903,
				"2": 0.3076923076923077,
				"3+": 0.3076923076923077
			},
			"clean_sheet": 0.29411764705882354
		},
		"bournemouth": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2564102564102564,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"jarrad branthwaite": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"michael keane": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reece welch": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"adam aznou": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"idrissa gueye": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"jake obrien": {
			"goal": 0.05,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.07142857142857142,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"wesley fofana": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"timothy iroegbunam": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"benoit badiashile": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"vitaliy mykolenko": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"trevoh chalobah": {
			"goal": 0.09523809523809523,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"james tarkowski": {
			"goal": 0.0625,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"seamus coleman": {
			"goal": 0.043478260869565216,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"beto": {
			"goal": 0.21052631578947367,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"elijah campbell": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nathan patterson": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"thierno barry": {
			"goal": 0.2222222222222222,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"tyler dibling": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james garner": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"merlin rohl": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"marc cucurella": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andrey santos": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"josh acheampong": {
			"goal": 0.07142857142857142,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kiernan dewsbury-hall": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jorrel hato": {
			"goal": 0.08,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"carlos alcaraz": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"dwight mcneil": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romeo lavia": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack grealish": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"malo gusto": {
			"goal": 0.08,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"marc guiu": {
			"goal": 0.29411764705882354,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"reece james": {
			"goal": 0.10526315789473684,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jamie bynoe-gittens": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enzo fernandez": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"tyrique george": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"alejandro garnacho": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"facundo buonanotte": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"pedro neto": {
			"goal": 0.2631578947368421,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"estevao": {
			"goal": 0.3125,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"cole palmer": {
			"goal": 0.36363636363636365,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"de jesus joao pedro": {
			"goal": 0.38461538461538464,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
	},
	"game_stats": {
		"chelsea": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3225806451612903,
				"2": 0.3076923076923077,
				"3+": 0.29411764705882354
			},
			"clean_sheet": 0.42105263157894735
		},
		"everton": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.18181818181818182
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.05,
			"assist": 0.0196078431372549,
			"no_assist": 0.998003992015968
		},
		"calvin bassey": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"issa diop": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"joachim andersen": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"luis florentino": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"axel tuanzebe": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"joe worrall": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"hjalmar ekdal": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jorge cuenca": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"bashir humphreys": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ashley barnes": {
			"goal": 0.2,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.16,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"loum tchaouna": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.23076923076923078,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jaydon banel": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lesley ugochukwu": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh laurent": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"timothy castagne": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"marcus edwards": {
			"goal": 0.17391304347826086,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh cullen": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"zian flemming": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"harrison reed": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"brandon pouani": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kenny tete": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"emile smith rowe": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lyle foster": {
			"goal": 0.21739130434782608,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joshua king": {
			"goal": 0.23529411764705882,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"raul jimenez": {
			"goal": 0.38095238095238093,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"antonee robinson": {
			"goal": 0.07142857142857142,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.3125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jacob bruun larsen": {
			"goal": 0.1724137931034483,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.08,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"kevin macedo": {
			"goal": 0.19230769230769232,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sasa lukic": {
			"goal": 0.10526315789473684,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan sessegnon": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adama traore": {
			"goal": 0.17391304347826086,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harry wilson": {
			"goal": 0.2777777777777778,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"alex iwobi": {
			"goal": 0.2222222222222222,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
	},
	"game_stats": {
		"burnley": {
			"goals": {
				"0": 0.38095238095238093,
				"1": 0.4,
				"2": 0.21052631578947367,
				"3+": 0.1
			},
			"clean_sheet": 0.23076923076923078
		},
		"fulham": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.38095238095238093
		}
	}
},
]
"""

"""
DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"alex murphy": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.0625,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"benoit badiashile": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"fabian schar": {
			"goal": 0.11764705882352941,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"wesley fofana": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jamaal lascelles": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"trevoh chalobah": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan burn": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"moises caicedo": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"marc cucurella": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.2777777777777778,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"william osula": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"romeo lavia": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andrey santos": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh acheampong": {
			"goal": 0.05,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jorrel hato": {
			"goal": 0.07142857142857142,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jacob ramsey": {
			"goal": 0.1724137931034483,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"liam delap": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.16,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"marc guiu": {
			"goal": 0.23809523809523808,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.0625,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.07142857142857142,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.40816326530612246,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"facundo buonanotte": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.08333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jamie bynoe-gittens": {
			"goal": 0.19047619047619047,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tyrique george": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alejandro garnacho": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"enzo fernandez": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"anthony gordon": {
			"goal": 0.3076923076923077,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"pedro neto": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.23809523809523808,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.13333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony elanga": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.2631578947368421,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"estevao": {
			"goal": 0.2631578947368421,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"cole palmer": {
			"goal": 0.29411764705882354,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"bruno guimaraes": {
			"goal": 0.125,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"de jesus joao pedro": {
			"goal": 0.3225806451612903,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		}
	},
	"game_stats": {
		"newcastle": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.26666666666666666
		},
		"chelsea": {
			"goals": {
				"0": 0.26666666666666666,
				"1": 0.38095238095238093,
				"2": 0.2702702702702703,
				"3+": 0.2
			},
			"clean_sheet": 0.23809523809523808
		}
	}
},
{
	"player_stats": {
		"santiago bueno": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"yerson mosquera": {
			"goal": 0.07142857142857142,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ethan pinnock": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"aaron hickey": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"nathan collins": {
			"goal": 0.07142857142857142,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"joao gomes": {
			"goal": 0.09523809523809523,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"emmanuel agbadou": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"ladislav krejci": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"benjamin arthur": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ki-jana hoever": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"toti gomes": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"toluwalase arokodare": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"matt doherty": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"rico henry": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.23076923076923078,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kristoffer ajer": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"rodrigo gomes": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andre trindade": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yegor yarmolyuk": {
			"goal": 0.14814814814814814,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"david wolfe": {
			"goal": 0.05,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"mateus mane": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"hee-chan hwang": {
			"goal": 0.23255813953488372,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.07142857142857142,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"tawanda chirewa": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jorgen larsen": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"hugo bueno": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"marshall munetsi": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jackson tchatchoua": {
			"goal": 0.0625,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jordan henderson": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"fernando lopez": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jeanricner bellegarde": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"frank onyeka": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jhon arias": {
			"goal": 0.23255813953488372,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"kevin schade": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mathias jensen": {
			"goal": 0.125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"reiss nelson": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dango ouattara": {
			"goal": 0.3076923076923077,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"igor thiago": {
			"goal": 0.4166666666666667,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mikkel damsgaard": {
			"goal": 0.15625,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"wolverhampton": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.1111111111111111
			},
			"clean_sheet": 0.23076923076923078
		},
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.34782608695652173
		}
	}
},
{
	"player_stats": {
		"omar alderete": {
			"goal": 0.08,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reinildo mandava": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"lutsharel geertruida": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"dan neil": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"noah sadiki": {
			"goal": 0.11764705882352941,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"arthur masuaku": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jan paul van hecke": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"lewis dunk": {
			"goal": 0.11764705882352941,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"diego coppola": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"freddie simmonds": {
			"goal": 0.11764705882352941,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"daniel ballard": {
			"goal": 0.1,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"wilson isidor": {
			"goal": 0.26666666666666666,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nordi mukiele": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"eliezer mayenda": {
			"goal": 0.23076923076923078,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"trai hume": {
			"goal": 0.05,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"olivier boscagli": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ferdi kadioglu": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"carlos baleba": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"charlie tasker": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel veltman": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"brian brobbey": {
			"goal": 0.2222222222222222,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chris rigg": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"danny welbeck": {
			"goal": 0.4166666666666667,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"enzo le fee": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chemsdine talbi": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jack hinshelwood": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yasin ayari": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"harrison jones": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"bertrand traore": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"simon adingra": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"granit xhaka": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"stefanos tzimas": {
			"goal": 0.4,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"charalampos kostoulas": {
			"goal": 0.30303030303030304,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"maxim de cuyper": {
			"goal": 0.15384615384615385,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"james milner": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tom watson": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"brajan gruda": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mats wieffer": {
			"goal": 0.1111111111111111,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"joe knight": {
			"goal": 0.21052631578947367,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"diego gomez": {
			"goal": 0.2857142857142857,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"nehemiah oriola": {
			"goal": 0.2857142857142857,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"kaoru mitoma": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"georginio rutter": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"yankuba minteh": {
			"goal": 0.2777777777777778,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"romain mundle": {
			"goal": 0.18181818181818182,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"brighton": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3225806451612903,
				"2": 0.3076923076923077,
				"3+": 0.3333333333333333
			},
			"clean_sheet": 0.4166666666666667
		},
		"sunderland": {
			"goals": {
				"0": 0.4166666666666667,
				"1": 0.40816326530612246,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.05,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.05555555555555555,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"axel tuanzebe": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"joe worrall": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"veljko milosavljevic": {
			"goal": 0.1,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"ashley barnes": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lucas pires": {
			"goal": 0.04,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"julio soler": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"bashir humphreys": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"marcos senesi": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler adams": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jaydon banel": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh laurent": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"lesley ugochukwu": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"adam smith": {
			"goal": 0.07142857142857142,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"brandon pouani": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"zian flemming": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"malcom dacosta": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lyle foster": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"alejandro jimenez": {
			"goal": 0.1,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"evanilson": {
			"goal": 0.35714285714285715,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.16,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"julian araujo": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"bafode diakite": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james hill": {
			"goal": 0.09090909090909091,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"lewis cook": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"alex scott": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"eli junior kroupi": {
			"goal": 0.38461538461538464,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adrien truffert": {
			"goal": 0.09523809523809523,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"ryan christie": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"amine adli": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enes unal": {
			"goal": 0.4166666666666667,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"marcus tavernier": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"justin kluivert": {
			"goal": 0.2777777777777778,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"antoine semenyo": {
			"goal": 0.43478260869565216,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"david brooks": {
			"goal": 0.2702702702702703,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"bournemouth": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.29411764705882354,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"burnley": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.40816326530612246,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"konstantinos mavropanos": {
			"goal": 0.043478260869565216,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jean-clair todibo": {
			"goal": 0.038461538461538464,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"max kilman": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"soungoutou magassa": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ruben dias": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"airidas golambeckis": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"guido rodriguez": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"oliver scarles": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan ake": {
			"goal": 0.08695652173913043,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"aaron wan-bissaka": {
			"goal": 0.034482758620689655,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"freddie potts": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tomas soucek": {
			"goal": 0.13333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum marshall": {
			"goal": 0.16666666666666666,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum wilson": {
			"goal": 0.21739130434782608,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luis guilherme lira": {
			"goal": 0.1111111111111111,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mohamadou kante": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"el hadji diouf": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kyle walker-peters": {
			"goal": 0.034482758620689655,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"andrew irving": {
			"goal": 0.09523809523809523,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james ward-prowse": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"crysencio summerville": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"george earthy": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"john stones": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lucas paqueta": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"niclas fullkrug": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"abduqodir khusanov": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mateus fernandes": {
			"goal": 0.08333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jarrod bowen": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"nico oreilly": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"nico gonzalez": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rico lewis": {
			"goal": 0.08695652173913043,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"erling haaland": {
			"goal": 0.7142857142857143,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"rayan ait nouri": {
			"goal": 0.15384615384615385,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"kalvin phillips": {
			"goal": 0.15384615384615385,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"tijjani reijnders": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"oscar bobb": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bernardo silva": {
			"goal": 0.2,
			"assist": 0.20833333333333334,
			"no_assist": 0.875
		},
		"divine mukasa": {
			"goal": 0.29411764705882354,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"phil foden": {
			"goal": 0.42105263157894735,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"jeremy doku": {
			"goal": 0.2702702702702703,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"rayan cherki": {
			"goal": 0.29411764705882354,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"omar marmoush": {
			"goal": 0.5,
			"assist": 0.36363636363636365,
			"no_assist": 0.8181818181818182
		},
		"de paulo igor": {
			"goal": 0.034482758620689655,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"matheus nunes": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"de oliveira savio": {
			"goal": 0.3225806451612903,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man city": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.2,
				"2": 0.26666666666666666,
				"3+": 0.5789473684210527
			},
			"clean_sheet": 0.47619047619047616
		},
		"west ham": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.06666666666666667
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.07692307692307693,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"junai byfield": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ben davies": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"kevin danso": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joao palhinha": {
			"goal": 0.10526315789473684,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ibrahima konate": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joe gomez": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"yves bissouma": {
			"goal": 0.14285714285714285,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"virgil van dijk": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"wataru endo": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"archie gray": {
			"goal": 0.043478260869565216,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"dominic solanke": {
			"goal": 0.34782608695652173,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"trey nyoni": {
			"goal": 0.16666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"milos kerkez": {
			"goal": 0.07142857142857142,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.29411764705882354,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"curtis jones": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"alexis mac allister": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"randal muani": {
			"goal": 0.2857142857142857,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ryan gravenberch": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"andrew robertson": {
			"goal": 0.05555555555555555,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.09090909090909091,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"conor bradley": {
			"goal": 0.08695652173913043,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"mathys tel": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"calvin ramsay": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"federico chiesa": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rio ngumoha": {
			"goal": 0.22727272727272727,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jeremie frimpong": {
			"goal": 0.13333333333333333,
			"assist": 0.16,
			"no_assist": 0.9333333333333333
		},
		"jayden danns": {
			"goal": 0.3225806451612903,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"alexander isak": {
			"goal": 0.39215686274509803,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"brennan johnson": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"richarlison": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"cody gakpo": {
			"goal": 0.29411764705882354,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"xavi simons": {
			"goal": 0.21739130434782608,
			"assist": 0.1724137931034483,
			"no_assist": 0.9230769230769231
		},
		"hugo ekitike": {
			"goal": 0.35714285714285715,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"florian wirtz": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"mohammed kudus": {
			"goal": 0.23255813953488372,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"dominik szoboszlai": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"mohamed salah": {
			"goal": 0.42105263157894735,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"mickey van de ven": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"destiny udogie": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"pape matar sarr": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"tottenham": {
			"goals": {
				"0": 0.2857142857142857,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.2
		},
		"liverpool": {
			"goals": {
				"0": 0.2,
				"1": 0.3333333333333333,
				"2": 0.30303030303030304,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"jarrad branthwaite": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"michael keane": {
			"goal": 0.058823529411764705,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"william saliba": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"reece welch": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"adam aznou": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jake obrien": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"idrissa gueye": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"vitaliy mykolenko": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"timothy iroegbunam": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"cristhian mosquera": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"seamus coleman": {
			"goal": 0.038461538461538464,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"james tarkowski": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"beto": {
			"goal": 0.2222222222222222,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"elijah campbell": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"nathan patterson": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.09523809523809523,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jurrien timber": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"thierno barry": {
			"goal": 0.20833333333333334,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ben white": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"viktor gyokeres": {
			"goal": 0.4,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"merlin rohl": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"riccardo calafiori": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tyler dibling": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james garner": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"piero hincapie": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.2222222222222222,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"dwight mcneil": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"carlos alcaraz": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"martin zubimendi": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kiernan dewsbury-hall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"max dowman": {
			"goal": 0.23076923076923078,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ethan nwaneri": {
			"goal": 0.21739130434782608,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jack grealish": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"gabriel martinelli": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"gabriel jesus": {
			"goal": 0.34782608695652173,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"mikel merino": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"declan rice": {
			"goal": 0.14285714285714285,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"leandro trossard": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"noni madueke": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"eberechi eze": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"martin odegaard": {
			"goal": 0.17391304347826086,
			"assist": 0.20833333333333334,
			"no_assist": 0.9
		},
		"bukayo saka": {
			"goal": 0.3225806451612903,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"everton": {
			"goals": {
				"0": 0.4444444444444444,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.2222222222222222
		},
		"arsenal": {
			"goals": {
				"0": 0.21739130434782608,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.4444444444444444
		}
	}
},
{
	"player_stats": {
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"joe rodon": {
			"goal": 0.08,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"pascal struijk": {
			"goal": 0.1,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"rio cardines": {
			"goal": 0.25,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"james justin": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ilia gruev": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel piroe": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jefferson lerma": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"tyrick mitchell": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jean-philippe mateta": {
			"goal": 0.4,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lukas nmecha": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.08,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"chrisantus uche": {
			"goal": 0.2222222222222222,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"anton stach": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dominic calvert-lewin": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"adam wharton": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"eddie nketiah": {
			"goal": 0.2564102564102564,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daichi kamada": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.2222222222222222,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"justin devenny": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"borna sosa": {
			"goal": 0.07142857142857142,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"degnand gnonto": {
			"goal": 0.22727272727272727,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ismaila sarr": {
			"goal": 0.2857142857142857,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"leeds": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.29411764705882354
		},
		"crystal palace": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.3333333333333333
		}
	}
},
{
	"player_stats": {
		"matthijs de ligt": {
			"goal": 0.08333333333333333,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"lisandro martinez": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"tyler fredricson": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pau torres": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"leny yoro": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ayden heaven": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"yeimar mosquera": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"noussair mazraoui": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"diego leon": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"tyrell malacia": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jack fletcher": {
			"goal": 0.125,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luke shaw": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"manuel ugarte": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kobbie mainoo": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"george hemmings": {
			"goal": 0.21052631578947367,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lamare bogarde": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"amadou onana": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"shea lacey": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joshua zirkzee": {
			"goal": 0.23809523809523808,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"casemiro": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"diogo dalot": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mason mount": {
			"goal": 0.17391304347826086,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"benjamin sesko": {
			"goal": 0.3225806451612903,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andres garcia": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"patrick dorgu": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jamaldeen jimoh": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"travis patterson": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"donyell malen": {
			"goal": 0.3225806451612903,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"amad diallo": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"john mcginn": {
			"goal": 0.20833333333333334,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ben broggio": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ian maatsen": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9333333333333333
		},
		"bryan mbeumo": {
			"goal": 0.29411764705882354,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"lucas digne": {
			"goal": 0.08333333333333333,
			"assist": 0.14814814814814814,
			"no_assist": 0.9230769230769231
		},
		"evann guessand": {
			"goal": 0.34782608695652173,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"ollie watkins": {
			"goal": 0.43478260869565216,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jadon sancho": {
			"goal": 0.16666666666666666,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"emiliano buendia": {
			"goal": 0.2777777777777778,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"bruno fernandes": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.21052631578947367,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.25,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"matheus cunha": {
			"goal": 0.2777777777777778,
			"assist": 0.20833333333333334,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"aston villa": {
			"goals": {
				"0": 0.2,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.29411764705882354
		},
		"man utd": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.06666666666666667,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"nikola milenkovic": {
			"goal": 0.08,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"calvin bassey": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joachim andersen": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"zach abbott": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jack thompson": {
			"goal": 0.16666666666666666,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jorge cuenca": {
			"goal": 0.08695652173913043,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"felipe morato": {
			"goal": 0.07142857142857142,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ibrahim sangare": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"neco williams": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"murillo dos santos": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ryan yates": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"chris wood": {
			"goal": 0.3125,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"timothy castagne": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kenny tete": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nicolas dominguez": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.17391304347826086,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"arnaud kalimuendo": {
			"goal": 0.2564102564102564,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.3333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.36363636363636365,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"emile smith rowe": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"igor jesus": {
			"goal": 0.3125,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"antonee robinson": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joshua king": {
			"goal": 0.21739130434782608,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.21052631578947367,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"dan ndoye": {
			"goal": 0.14285714285714285,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"jimmy sinclair": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ryan sessegnon": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"sasa lukic": {
			"goal": 0.10526315789473684,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.18518518518518517,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.08695652173913043,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.3125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"omari giraud-hutchinson": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"elliot anderson": {
			"goal": 0.10526315789473684,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"morgan gibbs-white": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dilane bakwa": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harry wilson": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"alex iwobi": {
			"goal": 0.21052631578947367,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"willy boly": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		}
	},
	"game_stats": {
		"fulham": {
			"goals": {
				"0": 0.2631578947368421,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.34782608695652173
		},
		"nottingham forest": {
			"goals": {
				"0": 0.35714285714285715,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.2631578947368421
		}
	}
},
]
"""

"""
DATA = [
{
	"player_stats": {
		"lewis dunk": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jan paul van hecke": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"diego coppola": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"freddie simmonds": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"olivier boscagli": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"ferdi kadioglu": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"charlie tasker": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"carlos baleba": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ibrahima konate": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9876543209876543
		},
		"joel veltman": {
			"goal": 0.043478260869565216,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"joe gomez": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jack hinshelwood": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"danny welbeck": {
			"goal": 0.30303030303030304,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"yasin ayari": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"wellity lucky": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"virgil van dijk": {
			"goal": 0.1,
			"assist": 0.043478260869565216,
			"no_assist": 0.9705882352941176
		},
		"maxim de cuyper": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"charalampos kostoulas": {
			"goal": 0.2222222222222222,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"trey nyoni": {
			"goal": 0.17391304347826086,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"diego gomez": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"curtis jones": {
			"goal": 0.125,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"milos kerkez": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"tom watson": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brajan gruda": {
			"goal": 0.16,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ryan gravenberch": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"nehemiah oriola": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"joe knight": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"mats wieffer": {
			"goal": 0.058823529411764705,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"alexis mac allister": {
			"goal": 0.14285714285714285,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kaoru mitoma": {
			"goal": 0.19047619047619047,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"calvin ramsay": {
			"goal": 0.08333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"georginio rutter": {
			"goal": 0.18181818181818182,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"andrew robertson": {
			"goal": 0.0625,
			"assist": 0.11764705882352941,
			"no_assist": 0.9333333333333333
		},
		"yankuba minteh": {
			"goal": 0.17391304347826086,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"rio ngumoha": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jayden danns": {
			"goal": 0.36363636363636365,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"alexander isak": {
			"goal": 0.42105263157894735,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"jeremie frimpong": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"federico chiesa": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"hugo ekitike": {
			"goal": 0.39215686274509803,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"dominik szoboszlai": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.8888888888888888
		},
		"florian wirtz": {
			"goal": 0.2564102564102564,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"mohamed salah": {
			"goal": 0.4,
			"assist": 0.2222222222222222,
			"no_assist": 0.875
		},
	},
	"game_stats": {
		"liverpool": {
			"goals": {
				"0": 0.15384615384615385,
				"1": 0.30303030303030304,
				"2": 0.3076923076923077,
				"3+": 0.3448275862068966
			},
			"clean_sheet": 0.3333333333333333
		},
		"brighton": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.24390243902439024,
				"3+": 0.13333333333333333
			},
			"clean_sheet": 0.15384615384615385
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.029411764705882353,
			"assist": 0.0196078431372549,
			"no_assist": 0.998003992015968
		},
		"issa diop": {
			"goal": 0.05555555555555555,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"calvin bassey": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"luis florentino": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9900990099009901
		},
		"joe worrall": {
			"goal": 0.029411764705882353,
			"assist": 0.034482758620689655,
			"no_assist": 0.9900990099009901
		},
		"jorge cuenca": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9876543209876543
		},
		"joachim andersen": {
			"goal": 0.058823529411764705,
			"assist": 0.05263157894736842,
			"no_assist": 0.9850746268656716
		},
		"ashley barnes": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"kenny tete": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"josh cullen": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.125,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"loum tchaouna": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"sander berge": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"mike tresor": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"timothy castagne": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.2,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"josh laurent": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9705882352941176
		},
		"lesley ugochukwu": {
			"goal": 0.1,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"lyle foster": {
			"goal": 0.2222222222222222,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"harrison reed": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"zian flemming": {
			"goal": 0.23076923076923078,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.3076923076923077,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"emile smith rowe": {
			"goal": 0.1724137931034483,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"quilindschy hartman": {
			"goal": 0.043478260869565216,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"ryan sessegnon": {
			"goal": 0.14285714285714285,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.26666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jacob bruun larsen": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"joshua king": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"tom cairney": {
			"goal": 0.08333333333333333,
			"assist": 0.11764705882352941,
			"no_assist": 0.9333333333333333
		},
		"kevin macedo": {
			"goal": 0.19047619047619047,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"sasa lukic": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"adama traore": {
			"goal": 0.17857142857142858,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harry wilson": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"alex iwobi": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9090909090909091
		},
	},
	"game_stats": {
		"burnley": {
			"goals": {
				"0": 0.38095238095238093,
				"1": 0.4,
				"2": 0.21052631578947367,
				"3+": 0.09090909090909091
			}
		},
		"fulham": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			}
		}
	}
},
{
	"player_stats": {
		"yerson mosquera": {
			"goal": 0.029411764705882353,
			"assist": 0.014925373134328358,
			"no_assist": 0.9986684420772304
		},
		"santiago bueno": {
			"goal": 0.014925373134328358,
			"assist": 0.014925373134328358,
			"no_assist": 0.9986684420772304
		},
		"ki-jana hoever": {
			"goal": 0.029411764705882353,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ladislav krejci": {
			"goal": 0.034482758620689655,
			"assist": 0.0196078431372549,
			"no_assist": 0.9960159362549801
		},
		"emmanuel agbadou": {
			"goal": 0.029411764705882353,
			"assist": 0.024390243902439025,
			"no_assist": 0.9960159362549801
		},
		"joao gomes": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"toti gomes": {
			"goal": 0.024390243902439025,
			"assist": 0.0196078431372549,
			"no_assist": 0.9950248756218906
		},
		"toluwalase arokodare": {
			"goal": 0.1111111111111111,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"andre trindade": {
			"goal": 0.021739130434782608,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"matt doherty": {
			"goal": 0.029411764705882353,
			"assist": 0.034482758620689655,
			"no_assist": 0.9933774834437086
		},
		"william saliba": {
			"goal": 0.034482758620689655,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"hugo bueno": {
			"goal": 0.0196078431372549,
			"assist": 0.038461538461538464,
			"no_assist": 0.9900990099009901
		},
		"david wolfe": {
			"goal": 0.021739130434782608,
			"assist": 0.038461538461538464,
			"no_assist": 0.9900990099009901
		},
		"mateus mane": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"marli salmon": {
			"goal": 0.034482758620689655,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jorgen larsen": {
			"goal": 0.13333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jackson tchatchoua": {
			"goal": 0.024390243902439025,
			"assist": 0.047619047619047616,
			"no_assist": 0.9876543209876543
		},
		"tawanda chirewa": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"hee-chan hwang": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"fernando lopez": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"jhon arias": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jurrien timber": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"viktor gyokeres": {
			"goal": 0.5,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ben white": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"piero hincapie": {
			"goal": 0.034482758620689655,
			"assist": 0.08333333333333333,
			"no_assist": 0.9333333333333333
		},
		"martin zubimendi": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"myles lewis-skelly": {
			"goal": 0.058823529411764705,
			"assist": 0.11764705882352941,
			"no_assist": 0.9230769230769231
		},
		"ethan nwaneri": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"gabriel martinelli": {
			"goal": 0.37037037037037035,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"gabriel jesus": {
			"goal": 0.4166666666666667,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"josh nichols": {
			"goal": 0.16666666666666666,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"mikel merino": {
			"goal": 0.37037037037037035,
			"assist": 0.23076923076923078,
			"no_assist": 0.875
		},
		"leandro trossard": {
			"goal": 0.4,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"louie copley": {
			"goal": 0.23809523809523808,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"declan rice": {
			"goal": 0.18181818181818182,
			"assist": 0.23076923076923078,
			"no_assist": 0.8571428571428571
		},
		"noni madueke": {
			"goal": 0.35714285714285715,
			"assist": 0.2631578947368421,
			"no_assist": 0.8461538461538461
		},
		"eberechi eze": {
			"goal": 0.39215686274509803,
			"assist": 0.26666666666666666,
			"no_assist": 0.8461538461538461
		},
		"martin odegaard": {
			"goal": 0.19047619047619047,
			"assist": 0.2777777777777778,
			"no_assist": 0.8333333333333334
		},
		"bukayo saka": {
			"goal": 0.4166666666666667,
			"assist": 0.3076923076923077,
			"no_assist": 0.8
		},
	},
	"game_stats": {
		"arsenal": {
			"goals": {
				"0": 0.06666666666666667,
				"1": 0.19047619047619047,
				"2": 0.26666666666666666,
				"3+": 0.5714285714285714
			},
			"clean_sheet": 0.6521739130434783
		},
		"wolverhampton": {
			"goals": {
				"0": 0.6666666666666666,
				"1": 0.3225806451612903,
				"2": 0.08333333333333333,
				"3+": 0.024390243902439025
			},
			"clean_sheet": 0.07692307692307693
		}
	}
},
{
	"player_stats": {
		"ruben dias": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nathan ake": {
			"goal": 0.0625,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"maxence lacroix": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.05,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.03225806451612903,
			"assist": 0.043478260869565216,
			"no_assist": 0.9876543209876543
		},
		"john stones": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9850746268656716
		},
		"abduqodir khusanov": {
			"goal": 0.05555555555555555,
			"assist": 0.058823529411764705,
			"no_assist": 0.9803921568627451
		},
		"chrisantus uche": {
			"goal": 0.15384615384615385,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"josko gvardiol": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"jean-philippe mateta": {
			"goal": 0.34782608695652173,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"tyrick mitchell": {
			"goal": 0.047619047619047616,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"nico oreilly": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.058823529411764705,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"eddie nketiah": {
			"goal": 0.23255813953488372,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"adam wharton": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"rico lewis": {
			"goal": 0.05555555555555555,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nico gonzalez": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"daichi kamada": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"erling haaland": {
			"goal": 0.5555555555555556,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"rayan ait nouri": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kalvin phillips": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.14285714285714285,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"ismaila sarr": {
			"goal": 0.25,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"borna sosa": {
			"goal": 0.038461538461538464,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"justin devenny": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"tijjani reijnders": {
			"goal": 0.15384615384615385,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.15384615384615385,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"oscar bobb": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"bernardo silva": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"phil foden": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9090909090909091
		},
		"divine mukasa": {
			"goal": 0.18181818181818182,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"rayan cherki": {
			"goal": 0.16666666666666666,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"jeremy doku": {
			"goal": 0.19047619047619047,
			"assist": 0.21739130434782608,
			"no_assist": 0.9
		},
		"omar marmoush": {
			"goal": 0.30303030303030304,
			"assist": 0.2,
			"no_assist": 0.8888888888888888
		},
		"matheus nunes": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"de oliveira savio": {
			"goal": 0.16666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
	},
	"game_stats": {
		"crystal palace": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.23809523809523808,
				"3+": 0.13333333333333333
			},
			"clean_sheet": 0.18181818181818182
		},
		"man city": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3333333333333333,
				"2": 0.30303030303030304,
				"3+": 0.29411764705882354
			},
			"clean_sheet": 0.3225806451612903
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jair cunha": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"ben davies": {
			"goal": 0.038461538461538464,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jack thompson": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"joao palhinha": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"callum olusesi": {
			"goal": 0.125,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"luca williams-barnet": {
			"goal": 0.16666666666666666,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"felipe morato": {
			"goal": 0.038461538461538464,
			"assist": 0.038461538461538464,
			"no_assist": 0.9850746268656716
		},
		"archie gray": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.975609756097561
		},
		"ryan yates": {
			"goal": 0.1111111111111111,
			"assist": 0.07142857142857142,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.08695652173913043,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"murillo dos santos": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.975609756097561
		},
		"ibrahim sangare": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"neco williams": {
			"goal": 0.08333333333333333,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.038461538461538464,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"dane scarlett": {
			"goal": 0.26666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"nicolo savona": {
			"goal": 0.07142857142857142,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"nicolas dominguez": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"archie whitehall": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.11764705882352941,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"arnaud kalimuendo": {
			"goal": 0.2857142857142857,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.23255813953488372,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"callum hudson-odoi": {
			"goal": 0.19047619047619047,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"taiwo awoniyi": {
			"goal": 0.29411764705882354,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"randal muani": {
			"goal": 0.23809523809523808,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.09523809523809523,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"wilson odobert": {
			"goal": 0.16666666666666666,
			"assist": 0.11764705882352941,
			"no_assist": 0.9411764705882353
		},
		"igor jesus": {
			"goal": 0.29411764705882354,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"james mcatee": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.20833333333333334,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"richarlison": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9333333333333333
		},
		"jimmy sinclair": {
			"goal": 0.13333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"omari giraud-hutchinson": {
			"goal": 0.1724137931034483,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"dan ndoye": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"morgan gibbs-white": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"elliot anderson": {
			"goal": 0.10526315789473684,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"dilane bakwa": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9090909090909091
		},
		"mohammed kudus": {
			"goal": 0.19047619047619047,
			"assist": 0.16666666666666666,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"willy boly": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"pape matar sarr": {
			"goal": 0.14285714285714285,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
	},
	"game_stats": {
		"nottingham forest": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.3076923076923077
		},
		"tottenham": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"jean-clair todibo": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"konstantinos mavropanos": {
			"goal": 0.047619047619047616,
			"assist": 0.024390243902439025,
			"no_assist": 0.9960159362549801
		},
		"pau torres": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.038461538461538464,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"max kilman": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"yeimar mosquera": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ezri konsa": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.9900990099009901
		},
		"airidas golambeckis": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ezra mayers": {
			"goal": 0.027777777777777776,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"soungoutou magassa": {
			"goal": 0.038461538461538464,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"guido rodriguez": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"amadou onana": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"freddie potts": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"aaron wan-bissaka": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"tomas soucek": {
			"goal": 0.16666666666666666,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"callum marshall": {
			"goal": 0.2222222222222222,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lamare bogarde": {
			"goal": 0.05263157894736842,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"callum wilson": {
			"goal": 0.2777777777777778,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"george hemmings": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"luis guilherme lira": {
			"goal": 0.11764705882352941,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"kyle walker-peters": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"andres garcia": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.06666666666666667,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"el hadji diouf": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"mohamadou kante": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jamaldeen jimoh": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"travis patterson": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"andrew irving": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"lucas paqueta": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"crysencio summerville": {
			"goal": 0.16,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"niclas fullkrug": {
			"goal": 0.2702702702702703,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"james ward-prowse": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"george earthy": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9523809523809523
		},
		"ben broggio": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"john mcginn": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"donyell malen": {
			"goal": 0.30303030303030304,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"lucas digne": {
			"goal": 0.058823529411764705,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"mateus fernandes": {
			"goal": 0.1111111111111111,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"ian maatsen": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"evann guessand": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"ollie watkins": {
			"goal": 0.38461538461538464,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"jarrod bowen": {
			"goal": 0.2777777777777778,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"emiliano buendia": {
			"goal": 0.23809523809523808,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.18181818181818182,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"jadon sancho": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.23809523809523808,
			"assist": 0.18181818181818182,
			"no_assist": 0.9
		},
		"de paulo igor": {
			"goal": 0.034482758620689655,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
	},
	"game_stats": {
		"west ham": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.23809523809523808,
				"3+": 0.125
			},
			"clean_sheet": 0.21739130434782608
		},
		"aston villa": {
			"goals": {
				"0": 0.21739130434782608,
				"1": 0.35714285714285715,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.3333333333333333
		}
	}
},
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"omar alderete": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"fabian schar": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"alex murphy": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"lutsharel geertruida": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"reinildo mandava": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan neil": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jamaal lascelles": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan burn": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"arthur masuaku": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"noah sadiki": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"daniel ballard": {
			"goal": 0.10526315789473684,
			"assist": 0.034482758620689655,
			"no_assist": 0.9803921568627451
		},
		"nordi mukiele": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9803921568627451
		},
		"wilson isidor": {
			"goal": 0.29411764705882354,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.25,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"eliezer mayenda": {
			"goal": 0.26666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"william osula": {
			"goal": 0.29411764705882354,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.034482758620689655,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"trai hume": {
			"goal": 0.05263157894736842,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"brian brobbey": {
			"goal": 0.25,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"jacob ramsey": {
			"goal": 0.15384615384615385,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.13333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"chris rigg": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yoane wissa": {
			"goal": 0.3076923076923077,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"joelinton": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.10526315789473684,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"chemsdine talbi": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.058823529411764705,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"harrison jones": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.3448275862068966,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"enzo le fee": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bertrand traore": {
			"goal": 0.19047619047619047,
			"assist": 0.11764705882352941,
			"no_assist": 0.9411764705882353
		},
		"anthony gordon": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.17391304347826086,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.1,
			"assist": 0.10526315789473684,
			"no_assist": 0.9333333333333333
		},
		"granit xhaka": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9333333333333333
		},
		"simon adingra": {
			"goal": 0.17391304347826086,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"anthony elanga": {
			"goal": 0.16666666666666666,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.23809523809523808,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"romain mundle": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		}
	},
	"game_stats": {
		"sunderland": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.23809523809523808,
				"3+": 0.125
			},
			"clean_sheet": 0.25
		},
		"newcastle": {
			"goals": {
				"0": 0.25,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.3333333333333333
		}
	}
},
{
	"player_stats": {
		"sebastiaan bornauw": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"pascal struijk": {
			"goal": 0.07692307692307693,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"joe rodon": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jaka bijol": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"ethan ampadu": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ethan pinnock": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sam byram": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"aaron hickey": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sepp van den berg": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.07142857142857142,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.2631578947368421,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jayden bogle": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"james justin": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"gabriel gudmundsson": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ilia gruev": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"lukas nmecha": {
			"goal": 0.25,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.058823529411764705,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"kristoffer ajer": {
			"goal": 0.07692307692307693,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.21739130434782608,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.26666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"anton stach": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.038461538461538464,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jack harrison": {
			"goal": 0.14285714285714285,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.09090909090909091,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"vitaly janelt": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"degnand gnonto": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.2222222222222222,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"frank onyeka": {
			"goal": 0.08333333333333333,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"reiss nelson": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"mathias jensen": {
			"goal": 0.10526315789473684,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"dango ouattara": {
			"goal": 0.2631578947368421,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"igor thiago": {
			"goal": 0.42105263157894735,
			"assist": 0.125,
			"no_assist": 0.9090909090909091
		},
		"mikkel damsgaard": {
			"goal": 0.13333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"brentford": {
			"goals": {
				"0": 0.2222222222222222,
				"1": 0.35714285714285715,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.34782608695652173
		},
		"leeds": {
			"goals": {
				"0": 0.35714285714285715,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.1111111111111111
			},
			"clean_sheet": 0.2222222222222222
		}
	}
},
{
	"player_stats": {
		"lisandro martinez": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"veljko milosavljevic": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"tyler fredricson": {
			"goal": 0.1,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"julio soler": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"marcos senesi": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"leny yoro": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ayden heaven": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"adam smith": {
			"goal": 0.029411764705882353,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"alejandro jimenez": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"diego leon": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"malcom dacosta": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"tyrell malacia": {
			"goal": 0.038461538461538464,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jack fletcher": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"noussair mazraoui": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"bafode diakite": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.975609756097561
		},
		"evanilson": {
			"goal": 0.2564102564102564,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"matthijs de ligt": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.975609756097561
		},
		"julian araujo": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"alex scott": {
			"goal": 0.08333333333333333,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"james hill": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9705882352941176
		},
		"eli junior kroupi": {
			"goal": 0.2777777777777778,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"manuel ugarte": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"amine adli": {
			"goal": 0.16666666666666666,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"kobbie mainoo": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"luke shaw": {
			"goal": 0.024390243902439025,
			"assist": 0.07692307692307693,
			"no_assist": 0.9615384615384616
		},
		"adrien truffert": {
			"goal": 0.047619047619047616,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"joshua zirkzee": {
			"goal": 0.3333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"diogo dalot": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"marcus tavernier": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"enes unal": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"casemiro": {
			"goal": 0.15384615384615385,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"shea lacey": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"patrick dorgu": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"mason mount": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"justin kluivert": {
			"goal": 0.19230769230769232,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"antoine semenyo": {
			"goal": 0.2857142857142857,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"david brooks": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"amad diallo": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9090909090909091
		},
		"bryan mbeumo": {
			"goal": 0.38095238095238093,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"bruno fernandes": {
			"goal": 0.30303030303030304,
			"assist": 0.23076923076923078,
			"no_assist": 0.875
		},
		"matheus cunha": {
			"goal": 0.36363636363636365,
			"assist": 0.2,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man utd": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3125,
				"2": 0.3076923076923077,
				"3+": 0.3333333333333333
			},
			"clean_sheet": 0.30303030303030304
		},
		"bournemouth": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"michael keane": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jarrad branthwaite": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reece welch": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"adam aznou": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"timothy iroegbunam": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"vitaliy mykolenko": {
			"goal": 0.034482758620689655,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jake obrien": {
			"goal": 0.05555555555555555,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"idrissa gueye": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"benoit badiashile": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tosin adarabioyo": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"wesley fofana": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"james tarkowski": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9850746268656716
		},
		"trevoh chalobah": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9850746268656716
		},
		"beto": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"elijah campbell": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9850746268656716
		},
		"nathan patterson": {
			"goal": 0.034482758620689655,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"thierno barry": {
			"goal": 0.19047619047619047,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"tyler dibling": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james garner": {
			"goal": 0.06666666666666667,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"andrey santos": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"josh acheampong": {
			"goal": 0.0625,
			"assist": 0.05263157894736842,
			"no_assist": 0.9615384615384616
		},
		"marc cucurella": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kiernan dewsbury-hall": {
			"goal": 0.125,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"jorrel hato": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"dwight mcneil": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"carlos alcaraz": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"marc guiu": {
			"goal": 0.2857142857142857,
			"assist": 0.11764705882352941,
			"no_assist": 0.9411764705882353
		},
		"malo gusto": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"jack grealish": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"facundo buonanotte": {
			"goal": 0.21052631578947367,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"enzo fernandez": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"alejandro garnacho": {
			"goal": 0.2631578947368421,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"reece james": {
			"goal": 0.1,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"tyrique george": {
			"goal": 0.2857142857142857,
			"assist": 0.1724137931034483,
			"no_assist": 0.9230769230769231
		},
		"jamie bynoe-gittens": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"pedro neto": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"estevao": {
			"goal": 0.2631578947368421,
			"assist": 0.15384615384615385,
			"no_assist": 0.9
		},
		"cole palmer": {
			"goal": 0.3448275862068966,
			"assist": 0.2,
			"no_assist": 0.875
		},
		"de jesus joao pedro": {
			"goal": 0.30303030303030304,
			"assist": 0.18181818181818182,
			"no_assist": 0.9090909090909091
		},
	},
	"game_stats": {
		"chelsea": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3225806451612903,
				"2": 0.30303030303030304,
				"3+": 0.29411764705882354
			},
			"clean_sheet": 0.40816326530612246
		},
		"everton": {
			"goals": {
				"0": 0.4166666666666667,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.08333333333333333
			},
			"clean_sheet": 0.18181818181818182
		}
	}
}
]
"""

"""
DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"alex murphy": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"benoit badiashile": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"fabian schar": {
			"goal": 0.1111111111111111,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"wesley fofana": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"trevoh chalobah": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jamaal lascelles": {
			"goal": 0.058823529411764705,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan burn": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"moises caicedo": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"marc cucurella": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"william osula": {
			"goal": 0.2564102564102564,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"romeo lavia": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andrey santos": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh acheampong": {
			"goal": 0.05,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.0625,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jorrel hato": {
			"goal": 0.05263157894736842,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jacob ramsey": {
			"goal": 0.1724137931034483,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"liam delap": {
			"goal": 0.30303030303030304,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"marc guiu": {
			"goal": 0.23809523809523808,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.05263157894736842,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.4,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"facundo buonanotte": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jamie bynoe-gittens": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tyrique george": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alejandro garnacho": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"enzo fernandez": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"anthony gordon": {
			"goal": 0.29411764705882354,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"pedro neto": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.13333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"estevao": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"cole palmer": {
			"goal": 0.30303030303030304,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"bruno guimaraes": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"de jesus joao pedro": {
			"goal": 0.30303030303030304,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		}
	},
	"game_stats": {
		"newcastle": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.2631578947368421
		},
		"chelsea": {
			"goals": {
				"0": 0.26666666666666666,
				"1": 0.38095238095238093,
				"2": 0.2702702702702703,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.23809523809523808
		}
	}
},
{
	"player_stats": {
		"santiago bueno": {
			"goal": 0.038461538461538464,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"yerson mosquera": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ethan pinnock": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"aaron hickey": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"emmanuel agbadou": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ladislav krejci": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"toti gomes": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"joao gomes": {
			"goal": 0.09523809523809523,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"benjamin arthur": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"kristoffer ajer": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"toluwalase arokodare": {
			"goal": 0.2777777777777778,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"andre trindade": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"matt doherty": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"yunus emre konak": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mateus mane": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"david wolfe": {
			"goal": 0.05,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"hugo bueno": {
			"goal": 0.05263157894736842,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"michael kayode": {
			"goal": 0.058823529411764705,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"jorgen larsen": {
			"goal": 0.29411764705882354,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"tawanda chirewa": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"hee-chan hwang": {
			"goal": 0.2222222222222222,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jackson tchatchoua": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jordan henderson": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"frank onyeka": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"fernando lopez": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jhon arias": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"keane lewis-potter": {
			"goal": 0.14285714285714285,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kevin schade": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.23255813953488372,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mathias jensen": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dango ouattara": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.38095238095238093,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.15384615384615385,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"wolverhampton": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.23076923076923078
		},
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.34782608695652173
		}
	}
},
{
	"player_stats": {
		"omar alderete": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reinildo mandava": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"lutsharel geertruida": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"lewis dunk": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"noah sadiki": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"arthur masuaku": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jan paul van hecke": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan neil": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"freddie simmonds": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"diego coppola": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"daniel ballard": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"eliezer mayenda": {
			"goal": 0.23076923076923078,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nordi mukiele": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"wilson isidor": {
			"goal": 0.23809523809523808,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"brian brobbey": {
			"goal": 0.21739130434782608,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"trai hume": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"carlos baleba": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel veltman": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"charlie tasker": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"olivier boscagli": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ferdi kadioglu": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chris rigg": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"danny welbeck": {
			"goal": 0.40816326530612246,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yasin ayari": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jack hinshelwood": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"harrison jones": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"chemsdine talbi": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"enzo le fee": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"bertrand traore": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"simon adingra": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"granit xhaka": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"james milner": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"maxim de cuyper": {
			"goal": 0.15384615384615385,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"charalampos kostoulas": {
			"goal": 0.30303030303030304,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tom watson": {
			"goal": 0.21739130434782608,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mats wieffer": {
			"goal": 0.10526315789473684,
			"assist": 0.18518518518518517,
			"no_assist": 0.9090909090909091
		},
		"joe knight": {
			"goal": 0.18181818181818182,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"diego gomez": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"brajan gruda": {
			"goal": 0.23255813953488372,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"kaoru mitoma": {
			"goal": 0.2702702702702703,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"nehemiah oriola": {
			"goal": 0.26666666666666666,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"georginio rutter": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"yankuba minteh": {
			"goal": 0.2702702702702703,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"romain mundle": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"brighton": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3125,
				"2": 0.3076923076923077,
				"3+": 0.3333333333333333
			},
			"clean_sheet": 0.40816326530612246
		},
		"sunderland": {
			"goals": {
				"0": 0.4166666666666667,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.038461538461538464,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"axel tuanzebe": {
			"goal": 0.029411764705882353,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"joe worrall": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.029411764705882353,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"veljko milosavljevic": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"ashley barnes": {
			"goal": 0.16666666666666666,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lucas pires": {
			"goal": 0.04,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"julio soler": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"bashir humphreys": {
			"goal": 0.043478260869565216,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"marcos senesi": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler adams": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jaydon banel": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh laurent": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"lesley ugochukwu": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"adam smith": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"brandon pouani": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"zian flemming": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"quilindschy hartman": {
			"goal": 0.05263157894736842,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"malcom dacosta": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lyle foster": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"alejandro jimenez": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"evanilson": {
			"goal": 0.35714285714285715,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"julian araujo": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"bafode diakite": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james hill": {
			"goal": 0.09090909090909091,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"lewis cook": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"alex scott": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"eli junior kroupi": {
			"goal": 0.37735849056603776,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan christie": {
			"goal": 0.15384615384615385,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adrien truffert": {
			"goal": 0.07692307692307693,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"amine adli": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enes unal": {
			"goal": 0.38095238095238093,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"marcus tavernier": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"justin kluivert": {
			"goal": 0.2857142857142857,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"antoine semenyo": {
			"goal": 0.42105263157894735,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"david brooks": {
			"goal": 0.2777777777777778,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"bournemouth": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.2857142857142857,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"burnley": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"konstantinos mavropanos": {
			"goal": 0.034482758620689655,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jean-clair todibo": {
			"goal": 0.024390243902439025,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"max kilman": {
			"goal": 0.024390243902439025,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"soungoutou magassa": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ruben dias": {
			"goal": 0.08,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"airidas golambeckis": {
			"goal": 0.034482758620689655,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"guido rodriguez": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"oliver scarles": {
			"goal": 0.034482758620689655,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan ake": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"aaron wan-bissaka": {
			"goal": 0.0196078431372549,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"freddie potts": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tomas soucek": {
			"goal": 0.1111111111111111,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum marshall": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum wilson": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luis guilherme lira": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mohamadou kante": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"el hadji diouf": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kyle walker-peters": {
			"goal": 0.024390243902439025,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"andrew irving": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james ward-prowse": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"crysencio summerville": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"george earthy": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"john stones": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lucas paqueta": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"niclas fullkrug": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"abduqodir khusanov": {
			"goal": 0.08,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"mateus fernandes": {
			"goal": 0.06666666666666667,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jarrod bowen": {
			"goal": 0.21739130434782608,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"nico oreilly": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"nico gonzalez": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rico lewis": {
			"goal": 0.08695652173913043,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"erling haaland": {
			"goal": 0.6923076923076923,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"rayan ait nouri": {
			"goal": 0.13333333333333333,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"kalvin phillips": {
			"goal": 0.13333333333333333,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"tijjani reijnders": {
			"goal": 0.2702702702702703,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"oscar bobb": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bernardo silva": {
			"goal": 0.2,
			"assist": 0.21739130434782608,
			"no_assist": 0.875
		},
		"divine mukasa": {
			"goal": 0.29411764705882354,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"phil foden": {
			"goal": 0.4166666666666667,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"rayan cherki": {
			"goal": 0.29411764705882354,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"jeremy doku": {
			"goal": 0.2631578947368421,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"omar marmoush": {
			"goal": 0.46511627906976744,
			"assist": 0.36363636363636365,
			"no_assist": 0.8181818181818182
		},
		"de paulo igor": {
			"goal": 0.024390243902439025,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"matheus nunes": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"de oliveira savio": {
			"goal": 0.30303030303030304,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man city": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.2,
				"2": 0.26666666666666666,
				"3+": 0.5789473684210527
			},
			"clean_sheet": 0.47619047619047616
		},
		"west ham": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.06666666666666667
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.058823529411764705,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"ben davies": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"junai byfield": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"kevin danso": {
			"goal": 0.058823529411764705,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joao palhinha": {
			"goal": 0.10526315789473684,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ibrahima konate": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joe gomez": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"rodrigo bentancur": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"virgil van dijk": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"wataru endo": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"archie gray": {
			"goal": 0.043478260869565216,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.043478260869565216,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"trey nyoni": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"milos kerkez": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.26666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"curtis jones": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"alexis mac allister": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"randal muani": {
			"goal": 0.2857142857142857,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ryan gravenberch": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"andrew robertson": {
			"goal": 0.0625,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"calvin ramsay": {
			"goal": 0.1111111111111111,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"conor bradley": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"federico chiesa": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jayden danns": {
			"goal": 0.3333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"richarlison": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jeremie frimpong": {
			"goal": 0.11764705882352941,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"alexander isak": {
			"goal": 0.39215686274509803,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rio ngumoha": {
			"goal": 0.22727272727272727,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.2,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"cody gakpo": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"hugo ekitike": {
			"goal": 0.35714285714285715,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mohammed kudus": {
			"goal": 0.23809523809523808,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"florian wirtz": {
			"goal": 0.23809523809523808,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"dominik szoboszlai": {
			"goal": 0.23076923076923078,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"mohamed salah": {
			"goal": 0.38461538461538464,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"mickey van de ven": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"pape matar sarr": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"tottenham": {
			"goals": {
				"0": 0.2857142857142857,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.18181818181818182
		},
		"liverpool": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3333333333333333,
				"2": 0.30303030303030304,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"michael keane": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jarrad branthwaite": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"william saliba": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"reece welch": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"adam aznou": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"idrissa gueye": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jake obrien": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"vitaliy mykolenko": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"timothy iroegbunam": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"james tarkowski": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"beto": {
			"goal": 0.21739130434782608,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"elijah campbell": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"christian norgaard": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"nathan patterson": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jurrien timber": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"thierno barry": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"viktor gyokeres": {
			"goal": 0.4,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james garner": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"merlin rohl": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"piero hincapie": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ben white": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"riccardo calafiori": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tyler dibling": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kiernan dewsbury-hall": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"carlos alcaraz": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"martin zubimendi": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dwight mcneil": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ethan nwaneri": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jack grealish": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"gabriel martinelli": {
			"goal": 0.2564102564102564,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"gabriel jesus": {
			"goal": 0.3225806451612903,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"mikel merino": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"declan rice": {
			"goal": 0.125,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"leandro trossard": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"noni madueke": {
			"goal": 0.23809523809523808,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"eberechi eze": {
			"goal": 0.2631578947368421,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"martin odegaard": {
			"goal": 0.16666666666666666,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"bukayo saka": {
			"goal": 0.3076923076923077,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"everton": {
			"goals": {
				"0": 0.4444444444444444,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.2222222222222222
		},
		"arsenal": {
			"goals": {
				"0": 0.21739130434782608,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.4444444444444444
		}
	}
},
{
	"player_stats": {
		"joe rodon": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"sebastiaan bornauw": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"chris richards": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"rio cardines": {
			"goal": 0.21739130434782608,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sam byram": {
			"goal": 0.038461538461538464,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"james justin": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ilia gruev": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"joel piroe": {
			"goal": 0.29411764705882354,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"tyrick mitchell": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"chrisantus uche": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lukas nmecha": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jean-philippe mateta": {
			"goal": 0.36363636363636365,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.1,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"anton stach": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"noah okafor": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"adam wharton": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daichi kamada": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"eddie nketiah": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ismaila sarr": {
			"goal": 0.25,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"justin devenny": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"degnand gnonto": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"borna sosa": {
			"goal": 0.058823529411764705,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"leeds": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.29411764705882354
		},
		"crystal palace": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3225806451612903
		}
	}
},
{
	"player_stats": {
		"matthijs de ligt": {
			"goal": 0.07692307692307693,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"lisandro martinez": {
			"goal": 0.058823529411764705,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"tyler fredricson": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pau torres": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"leny yoro": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ayden heaven": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"yeimar mosquera": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"diego leon": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"tyrell malacia": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"noussair mazraoui": {
			"goal": 0.043478260869565216,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"jack fletcher": {
			"goal": 0.1111111111111111,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"luke shaw": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"manuel ugarte": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kobbie mainoo": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"amadou onana": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"george hemmings": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lamare bogarde": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"casemiro": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"diogo dalot": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"andres garcia": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joshua zirkzee": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"travis patterson": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"benjamin sesko": {
			"goal": 0.3225806451612903,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"mason mount": {
			"goal": 0.1724137931034483,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jamaldeen jimoh": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"patrick dorgu": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"shea lacey": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"donyell malen": {
			"goal": 0.3225806451612903,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"john mcginn": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"amad diallo": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ben broggio": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"youri tielemans": {
			"goal": 0.15384615384615385,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"bryan mbeumo": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ian maatsen": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9333333333333333
		},
		"lucas digne": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"evann guessand": {
			"goal": 0.3225806451612903,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"ollie watkins": {
			"goal": 0.43478260869565216,
			"assist": 0.1724137931034483,
			"no_assist": 0.9230769230769231
		},
		"bruno fernandes": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"emiliano buendia": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"jadon sancho": {
			"goal": 0.1724137931034483,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.18181818181818182,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.23809523809523808,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"matheus cunha": {
			"goal": 0.29411764705882354,
			"assist": 0.20833333333333334,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"aston villa": {
			"goals": {
				"0": 0.21052631578947367,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.25
			},
			"clean_sheet": 0.29411764705882354
		},
		"man utd": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.39215686274509803,
				"2": 0.2631578947368421,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.21052631578947367
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"calvin bassey": {
			"goal": 0.058823529411764705,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joachim andersen": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jack thompson": {
			"goal": 0.14285714285714285,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"felipe morato": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jorge cuenca": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"neco williams": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ryan yates": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ibrahim sangare": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"timothy castagne": {
			"goal": 0.08695652173913043,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kenny tete": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolas dominguez": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"chris wood": {
			"goal": 0.29411764705882354,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolo savona": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.17391304347826086,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"arnaud kalimuendo": {
			"goal": 0.2564102564102564,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.3125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.34782608695652173,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"emile smith rowe": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joshua king": {
			"goal": 0.2222222222222222,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"igor jesus": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"antonee robinson": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"omari giraud-hutchinson": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ryan sessegnon": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jimmy sinclair": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"sasa lukic": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.19047619047619047,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.29411764705882354,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"dan ndoye": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.08,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"morgan gibbs-white": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"elliot anderson": {
			"goal": 0.09090909090909091,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dilane bakwa": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harry wilson": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"alex iwobi": {
			"goal": 0.18181818181818182,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"willy boly": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		}
	},
	"game_stats": {
		"fulham": {
			"goals": {
				"0": 0.2631578947368421,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.34782608695652173
		},
		"nottingham forest": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.2631578947368421
		}
	}
},
]
"""

"""
DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"alex murphy": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.05555555555555555,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"benoit badiashile": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"fabian schar": {
			"goal": 0.1111111111111111,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"wesley fofana": {
			"goal": 0.05555555555555555,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"trevoh chalobah": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jamaal lascelles": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan burn": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"moises caicedo": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"marc cucurella": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"william osula": {
			"goal": 0.2564102564102564,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"romeo lavia": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andrey santos": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh acheampong": {
			"goal": 0.05,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.0625,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jorrel hato": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jacob ramsey": {
			"goal": 0.1724137931034483,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"liam delap": {
			"goal": 0.3125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"marc guiu": {
			"goal": 0.23809523809523808,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.4,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"facundo buonanotte": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jamie bynoe-gittens": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tyrique george": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alejandro garnacho": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"enzo fernandez": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"anthony gordon": {
			"goal": 0.3076923076923077,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"pedro neto": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.14285714285714285,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"estevao": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"cole palmer": {
			"goal": 0.30303030303030304,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"de jesus joao pedro": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		}
	},
	"game_stats": {
		"newcastle": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.2631578947368421
		},
		"chelsea": {
			"goals": {
				"0": 0.26666666666666666,
				"1": 0.38095238095238093,
				"2": 0.2702702702702703,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.23809523809523808
		}
	}
},
{
	"player_stats": {
		"santiago bueno": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"yerson mosquera": {
			"goal": 0.0625,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ethan pinnock": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"aaron hickey": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"emmanuel agbadou": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ladislav krejci": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"toti gomes": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"joao gomes": {
			"goal": 0.09523809523809523,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"benjamin arthur": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"kristoffer ajer": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"toluwalase arokodare": {
			"goal": 0.2777777777777778,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"andre trindade": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"matt doherty": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"yunus emre konak": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mateus mane": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"david wolfe": {
			"goal": 0.05,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.21739130434782608,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"hugo bueno": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"michael kayode": {
			"goal": 0.06666666666666667,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"jorgen larsen": {
			"goal": 0.3076923076923077,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"tawanda chirewa": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"hee-chan hwang": {
			"goal": 0.2222222222222222,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jackson tchatchoua": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jordan henderson": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"frank onyeka": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"fernando lopez": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jhon arias": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kevin schade": {
			"goal": 0.2777777777777778,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.23255813953488372,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mathias jensen": {
			"goal": 0.125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dango ouattara": {
			"goal": 0.29411764705882354,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.38461538461538464,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.15384615384615385,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"wolverhampton": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.23076923076923078
		},
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.34782608695652173
		}
	}
},
{
	"player_stats": {
		"omar alderete": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reinildo mandava": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"lutsharel geertruida": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"diego coppola": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jan paul van hecke": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan neil": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"freddie simmonds": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"arthur masuaku": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"daniel ballard": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"eliezer mayenda": {
			"goal": 0.2222222222222222,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"wilson isidor": {
			"goal": 0.25,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nordi mukiele": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"brian brobbey": {
			"goal": 0.21739130434782608,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"trai hume": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"joel veltman": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"ferdi kadioglu": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"olivier boscagli": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"charlie tasker": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chris rigg": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison jones": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"yasin ayari": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jack hinshelwood": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"danny welbeck": {
			"goal": 0.40816326530612246,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"enzo le fee": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chemsdine talbi": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"bertrand traore": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"simon adingra": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"granit xhaka": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"james milner": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"charalampos kostoulas": {
			"goal": 0.30303030303030304,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"maxim de cuyper": {
			"goal": 0.19230769230769232,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tom watson": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"brajan gruda": {
			"goal": 0.23255813953488372,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mats wieffer": {
			"goal": 0.10526315789473684,
			"assist": 0.18518518518518517,
			"no_assist": 0.9090909090909091
		},
		"joe knight": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"nehemiah oriola": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"kaoru mitoma": {
			"goal": 0.2702702702702703,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"georginio rutter": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"yankuba minteh": {
			"goal": 0.2702702702702703,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"romain mundle": {
			"goal": 0.16666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
	},
	"game_stats": {
		"brighton": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3125,
				"2": 0.3076923076923077,
				"3+": 0.3076923076923077
			},
			"clean_sheet": 0.40816326530612246
		},
		"sunderland": {
			"goals": {
				"0": 0.4166666666666667,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.047619047619047616,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.05555555555555555,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"axel tuanzebe": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"joe worrall": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"veljko milosavljevic": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"ashley barnes": {
			"goal": 0.16666666666666666,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lucas pires": {
			"goal": 0.04,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"julio soler": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"bashir humphreys": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"marcos senesi": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler adams": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jaydon banel": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh laurent": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"lesley ugochukwu": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"adam smith": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"brandon pouani": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"zian flemming": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"malcom dacosta": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lyle foster": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"alejandro jimenez": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"evanilson": {
			"goal": 0.36363636363636365,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"julian araujo": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"bafode diakite": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james hill": {
			"goal": 0.1,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"lewis cook": {
			"goal": 0.10526315789473684,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"alex scott": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"eli junior kroupi": {
			"goal": 0.38461538461538464,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan christie": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"amine adli": {
			"goal": 0.23809523809523808,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adrien truffert": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"enes unal": {
			"goal": 0.4,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"marcus tavernier": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"justin kluivert": {
			"goal": 0.2857142857142857,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"david brooks": {
			"goal": 0.2777777777777778,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"antoine semenyo": {
			"goal": 0.43478260869565216,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"bournemouth": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.29411764705882354,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"burnley": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"jean-clair todibo": {
			"goal": 0.029411764705882353,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"konstantinos mavropanos": {
			"goal": 0.038461538461538464,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"max kilman": {
			"goal": 0.024390243902439025,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"soungoutou magassa": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"airidas golambeckis": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ruben dias": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"guido rodriguez": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"freddie potts": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan ake": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"aaron wan-bissaka": {
			"goal": 0.024390243902439025,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"oliver scarles": {
			"goal": 0.038461538461538464,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tomas soucek": {
			"goal": 0.125,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum marshall": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum wilson": {
			"goal": 0.2,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"mohamadou kante": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"el hadji diouf": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"luis guilherme lira": {
			"goal": 0.1111111111111111,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"kyle walker-peters": {
			"goal": 0.029411764705882353,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"andrew irving": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"george earthy": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james ward-prowse": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"niclas fullkrug": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lucas paqueta": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"john stones": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"crysencio summerville": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mateus fernandes": {
			"goal": 0.07692307692307693,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"abduqodir khusanov": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jarrod bowen": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"nico oreilly": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"nico gonzalez": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rico lewis": {
			"goal": 0.08695652173913043,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"erling haaland": {
			"goal": 0.7142857142857143,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"rayan ait nouri": {
			"goal": 0.14285714285714285,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"kalvin phillips": {
			"goal": 0.14285714285714285,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"tijjani reijnders": {
			"goal": 0.2702702702702703,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"oscar bobb": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bernardo silva": {
			"goal": 0.2,
			"assist": 0.20833333333333334,
			"no_assist": 0.875
		},
		"divine mukasa": {
			"goal": 0.2857142857142857,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"phil foden": {
			"goal": 0.42105263157894735,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"jeremy doku": {
			"goal": 0.2702702702702703,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"rayan cherki": {
			"goal": 0.29411764705882354,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"omar marmoush": {
			"goal": 0.4878048780487805,
			"assist": 0.36363636363636365,
			"no_assist": 0.8181818181818182
		},
		"de paulo igor": {
			"goal": 0.029411764705882353,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"matheus nunes": {
			"goal": 0.1111111111111111,
			"assist": 0.16,
			"no_assist": 0.9230769230769231
		},
		"de oliveira savio": {
			"goal": 0.3125,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man city": {
			"goals": {
				"0": 0.06666666666666667,
				"1": 0.2,
				"2": 0.2702702702702703,
				"3+": 0.5789473684210527
			},
			"clean_sheet": 0.47619047619047616
		},
		"west ham": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.06666666666666667
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"ben davies": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"junai byfield": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"joao palhinha": {
			"goal": 0.10526315789473684,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.0625,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ibrahima konate": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joe gomez": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"archie gray": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.08695652173913043,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"virgil van dijk": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"trey nyoni": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"djed spence": {
			"goal": 0.05,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"curtis jones": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.2857142857142857,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"milos kerkez": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ryan gravenberch": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"randal muani": {
			"goal": 0.2857142857142857,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"alexis mac allister": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"conor bradley": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"andrew robertson": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"calvin ramsay": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alexander isak": {
			"goal": 0.39215686274509803,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"federico chiesa": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"rio ngumoha": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"richarlison": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jayden danns": {
			"goal": 0.3333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jeremie frimpong": {
			"goal": 0.125,
			"assist": 0.16,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.21739130434782608,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"hugo ekitike": {
			"goal": 0.35714285714285715,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mohammed kudus": {
			"goal": 0.23809523809523808,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"dominik szoboszlai": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"florian wirtz": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"mickey van de ven": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"pape matar sarr": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"tottenham": {
			"goals": {
				"0": 0.2857142857142857,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.18181818181818182
		},
		"liverpool": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3333333333333333,
				"2": 0.30303030303030304,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"jarrad branthwaite": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"michael keane": {
			"goal": 0.058823529411764705,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"reece welch": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"william saliba": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jake obrien": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"idrissa gueye": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"adam aznou": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"vitaliy mykolenko": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"timothy iroegbunam": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"elijah campbell": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"beto": {
			"goal": 0.2,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"james tarkowski": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan patterson": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler dibling": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"thierno barry": {
			"goal": 0.20833333333333334,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james garner": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"jurrien timber": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ben white": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"viktor gyokeres": {
			"goal": 0.4,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"merlin rohl": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"riccardo calafiori": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"carlos alcaraz": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kiernan dewsbury-hall": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dwight mcneil": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"piero hincapie": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"martin zubimendi": {
			"goal": 0.09523809523809523,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"gabriel jesus": {
			"goal": 0.36363636363636365,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jack grealish": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ethan nwaneri": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"gabriel martinelli": {
			"goal": 0.2631578947368421,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"mikel merino": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"eberechi eze": {
			"goal": 0.2631578947368421,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"noni madueke": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"leandro trossard": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"declan rice": {
			"goal": 0.13333333333333333,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"martin odegaard": {
			"goal": 0.16666666666666666,
			"assist": 0.20833333333333334,
			"no_assist": 0.9
		},
		"bukayo saka": {
			"goal": 0.3225806451612903,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"everton": {
			"goals": {
				"0": 0.4444444444444444,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.2
		},
		"arsenal": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.4444444444444444
		}
	}
},
{
	"player_stats": {
		"joe rodon": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pascal struijk": {
			"goal": 0.1,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"chris richards": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"rio cardines": {
			"goal": 0.23076923076923078,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"james justin": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ilia gruev": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"joel piroe": {
			"goal": 0.3076923076923077,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"tyrick mitchell": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"chrisantus uche": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lukas nmecha": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jean-philippe mateta": {
			"goal": 0.38461538461538464,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.1111111111111111,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"anton stach": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"noah okafor": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"adam wharton": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daichi kamada": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"eddie nketiah": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ismaila sarr": {
			"goal": 0.26666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"justin devenny": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"degnand gnonto": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"borna sosa": {
			"goal": 0.06666666666666667,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"leeds": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.29411764705882354
		},
		"crystal palace": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3225806451612903
		}
	}
},
{
	"player_stats": {
		"matthijs de ligt": {
			"goal": 0.07692307692307693,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"lisandro martinez": {
			"goal": 0.058823529411764705,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"tyler fredricson": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pau torres": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"leny yoro": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ayden heaven": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"yeimar mosquera": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tyrell malacia": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"noussair mazraoui": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"diego leon": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jack fletcher": {
			"goal": 0.1111111111111111,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"kobbie mainoo": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"manuel ugarte": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"luke shaw": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"george hemmings": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"amadou onana": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"shea lacey": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"diogo dalot": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.08695652173913043,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joshua zirkzee": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"benjamin sesko": {
			"goal": 0.3225806451612903,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lamare bogarde": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"casemiro": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mason mount": {
			"goal": 0.1724137931034483,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"andres garcia": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jamaldeen jimoh": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"travis patterson": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.09090909090909091,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"patrick dorgu": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ben broggio": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"john mcginn": {
			"goal": 0.20833333333333334,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"donyell malen": {
			"goal": 0.3333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"amad diallo": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.21052631578947367,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"bryan mbeumo": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ian maatsen": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"evann guessand": {
			"goal": 0.3333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"lucas digne": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"ollie watkins": {
			"goal": 0.43478260869565216,
			"assist": 0.1724137931034483,
			"no_assist": 0.9230769230769231
		},
		"emiliano buendia": {
			"goal": 0.2777777777777778,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"bruno fernandes": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"jadon sancho": {
			"goal": 0.1724137931034483,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.23809523809523808,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"matheus cunha": {
			"goal": 0.2857142857142857,
			"assist": 0.20833333333333334,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"aston villa": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.29411764705882354
		},
		"man utd": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"calvin bassey": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joachim andersen": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jack thompson": {
			"goal": 0.15384615384615385,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"felipe morato": {
			"goal": 0.07142857142857142,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jorge cuenca": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"neco williams": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ryan yates": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ibrahim sangare": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"timothy castagne": {
			"goal": 0.08695652173913043,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kenny tete": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolas dominguez": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"chris wood": {
			"goal": 0.3076923076923077,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.1724137931034483,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.34782608695652173,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"emile smith rowe": {
			"goal": 0.1724137931034483,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joshua king": {
			"goal": 0.2222222222222222,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"igor jesus": {
			"goal": 0.3076923076923077,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"antonee robinson": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"omari giraud-hutchinson": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"sasa lukic": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ryan sessegnon": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jimmy sinclair": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"dan ndoye": {
			"goal": 0.14814814814814814,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.3076923076923077,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"elliot anderson": {
			"goal": 0.1,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"morgan gibbs-white": {
			"goal": 0.20833333333333334,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dilane bakwa": {
			"goal": 0.21739130434782608,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adama traore": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harry wilson": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"alex iwobi": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"willy boly": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		}
	},
	"game_stats": {
		"fulham": {
			"goals": {
				"0": 0.2631578947368421,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.3448275862068966
		},
		"nottingham forest": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.2631578947368421
		}
	}
},
]
"""

DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.1,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"lisandro martinez": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"fabian schar": {
			"goal": 0.14285714285714285,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"tyler fredricson": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.1,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"alex murphy": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"leny yoro": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jamaal lascelles": {
			"goal": 0.058823529411764705,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ayden heaven": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan burn": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tyrell malacia": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"diego leon": {
			"goal": 0.125,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"jack fletcher": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"matthijs de ligt": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"noussair mazraoui": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"sean neave": {
			"goal": 0.2777777777777778,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"valentino livramento": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kobbie mainoo": {
			"goal": 0.18181818181818182,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"manuel ugarte": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"luke shaw": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.3225806451612903,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joe willock": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"diogo dalot": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"casemiro": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yoane wissa": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joshua zirkzee": {
			"goal": 0.3333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jacob ramsey": {
			"goal": 0.23076923076923078,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"benjamin sesko": {
			"goal": 0.4,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"shea lacey": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mason mount": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"patrick dorgu": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.38095238095238093,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"sandro tonali": {
			"goal": 0.14285714285714285,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony gordon": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"harvey barnes": {
			"goal": 0.2857142857142857,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"amad diallo": {
			"goal": 0.3076923076923077,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bryan mbeumo": {
			"goal": 0.34782608695652173,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"bruno fernandes": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"matheus cunha": {
			"goal": 0.34782608695652173,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"man utd": {
			"goals": {
				"0": 0.2,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.26666666666666666
		},
		"newcastle": {
			"goals": {
				"0": 0.26666666666666666,
				"1": 0.38461538461538464,
				"2": 0.2777777777777778,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.058823529411764705,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"nikola milenkovic": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ruben dias": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"zach abbott": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"nathan ake": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jack thompson": {
			"goal": 0.15384615384615385,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"felipe morato": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"neco williams": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ibrahim sangare": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ryan yates": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"john stones": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"nicolas dominguez": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chris wood": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"abduqodir khusanov": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"taiwo awoniyi": {
			"goal": 0.2857142857142857,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josko gvardiol": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.18181818181818182,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james mcatee": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"douglas luiz": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"igor jesus": {
			"goal": 0.26666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"archie whitehall": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"nico oreilly": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jimmy sinclair": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"erling haaland": {
			"goal": 0.6190476190476191,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"omari giraud-hutchinson": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"nico gonzalez": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"dan ndoye": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"rico lewis": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"rayan ait nouri": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"morgan gibbs-white": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"elliot anderson": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kalvin phillips": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"tijjani reijnders": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dilane bakwa": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"oscar bobb": {
			"goal": 0.2857142857142857,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bernardo silva": {
			"goal": 0.18181818181818182,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"divine mukasa": {
			"goal": 0.21052631578947367,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"phil foden": {
			"goal": 0.3333333333333333,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"rayan cherki": {
			"goal": 0.2857142857142857,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"jeremy doku": {
			"goal": 0.25,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"omar marmoush": {
			"goal": 0.38461538461538464,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"willy boly": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"matheus nunes": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"de oliveira savio": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		}
	},
	"game_stats": {
		"nottingham forest": {
			"goals": {
				"0": 0.4,
				"1": 0.40816326530612246,
				"2": 0.21052631578947367,
				"3+": 0.09090909090909091
			},
			"clean_sheet": 0.14285714285714285
		},
		"man city": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.29411764705882354,
				"2": 0.3076923076923077,
				"3+": 0.36363636363636365
			},
			"clean_sheet": 0.4
		}
	}
},
{
	"player_stats": {
		"santiago bueno": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"yerson mosquera": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"ladislav krejci": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emmanuel agbadou": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"toti gomes": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"joao gomes": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"toluwalase arokodare": {
			"goal": 0.21052631578947367,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"matt doherty": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"andre trindade": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"mateus mane": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"david wolfe": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"marshall munetsi": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"rodrigo gomes": {
			"goal": 0.125,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"ibrahima konate": {
			"goal": 0.15384615384615385,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"hugo bueno": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jackson tchatchoua": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"tawanda chirewa": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joe gomez": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"jorgen larsen": {
			"goal": 0.23076923076923078,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"hee-chan hwang": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"fernando lopez": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jhon arias": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"virgil van dijk": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"wataru endo": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"milos kerkez": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"trey nyoni": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"curtis jones": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"alexis mac allister": {
			"goal": 0.21052631578947367,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"ryan gravenberch": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"andrew robertson": {
			"goal": 0.15384615384615385,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"conor bradley": {
			"goal": 0.15384615384615385,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"calvin ramsay": {
			"goal": 0.18181818181818182,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"rio ngumoha": {
			"goal": 0.36363636363636365,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"jayden danns": {
			"goal": 0.45454545454545453,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"federico chiesa": {
			"goal": 0.36363636363636365,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"alexander isak": {
			"goal": 0.5789473684210527,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"jeremie frimpong": {
			"goal": 0.18181818181818182,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"cody gakpo": {
			"goal": 0.4,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"hugo ekitike": {
			"goal": 0.5454545454545454,
			"assist": 0.2857142857142857,
			"no_assist": 0.875
		},
		"florian wirtz": {
			"goal": 0.34782608695652173,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"dominik szoboszlai": {
			"goal": 0.34782608695652173,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"mohamed salah": {
			"goal": 0.5555555555555556,
			"assist": 0.36363636363636365,
			"no_assist": 0.8181818181818182
		}
	},
	"game_stats": {
		"liverpool": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.21052631578947367,
				"2": 0.2857142857142857,
				"3+": 0.5454545454545454
			},
			"clean_sheet": 0.5
		},
		"wolverhampton": {
			"goals": {
				"0": 0.5,
				"1": 0.4,
				"2": 0.15384615384615385,
				"3+": 0.05263157894736842
			},
			"clean_sheet": 0.07692307692307693
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.058823529411764705,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"jarrad branthwaite": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"luis florentino": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"michael keane": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"joe worrall": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"axel tuanzebe": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"hjalmar ekdal": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"reece welch": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jake obrien": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"lucas pires": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"idrissa gueye": {
			"goal": 0.11764705882352941,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ashley barnes": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"adam aznou": {
			"goal": 0.10526315789473684,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"vitaliy mykolenko": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"timothy iroegbunam": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"bashir humphreys": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"marcus edwards": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"beto": {
			"goal": 0.34782608695652173,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"armando broja": {
			"goal": 0.23076923076923078,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh laurent": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"elijah campbell": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lesley ugochukwu": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james tarkowski": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"seamus coleman": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nathan patterson": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lyle foster": {
			"goal": 0.23076923076923078,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"zian flemming": {
			"goal": 0.23076923076923078,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"brandon pouani": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"thierno barry": {
			"goal": 0.34782608695652173,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"tyler dibling": {
			"goal": 0.26666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"james garner": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"iliman-cheikh ndiaye": {
			"goal": 0.34782608695652173,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"merlin rohl": {
			"goal": 0.21052631578947367,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"kiernan dewsbury-hall": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dwight mcneil": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"carlos alcaraz": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jack grealish": {
			"goal": 0.23076923076923078,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"burnley": {
			"goals": {
				"0": 0.42105263157894735,
				"1": 0.40816326530612246,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.25
		},
		"everton": {
			"goals": {
				"0": 0.25,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.42105263157894735
		}
	}
},
{
	"player_stats": {
		"jean-clair todibo": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"konstantinos mavropanos": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"calvin bassey": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"max kilman": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"joachim andersen": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"jorge cuenca": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"soungoutou magassa": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"airidas golambeckis": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"guido rodriguez": {
			"goal": 0.10526315789473684,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"callum marshall": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"tomas soucek": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"freddie potts": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"aaron wan-bissaka": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"oliver scarles": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"timothy castagne": {
			"goal": 0.18181818181818182,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum wilson": {
			"goal": 0.3333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"luis guilherme lira": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kenny tete": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"mohamadou kante": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"el hadji diouf": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"harrison reed": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kyle walker-peters": {
			"goal": 0.05263157894736842,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"antonee robinson": {
			"goal": 0.08333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"raul jimenez": {
			"goal": 0.38095238095238093,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"emile smith rowe": {
			"goal": 0.26666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"andrew irving": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"george earthy": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"joshua king": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas paqueta": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"niclas fullkrug": {
			"goal": 0.29411764705882354,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ryan sessegnon": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"crysencio summerville": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"james ward-prowse": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.3333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"samuel chukwueze": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"kevin macedo": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"sasa lukic": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mateus fernandes": {
			"goal": 0.125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jarrod bowen": {
			"goal": 0.3333333333333333,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"harry wilson": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"alex iwobi": {
			"goal": 0.2222222222222222,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"de paulo igor": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		}
	},
	"game_stats": {
		"west ham": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.25
		},
		"fulham": {
			"goals": {
				"0": 0.25,
				"1": 0.37735849056603776,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.29411764705882354
		}
	}
},
{
	"player_stats": {
		"jan paul van hecke": {
			"goal": 0.038461538461538464,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"lewis dunk": {
			"goal": 0.05263157894736842,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"freddie simmonds": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"diego coppola": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"carlos baleba": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ferdi kadioglu": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"marli salmon": {
			"goal": 0.11764705882352941,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"olivier boscagli": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"joel veltman": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"charlie tasker": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"william saliba": {
			"goal": 0.11764705882352941,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"danny welbeck": {
			"goal": 0.2222222222222222,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"yasin ayari": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jack hinshelwood": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"james milner": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"christian norgaard": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"charalampos kostoulas": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"maxim de cuyper": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joe knight": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"tom watson": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"brajan gruda": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"diego gomez": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jurrien timber": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"mats wieffer": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"georginio rutter": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ben white": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"riccardo calafiori": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"viktor gyokeres": {
			"goal": 0.47619047619047616,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nehemiah oriola": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kaoru mitoma": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yankuba minteh": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"piero hincapie": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"myles lewis-skelly": {
			"goal": 0.11764705882352941,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"martin zubimendi": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ethan nwaneri": {
			"goal": 0.3076923076923077,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel martinelli": {
			"goal": 0.3225806451612903,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel jesus": {
			"goal": 0.43478260869565216,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikel merino": {
			"goal": 0.3225806451612903,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"eberechi eze": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"noni madueke": {
			"goal": 0.3225806451612903,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"leandro trossard": {
			"goal": 0.36363636363636365,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"declan rice": {
			"goal": 0.18181818181818182,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"martin odegaard": {
			"goal": 0.2222222222222222,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"bukayo saka": {
			"goal": 0.38095238095238093,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		}
	},
	"game_stats": {
		"arsenal": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.29411764705882354,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.47619047619047616
		},
		"brighton": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"aaron hickey": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ethan pinnock": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"veljko milosavljevic": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"marcos senesi": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"julio soler": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tyler adams": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sepp van den berg": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"adam smith": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"alejandro jimenez": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"malcom dacosta": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"julian araujo": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"evanilson": {
			"goal": 0.3125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"bafode diakite": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"kristoffer ajer": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"rico henry": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lewis cook": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"james hill": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.2222222222222222,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"alex scott": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"michael kayode": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"eli junior kroupi": {
			"goal": 0.34782608695652173,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"amine adli": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"gustavo nunes gomes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ryan christie": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"marcus tavernier": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"frank onyeka": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"enes unal": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"adrien truffert": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"justin kluivert": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin schade": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"antoine semenyo": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"david brooks": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dango ouattara": {
			"goal": 0.3125,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"mathias jensen": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"reiss nelson": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.43478260869565216,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.2,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.3076923076923077
		},
		"bournemouth": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.23076923076923078
		}
	}
},
{
	"player_stats": {
		"victor lindelof": {
			"goal": 0.043478260869565216,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"pau torres": {
			"goal": 0.06666666666666667,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"yeimar mosquera": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ezri konsa": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"wesley fofana": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tosin adarabioyo": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"benoit badiashile": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"trevoh chalobah": {
			"goal": 0.10526315789473684,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lamare bogarde": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"amadou onana": {
			"goal": 0.11764705882352941,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"george hemmings": {
			"goal": 0.15384615384615385,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"andres garcia": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"boubacar kamara": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"moises caicedo": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"travis patterson": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jamaldeen jimoh": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"matty cash": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"marc cucurella": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ben broggio": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"bradley burrowes": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"aidan borland": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andrey santos": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jorrel hato": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"josh acheampong": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"donyell malen": {
			"goal": 0.23076923076923078,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romeo lavia": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"john mcginn": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ian maatsen": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ollie watkins": {
			"goal": 0.34782608695652173,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"youri tielemans": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"evann guessand": {
			"goal": 0.26666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas digne": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"emiliano buendia": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"harvey elliott": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"malo gusto": {
			"goal": 0.08333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"marc guiu": {
			"goal": 0.38095238095238093,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jadon sancho": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.13333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jamie bynoe-gittens": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tyrique george": {
			"goal": 0.2777777777777778,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"alejandro garnacho": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"facundo buonanotte": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"morgan rogers": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"enzo fernandez": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"pedro neto": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"estevao": {
			"goal": 0.29411764705882354,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"cole palmer": {
			"goal": 0.4,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"de jesus joao pedro": {
			"goal": 0.38095238095238093,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"chelsea": {
			"goals": {
				"0": 0.2,
				"1": 0.34782608695652173,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.3448275862068966
		},
		"aston villa": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"joe rodon": {
			"goal": 0.09090909090909091,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"omar alderete": {
			"goal": 0.10526315789473684,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"luke onien": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"reinildo mandava": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"lutsharel geertruida": {
			"goal": 0.09090909090909091,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"dan neil": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"arthur masuaku": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"noah sadiki": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"james justin": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"daniel ballard": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ilia gruev": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"wilson isidor": {
			"goal": 0.3225806451612903,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"nordi mukiele": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"eliezer mayenda": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"brian brobbey": {
			"goal": 0.29411764705882354,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"trai hume": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lukas nmecha": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"chris rigg": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dominic calvert-lewin": {
			"goal": 0.3225806451612903,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"anton stach": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"degnand gnonto": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"chemsdine talbi": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.3225806451612903,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"harrison jones": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"enzo le fee": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bertrand traore": {
			"goal": 0.23076923076923078,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"granit xhaka": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"simon adingra": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"romain mundle": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		}
	},
	"game_stats": {
		"sunderland": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3333333333333333
		},
		"leeds": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.125
			},
			"clean_sheet": 0.3076923076923077
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"ben davies": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joao palhinha": {
			"goal": 0.11764705882352941,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"rio cardines": {
			"goal": 0.2777777777777778,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"marc guehi": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"maxence lacroix": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jaydee canvot": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"yves bissouma": {
			"goal": 0.11764705882352941,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"nathaniel clyne": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"archie gray": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"rodrigo bentancur": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"dominic solanke": {
			"goal": 0.3076923076923077,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"dane scarlett": {
			"goal": 0.26666666666666666,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kaden rodney": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"tyrick mitchell": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"will hughes": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"randal muani": {
			"goal": 0.2857142857142857,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chrisantus uche": {
			"goal": 0.26666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jean-philippe mateta": {
			"goal": 0.47619047619047616,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lucas bergvall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"wilson odobert": {
			"goal": 0.21052631578947367,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brennan johnson": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.16666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"eddie nketiah": {
			"goal": 0.34782608695652173,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"daichi kamada": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"adam wharton": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"richarlison": {
			"goal": 0.2857142857142857,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"romain esse": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"borna sosa": {
			"goal": 0.07692307692307693,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"justin devenny": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ismaila sarr": {
			"goal": 0.3225806451612903,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mohammed kudus": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"yeremy pino": {
			"goal": 0.23076923076923078,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"destiny udogie": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"pape matar sarr": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		}
	},
	"game_stats": {
		"crystal palace": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.3448275862068966
		},
		"tottenham": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.23076923076923078
		}
	}
},
]

DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"benoit badiashile": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"fabian schar": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"wesley fofana": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"alex murphy": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"dan burn": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jamaal lascelles": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"trevoh chalobah": {
			"goal": 0.08,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"moises caicedo": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sean neave": {
			"goal": 0.26666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"andrey santos": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"marc cucurella": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.034482758620689655,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh acheampong": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jorrel hato": {
			"goal": 0.043478260869565216,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jacob ramsey": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yoane wissa": {
			"goal": 0.3076923076923077,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"marc guiu": {
			"goal": 0.23076923076923078,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.07142857142857142,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"facundo buonanotte": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jamie bynoe-gittens": {
			"goal": 0.19230769230769232,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"nick woltemade": {
			"goal": 0.34782608695652173,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alejandro garnacho": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"tyrique george": {
			"goal": 0.21052631578947367,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.07692307692307693,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"sandro tonali": {
			"goal": 0.1,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"pedro neto": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony gordon": {
			"goal": 0.23809523809523808,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"enzo fernandez": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony elanga": {
			"goal": 0.19047619047619047,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"harvey barnes": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"estevao": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"cole palmer": {
			"goal": 0.29411764705882354,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"bruno guimaraes": {
			"goal": 0.125,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"de jesus joao pedro": {
			"goal": 0.23076923076923078,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"newcastle": {
			"goals": {
				"0": 0.2564102564102564,
				"1": 0.37037037037037035,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.23809523809523808
		},
		"chelsea": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.25
		}
	}
},
{
	"player_stats": {
		"yerson mosquera": {
			"goal": 0.07142857142857142,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"santiago bueno": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"aaron hickey": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ethan pinnock": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ladislav krejci": {
			"goal": 0.07142857142857142,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"toti gomes": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"benjamin arthur": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"joao gomes": {
			"goal": 0.09523809523809523,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"matt doherty": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"andre trindade": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"toluwalase arokodare": {
			"goal": 0.26666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"kristoffer ajer": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"david wolfe": {
			"goal": 0.05,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"hugo bueno": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"mateus mane": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.21052631578947367,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"romelle donovan": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jorgen larsen": {
			"goal": 0.30303030303030304,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"hee-chan hwang": {
			"goal": 0.2222222222222222,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jackson tchatchoua": {
			"goal": 0.05555555555555555,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.06666666666666667,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"gustavo nunes gomes": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"fernando lopez": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.14285714285714285,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jhon arias": {
			"goal": 0.21739130434782608,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin schade": {
			"goal": 0.2777777777777778,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.23255813953488372,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mathias jensen": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.4,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.16,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
	},
	"game_stats": {
		"wolverhampton": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.1111111111111111
			},
			"clean_sheet": 0.23809523809523808
		},
		"brentford": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.34782608695652173
		}
	}
},
{
	"player_stats": {
		"omar alderete": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"lutsharel geertruida": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"dan neil": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jan paul van hecke": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"freddie simmonds": {
			"goal": 0.10526315789473684,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"diego coppola": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"wilson isidor": {
			"goal": 0.25,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"nordi mukiele": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"eliezer mayenda": {
			"goal": 0.23809523809523808,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"daniel ballard": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"charlie tasker": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"olivier boscagli": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel veltman": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"ferdi kadioglu": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"trai hume": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"brian brobbey": {
			"goal": 0.21739130434782608,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"chris rigg": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"danny welbeck": {
			"goal": 0.4074074074074074,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"harrison jones": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jack hinshelwood": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yasin ayari": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"enzo le fee": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"granit xhaka": {
			"goal": 0.1,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"simon adingra": {
			"goal": 0.16,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"maxim de cuyper": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"charalampos kostoulas": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"james milner": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tom watson": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mats wieffer": {
			"goal": 0.1111111111111111,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"brajan gruda": {
			"goal": 0.23809523809523808,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"joe knight": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"kaoru mitoma": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"nehemiah oriola": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"georginio rutter": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"yankuba minteh": {
			"goal": 0.2777777777777778,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"romain mundle": {
			"goal": 0.16666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"brighton": {
			"goals": {
				"0": 0.16666666666666666,
				"1": 0.3225806451612903,
				"2": 0.3076923076923077,
				"3+": 0.3333333333333333
			},
			"clean_sheet": 0.40816326530612246
		},
		"sunderland": {
			"goals": {
				"0": 0.42105263157894735,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.09090909090909091
			},
			"clean_sheet": 0.16666666666666666
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.043478260869565216,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.05555555555555555,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"joe worrall": {
			"goal": 0.034482758620689655,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"axel tuanzebe": {
			"goal": 0.029411764705882353,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"veljko milosavljevic": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"ashley barnes": {
			"goal": 0.15384615384615385,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lucas pires": {
			"goal": 0.034482758620689655,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"marcos senesi": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"julio soler": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler adams": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"marcus edwards": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lesley ugochukwu": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh laurent": {
			"goal": 0.09523809523809523,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"adam smith": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"zian flemming": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lyle foster": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"alejandro jimenez": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"malcom dacosta": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"bafode diakite": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"evanilson": {
			"goal": 0.36363636363636365,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"julian araujo": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"james hill": {
			"goal": 0.1,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"alex scott": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"lewis cook": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"eli junior kroupi": {
			"goal": 0.37037037037037035,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan christie": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"amine adli": {
			"goal": 0.23809523809523808,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adrien truffert": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"enes unal": {
			"goal": 0.42105263157894735,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"marcus tavernier": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"justin kluivert": {
			"goal": 0.2857142857142857,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"david brooks": {
			"goal": 0.2777777777777778,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"antoine semenyo": {
			"goal": 0.4074074074074074,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"bournemouth": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.2857142857142857,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"burnley": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"konstantinos mavropanos": {
			"goal": 0.047619047619047616,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"jean-clair todibo": {
			"goal": 0.029411764705882353,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"max kilman": {
			"goal": 0.029411764705882353,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"soungoutou magassa": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ruben dias": {
			"goal": 0.08695652173913043,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"airidas golambeckis": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"guido rodriguez": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"oliver scarles": {
			"goal": 0.043478260869565216,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tomas soucek": {
			"goal": 0.125,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan ake": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"freddie potts": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum marshall": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum wilson": {
			"goal": 0.2222222222222222,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luis guilherme lira": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"kyle walker-peters": {
			"goal": 0.029411764705882353,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"mohamadou kante": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"andrew irving": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lucas paqueta": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james ward-prowse": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"niclas fullkrug": {
			"goal": 0.19047619047619047,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"george earthy": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"crysencio summerville": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"john stones": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"abduqodir khusanov": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mateus fernandes": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jarrod bowen": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"nico oreilly": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"rico lewis": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"nico gonzalez": {
			"goal": 0.11764705882352941,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"erling haaland": {
			"goal": 0.7333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"kalvin phillips": {
			"goal": 0.16666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"tijjani reijnders": {
			"goal": 0.2777777777777778,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"oscar bobb": {
			"goal": 0.3125,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bernardo silva": {
			"goal": 0.2,
			"assist": 0.20833333333333334,
			"no_assist": 0.875
		},
		"divine mukasa": {
			"goal": 0.29411764705882354,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"phil foden": {
			"goal": 0.43478260869565216,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
		"jeremy doku": {
			"goal": 0.2777777777777778,
			"assist": 0.3076923076923077,
			"no_assist": 0.8333333333333334
		},
		"rayan cherki": {
			"goal": 0.30303030303030304,
			"assist": 0.3076923076923077,
			"no_assist": 0.8333333333333334
		},
		"de paulo igor": {
			"goal": 0.029411764705882353,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"matheus nunes": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"de oliveira savio": {
			"goal": 0.3125,
			"assist": 0.29411764705882354,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man city": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.18181818181818182,
				"2": 0.26666666666666666,
				"3+": 0.6
			},
			"clean_sheet": 0.45454545454545453
		},
		"west ham": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.06666666666666667
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ben davies": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"joao palhinha": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.0625,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ibrahima konate": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"callum olusesi": {
			"goal": 0.13333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"joe gomez": {
			"goal": 0.058823529411764705,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luca williams-barnet": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"wellity lucky": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"archie gray": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.08695652173913043,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"virgil van dijk": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"djed spence": {
			"goal": 0.047619047619047616,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"trey nyoni": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"dane scarlett": {
			"goal": 0.26666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"curtis jones": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"milos kerkez": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"randal muani": {
			"goal": 0.2857142857142857,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"lucas bergvall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"alexis mac allister": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ryan gravenberch": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"calvin ramsay": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"andrew robertson": {
			"goal": 0.05555555555555555,
			"assist": 0.1,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"pedro porro": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"conor bradley": {
			"goal": 0.08333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"rio ngumoha": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"richarlison": {
			"goal": 0.30303030303030304,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"federico chiesa": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"alexander isak": {
			"goal": 0.39215686274509803,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jeremie frimpong": {
			"goal": 0.125,
			"assist": 0.16,
			"no_assist": 0.9333333333333333
		},
		"jayden danns": {
			"goal": 0.3333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.21052631578947367,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"hugo ekitike": {
			"goal": 0.35714285714285715,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"florian wirtz": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"dominik szoboszlai": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"mohammed kudus": {
			"goal": 0.23809523809523808,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		}
	},
	"game_stats": {
		"tottenham": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2631578947368421,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.2
		},
		"liverpool": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.30303030303030304,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"michael keane": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"william saliba": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"reece welch": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"marli salmon": {
			"goal": 0.1,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"adam aznou": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"timothy iroegbunam": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"jake obrien": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"vitaliy mykolenko": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"james tarkowski": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"elijah campbell": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"beto": {
			"goal": 0.2,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"nathan patterson": {
			"goal": 0.038461538461538464,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"thierno barry": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler dibling": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jurrien timber": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james garner": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"kiernan dewsbury-hall": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"riccardo calafiori": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"viktor gyokeres": {
			"goal": 0.4,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"dwight mcneil": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"piero hincapie": {
			"goal": 0.08333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"carlos alcaraz": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.09523809523809523,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"martin zubimendi": {
			"goal": 0.09523809523809523,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"jack grealish": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"josh nichols": {
			"goal": 0.11764705882352941,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ethan nwaneri": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"gabriel martinelli": {
			"goal": 0.25,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"gabriel jesus": {
			"goal": 0.36363636363636365,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"louie copley": {
			"goal": 0.15384615384615385,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikel merino": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"leandro trossard": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"declan rice": {
			"goal": 0.14814814814814814,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"eberechi eze": {
			"goal": 0.26666666666666666,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"noni madueke": {
			"goal": 0.25,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"martin odegaard": {
			"goal": 0.17391304347826086,
			"assist": 0.20833333333333334,
			"no_assist": 0.9
		},
		"bukayo saka": {
			"goal": 0.3225806451612903,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
	},
	"game_stats": {
		"everton": {
			"goals": {
				"0": 0.46511627906976744,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.2
		},
		"arsenal": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.46511627906976744
		}
	}
},
{
	"player_stats": {
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joe rodon": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"marc guehi": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ethan ampadu": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"nathaniel clyne": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"james justin": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.29411764705882354,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jean-philippe mateta": {
			"goal": 0.4,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jefferson lerma": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"tyrick mitchell": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"lukas nmecha": {
			"goal": 0.2777777777777778,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ilia gruev": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"chrisantus uche": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.29411764705882354,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.10526315789473684,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"eddie nketiah": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ben casey": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"borna sosa": {
			"goal": 0.07692307692307693,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"anton stach": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"justin devenny": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"adam wharton": {
			"goal": 0.08,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daichi kamada": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"daniel munoz": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joel drakes-thomas": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"degnand gnonto": {
			"goal": 0.21739130434782608,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
	},
	"game_stats": {
		"leeds": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.3076923076923077
		},
		"crystal palace": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3076923076923077
		}
	}
},
{
	"player_stats": {
		"lisandro martinez": {
			"goal": 0.058823529411764705,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"tyler fredricson": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"leny yoro": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"pau torres": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ayden heaven": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"yeimar mosquera": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"tyrell malacia": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"diego leon": {
			"goal": 0.1111111111111111,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jack fletcher": {
			"goal": 0.125,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"matthijs de ligt": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"luke shaw": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"manuel ugarte": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kobbie mainoo": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"amadou onana": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"george hemmings": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lamare bogarde": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"boubacar kamara": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"casemiro": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joshua zirkzee": {
			"goal": 0.25,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"diogo dalot": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"travis patterson": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.09523809523809523,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"benjamin sesko": {
			"goal": 0.3125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"patrick dorgu": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mason mount": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andres garcia": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jamaldeen jimoh": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"shea lacey": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"john mcginn": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"aidan borland": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"donyell malen": {
			"goal": 0.3333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ben broggio": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ian maatsen": {
			"goal": 0.10526315789473684,
			"assist": 0.11764705882352941,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"lucas digne": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"evann guessand": {
			"goal": 0.3333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"ollie watkins": {
			"goal": 0.42105263157894735,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bruno fernandes": {
			"goal": 0.26666666666666666,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"jadon sancho": {
			"goal": 0.21739130434782608,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.2,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"emiliano buendia": {
			"goal": 0.24390243902439024,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.25,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"matheus cunha": {
			"goal": 0.29411764705882354,
			"assist": 0.21739130434782608,
			"no_assist": 0.9
		},
	},
	"game_stats": {
		"aston villa": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.29411764705882354
		},
		"man utd": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.38461538461538464,
				"2": 0.2631578947368421,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"issa diop": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jorge cuenca": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jack thompson": {
			"goal": 0.15384615384615385,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"felipe morato": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"joachim andersen": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"timothy castagne": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kenny tete": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ryan yates": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"oleksandr zinchenko": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"neco williams": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"nicolas dominguez": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"chris wood": {
			"goal": 0.3076923076923077,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.1724137931034483,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.34782608695652173,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"emile smith rowe": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"antonee robinson": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.08695652173913043,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ryan sessegnon": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jonah kusi-asare": {
			"goal": 0.29411764705882354,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.125,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"igor jesus": {
			"goal": 0.3125,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.19047619047619047,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"tom cairney": {
			"goal": 0.08333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"jimmy sinclair": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"dan ndoye": {
			"goal": 0.14814814814814814,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"joshua king": {
			"goal": 0.21739130434782608,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"omari giraud-hutchinson": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"sasa lukic": {
			"goal": 0.10526315789473684,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"morgan gibbs-white": {
			"goal": 0.19047619047619047,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"harry wilson": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"elliot anderson": {
			"goal": 0.10526315789473684,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dilane bakwa": {
			"goal": 0.19047619047619047,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"fulham": {
			"goals": {
				"0": 0.2631578947368421,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.3333333333333333
		},
		"nottingham forest": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.2631578947368421
		}
	}
},
]

DATA = [
{
	"player_stats": {
		"lisandro martinez": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"malick thiaw": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"tyler fredricson": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"fabian schar": {
			"goal": 0.10526315789473684,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.10526315789473684,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"leny yoro": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"alex murphy": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jamaal lascelles": {
			"goal": 0.058823529411764705,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"dan burn": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"ayden heaven": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"diego leon": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"tyrell malacia": {
			"goal": 0.10526315789473684,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"matthijs de ligt": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jack fletcher": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.25,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"luke shaw": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.3225806451612903,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kobbie mainoo": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"manuel ugarte": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"joe willock": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"casemiro": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joshua zirkzee": {
			"goal": 0.30303030303030304,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"yoane wissa": {
			"goal": 0.3225806451612903,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jacob ramsey": {
			"goal": 0.16,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"diogo dalot": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lewis hall": {
			"goal": 0.08,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.10526315789473684,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"mason mount": {
			"goal": 0.2222222222222222,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"shea lacey": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"joelinton": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.38095238095238093,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"benjamin sesko": {
			"goal": 0.37735849056603776,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"seung-soo park": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"patrick dorgu": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jacob murphy": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"anthony gordon": {
			"goal": 0.2857142857142857,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"harvey barnes": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bruno fernandes": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"matheus cunha": {
			"goal": 0.36363636363636365,
			"assist": 0.25,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"man utd": {
			"goals": {
				"0": 0.2,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.2777777777777778
		},
		"newcastle": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"ruben dias": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nathan ake": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jack thompson": {
			"goal": 0.16666666666666666,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"felipe morato": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"john stones": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"neco williams": {
			"goal": 0.08,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"ryan yates": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"abduqodir khusanov": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"nicolas dominguez": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"oleksandr zinchenko": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"chris wood": {
			"goal": 0.2857142857142857,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"james mcatee": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.29411764705882354,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"archie whitehall": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"igor jesus": {
			"goal": 0.2857142857142857,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nico oreilly": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"douglas luiz": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"omari giraud-hutchinson": {
			"goal": 0.11764705882352941,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"nico gonzalez": {
			"goal": 0.09523809523809523,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jimmy sinclair": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"rico lewis": {
			"goal": 0.08333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"dan ndoye": {
			"goal": 0.14814814814814814,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"erling haaland": {
			"goal": 0.5789473684210527,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"morgan gibbs-white": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"elliot anderson": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kalvin phillips": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"dilane bakwa": {
			"goal": 0.21052631578947367,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tijjani reijnders": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"oscar bobb": {
			"goal": 0.2631578947368421,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bernardo silva": {
			"goal": 0.14814814814814814,
			"assist": 0.16,
			"no_assist": 0.9230769230769231
		},
		"divine mukasa": {
			"goal": 0.21052631578947367,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"phil foden": {
			"goal": 0.3448275862068966,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"jeremy doku": {
			"goal": 0.21739130434782608,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"rayan cherki": {
			"goal": 0.23809523809523808,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"matheus nunes": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"de oliveira savio": {
			"goal": 0.23255813953488372,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		}
	},
	"game_stats": {
		"nottingham forest": {
			"goals": {
				"0": 0.37735849056603776,
				"1": 0.4,
				"2": 0.2222222222222222,
				"3+": 0.1
			},
			"clean_sheet": 0.15384615384615385
		},
		"man city": {
			"goals": {
				"0": 0.15384615384615385,
				"1": 0.30303030303030304,
				"2": 0.3076923076923077,
				"3+": 0.36363636363636365
			},
			"clean_sheet": 0.37735849056603776
		}
	}
},
{
	"player_stats": {
		"lewis dunk": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"jan paul van hecke": {
			"goal": 0.038461538461538464,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"freddie simmonds": {
			"goal": 0.058823529411764705,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"diego coppola": {
			"goal": 0.05555555555555555,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ferdi kadioglu": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"william saliba": {
			"goal": 0.11764705882352941,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"olivier boscagli": {
			"goal": 0.05555555555555555,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"marli salmon": {
			"goal": 0.125,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"charlie tasker": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"joel veltman": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jack hinshelwood": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"yasin ayari": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"danny welbeck": {
			"goal": 0.25,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"charalampos kostoulas": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james milner": {
			"goal": 0.0625,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"maxim de cuyper": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"christian norgaard": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"tom watson": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"brajan gruda": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jurrien timber": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"diego gomez": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"joe knight": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"viktor gyokeres": {
			"goal": 0.47619047619047616,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"nehemiah oriola": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"ben white": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kaoru mitoma": {
			"goal": 0.14814814814814814,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mats wieffer": {
			"goal": 0.0625,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"georginio rutter": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"yankuba minteh": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"piero hincapie": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"riccardo calafiori": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"martin zubimendi": {
			"goal": 0.10526315789473684,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"myles lewis-skelly": {
			"goal": 0.1111111111111111,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"josh nichols": {
			"goal": 0.15384615384615385,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel martinelli": {
			"goal": 0.29411764705882354,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel jesus": {
			"goal": 0.4444444444444444,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"ethan nwaneri": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"louie copley": {
			"goal": 0.21052631578947367,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"mikel merino": {
			"goal": 0.3125,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"leandro trossard": {
			"goal": 0.3125,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"eberechi eze": {
			"goal": 0.30303030303030304,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"declan rice": {
			"goal": 0.17391304347826086,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"noni madueke": {
			"goal": 0.2857142857142857,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"martin odegaard": {
			"goal": 0.20833333333333334,
			"assist": 0.23255813953488372,
			"no_assist": 0.875
		},
		"bukayo saka": {
			"goal": 0.38461538461538464,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		}
	},
	"game_stats": {
		"arsenal": {
			"goals": {
				"0": 0.125,
				"1": 0.2857142857142857,
				"2": 0.3076923076923077,
				"3+": 0.4
			},
			"clean_sheet": 0.4444444444444444
		},
		"brighton": {
			"goals": {
				"0": 0.4444444444444444,
				"1": 0.40816326530612246,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.125
		}
	}
},
{
	"player_stats": {
		"yerson mosquera": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"santiago bueno": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"joao gomes": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.05555555555555555,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ladislav krejci": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"toti gomes": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"matt doherty": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"toluwalase arokodare": {
			"goal": 0.2,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"andre trindade": {
			"goal": 0.05,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"david wolfe": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"ibrahima konate": {
			"goal": 0.13333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jackson tchatchoua": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"hugo bueno": {
			"goal": 0.043478260869565216,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mateus mane": {
			"goal": 0.15384615384615385,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jorgen larsen": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"hee-chan hwang": {
			"goal": 0.16,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joe gomez": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"fernando lopez": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jhon arias": {
			"goal": 0.16,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"wellity lucky": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"trey nyoni": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"virgil van dijk": {
			"goal": 0.16666666666666666,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"milos kerkez": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"curtis jones": {
			"goal": 0.14814814814814814,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan gravenberch": {
			"goal": 0.14285714285714285,
			"assist": 0.17391304347826086,
			"no_assist": 0.9230769230769231
		},
		"alexis mac allister": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"andrew robertson": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9090909090909091
		},
		"conor bradley": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9090909090909091
		},
		"calvin ramsay": {
			"goal": 0.18181818181818182,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"rio ngumoha": {
			"goal": 0.30303030303030304,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"jeremie frimpong": {
			"goal": 0.18181818181818182,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"alexander isak": {
			"goal": 0.5238095238095238,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"federico chiesa": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"jayden danns": {
			"goal": 0.45454545454545453,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"hugo ekitike": {
			"goal": 0.5454545454545454,
			"assist": 0.2857142857142857,
			"no_assist": 0.875
		},
		"florian wirtz": {
			"goal": 0.3125,
			"assist": 0.29411764705882354,
			"no_assist": 0.8461538461538461
		},
		"dominik szoboszlai": {
			"goal": 0.3225806451612903,
			"assist": 0.29411764705882354,
			"no_assist": 0.8461538461538461
		},
		"mohamed salah": {
			"goal": 0.5555555555555556,
			"assist": 0.36363636363636365,
			"no_assist": 0.8181818181818182
		},
	},
	"game_stats": {
		"liverpool": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.21052631578947367,
				"2": 0.2857142857142857,
				"3+": 0.5454545454545454
			},
			"clean_sheet": 0.5238095238095238
		},
		"wolverhampton": {
			"goals": {
				"0": 0.5238095238095238,
				"1": 0.39215686274509803,
				"2": 0.15384615384615385,
				"3+": 0.05263157894736842
			},
			"clean_sheet": 0.07692307692307693
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.058823529411764705,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"jarrad branthwaite": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"michael keane": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"luis florentino": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"joe worrall": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"axel tuanzebe": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"hjalmar ekdal": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"reece welch": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"lucas pires": {
			"goal": 0.05555555555555555,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ashley barnes": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"jake obrien": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"adam aznou": {
			"goal": 0.10526315789473684,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"timothy iroegbunam": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"vitaliy mykolenko": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"josh cullen": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"mike tresor": {
			"goal": 0.21052631578947367,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"loum tchaouna": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"elijah campbell": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lesley ugochukwu": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"beto": {
			"goal": 0.3225806451612903,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh laurent": {
			"goal": 0.08695652173913043,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"armando broja": {
			"goal": 0.20833333333333334,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james tarkowski": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nathan patterson": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lyle foster": {
			"goal": 0.23076923076923078,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"zian flemming": {
			"goal": 0.23076923076923078,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jacob bruun larsen": {
			"goal": 0.16,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"thierno barry": {
			"goal": 0.30303030303030304,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james garner": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"tyler dibling": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"merlin rohl": {
			"goal": 0.21052631578947367,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"carlos alcaraz": {
			"goal": 0.20833333333333334,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"dwight mcneil": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"kiernan dewsbury-hall": {
			"goal": 0.18518518518518517,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jack grealish": {
			"goal": 0.23076923076923078,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"burnley": {
			"goals": {
				"0": 0.4,
				"1": 0.40816326530612246,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.23809523809523808
		},
		"everton": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.4
		}
	}
},
{
	"player_stats": {
		"veljko milosavljevic": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ethan pinnock": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"aaron hickey": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"julio soler": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tyler adams": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"marcos senesi": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"adam smith": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.09523809523809523,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.09523809523809523,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"malcom dacosta": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"alejandro jimenez": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"evanilson": {
			"goal": 0.2564102564102564,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"kristoffer ajer": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"julian araujo": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"bafode diakite": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"myles peart-harris": {
			"goal": 0.2222222222222222,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james hill": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yegor yarmolyuk": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.08333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"eli junior kroupi": {
			"goal": 0.2777777777777778,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"alex scott": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"lewis cook": {
			"goal": 0.08,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"amine adli": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"gustavo nunes gomes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"enes unal": {
			"goal": 0.29411764705882354,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ryan christie": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"adrien truffert": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"marcus tavernier": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"justin kluivert": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"david brooks": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"antoine semenyo": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"kevin schade": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.43478260869565216,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"mathias jensen": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.15384615384615385,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"brentford": {
			"goals": {
				"0": 0.25,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.29411764705882354
		},
		"bournemouth": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.4,
				"2": 0.2564102564102564,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.23809523809523808
		}
	}
},
{
	"player_stats": {
		"jean-clair todibo": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"konstantinos mavropanos": {
			"goal": 0.08,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"max kilman": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jorge cuenca": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"joachim andersen": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"ezra mayers": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"soungoutou magassa": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"airidas golambeckis": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"timothy castagne": {
			"goal": 0.08333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"guido rodriguez": {
			"goal": 0.08,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kenny tete": {
			"goal": 0.08695652173913043,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"oliver scarles": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"freddie potts": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"callum marshall": {
			"goal": 0.2857142857142857,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum wilson": {
			"goal": 0.34782608695652173,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tomas soucek": {
			"goal": 0.18181818181818182,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"mohamadou kante": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kyle walker-peters": {
			"goal": 0.05263157894736842,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.34782608695652173,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"luis guilherme lira": {
			"goal": 0.14814814814814814,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"emile smith rowe": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"antonee robinson": {
			"goal": 0.08333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"andrew irving": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas paqueta": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"ryan sessegnon": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jonah kusi-asare": {
			"goal": 0.3333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"crysencio summerville": {
			"goal": 0.17391304347826086,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.08,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"joshua king": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"george earthy": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.19047619047619047,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"niclas fullkrug": {
			"goal": 0.3125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"harry wilson": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.16666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"james ward-prowse": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"sasa lukic": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mateus fernandes": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"jarrod bowen": {
			"goal": 0.3448275862068966,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"de paulo igor": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		}
	},
	"game_stats": {
		"west ham": {
			"goals": {
				"0": 0.2857142857142857,
				"1": 0.38461538461538464,
				"2": 0.2631578947368421,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.25
		},
		"fulham": {
			"goals": {
				"0": 0.25,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.2777777777777778
		}
	}
},
{
	"player_stats": {
		"victor lindelof": {
			"goal": 0.043478260869565216,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"pau torres": {
			"goal": 0.06666666666666667,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"ezri konsa": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"yeimar mosquera": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"wesley fofana": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tosin adarabioyo": {
			"goal": 0.09523809523809523,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"benoit badiashile": {
			"goal": 0.1,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"amadou onana": {
			"goal": 0.09523809523809523,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"george hemmings": {
			"goal": 0.14285714285714285,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lamare bogarde": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"trevoh chalobah": {
			"goal": 0.1,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"andres garcia": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"boubacar kamara": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"travis patterson": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"moises caicedo": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"matty cash": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jamaldeen jimoh": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"donyell malen": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jorrel hato": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9615384615384616
		},
		"aidan borland": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"josh acheampong": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"bradley burrowes": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andrey santos": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"marc cucurella": {
			"goal": 0.09523809523809523,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ben broggio": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"john mcginn": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ollie watkins": {
			"goal": 0.3225806451612903,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"evann guessand": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"youri tielemans": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ian maatsen": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas digne": {
			"goal": 0.0625,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.09090909090909091,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"harvey elliott": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jadon sancho": {
			"goal": 0.11764705882352941,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"emiliano buendia": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"marc guiu": {
			"goal": 0.2702702702702703,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"morgan rogers": {
			"goal": 0.17391304347826086,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reece james": {
			"goal": 0.1,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"facundo buonanotte": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"tyrique george": {
			"goal": 0.2857142857142857,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jamie bynoe-gittens": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enzo fernandez": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"alejandro garnacho": {
			"goal": 0.2631578947368421,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"pedro neto": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"estevao": {
			"goal": 0.30303030303030304,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"cole palmer": {
			"goal": 0.37735849056603776,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"de jesus joao pedro": {
			"goal": 0.37735849056603776,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"chelsea": {
			"goals": {
				"0": 0.19047619047619047,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.3448275862068966
		},
		"aston villa": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.18181818181818182
		}
	}
},
{
	"player_stats": {
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joe rodon": {
			"goal": 0.08,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"omar alderete": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"luke onien": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"lutsharel geertruida": {
			"goal": 0.08,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan neil": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nordi mukiele": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"james justin": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"daniel ballard": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.29411764705882354,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"wilson isidor": {
			"goal": 0.3225806451612903,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ilia gruev": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"eliezer mayenda": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lukas nmecha": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"brian brobbey": {
			"goal": 0.2564102564102564,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"trai hume": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ao tanaka": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chris rigg": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dominic calvert-lewin": {
			"goal": 0.3333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jack harrison": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"anton stach": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"harrison jones": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"enzo le fee": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"degnand gnonto": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"simon adingra": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"granit xhaka": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"romain mundle": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		}
	},
	"game_stats": {
		"sunderland": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3225806451612903
		},
		"leeds": {
			"goals": {
				"0": 0.3225806451612903,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.3076923076923077
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"ben davies": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joao palhinha": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"maxence lacroix": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"callum olusesi": {
			"goal": 0.14285714285714285,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"marc guehi": {
			"goal": 0.08695652173913043,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jaydee canvot": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"chris richards": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"luca williams-barnet": {
			"goal": 0.18181818181818182,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"nathaniel clyne": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"djed spence": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"archie gray": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"rodrigo bentancur": {
			"goal": 0.08,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jean-philippe mateta": {
			"goal": 0.45454545454545453,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"will hughes": {
			"goal": 0.08333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"tyrick mitchell": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jefferson lerma": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"lucas bergvall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.26666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"randal muani": {
			"goal": 0.2564102564102564,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chrisantus uche": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kaden rodney": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"wilson odobert": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"mathys tel": {
			"goal": 0.21739130434782608,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"eddie nketiah": {
			"goal": 0.2777777777777778,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"romain esse": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"daniel munoz": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"adam wharton": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"richarlison": {
			"goal": 0.2857142857142857,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"brennan johnson": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ben casey": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"daichi kamada": {
			"goal": 0.21052631578947367,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"xavi simons": {
			"goal": 0.19047619047619047,
			"assist": 0.16,
			"no_assist": 0.9333333333333333
		},
		"borna sosa": {
			"goal": 0.07692307692307693,
			"assist": 0.14814814814814814,
			"no_assist": 0.9333333333333333
		},
		"justin devenny": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mohammed kudus": {
			"goal": 0.21739130434782608,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"joel drakes-thomas": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"yeremy pino": {
			"goal": 0.2222222222222222,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		}
	},
	"game_stats": {
		"crystal palace": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.3333333333333333
		},
		"tottenham": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.125
			},
			"clean_sheet": 0.23076923076923078
		}
	}
},
]

DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"fabian schar": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"alex murphy": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"benoit badiashile": {
			"goal": 0.034482758620689655,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"tosin adarabioyo": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"wesley fofana": {
			"goal": 0.034482758620689655,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"jamaal lascelles": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"trevoh chalobah": {
			"goal": 0.08,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"moises caicedo": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sean neave": {
			"goal": 0.26666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"andrey santos": {
			"goal": 0.125,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"marc cucurella": {
			"goal": 0.06666666666666667,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.3225806451612903,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh acheampong": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.034482758620689655,
			"assist": 0.06666666666666667,
			"no_assist": 0.9705882352941176
		},
		"yoane wissa": {
			"goal": 0.3076923076923077,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jorrel hato": {
			"goal": 0.043478260869565216,
			"assist": 0.08333333333333333,
			"no_assist": 0.9615384615384616
		},
		"jacob ramsey": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joelinton": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"malo gusto": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.3448275862068966,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"marc guiu": {
			"goal": 0.23809523809523808,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"facundo buonanotte": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"jamie bynoe-gittens": {
			"goal": 0.20833333333333334,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"reece james": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"tyrique george": {
			"goal": 0.21739130434782608,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"alejandro garnacho": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"pedro neto": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.21052631578947367,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"anthony gordon": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"enzo fernandez": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9333333333333333
		},
		"harvey barnes": {
			"goal": 0.2631578947368421,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.18181818181818182,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"estevao": {
			"goal": 0.2222222222222222,
			"assist": 0.13333333333333333,
			"no_assist": 0.9230769230769231
		},
		"cole palmer": {
			"goal": 0.3125,
			"assist": 0.18181818181818182,
			"no_assist": 0.9
		},
		"bruno guimaraes": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"de jesus joao pedro": {
			"goal": 0.23809523809523808,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
	},
	"game_stats": {
		"newcastle": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2777777777777778,
				"3+": 0.2
			},
			"clean_sheet": 0.23809523809523808
		},
		"chelsea": {
			"goals": {
				"0": 0.23809523809523808,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.25
		}
	}
},
{
	"player_stats": {
		"santiago bueno": {
			"goal": 0.024390243902439025,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"ethan pinnock": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"aaron hickey": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"nathan collins": {
			"goal": 0.07692307692307693,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"joao gomes": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"ki-jana hoever": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"ladislav krejci": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9850746268656716
		},
		"toti gomes": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9850746268656716
		},
		"matt doherty": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"kristoffer ajer": {
			"goal": 0.06666666666666667,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"toluwalase arokodare": {
			"goal": 0.23809523809523808,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"rico henry": {
			"goal": 0.058823529411764705,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"andre trindade": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"myles peart-harris": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jackson tchatchoua": {
			"goal": 0.038461538461538464,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"hee-chan hwang": {
			"goal": 0.21052631578947367,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"hugo bueno": {
			"goal": 0.047619047619047616,
			"assist": 0.08333333333333333,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.047619047619047616,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jorgen larsen": {
			"goal": 0.29411764705882354,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"david wolfe": {
			"goal": 0.038461538461538464,
			"assist": 0.08333333333333333,
			"no_assist": 0.9615384615384616
		},
		"mateus mane": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"yegor yarmolyuk": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"fernando lopez": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"kevin schade": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.21052631578947367,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"jhon arias": {
			"goal": 0.19047619047619047,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"mathias jensen": {
			"goal": 0.09090909090909091,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.43478260869565216,
			"assist": 0.11764705882352941,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.11764705882352941,
			"assist": 0.19047619047619047,
			"no_assist": 0.8888888888888888
		},
	},
	"game_stats": {
		"wolverhampton": {
			"goals": {
				"0": 0.34782608695652173,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.1111111111111111
			},
			"clean_sheet": 0.23809523809523808
		},
		"brentford": {
			"goals": {
				"0": 0.25,
				"1": 0.36363636363636365,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.34782608695652173
		}
	}
},
{
	"player_stats": {
		"omar alderete": {
			"goal": 0.058823529411764705,
			"assist": 0.027777777777777776,
			"no_assist": 0.9960159362549801
		},
		"lutsharel geertruida": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jan paul van hecke": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"dan neil": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"freddie simmonds": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"diego coppola": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"nordi mukiele": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9850746268656716
		},
		"wilson isidor": {
			"goal": 0.26666666666666666,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"daniel ballard": {
			"goal": 0.08333333333333333,
			"assist": 0.029411764705882353,
			"no_assist": 0.9850746268656716
		},
		"eliezer mayenda": {
			"goal": 0.23076923076923078,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ferdi kadioglu": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"olivier boscagli": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9803921568627451
		},
		"brian brobbey": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"trai hume": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel veltman": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"yasin ayari": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"jack hinshelwood": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"danny welbeck": {
			"goal": 0.4166666666666667,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"chris rigg": {
			"goal": 0.11764705882352941,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"harrison jones": {
			"goal": 0.125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"enzo le fee": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"simon adingra": {
			"goal": 0.14285714285714285,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"granit xhaka": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9523809523809523
		},
		"james milner": {
			"goal": 0.1111111111111111,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"charalampos kostoulas": {
			"goal": 0.30303030303030304,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"maxim de cuyper": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"tom watson": {
			"goal": 0.21052631578947367,
			"assist": 0.1724137931034483,
			"no_assist": 0.9230769230769231
		},
		"brajan gruda": {
			"goal": 0.22727272727272727,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"joe knight": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9090909090909091
		},
		"mats wieffer": {
			"goal": 0.08333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9090909090909091
		},
		"kaoru mitoma": {
			"goal": 0.2631578947368421,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"georginio rutter": {
			"goal": 0.2857142857142857,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"nehemiah oriola": {
			"goal": 0.2222222222222222,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"yankuba minteh": {
			"goal": 0.2564102564102564,
			"assist": 0.2222222222222222,
			"no_assist": 0.875
		},
		"romain mundle": {
			"goal": 0.14285714285714285,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		}
	},
	"game_stats": {
		"brighton": {
			"goals": {
				"0": 0.18181818181818182,
				"1": 0.3225806451612903,
				"2": 0.3076923076923077,
				"3+": 0.29411764705882354
			}
		},
		"sunderland": {
			"goals": {
				"0": 0.42105263157894735,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.09090909090909091
			}
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.029411764705882353,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"oliver sonne": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"joe worrall": {
			"goal": 0.029411764705882353,
			"assist": 0.029411764705882353,
			"no_assist": 0.9933774834437086
		},
		"hjalmar ekdal": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9933774834437086
		},
		"kyle walker": {
			"goal": 0.024390243902439025,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"veljko milosavljevic": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"lucas pires": {
			"goal": 0.024390243902439025,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"ashley barnes": {
			"goal": 0.1724137931034483,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"loum tchaouna": {
			"goal": 0.11764705882352941,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mike tresor": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"marcos senesi": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"julio soler": {
			"goal": 0.058823529411764705,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"tyler adams": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"lesley ugochukwu": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"armando broja": {
			"goal": 0.2,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.125,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"josh cullen": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"josh laurent": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.975609756097561
		},
		"adam smith": {
			"goal": 0.043478260869565216,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"zian flemming": {
			"goal": 0.2222222222222222,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"quilindschy hartman": {
			"goal": 0.038461538461538464,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"alejandro jimenez": {
			"goal": 0.10526315789473684,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"malcom dacosta": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"julian araujo": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"evanilson": {
			"goal": 0.35714285714285715,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"james hill": {
			"goal": 0.07692307692307693,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"bafode diakite": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9523809523809523
		},
		"lewis cook": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"alex scott": {
			"goal": 0.11764705882352941,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"eli junior kroupi": {
			"goal": 0.37735849056603776,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"ryan christie": {
			"goal": 0.16666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"adrien truffert": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9230769230769231
		},
		"amine adli": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enes unal": {
			"goal": 0.38095238095238093,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"marcus tavernier": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9090909090909091
		},
		"justin kluivert": {
			"goal": 0.2777777777777778,
			"assist": 0.18181818181818182,
			"no_assist": 0.9
		},
		"antoine semenyo": {
			"goal": 0.4074074074074074,
			"assist": 0.21739130434782608,
			"no_assist": 0.8888888888888888
		},
		"david brooks": {
			"goal": 0.25,
			"assist": 0.22727272727272727,
			"no_assist": 0.8888888888888888
		},
	},
	"game_stats": {
		"bournemouth": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.2857142857142857,
				"2": 0.30303030303030304,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"burnley": {
			"goals": {
				"0": 0.43478260869565216,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"jean-clair todibo": {
			"goal": 0.024390243902439025,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"konstantinos mavropanos": {
			"goal": 0.034482758620689655,
			"assist": 0.0196078431372549,
			"no_assist": 0.998003992015968
		},
		"max kilman": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"airidas golambeckis": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"soungoutou magassa": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ezra mayers": {
			"goal": 0.021739130434782608,
			"assist": 0.027777777777777776,
			"no_assist": 0.9933774834437086
		},
		"ruben dias": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"guido rodriguez": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"freddie potts": {
			"goal": 0.038461538461538464,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"tomas soucek": {
			"goal": 0.125,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"callum marshall": {
			"goal": 0.16666666666666666,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan ake": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"oliver scarles": {
			"goal": 0.038461538461538464,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"callum wilson": {
			"goal": 0.2,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"mohamadou kante": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"kyle walker-peters": {
			"goal": 0.034482758620689655,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"luis guilherme lira": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"andrew irving": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lucas paqueta": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"james ward-prowse": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"george earthy": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"crysencio summerville": {
			"goal": 0.1111111111111111,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"niclas fullkrug": {
			"goal": 0.2,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"john stones": {
			"goal": 0.1111111111111111,
			"assist": 0.06666666666666667,
			"no_assist": 0.9705882352941176
		},
		"josko gvardiol": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"abduqodir khusanov": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"mateus fernandes": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"jarrod bowen": {
			"goal": 0.21052631578947367,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"nico oreilly": {
			"goal": 0.125,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"rico lewis": {
			"goal": 0.08,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"nico gonzalez": {
			"goal": 0.1111111111111111,
			"assist": 0.13333333333333333,
			"no_assist": 0.9333333333333333
		},
		"erling haaland": {
			"goal": 0.7333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"kalvin phillips": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9090909090909091
		},
		"tijjani reijnders": {
			"goal": 0.23809523809523808,
			"assist": 0.21739130434782608,
			"no_assist": 0.9
		},
		"oscar bobb": {
			"goal": 0.2631578947368421,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bernardo silva": {
			"goal": 0.14285714285714285,
			"assist": 0.21739130434782608,
			"no_assist": 0.875
		},
		"phil foden": {
			"goal": 0.43478260869565216,
			"assist": 0.2631578947368421,
			"no_assist": 0.8571428571428571
		},
		"divine mukasa": {
			"goal": 0.21739130434782608,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
		"rayan cherki": {
			"goal": 0.25,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		},
		"de paulo igor": {
			"goal": 0.024390243902439025,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"matheus nunes": {
			"goal": 0.08333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"de oliveira savio": {
			"goal": 0.23809523809523808,
			"assist": 0.2857142857142857,
			"no_assist": 0.8571428571428571
		},
	},
	"game_stats": {
		"man city": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.18181818181818182,
				"2": 0.26666666666666666,
				"3+": 0.5789473684210527
			},
			"clean_sheet": 0.47619047619047616
		},
		"west ham": {
			"goals": {
				"0": 0.47619047619047616,
				"1": 0.4,
				"2": 0.16666666666666666,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.06666666666666667
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ben davies": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"kevin danso": {
			"goal": 0.043478260869565216,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"joao palhinha": {
			"goal": 0.10526315789473684,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ibrahima konate": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"archie gray": {
			"goal": 0.047619047619047616,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"virgil van dijk": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9850746268656716
		},
		"djed spence": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"wellity lucky": {
			"goal": 0.038461538461538464,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"rodrigo bentancur": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"lucas bergvall": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"randal muani": {
			"goal": 0.23809523809523808,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"trey nyoni": {
			"goal": 0.16666666666666666,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"ryan gravenberch": {
			"goal": 0.1,
			"assist": 0.08333333333333333,
			"no_assist": 0.9615384615384616
		},
		"milos kerkez": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joe gomez": {
			"goal": 0.05263157894736842,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"brennan johnson": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"curtis jones": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mathys tel": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dane scarlett": {
			"goal": 0.2631578947368421,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andrew robertson": {
			"goal": 0.05555555555555555,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"conor bradley": {
			"goal": 0.08333333333333333,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"richarlison": {
			"goal": 0.29411764705882354,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"hugo ekitike": {
			"goal": 0.38095238095238093,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"alexis mac allister": {
			"goal": 0.14285714285714285,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"calvin ramsay": {
			"goal": 0.07692307692307693,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"wilson odobert": {
			"goal": 0.18181818181818182,
			"assist": 0.11764705882352941,
			"no_assist": 0.9411764705882353
		},
		"jeremie frimpong": {
			"goal": 0.125,
			"assist": 0.16,
			"no_assist": 0.9333333333333333
		},
		"jayden danns": {
			"goal": 0.3333333333333333,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"alexander isak": {
			"goal": 0.38461538461538464,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"rio ngumoha": {
			"goal": 0.2222222222222222,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dominik szoboszlai": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"federico chiesa": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mohammed kudus": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"xavi simons": {
			"goal": 0.17391304347826086,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"florian wirtz": {
			"goal": 0.23255813953488372,
			"assist": 0.21739130434782608,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
	},
	"game_stats": {
		"tottenham": {
			"goals": {
				"0": 0.30303030303030304,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.2
		},
		"liverpool": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.2857142857142857
		}
	}
},
{
	"player_stats": {
		"michael keane": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"reece welch": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"marli salmon": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"william saliba": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"jake obrien": {
			"goal": 0.047619047619047616,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"vitaliy mykolenko": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"adam aznou": {
			"goal": 0.029411764705882353,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"timothy iroegbunam": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"elijah campbell": {
			"goal": 0.03225806451612903,
			"assist": 0.038461538461538464,
			"no_assist": 0.9876543209876543
		},
		"beto": {
			"goal": 0.18181818181818182,
			"assist": 0.05,
			"no_assist": 0.9876543209876543
		},
		"james tarkowski": {
			"goal": 0.038461538461538464,
			"assist": 0.029411764705882353,
			"no_assist": 0.9876543209876543
		},
		"nathan patterson": {
			"goal": 0.029411764705882353,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"thierno barry": {
			"goal": 0.19047619047619047,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"christian norgaard": {
			"goal": 0.10526315789473684,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"james garner": {
			"goal": 0.05263157894736842,
			"assist": 0.06666666666666667,
			"no_assist": 0.975609756097561
		},
		"tyler dibling": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jurrien timber": {
			"goal": 0.08333333333333333,
			"assist": 0.08333333333333333,
			"no_assist": 0.975609756097561
		},
		"viktor gyokeres": {
			"goal": 0.3448275862068966,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"kiernan dewsbury-hall": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"riccardo calafiori": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"carlos alcaraz": {
			"goal": 0.1111111111111111,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"dwight mcneil": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9615384615384616
		},
		"piero hincapie": {
			"goal": 0.043478260869565216,
			"assist": 0.047619047619047616,
			"no_assist": 0.9615384615384616
		},
		"jack grealish": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"max dowman": {
			"goal": 0.25,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"martin zubimendi": {
			"goal": 0.09523809523809523,
			"assist": 0.08333333333333333,
			"no_assist": 0.9523809523809523
		},
		"ethan nwaneri": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"gabriel martinelli": {
			"goal": 0.25,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"josh nichols": {
			"goal": 0.11764705882352941,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"gabriel jesus": {
			"goal": 0.30303030303030304,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"mikel merino": {
			"goal": 0.26666666666666666,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		},
		"louie copley": {
			"goal": 0.15384615384615385,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"noni madueke": {
			"goal": 0.2564102564102564,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"eberechi eze": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9090909090909091
		},
		"leandro trossard": {
			"goal": 0.2702702702702703,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"declan rice": {
			"goal": 0.14285714285714285,
			"assist": 0.16666666666666666,
			"no_assist": 0.9090909090909091
		},
		"martin odegaard": {
			"goal": 0.15384615384615385,
			"assist": 0.19047619047619047,
			"no_assist": 0.8888888888888888
		},
		"bukayo saka": {
			"goal": 0.29411764705882354,
			"assist": 0.23809523809523808,
			"no_assist": 0.875
		},
	},
	"game_stats": {
		"everton": {
			"goals": {
				"0": 0.4878048780487805,
				"1": 0.38461538461538464,
				"2": 0.15384615384615385,
				"3+": 0.058823529411764705
			},
			"clean_sheet": 0.2
		},
		"arsenal": {
			"goals": {
				"0": 0.2,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.4878048780487805
		}
	}
},
{
	"player_stats": {
		"sebastiaan bornauw": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joe rodon": {
			"goal": 0.07692307692307693,
			"assist": 0.024390243902439025,
			"no_assist": 0.9960159362549801
		},
		"pascal struijk": {
			"goal": 0.08333333333333333,
			"assist": 0.029411764705882353,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"maxence lacroix": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"chris richards": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9900990099009901
		},
		"ethan ampadu": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.05263157894736842,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"marc guehi": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"nathaniel clyne": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9876543209876543
		},
		"sam byram": {
			"goal": 0.047619047619047616,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"gabriel gudmundsson": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"joel piroe": {
			"goal": 0.2631578947368421,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james justin": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jefferson lerma": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"kaden rodney": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tyrick mitchell": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"ilia gruev": {
			"goal": 0.05263157894736842,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"chrisantus uche": {
			"goal": 0.21052631578947367,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"jean-philippe mateta": {
			"goal": 0.35714285714285715,
			"assist": 0.07692307692307693,
			"no_assist": 0.9705882352941176
		},
		"dominic calvert-lewin": {
			"goal": 0.30303030303030304,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"eddie nketiah": {
			"goal": 0.25,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"ao tanaka": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9615384615384616
		},
		"justin devenny": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"romain esse": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ben casey": {
			"goal": 0.16666666666666666,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"anton stach": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"borna sosa": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jack harrison": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"adam wharton": {
			"goal": 0.07142857142857142,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"degnand gnonto": {
			"goal": 0.18181818181818182,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"brenden aaronson": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9411764705882353
		},
		"joel drakes-thomas": {
			"goal": 0.09090909090909091,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"noah okafor": {
			"goal": 0.21052631578947367,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"yeremy pino": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
	},
	"game_stats": {
		"leeds": {
			"goals": {
				"0": 0.30303030303030304,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3076923076923077
		},
		"crystal palace": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.29411764705882354
		}
	}
},
{
	"player_stats": {
		"lisandro martinez": {
			"goal": 0.047619047619047616,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"tyler fredricson": {
			"goal": 0.034482758620689655,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"pau torres": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"leny yoro": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"victor lindelof": {
			"goal": 0.043478260869565216,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"harry maguire": {
			"goal": 0.08333333333333333,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"ayden heaven": {
			"goal": 0.038461538461538464,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"yeimar mosquera": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"ezri konsa": {
			"goal": 0.06666666666666667,
			"assist": 0.029411764705882353,
			"no_assist": 0.9900990099009901
		},
		"tyrell malacia": {
			"goal": 0.029411764705882353,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"diego leon": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"jack fletcher": {
			"goal": 0.125,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"matthijs de ligt": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9850746268656716
		},
		"amadou onana": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"kobbie mainoo": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"luke shaw": {
			"goal": 0.029411764705882353,
			"assist": 0.058823529411764705,
			"no_assist": 0.975609756097561
		},
		"george hemmings": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"manuel ugarte": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"diogo dalot": {
			"goal": 0.047619047619047616,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"lamare bogarde": {
			"goal": 0.05263157894736842,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"joshua zirkzee": {
			"goal": 0.25,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"boubacar kamara": {
			"goal": 0.07142857142857142,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"jamaldeen jimoh": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"patrick dorgu": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"benjamin sesko": {
			"goal": 0.30303030303030304,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"shea lacey": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"mason mount": {
			"goal": 0.16666666666666666,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"travis patterson": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"matty cash": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andres garcia": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"aidan borland": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"bradley burrowes": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"donyell malen": {
			"goal": 0.3333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ben broggio": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"john mcginn": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"ian maatsen": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9333333333333333
		},
		"youri tielemans": {
			"goal": 0.17391304347826086,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"lucas digne": {
			"goal": 0.06666666666666667,
			"assist": 0.14285714285714285,
			"no_assist": 0.9230769230769231
		},
		"ollie watkins": {
			"goal": 0.4,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"evann guessand": {
			"goal": 0.25,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"bruno fernandes": {
			"goal": 0.23809523809523808,
			"assist": 0.17391304347826086,
			"no_assist": 0.9090909090909091
		},
		"harvey elliott": {
			"goal": 0.18181818181818182,
			"assist": 0.1724137931034483,
			"no_assist": 0.9090909090909091
		},
		"emiliano buendia": {
			"goal": 0.25,
			"assist": 0.19047619047619047,
			"no_assist": 0.9090909090909091
		},
		"morgan rogers": {
			"goal": 0.2857142857142857,
			"assist": 0.2,
			"no_assist": 0.9
		},
		"matheus cunha": {
			"goal": 0.2777777777777778,
			"assist": 0.15384615384615385,
			"no_assist": 0.9
		},
	},
	"game_stats": {
		"aston villa": {
			"goals": {
				"0": 0.2,
				"1": 0.3448275862068966,
				"2": 0.29411764705882354,
				"3+": 0.26666666666666666
			},
			"clean_sheet": 0.2857142857142857
		},
		"man utd": {
			"goals": {
				"0": 0.2857142857142857,
				"1": 0.38461538461538464,
				"2": 0.2631578947368421,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"issa diop": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9950248756218906
		},
		"jack thompson": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jorge cuenca": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9900990099009901
		},
		"zach abbott": {
			"goal": 0.038461538461538464,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"felipe morato": {
			"goal": 0.038461538461538464,
			"assist": 0.034482758620689655,
			"no_assist": 0.9876543209876543
		},
		"joachim andersen": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9876543209876543
		},
		"timothy castagne": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kenny tete": {
			"goal": 0.047619047619047616,
			"assist": 0.0625,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"ryan yates": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"neco williams": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"murillo dos santos": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.975609756097561
		},
		"oleksandr zinchenko": {
			"goal": 0.058823529411764705,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nicolas dominguez": {
			"goal": 0.10526315789473684,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.08333333333333333,
			"assist": 0.08333333333333333,
			"no_assist": 0.9705882352941176
		},
		"chris wood": {
			"goal": 0.3076923076923077,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"emile smith rowe": {
			"goal": 0.17391304347826086,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"callum hudson-odoi": {
			"goal": 0.18181818181818182,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.3225806451612903,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"antonee robinson": {
			"goal": 0.047619047619047616,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"igor jesus": {
			"goal": 0.2631578947368421,
			"assist": 0.09523809523809523,
			"no_assist": 0.9523809523809523
		},
		"james mcatee": {
			"goal": 0.19047619047619047,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"jonah kusi-asare": {
			"goal": 0.2777777777777778,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"taiwo awoniyi": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"douglas luiz": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9523809523809523
		},
		"ryan sessegnon": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"archie whitehall": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"sasa lukic": {
			"goal": 0.09523809523809523,
			"assist": 0.07692307692307693,
			"no_assist": 0.9411764705882353
		},
		"joshua king": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"harry wilson": {
			"goal": 0.2222222222222222,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.2,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"tom cairney": {
			"goal": 0.07692307692307693,
			"assist": 0.13333333333333333,
			"no_assist": 0.9411764705882353
		},
		"jimmy sinclair": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"dan ndoye": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.16,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"omari giraud-hutchinson": {
			"goal": 0.17391304347826086,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"elliot anderson": {
			"goal": 0.09090909090909091,
			"assist": 0.11764705882352941,
			"no_assist": 0.9230769230769231
		},
		"dilane bakwa": {
			"goal": 0.15384615384615385,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"morgan gibbs-white": {
			"goal": 0.19047619047619047,
			"assist": 0.16666666666666666,
			"no_assist": 0.9230769230769231
		}
	},
	"game_stats": {
		"fulham": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.3225806451612903
		},
		"nottingham forest": {
			"goals": {
				"0": 0.3333333333333333,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.2777777777777778
		}
	}
},
]

DATA = [
{
	"player_stats": {
		"malick thiaw": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"lisandro martinez": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"fabian schar": {
			"goal": 0.10526315789473684,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"tyler fredricson": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"leny yoro": {
			"goal": 0.08333333333333333,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"harry maguire": {
			"goal": 0.09090909090909091,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"alex murphy": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"sven botman": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"emil krafth": {
			"goal": 0.05263157894736842,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ayden heaven": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"jamaal lascelles": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tyrell malacia": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"diego leon": {
			"goal": 0.14285714285714285,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"matthijs de ligt": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"jack fletcher": {
			"goal": 0.14285714285714285,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"sean neave": {
			"goal": 0.25,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"luke shaw": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"manuel ugarte": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"kobbie mainoo": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"william osula": {
			"goal": 0.3125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"valentino livramento": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yoane wissa": {
			"goal": 0.3125,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"diogo dalot": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joe willock": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"casemiro": {
			"goal": 0.125,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jacob ramsey": {
			"goal": 0.16,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"joshua zirkzee": {
			"goal": 0.30303030303030304,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"joelinton": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis hall": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"benjamin sesko": {
			"goal": 0.37735849056603776,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"nick woltemade": {
			"goal": 0.37735849056603776,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"kieran trippier": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lewis miley": {
			"goal": 0.10526315789473684,
			"assist": 0.11764705882352941,
			"no_assist": 0.9523809523809523
		},
		"shea lacey": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"mason mount": {
			"goal": 0.23255813953488372,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"patrick dorgu": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"seung-soo park": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"anthony gordon": {
			"goal": 0.29411764705882354,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"sandro tonali": {
			"goal": 0.14285714285714285,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"jacob murphy": {
			"goal": 0.23076923076923078,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"harvey barnes": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"anthony elanga": {
			"goal": 0.21739130434782608,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bruno fernandes": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"bruno guimaraes": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"matheus cunha": {
			"goal": 0.36363636363636365,
			"assist": 0.25,
			"no_assist": 0.875
		}
	},
	"game_stats": {
		"man utd": {
			"goals": {
				"0": 0.2,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.26666666666666666
		},
		"newcastle": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38095238095238093,
				"2": 0.26666666666666666,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.2
		}
	}
},
{
	"player_stats": {
		"jair cunha": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"ruben dias": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nikola milenkovic": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"nathan ake": {
			"goal": 0.07692307692307693,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jack thompson": {
			"goal": 0.15384615384615385,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"zach abbott": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"felipe morato": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"john stones": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ryan yates": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"neco williams": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"murillo dos santos": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"oleksandr zinchenko": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"nicolo savona": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"josko gvardiol": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"abduqodir khusanov": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"nicolas dominguez": {
			"goal": 0.09523809523809523,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"chris wood": {
			"goal": 0.2777777777777778,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum hudson-odoi": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"arnaud kalimuendo": {
			"goal": 0.25,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"nico gonzalez": {
			"goal": 0.09523809523809523,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"taiwo awoniyi": {
			"goal": 0.29411764705882354,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"archie whitehall": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"igor jesus": {
			"goal": 0.2777777777777778,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"james mcatee": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"rico lewis": {
			"goal": 0.07692307692307693,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"nico oreilly": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"douglas luiz": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jimmy sinclair": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"erling haaland": {
			"goal": 0.5789473684210527,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"omari giraud-hutchinson": {
			"goal": 0.11764705882352941,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"dan ndoye": {
			"goal": 0.14285714285714285,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"kalvin phillips": {
			"goal": 0.10526315789473684,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"morgan gibbs-white": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"elliot anderson": {
			"goal": 0.1,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"dilane bakwa": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"tijjani reijnders": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"oscar bobb": {
			"goal": 0.26666666666666666,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"bernardo silva": {
			"goal": 0.14814814814814814,
			"assist": 0.16,
			"no_assist": 0.9230769230769231
		},
		"divine mukasa": {
			"goal": 0.21052631578947367,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"phil foden": {
			"goal": 0.3333333333333333,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"rayan cherki": {
			"goal": 0.23809523809523808,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"jeremy doku": {
			"goal": 0.21739130434782608,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"matheus nunes": {
			"goal": 0.10526315789473684,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"de oliveira savio": {
			"goal": 0.23076923076923078,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"nottingham forest": {
			"goals": {
				"0": 0.38095238095238093,
				"1": 0.4,
				"2": 0.2222222222222222,
				"3+": 0.1
			},
			"clean_sheet": 0.16666666666666666
		},
		"man city": {
			"goals": {
				"0": 0.15384615384615385,
				"1": 0.30303030303030304,
				"2": 0.3076923076923077,
				"3+": 0.3333333333333333
			},
			"clean_sheet": 0.36363636363636365
		}
	}
},
{
	"player_stats": {
		"jan paul van hecke": {
			"goal": 0.029411764705882353,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"lewis dunk": {
			"goal": 0.05263157894736842,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"diego coppola": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"freddie simmonds": {
			"goal": 0.047619047619047616,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"charlie tasker": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"olivier boscagli": {
			"goal": 0.047619047619047616,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"marli salmon": {
			"goal": 0.1111111111111111,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ferdi kadioglu": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"william saliba": {
			"goal": 0.1111111111111111,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"joel veltman": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jack hinshelwood": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"danny welbeck": {
			"goal": 0.23809523809523808,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"yasin ayari": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"charalampos kostoulas": {
			"goal": 0.16666666666666666,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"james milner": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"christian norgaard": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"maxim de cuyper": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"diego gomez": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"brajan gruda": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"tom watson": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"jurrien timber": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"joe knight": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kaoru mitoma": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mats wieffer": {
			"goal": 0.058823529411764705,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"nehemiah oriola": {
			"goal": 0.13333333333333333,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"viktor gyokeres": {
			"goal": 0.47619047619047616,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"riccardo calafiori": {
			"goal": 0.1111111111111111,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"myles lewis-skelly": {
			"goal": 0.1111111111111111,
			"assist": 0.10526315789473684,
			"no_assist": 0.9523809523809523
		},
		"georginio rutter": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"piero hincapie": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"max dowman": {
			"goal": 0.26666666666666666,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"yankuba minteh": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"martin zubimendi": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"gabriel jesus": {
			"goal": 0.4,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"gabriel martinelli": {
			"goal": 0.29411764705882354,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"josh nichols": {
			"goal": 0.13333333333333333,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"ethan nwaneri": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mikel merino": {
			"goal": 0.3225806451612903,
			"assist": 0.2222222222222222,
			"no_assist": 0.9090909090909091
		},
		"louie copley": {
			"goal": 0.2,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"noni madueke": {
			"goal": 0.2857142857142857,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"declan rice": {
			"goal": 0.16666666666666666,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"eberechi eze": {
			"goal": 0.3125,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"leandro trossard": {
			"goal": 0.3125,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"martin odegaard": {
			"goal": 0.21739130434782608,
			"assist": 0.23809523809523808,
			"no_assist": 0.875
		},
		"bukayo saka": {
			"goal": 0.38095238095238093,
			"assist": 0.3076923076923077,
			"no_assist": 0.8461538461538461
		}
	},
	"game_stats": {
		"arsenal": {
			"goals": {
				"0": 0.14285714285714285,
				"1": 0.2857142857142857,
				"2": 0.3076923076923077,
				"3+": 0.38095238095238093
			},
			"clean_sheet": 0.43478260869565216
		},
		"brighton": {
			"goals": {
				"0": 0.4444444444444444,
				"1": 0.4,
				"2": 0.18181818181818182,
				"3+": 0.06666666666666667
			},
			"clean_sheet": 0.14285714285714285
		}
	}
},
{
	"player_stats": {
		"yerson mosquera": {
			"goal": 0.038461538461538464,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"santiago bueno": {
			"goal": 0.034482758620689655,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"joao gomes": {
			"goal": 0.07142857142857142,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"ladislav krejci": {
			"goal": 0.05,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ki-jana hoever": {
			"goal": 0.058823529411764705,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"toti gomes": {
			"goal": 0.038461538461538464,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"matt doherty": {
			"goal": 0.043478260869565216,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"toluwalase arokodare": {
			"goal": 0.19230769230769232,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"andre trindade": {
			"goal": 0.05,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"ibrahima konate": {
			"goal": 0.13333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jackson tchatchoua": {
			"goal": 0.047619047619047616,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"david wolfe": {
			"goal": 0.047619047619047616,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"hugo bueno": {
			"goal": 0.034482758620689655,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"mateus mane": {
			"goal": 0.13333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"jorgen larsen": {
			"goal": 0.18181818181818182,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"virgil van dijk": {
			"goal": 0.15384615384615385,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"hee-chan hwang": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"fernando lopez": {
			"goal": 0.1111111111111111,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"wellity lucky": {
			"goal": 0.13333333333333333,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jhon arias": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"trey nyoni": {
			"goal": 0.23809523809523808,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"milos kerkez": {
			"goal": 0.11764705882352941,
			"assist": 0.10526315789473684,
			"no_assist": 0.9411764705882353
		},
		"ryan gravenberch": {
			"goal": 0.14285714285714285,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"curtis jones": {
			"goal": 0.15384615384615385,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"joe gomez": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"andrew robertson": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9090909090909091
		},
		"conor bradley": {
			"goal": 0.13333333333333333,
			"assist": 0.14285714285714285,
			"no_assist": 0.9090909090909091
		},
		"alexis mac allister": {
			"goal": 0.2,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"calvin ramsay": {
			"goal": 0.16666666666666666,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"hugo ekitike": {
			"goal": 0.5128205128205128,
			"assist": 0.23076923076923078,
			"no_assist": 0.9
		},
		"federico chiesa": {
			"goal": 0.3333333333333333,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		},
		"jayden danns": {
			"goal": 0.45454545454545453,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"jeremie frimpong": {
			"goal": 0.16666666666666666,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"alexander isak": {
			"goal": 0.5128205128205128,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"rio ngumoha": {
			"goal": 0.30303030303030304,
			"assist": 0.23076923076923078,
			"no_assist": 0.8888888888888888
		},
		"dominik szoboszlai": {
			"goal": 0.3125,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"florian wirtz": {
			"goal": 0.3125,
			"assist": 0.29411764705882354,
			"no_assist": 0.8461538461538461
		},
	},
	"game_stats": {
		"liverpool": {
			"goals": {
				"0": 0.07692307692307693,
				"1": 0.2,
				"2": 0.2857142857142857,
				"3+": 0.5454545454545454
			}
		},
		"wolverhampton": {
			"goals": {
				"0": 0.5238095238095238,
				"1": 0.38095238095238093,
				"2": 0.15384615384615385,
				"3+": 0.05263157894736842
			}
		}
	}
},
{
	"player_stats": {
		"maxime esteve": {
			"goal": 0.058823529411764705,
			"assist": 0.0196078431372549,
			"no_assist": 0.9986684420772304
		},
		"luis florentino": {
			"goal": 0.05555555555555555,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"oliver sonne": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"michael keane": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"jarrad branthwaite": {
			"goal": 0.06666666666666667,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"joe worrall": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"kyle walker": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"hjalmar ekdal": {
			"goal": 0.047619047619047616,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"reece welch": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"lucas pires": {
			"goal": 0.05555555555555555,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"adam aznou": {
			"goal": 0.1,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"ashley barnes": {
			"goal": 0.18181818181818182,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"jake obrien": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"mike tresor": {
			"goal": 0.2,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"loum tchaouna": {
			"goal": 0.15384615384615385,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"timothy iroegbunam": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"vitaliy mykolenko": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"josh cullen": {
			"goal": 0.07142857142857142,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jaydon banel": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"marcus edwards": {
			"goal": 0.13333333333333333,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"beto": {
			"goal": 0.3125,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"armando broja": {
			"goal": 0.21739130434782608,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james tarkowski": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"josh laurent": {
			"goal": 0.09090909090909091,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"lesley ugochukwu": {
			"goal": 0.10526315789473684,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"elijah campbell": {
			"goal": 0.11764705882352941,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"nathan patterson": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"zian flemming": {
			"goal": 0.23076923076923078,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"jaidon anthony": {
			"goal": 0.2,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"thierno barry": {
			"goal": 0.30303030303030304,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"quilindschy hartman": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"jacob bruun larsen": {
			"goal": 0.16,
			"assist": 0.1111111111111111,
			"no_assist": 0.9523809523809523
		},
		"tyler dibling": {
			"goal": 0.16666666666666666,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"james garner": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9411764705882353
		},
		"merlin rohl": {
			"goal": 0.2,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"dwight mcneil": {
			"goal": 0.16,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"kiernan dewsbury-hall": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"carlos alcaraz": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jack grealish": {
			"goal": 0.23076923076923078,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"burnley": {
			"goals": {
				"0": 0.4,
				"1": 0.4,
				"2": 0.2,
				"3+": 0.07692307692307693
			},
			"clean_sheet": 0.23809523809523808
		},
		"everton": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.4
		}
	}
},
{
	"player_stats": {
		"veljko milosavljevic": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"ethan pinnock": {
			"goal": 0.08333333333333333,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"aaron hickey": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9933774834437086
		},
		"julio soler": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tyler adams": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"marcos senesi": {
			"goal": 0.05263157894736842,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"adam smith": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nathan collins": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"sepp van den berg": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"benjamin arthur": {
			"goal": 0.09090909090909091,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"malcom dacosta": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"alejandro jimenez": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"evanilson": {
			"goal": 0.2564102564102564,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"kristoffer ajer": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"julian araujo": {
			"goal": 0.06666666666666667,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"bafode diakite": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"myles peart-harris": {
			"goal": 0.21739130434782608,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yunus emre konak": {
			"goal": 0.13333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"rico henry": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"james hill": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"yegor yarmolyuk": {
			"goal": 0.14814814814814814,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"romelle donovan": {
			"goal": 0.2,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"michael kayode": {
			"goal": 0.07692307692307693,
			"assist": 0.10526315789473684,
			"no_assist": 0.9615384615384616
		},
		"eli junior kroupi": {
			"goal": 0.2777777777777778,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"alex scott": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"lewis cook": {
			"goal": 0.07692307692307693,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"vitaly janelt": {
			"goal": 0.1,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"amine adli": {
			"goal": 0.16666666666666666,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"adrien truffert": {
			"goal": 0.06666666666666667,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"enes unal": {
			"goal": 0.29411764705882354,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ryan christie": {
			"goal": 0.11764705882352941,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"gustavo nunes gomes": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"marcus tavernier": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jordan henderson": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"keane lewis-potter": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"justin kluivert": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"antoine semenyo": {
			"goal": 0.3125,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"david brooks": {
			"goal": 0.20833333333333334,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"kevin schade": {
			"goal": 0.2857142857142857,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"reiss nelson": {
			"goal": 0.23809523809523808,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"mathias jensen": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"igor thiago": {
			"goal": 0.43478260869565216,
			"assist": 0.2,
			"no_assist": 0.9230769230769231
		},
		"mikkel damsgaard": {
			"goal": 0.15384615384615385,
			"assist": 0.25,
			"no_assist": 0.8888888888888888
		}
	},
	"game_stats": {
		"brentford": {
			"goals": {
				"0": 0.23076923076923078,
				"1": 0.35714285714285715,
				"2": 0.2857142857142857,
				"3+": 0.23076923076923078
			},
			"clean_sheet": 0.2857142857142857
		},
		"bournemouth": {
			"goals": {
				"0": 0.29411764705882354,
				"1": 0.38461538461538464,
				"2": 0.26666666666666666,
				"3+": 0.16666666666666666
			},
			"clean_sheet": 0.23076923076923078
		}
	}
},
{
	"player_stats": {
		"issa diop": {
			"goal": 0.07692307692307693,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jean-clair todibo": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"konstantinos mavropanos": {
			"goal": 0.08333333333333333,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"max kilman": {
			"goal": 0.06666666666666667,
			"assist": 0.043478260869565216,
			"no_assist": 0.9933774834437086
		},
		"jorge cuenca": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"joachim andersen": {
			"goal": 0.06666666666666667,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"ezra mayers": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"soungoutou magassa": {
			"goal": 0.10526315789473684,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"airidas golambeckis": {
			"goal": 0.08333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"guido rodriguez": {
			"goal": 0.08,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"timothy castagne": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"sander berge": {
			"goal": 0.09090909090909091,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"kenny tete": {
			"goal": 0.08333333333333333,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"oliver scarles": {
			"goal": 0.08,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"tomas soucek": {
			"goal": 0.2,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"freddie potts": {
			"goal": 0.08333333333333333,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"callum marshall": {
			"goal": 0.2777777777777778,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"harrison reed": {
			"goal": 0.10526315789473684,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"callum wilson": {
			"goal": 0.34782608695652173,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"emile smith rowe": {
			"goal": 0.18181818181818182,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"kyle walker-peters": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"luis guilherme lira": {
			"goal": 0.14814814814814814,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"raul jimenez": {
			"goal": 0.34782608695652173,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mohamadou kante": {
			"goal": 0.15384615384615385,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"ryan sessegnon": {
			"goal": 0.15384615384615385,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"jonah kusi-asare": {
			"goal": 0.3076923076923077,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"antonee robinson": {
			"goal": 0.07692307692307693,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"andrew irving": {
			"goal": 0.14285714285714285,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"tom cairney": {
			"goal": 0.08,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"sasa lukic": {
			"goal": 0.1111111111111111,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"crysencio summerville": {
			"goal": 0.17391304347826086,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"joshua king": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"george earthy": {
			"goal": 0.2,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"lucas paqueta": {
			"goal": 0.2222222222222222,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"kevin macedo": {
			"goal": 0.19047619047619047,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"niclas fullkrug": {
			"goal": 0.30303030303030304,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"harry wilson": {
			"goal": 0.25,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"james ward-prowse": {
			"goal": 0.11764705882352941,
			"assist": 0.15384615384615385,
			"no_assist": 0.9333333333333333
		},
		"adama traore": {
			"goal": 0.1724137931034483,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"mateus fernandes": {
			"goal": 0.125,
			"assist": 0.15384615384615385,
			"no_assist": 0.9230769230769231
		},
		"jarrod bowen": {
			"goal": 0.3448275862068966,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"de paulo igor": {
			"goal": 0.07692307692307693,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		}
	},
	"game_stats": {
		"west ham": {
			"goals": {
				"0": 0.2777777777777778,
				"1": 0.38095238095238093,
				"2": 0.2631578947368421,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.26666666666666666
		},
		"fulham": {
			"goals": {
				"0": 0.26666666666666666,
				"1": 0.38095238095238093,
				"2": 0.2777777777777778,
				"3+": 0.18181818181818182
			},
			"clean_sheet": 0.26666666666666666
		}
	}
},
{
	"player_stats": {
		"victor lindelof": {
			"goal": 0.043478260869565216,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"pau torres": {
			"goal": 0.058823529411764705,
			"assist": 0.029411764705882353,
			"no_assist": 0.998003992015968
		},
		"ezri konsa": {
			"goal": 0.05263157894736842,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"yeimar mosquera": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"benoit badiashile": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"tosin adarabioyo": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"wesley fofana": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9900990099009901
		},
		"george hemmings": {
			"goal": 0.13333333333333333,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"trevoh chalobah": {
			"goal": 0.1,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"lamare bogarde": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"amadou onana": {
			"goal": 0.09090909090909091,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"andres garcia": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"boubacar kamara": {
			"goal": 0.06666666666666667,
			"assist": 0.06666666666666667,
			"no_assist": 0.9803921568627451
		},
		"matty cash": {
			"goal": 0.08695652173913043,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"travis patterson": {
			"goal": 0.10526315789473684,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jamaldeen jimoh": {
			"goal": 0.1,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"moises caicedo": {
			"goal": 0.1,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"jorrel hato": {
			"goal": 0.09090909090909091,
			"assist": 0.125,
			"no_assist": 0.9615384615384616
		},
		"ben broggio": {
			"goal": 0.11764705882352941,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"aidan borland": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"john mcginn": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"donyell malen": {
			"goal": 0.25,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"bradley burrowes": {
			"goal": 0.14285714285714285,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"josh acheampong": {
			"goal": 0.1,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"andrey santos": {
			"goal": 0.16,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"marc cucurella": {
			"goal": 0.09090909090909091,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"evann guessand": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"lucas digne": {
			"goal": 0.058823529411764705,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ian maatsen": {
			"goal": 0.1,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"youri tielemans": {
			"goal": 0.13333333333333333,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"ollie watkins": {
			"goal": 0.3333333333333333,
			"assist": 0.13333333333333333,
			"no_assist": 0.9523809523809523
		},
		"marc guiu": {
			"goal": 0.2777777777777778,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"malo gusto": {
			"goal": 0.09090909090909091,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"emiliano buendia": {
			"goal": 0.2,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"harvey elliott": {
			"goal": 0.13333333333333333,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"jadon sancho": {
			"goal": 0.11764705882352941,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"morgan rogers": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"facundo buonanotte": {
			"goal": 0.21739130434782608,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"enzo fernandez": {
			"goal": 0.25,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"tyrique george": {
			"goal": 0.2857142857142857,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"reece james": {
			"goal": 0.1,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"jamie bynoe-gittens": {
			"goal": 0.2222222222222222,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"alejandro garnacho": {
			"goal": 0.2564102564102564,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"pedro neto": {
			"goal": 0.25,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"estevao": {
			"goal": 0.30303030303030304,
			"assist": 0.2222222222222222,
			"no_assist": 0.9
		},
		"cole palmer": {
			"goal": 0.38461538461538464,
			"assist": 0.26666666666666666,
			"no_assist": 0.875
		},
		"de jesus joao pedro": {
			"goal": 0.38095238095238093,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		}
	},
	"game_stats": {
		"chelsea": {
			"goals": {
				"0": 0.19047619047619047,
				"1": 0.3333333333333333,
				"2": 0.29411764705882354,
				"3+": 0.2857142857142857
			},
			"clean_sheet": 0.3448275862068966
		},
		"aston villa": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.18181818181818182
		}
	}
},
{
	"player_stats": {
		"pascal struijk": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joe rodon": {
			"goal": 0.08,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"sebastiaan bornauw": {
			"goal": 0.043478260869565216,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"jaka bijol": {
			"goal": 0.058823529411764705,
			"assist": 0.038461538461538464,
			"no_assist": 0.9950248756218906
		},
		"omar alderete": {
			"goal": 0.09090909090909091,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"luke onien": {
			"goal": 0.06666666666666667,
			"assist": 0.038461538461538464,
			"no_assist": 0.9933774834437086
		},
		"ethan ampadu": {
			"goal": 0.058823529411764705,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"lutsharel geertruida": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"sam byram": {
			"goal": 0.043478260869565216,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"dan neil": {
			"goal": 0.07692307692307693,
			"assist": 0.058823529411764705,
			"no_assist": 0.9876543209876543
		},
		"nordi mukiele": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"james justin": {
			"goal": 0.06666666666666667,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"daniel ballard": {
			"goal": 0.11764705882352941,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"joel piroe": {
			"goal": 0.29411764705882354,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"jayden bogle": {
			"goal": 0.07692307692307693,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"wilson isidor": {
			"goal": 0.3225806451612903,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"gabriel gudmundsson": {
			"goal": 0.058823529411764705,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"ilia gruev": {
			"goal": 0.07692307692307693,
			"assist": 0.09090909090909091,
			"no_assist": 0.975609756097561
		},
		"eliezer mayenda": {
			"goal": 0.2857142857142857,
			"assist": 0.07692307692307693,
			"no_assist": 0.975609756097561
		},
		"lukas nmecha": {
			"goal": 0.26666666666666666,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"brian brobbey": {
			"goal": 0.2564102564102564,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"trai hume": {
			"goal": 0.06666666666666667,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"ao tanaka": {
			"goal": 0.11764705882352941,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"chris rigg": {
			"goal": 0.14285714285714285,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"dominic calvert-lewin": {
			"goal": 0.3225806451612903,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jack harrison": {
			"goal": 0.15384615384615385,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"anton stach": {
			"goal": 0.1111111111111111,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"noah okafor": {
			"goal": 0.22727272727272727,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"brenden aaronson": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"harrison jones": {
			"goal": 0.18181818181818182,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"degnand gnonto": {
			"goal": 0.23076923076923078,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"enzo le fee": {
			"goal": 0.18181818181818182,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"granit xhaka": {
			"goal": 0.11764705882352941,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"simon adingra": {
			"goal": 0.2,
			"assist": 0.18181818181818182,
			"no_assist": 0.9230769230769231
		},
		"romain mundle": {
			"goal": 0.21052631578947367,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		}
	},
	"game_stats": {
		"sunderland": {
			"goals": {
				"0": 0.3076923076923077,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.15384615384615385
			},
			"clean_sheet": 0.3225806451612903
		},
		"leeds": {
			"goals": {
				"0": 0.3225806451612903,
				"1": 0.4,
				"2": 0.25,
				"3+": 0.14285714285714285
			},
			"clean_sheet": 0.3076923076923077
		}
	}
},
{
	"player_stats": {
		"cristian romero": {
			"goal": 0.06666666666666667,
			"assist": 0.024390243902439025,
			"no_assist": 0.998003992015968
		},
		"junai byfield": {
			"goal": 0.06666666666666667,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"ben davies": {
			"goal": 0.05263157894736842,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		},
		"joao palhinha": {
			"goal": 0.1,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"kevin danso": {
			"goal": 0.07692307692307693,
			"assist": 0.047619047619047616,
			"no_assist": 0.9900990099009901
		},
		"jaydee canvot": {
			"goal": 0.09090909090909091,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"archie gray": {
			"goal": 0.06666666666666667,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"chris richards": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"maxence lacroix": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"marc guehi": {
			"goal": 0.08333333333333333,
			"assist": 0.05263157894736842,
			"no_assist": 0.9876543209876543
		},
		"djed spence": {
			"goal": 0.05263157894736842,
			"assist": 0.058823529411764705,
			"no_assist": 0.9850746268656716
		},
		"nathaniel clyne": {
			"goal": 0.07692307692307693,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"rodrigo bentancur": {
			"goal": 0.08,
			"assist": 0.06666666666666667,
			"no_assist": 0.9850746268656716
		},
		"lucas bergvall": {
			"goal": 0.1111111111111111,
			"assist": 0.07692307692307693,
			"no_assist": 0.9803921568627451
		},
		"dane scarlett": {
			"goal": 0.25,
			"assist": 0.1,
			"no_assist": 0.9705882352941176
		},
		"randal muani": {
			"goal": 0.2564102564102564,
			"assist": 0.09090909090909091,
			"no_assist": 0.9705882352941176
		},
		"will hughes": {
			"goal": 0.08695652173913043,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"pedro porro": {
			"goal": 0.07692307692307693,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jean-philippe mateta": {
			"goal": 0.43478260869565216,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"mathys tel": {
			"goal": 0.21739130434782608,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"chrisantus uche": {
			"goal": 0.18181818181818182,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"kaden rodney": {
			"goal": 0.15384615384615385,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"tyrick mitchell": {
			"goal": 0.06666666666666667,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"jefferson lerma": {
			"goal": 0.10526315789473684,
			"assist": 0.1111111111111111,
			"no_assist": 0.9615384615384616
		},
		"brennan johnson": {
			"goal": 0.21052631578947367,
			"assist": 0.1,
			"no_assist": 0.9615384615384616
		},
		"wilson odobert": {
			"goal": 0.16,
			"assist": 0.125,
			"no_assist": 0.9523809523809523
		},
		"richarlison": {
			"goal": 0.2857142857142857,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"eddie nketiah": {
			"goal": 0.2777777777777778,
			"assist": 0.14285714285714285,
			"no_assist": 0.9523809523809523
		},
		"ben casey": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"adam wharton": {
			"goal": 0.09523809523809523,
			"assist": 0.14285714285714285,
			"no_assist": 0.9411764705882353
		},
		"romain esse": {
			"goal": 0.18181818181818182,
			"assist": 0.15384615384615385,
			"no_assist": 0.9411764705882353
		},
		"mohammed kudus": {
			"goal": 0.21739130434782608,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"borna sosa": {
			"goal": 0.07692307692307693,
			"assist": 0.14285714285714285,
			"no_assist": 0.9333333333333333
		},
		"justin devenny": {
			"goal": 0.18181818181818182,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"xavi simons": {
			"goal": 0.19230769230769232,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"joel drakes-thomas": {
			"goal": 0.1111111111111111,
			"assist": 0.16666666666666666,
			"no_assist": 0.9333333333333333
		},
		"yeremy pino": {
			"goal": 0.21739130434782608,
			"assist": 0.2,
			"no_assist": 0.9090909090909091
		},
		"mickey van de ven": {
			"goal": 0.09090909090909091,
			"assist": 0.034482758620689655,
			"no_assist": 0.9960159362549801
		}
	},
	"game_stats": {
		"crystal palace": {
			"goals": {
				"0": 0.25,
				"1": 0.37037037037037035,
				"2": 0.2857142857142857,
				"3+": 0.2222222222222222
			},
			"clean_sheet": 0.3448275862068966
		},
		"tottenham": {
			"goals": {
				"0": 0.3448275862068966,
				"1": 0.4,
				"2": 0.23076923076923078,
				"3+": 0.125
			},
			"clean_sheet": 0.25
		}
	}
},
]

def p_to_rate(target):
    lo = 0
    hi = 3
    while lo < hi:
        rate = lo + ((hi - lo) / 2)
        k = 0
        p = 1 - e ** (-rate) * sum(
            (rate ** j) / factorial(j) for j in range(k + 1)
        )
        if abs(p - target) < 0.00000000001:
            break
        elif p < target:
            lo = rate
        elif p > target:
            hi = rate
    return rate

def ps_to_rate(targets):
    lo = 0
    hi = 20
    rate = lo
    best_rate = None
    best_err = 9e99
    for k in targets:
        targets[k] = fake_to_actual(targets[k])
    for i in range(2):
        total = sum(targets.values())
        for k in targets:
            targets[k] = targets[k] / total
    while rate < hi:
        sum_squared_error = 0
        polarity = 0
        for key, target in targets.items():
            target = fake_to_actual(target)
            if key == "3+":
                p = 1 - e ** (-rate) * sum(
                    (rate ** j) / factorial(j) for j in range(3)
                )
            else:
                p = (e ** (-rate) * rate ** int(key)) / factorial(int(key))
            error = p - target
            signed_square_error = error * abs(error)
            sum_squared_error += abs(signed_square_error)
            polarity += signed_square_error
        if sum_squared_error < best_err:
            best_err = sum_squared_error
            best_rate = rate
        rate += 0.001
    return best_rate

def rate_to_dist(rate):
    return [
        ((rate ** k) * e ** (-rate)) / factorial(k)
        for k in range(0, 100)
    ]

def p_to_dist(target):
    return rate_to_dist(p_to_rate(target))

def points(goals, assists, conceded, position):
    pts = 2
    bonus_pts = 6
    if position == "GKP":
        pts += goals * 10
        bonus_pts += goals * 12
        if conceded == 0:
            pts += 6
            bonus_pts += 12
        elif conceded >= 1:
            pts -= conceded // 2
            bonus_pts -= conceded * 4
    if position == "DEF":
        pts += goals * 6
        bonus_pts += goals * 12
        if conceded == 0:
            pts += 6
            bonus_pts += 12
        elif conceded >= 1:
            pts -= conceded // 2
            bonus_pts -= conceded * 4
    if position == "MID":
        pts += goals * 5
        bonus_pts += goals * 18
        if conceded == 0:
            pts += 1
    if position == "FWD":
        pts += goals * 4
        bonus_pts += goals * 24
    pts += assists * 3
    bonus_pts += assists * 9
    return pts, bonus_pts

def find_player(player, possible_teams):
    possible_teams = set(possible_teams)
    if "wolverhampton" in possible_teams:
        possible_teams.remove("wolverhampton")
        possible_teams.add("wolves")
    if "nottingham forest" in possible_teams:
        possible_teams.remove("nottingham forest")
        possible_teams.add("nott'm forest")
    if "tottenham" in possible_teams:
        possible_teams.remove("tottenham")
        possible_teams.add("spurs")
    if player == "casemiro": player = "carlos henrique casimiro"
    elif player == "beto": player = "norberto bercique gomes betuncal"
    elif player == "yegor yarmolyuk": player = "yehor yarmoliuk"
    elif player == "lucas paqueta": player = "lucas tolentino coelho de lima paqueta"
    search_template = name_template(player)
    a = set(part for part in search_template.split() if len(part) > 2)
    player_info = PLAYERS_BY_NAME.get(search_template)
    best = None
    best_intersect = 0
    multiple_candidates = None
    if player_info is None:
        for player_info in PLAYERS_BY_NAME.values():
            pid, candidate_template, pos, team = player_info
            if team not in possible_teams: continue
            b = set(part for part in candidate_template.split() if len(part) > 2)
            if a.intersection(b) == set(): continue
            intersect = a.intersection(b)
            a_diff = a - b
            b_diff = b - a
            similar_part = max([
                min(len(a_i), len(b_i)) / max(len(a_i), len(b_i))
                for a_i in a_diff
                for b_i in b_diff
                if (
                    match(a_i.replace("", ".*"), b_i) != None
                    or match(b_i.replace("", ".*"), a_i) != None
                )
            ] + [0])
            if len(intersect) + similar_part > best_intersect:
                best_intersect = len(intersect) + similar_part
                best = player_info
                multiple_candidates = None
            elif len(intersect) + similar_part == best_intersect:
                multiple_candidates = player_info
                best_intersect = 0
        if multiple_candidates is not None:
            raise Exception(f"Multiple candidates: {str(best)} {str(multiple_candidates)} {str(player)}")
        return best
    else: return player_info

for game_data in DATA:
    game_stats = {}
    for team, values in game_data["game_stats"].items():
        print(team)
        goals = values["goals"]
        #clean_sheet = fake_to_actual(values["clean_sheet"])
        goal_odds = {}
        for g, p in enumerate(rate_to_dist(ps_to_rate(goals))[:10]):
            if g < 2: goal_odds[g] = p
            else: goal_odds[g] = p
        game_stats[team] = {
            "goals": goal_odds,
            #"clean_sheet": clean_sheet,
        }
    player_pts_odds = []
    players_by_points = {}
    for player, values in game_data["player_stats"].items():
        # Academy players not included in FPL
        if player in set([
            "reggie walsh",
            "ryan kavuma-mcqueen",
            "brandon pouani",
            "freddie simmonds",
            "aidan borland",
        ]): continue
        goals = fake_to_actual(values["goal"])
        assist = fake_to_actual(values["assist"])
        no_assist = fake_to_actual(values["no_assist"])
        assist, no_assist = (
            assist / (assist + no_assist),
            no_assist / (assist + no_assist),
        )
        player_info = find_player(player, game_stats.keys())
        if player_info is None: print("Error:", player)
        else:
            pid, name, position, team = player_info
            stats = game_stats[list(game_stats.keys() - [team])[0]]
            probs = []
            for c, c_p in stats["goals"].items():
                for a, a_p in enumerate(p_to_dist(assist)[:13], start=0):
                    for g, g_p in enumerate(p_to_dist(goals)[:13], start=0):
                        p = a_p * g_p * c_p
                        if p > 0:
                            probs.append((p, a, g, c))
                probs.sort()
            expected_pts = 0
            pts_p = {}
            bonus_pts_p = {}
            for p, a, g, c in probs:
                pts, bonus_pts = points(g, a, c, position)
                pts_p[pts] = pts_p.get(pts, 0) + p
                bonus_pts_p[bonus_pts] = pts_p.get(bonus_pts, 0) + p
                expected_pts += p * pts
            total = sum(pts_p.values())
            for k in pts_p:
                pts_p[k] /= total
            total = sum(bonus_pts_p.values())
            for k in bonus_pts_p:
                bonus_pts_p[k] /= total
            players_by_points[pid] = players_by_points.get(player, 0) + expected_pts
            player_pts_odds.append([pid, pts_p, bonus_pts_p])
    bonus_point_dists = {}
    for _ in range(500):
        player_pts = [
            (int(
                random.choice(
                    list(bonus_pts_p.keys()),
                    p=list(bonus_pts_p.values()),
                )
            ), p)
            for p, pts_p, bonus_pts_p in player_pts_odds
        ]
        player_pts.sort(reverse=True)
        tops = []
        seconds = []
        thirds = []
        if player_pts[0][0] == player_pts[1][0]:
            tops = [player_pts.pop(0)]
            while player_pts[0][0] == tops[0][0]:
                tops.append(player_pts.pop(0))
            thirds = []
            if len(tops) <= 2:
                thirds.append(player_pts.pop(0))
        else:
            tops = [player_pts.pop(0)]
            if player_pts[0][0] == player_pts[1][0]:
                seconds = [player_pts.pop(0)]
                while player_pts[0][0] == seconds[0][0]:
                    seconds.append(player_pts.pop(0))
            else:
                seconds = [player_pts.pop(0)]
                thirds = [player_pts.pop(0)]
                while player_pts[0][0] == thirds[0][0]:
                    thirds.append(player_pts.pop(0))
        for _, pid in tops:
            if pid in bonus_point_dists:
                bonus_point_dists[pid][3] = bonus_point_dists[pid].get(3, 0) + 1
            else: bonus_point_dists[pid] = {3: 1}
        for _, pid in seconds:
            if pid in bonus_point_dists:
                bonus_point_dists[pid][2] = bonus_point_dists[pid].get(2, 0) + 1
            else: bonus_point_dists[pid] = {2: 1}
        for _, pid in thirds:
            if pid in bonus_point_dists:
                bonus_point_dists[pid][1] = bonus_point_dists[pid].get(1, 0) + 1
            else: bonus_point_dists[pid] = {1: 1}
    for pid, bonus_point_dist in bonus_point_dists.items():
        expected_pts = sum(bpts * (p / 500) for bpts, p in bonus_point_dist.items())
        players_by_points[pid] = players_by_points.get(pid, 0) + expected_pts
    players_by_points = [(pts, pid) for pid, pts in players_by_points.items()]
    players_by_points.sort()
    for pts, pid in players_by_points:
        print(pts, PLAYERS_BY_ID[pid])
    print("-----")
