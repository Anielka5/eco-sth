text1 = """
Zmiany klimatu
czym one są
Zmiany klimatu to zmiany w pogodzie na kuli ziemskiej, kiedy robi się np.: cieplej, zimniej, wietrzniej. W 21. wieku zmagamy się z globalnym ociepleniem, w większości spowodowany przez ludzi. Zmiana klimatu nie jest problemem przyszłości – dzieje się tu
i teraz i dotyczy każdego regionu świata. Globalne ocieplenie ma katastrofalne znaczenie dla środowiska, m.in. podnoszenie się poziomu mórz i ich zakwaszanie, topnienie powłok lodowych, fale upałów, susze i ekstremalne warunki pogodowe. Ma też także złe 
znaczenie dla człowieka. Może powodować astmę, choroby płuc itd. 
"""
text2 = '''
czy ten problem nas dotyczy?
Lata 2015–2024 były najcieplejszą dekadą w historii, a średnia temperatura na świecie w 2024 r. wyniosła 1,55 °C powyżej poziomu sprzed epoki przemysłowej. Globalne ocieplenie wywołane przez człowieka rośnie obecnie w tempie 0,25 °C na dziesięć lat.
Wzrost o 2 °C w stosunku do temperatury w okresie przedindustrialnym wiąże się z poważnymi negatywnymi skutkami dla środowiska naturalnego oraz zdrowia i dobrostanu ludzi. Między innymi powoduje znacznie większe ryzyko wystąpienia niebezpiecznych i 
potencjalnie katastrofalnych zmian w środowisku globalnym. Z tego powodu społeczność międzynarodowa uznała, że należy utrzymać ocieplenie znacznie poniżej 2 °C i kontynuować działania na rzecz ograniczenia tego wzrostu do 1,5 °C.
'''
text3 = '''
co powoduje zmiany klimatu
- W wyniku spalania węgla, ropy i gazu powstają dwutlenek węgla i podtlenek azotu.
- Wycinanie lasów (wylesianie). Drzewa pomagają regulować klimat poprzez pochłanianie CO2 z atmosfery. Kiedy są one wycinane, zmagazynowany w nich węgiel znów trafia do atmosfery, a to przyczynia się do efektu cieplarnianego.
- Intensywna hodowla zwierząt gospodarskich. Krowy i owce produkują duże ilości metanu podczas trawienia.
- Nawozy azotowe powodują emisje tlenków azotu.
- Fluorowane gazy cieplarniane są emitowane z urządzeń i produktów, które wykorzystują te gazy. Mają one bardzo wysoką wydajność cieplną, aż do 23 tys. razy wyższą niż CO2
Także wpływ mają na to super bogate osoby, np.: milionerzy, miliarderzy, którzy np. latają prywatnymi samolotami.
'''
text4 = """
Smog
smog to nienaturalna mieszanina dymu, spalin i pary wodnej, które jest szkodliwe dla zdrowia.
Te wszystkie powody zmiany klimatu zwiększają ilość smogu, czyli grupy gazów, które ocieplają ziemię. Gazy cieplarniane to:
- dwutlenek węgla (CO2)
- metan
- podtlenek azotu
- fluorowane gazy cieplarniane.
Polska jest na 20 miejscu listy najbardziej skażonych państw świata. Skutki zmian klimatu są nieodwracalne, więc warto dbać o nasze środowisko.
"""
text5 = """
Jak radzić ze smogiem
ty, jako dziecko możesz też coś zmienić. Oto kilka porad, jak stać się bardziej ekologicznym.
• Zamiana starych pieców grzewczych na nowe. Sprawdź, jaki piec masz w domu – porozmawiaj z rodzicami;
• Jeżeli twoi rodzice lub dziadkowie palą śmieciami to wytłumacz im, że szkodzą zdrowiu swojemu i innych;
• Kupowanie węgla dobrej jakości. Sprawdź, jakim węglem ogrzewa się twój dom?
• Wybieraj częściej rower;
• Sprawdzaj jakość powietrza (Wojewódzkie Inspektoraty Ochrony Środowiska);
• Oddychaj przez nos - to nasz naturalny filtr powietrza;
• Spacerując lub jeżdżąc na rowerze unikaj ruchliwych ulic;
• Jeżeli okna twojego mieszkania wychodzą na ulicę, w godzinach szczytu trzymaj je zamknięte;
• Zadbaj o odpowiednią dietę. Pożywienie powinno być bogate w witaminy A, C i E oraz selen;
• Dbaj o rośliny w twoim otoczeniu;
"""
def czym_sa_zmiany_klimatu():
    return text1.strip()
def czy_zmiany_klimatu_nas_dotycza():
    return text2
def co_powoduje_zmiany_klimatu():
    return text3
def smog():
    return text4
def jak_radzic_ze_smogiem():
    return text5