import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

lista = ["Zanieczyszczenie powietrza jest odpowiedzialne za około 7 milionów zgonów rocznie na całym świecie",
"Smog to mieszanka dymu i mgły, która powstaje głównie w wyniku spalania węgla i innych paliw kopalnych.",
"Zanieczyszczenie wody dotyka około 2 miliardów ludzi, którzy nie mają dostępu do czystej wody pitnej.",
"Plastik w oceanach stanowi poważne zagrożenie dla życia morskiego. Szacuje się, że do 2050 roku w oceanach będzie więcej plastiku niż ryb.",
"Kwaśne deszcze powstają w wyniku emisji dwutlenku siarki i tlenków azotu do atmosfery. Mogą one niszczyć lasy, jeziora oraz budynki.",
"Astma jest jedną z najczęstszych chorób wywoływanych przez zanieczyszczenie powietrza.",
"Choroby serca i układu krążenia są często związane z długotrwałym narażeniem na zanieczyszczenia powietrza.",
"Rak płuc może być wywołany przez długotrwałe wdychanie zanieczyszczonego powietrza, zwłaszcza w miastach o wysokim poziomie smogu.",
"Zanieczyszczenie wody może prowadzić do chorób przewodu pokarmowego, takich jak biegunka, która jest szczególnie niebezpieczna dla dzieci.",
"Hałas to również forma zanieczyszczenia, która może prowadzić do problemów ze snem, stresu oraz problemów z koncentracją.",
"Spalanie paliw kopalnych jest głównym źródłem zanieczyszczenia powietrza. Emituje ono duże ilości dwutlenku węgla, tlenków azotu oraz innych szkodliwych substancji.",
"Przemysł wytwarza ogromne ilości odpadów, które często trafiają do rzek, jezior oraz oceanów.",
"Rolnictwo również przyczynia się do zanieczyszczenia, głównie poprzez stosowanie pestycydów i nawozów sztucznych, które mogą zanieczyszczać gleby i wody gruntowe.",
"Transport jest odpowiedzialny za znaczną część emisji zanieczyszczeń powietrza, zwłaszcza w dużych miastach.",
"Odpady komunalne często trafiają na wysypiska, gdzie mogą wydzielać metan, gaz cieplarniany, który przyczynia się do globalnego ocieplenia.",
"Dwutlenek węgla jest głównym gazem cieplarnianym, który przyczynia się do globalnego ocieplenia.",
"Metan jest znacznie bardziej efektywnym gazem cieplarnianym niż dwutlenek węgla, choć jest go mniej w atmosferze.",
"Topnienie lodowców jest jednym z efektów globalnego ocieplenia, które jest napędzane przez zanieczyszczenie powietrza.",
"Ekstremalne zjawiska pogodowe, takie jak huragany, powodzie i susze, stają się coraz częstsze i bardziej intensywne z powodu zmian klimatycznych.",
"Podnoszenie się poziomu mórz zagraża milionom ludzi mieszkających w nisko położonych obszarach przybrzeżnych.",
"Recykling pomaga zmniejszyć ilość odpadów trafiających na wysypiska oraz zmniejsza zapotrzebowanie na surowce naturalne.",
"Oszczędzanie energii poprzez wyłączanie niepotrzebnych urządzeń elektrycznych oraz korzystanie z energooszczędnych żarówek może zmniejszyć emisję zanieczyszczeń.",
"Korzystanie z transportu publicznego zamiast samochodów osobowych może znacznie zmniejszyć emisję spalin.",
"Sadzenie drzew pomaga w absorpcji dwutlenku węgla oraz poprawia jakość powietrza.",
"Unikanie plastiku jednorazowego użytku może zmniejszyć ilość odpadów trafiających do oceanów.",
"Programy edukacyjne w szkołach mogą pomóc dzieciom zrozumieć znaczenie ochrony środowiska.",
"Kampanie społeczne mogą zachęcać ludzi do podejmowania działań na rzecz zmniejszenia zanieczyszczenia.",
"Współpraca międzynarodowa jest niezbędna do skutecznej walki z globalnym problemem zanieczyszczenia.",
"Badania naukowe pomagają w opracowywaniu nowych technologii i metod, które mogą zmniejszyć zanieczyszczenie i jego skutki.",
"w ciągu każdej sekundy na świecie wyrzucanych jest 50 ton śmieci",
"ustawione w szeregu ciężarówki wywożące rocznie 2,12 miliardów ton śmieci na wysypiska,  24 razy opasałyby kulę ziemską",
"przeciętny Polak marnuje 235 kg żywności w ciągu roku",
"42% Polaków zdarza się wyrzucać żywność",
"metan wytwarzany podczas rozkładu odpadów na wysypiskach stanowi 3-4 procenty rocznej emisji gazów cieplarnianych",
"metan pochłania promieniowanie podczerwone 60 razie bardziej niż dwutlenek węgla, który powszechnie uważa się za przyczynę „efektu cieplarnianego”",
"do produkcji 1 tony papieru potrzeba ściąć około 17 drzew, które w ciągu roku produkują tlen dla 170 osób",
"recykling makulatury to 65 procent oszczędność energii oraz 35 procent oszczędności wody w stosunku do procesów produkcji papieru z pierwotnych włókien celulozowych",
"od początku produkcji przemysłowej tworzyw sztucznych wytworzono ich ok. 10 miliardów ton, jedynie 9% zostało poddane recyklingowi"<
"recykling 1 kg aluminium to oszczędność do 6 kg boksytu oraz do 14 kWh energii elektrycznej",
"zużyte opakowania szklane można w nieskończoność przetapiać na nowe bez pogorszenia ich jakości, oszczędzając przy tym energię i chroniąc środowisko",
"każdego roku na świecie od 5 do 13 mln ton tworzyw sztucznych, czyli od 1,5 do 4 % produkowanych plastików trafia do mórz i oceanów",
"co 25 minut na naszej planecie ginie jeden gatunek zwierząt",
"co roku liczba owadów na świecie malej o 2,5%",
"w ciągu minuty na świecie znika las o powierzchni równej 36 boiskom do piłki nożnej",
"każdy z mieszkańców Polski zużywa około 150 litrów wody",
"na świecie zużywanych jest łącznie około 22 trylionów kWh energii rocznie, z czego około ¼ przeznacza się na oświetlenie",
"1 litr zużytego oleju silnikowego może zanieczyścić 1 mln litrów wody",
"2/3 mieszkańców miast na świecie oddycha powietrzem zawierającym smog",
"wokół Ziemi krąży około 19 tysięcy odpadów o wielkości do 10 cm i miliony mniejszej wielkości",
"75 procent zgonów następuje przedwcześnie wskutek zatrucia środowiska oraz niewłaściwego trybu życia.",
"Wielka Plama Pacyficzna z odpadów plastiku zajmuje powierzchnię 1,6 mln km²",
"butelka PET rozkłada się w środowisku 1000 lat, szkło – 4000 lat, reklamówka – 400 lat, puszka aluminiowa – 150 lat, guma do żucia – 5 lat",
"Rzucona w lesie butelka plastikowa rozłoży się w ziemi po 500 latach, guma do żucia po 5 latach, a niedopałki papierosów po 2 latach.",
"Jeden hektar lasu liściastego może wyprodukować około 700 kg tlenu, co stanowi dobowe zapotrzebowanie ponad 2500 ludzi.",
"W Polsce pracuje dziś 290 profesjonalnych elektrowni wiatrowych o łącznej mocy 10MW, podłączonych do sieci i sprzedających energię zakładom energetycznym. Razem produkują zaledwie 3% energii elektrycznej.",
"Aby zmniejszyć emisję dwutlenku węgla do atmosfery i zgładzić efekt cieplarniany, australijscy naukowcy zaproponowali metodę zakopywania dwutlenku węgla w stanie półpłynnym pod ziemią.",
"Według danych Najwyższej Izby Kontroli aż 86% polskich zakładów nie ma urządzeń do redukcji zanieczyszczeń gazowych. A wojewódzkie fundusze ochrony środowiska kupują papiery wartościowe, zamiast wspierać wszelkie przedsięwzięcia proekologiczne.",
"Jeden nieszczelny, lekko kapiący kran powoduje, że w ciągu doby wycieka około 36 litrów wody. Nieszczelna spłuczka w WC powoduje wyciek w ciągu dnia około 720 litrów wody, a rocznie - 260m sześciennych wody.",
"Aby wyprodukować jedną tonę papieru trzeba ściąć średnio 17 drzew.",
'Jeżeli każdy z nas wyrzuci na śmietnik tylko jeden słoik to na wysypisko w całej Polsce trafi rocznie 10 000t szkła.',
'W Polsce rocznie zużywa się 400 milionów aluminiowych puszek, które można powtórnie przetworzyć oraz wykorzystać i to nieskończenie wiele razy. Sześć puszek ze złomu to oszczędność energii równej spaleniu jednego litra paliwa.',
"W Polsce tylko 222 tysiące ton odpadów komunalnych jest kompostowanych (2%). Dla porównania w Danii, Szwajcarii, Szwecji od 60%-80%.",
"Każda szklana butelka ponownie wprowadzona do obiegu pozwala zaoszczędzić energię potrzebną do świecenia 100 watowej żarówki przez 4h.",
"Około 360mln kilometrów kwadratowych powierzchni Ziemi zajmują morza i oceany. Niestety człowiek wykorzystuje je często jak wysypisko śmieci, niszcząc ogromną część zamieszkujących je roślin i zwierząt.",
"Z osady niedaleko Niagary wysiedlono wszystkich (ok. 1000) mieszkańców, kiedy okazało się, że ich domy zostały wybudowane na starym od lat nieużywanym składowisku toksycznych odpadów. Wcześniej w tej okolicy odnotowano niepokojący wzrost zachorowań na raka i większy od przeciętnego odsetek dzieci z wadami wrodzonymi.",
"Metan który powstaje w przewodach pokarmowych bydła i innych zwierząt domowych dostaje się do atmosfery i przyczynia się do wzrostu temperatury naszej planety.",
"Według danych ONZ z 1988 roku aż 2/3 mieszkańców miast na świecie oddycha powietrzem zawierającym smog.",
"Ocieplenie klimatu może spowodować, że w 2050 roku tereny wokół wybrzeży Wielkiej Brytanii znajdą się pod wodą",
"Butelki, torebki śniadaniowe bądź torby na zakupy stanowią ok. 7% masy wszystkich śmieci, ale zajmują dużo miejsca, niemal 30% wszystkich odpadów.",
"Anglicy wyliczyli, że wyrzucane w ciągu roku butelki z politereftalanu etylu (PET), ustawione jedna na drugiej utworzyły by wieżę o wysokości 28mln km, co stanowi 73-krotną odległość Ziemi od Księżyca.",
"Jeden litr zużytego oleju silnikowego wylany do rzeki lub kanalizacji jest w stanie zanieczyścić 1 milion litrów wody!!!",
'Metan, który się uwalnia z wysypisk śmieci jest 27 razy bardziej agresywny od dwutlenku węgla.',
'W 1960 roku na polskie pola wylano 40 000 ton DDT. DDT wykrył Hans Miller i za to dostał nagrodę Nobla.',
'Aby Polska zrealizowała obowiązek odzysku w 2009 roku, trzeba było zebrać ok. 48kg odpadów opakowaniowych na osobę.',
'Aby Polska w 2009 roku mogła zrealizować obowiązek recyklingu szkła, każdy z nas powinien był zebrać 12.1kg tego surowca, czyli około 41 średniej wielkości słoików.',
'W Polsce poziom selektywnego odzyskiwania odpadów wynosi jedynie 4 kg na mieszkańca, podczas gdy w Czechach jest to 19 kg, natomiast w Niemczech 76 kg na mieszkańca!',
'Obecnie w Polsce wytwarzamy ok. 13.5mln ton odpadów komunalnych rocznie, co daje średnio daje 350kg na mieszkańca rocznie.',
'W składowiskach znajdują się 2mld ton odpadów przemysłowych i 4mln ton odpadów komunalnych.',
'Codziennie każde duże miasto w Polsce wysyła na składowisko 100 ciężarówek z odpadami.',
'W Polsce tylko 222 tysiące ton odpadów komunalnych jest kompostowanych (2 %). Dla porównania w Danii, Szwajcarii i Szwecji od 60-80 % .',
'Każdy z nas wyrzuca w ciągu roku około 56 opakowań szklanych nadających się w pełni do ponownego wykorzystania .',
'Produkty ze szkła w 100% nadają się do ponownego przerobu (recyklingu).',
'Wyprodukowanie 6 puszek ze złomu aluminiowego daje oszczędność energii równoważną energii uzyskanej ze spalenia 1 litra benzyny.',
'Ponowny przerób stosu gazet o wysokości 125cm pozwala na uratowanie sześciometrowej sosny. Wyprodukowanie 1 tony papieru wymaga ścięcia 17 drzew.',
'Każda tona odzyskanej makulatury pozwoli zaoszczędzić 1200l wody w papierni oraz 2.5m3 przestrzeni środowiska.',
'Każde 100kg papieru to średniej wielkości dwa drzewa, przy czym należy wiedzieć, że jedno drzewo produkuje w ciągu roku tlen wystarczający dla 10 osób.',
'Około 2mln ptaków i ssaków wodnych ginie na świecie na skutek połknięcia plastikowych odpadów wrzucanych do mórz i oceanów.',
'Ilość nagromadzonych odpadów zwiększyła się trzykrotnie przez ostatnie 20 lat. Zajmowana przez te odpady powierzchnia zwiększyła się dwukrotnie.']

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def ciekawostka(ctx, how_much:int):
    for i in range(how_much):
        losowanie = random.choice(lista)
        await ctx.send(losowanie)

bot.run("token")
