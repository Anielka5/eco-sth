# eco-sth
## spis treści:
* krótko o programie
* instrukcja dla użytkownika
* co ten program robi od strony backendu i proponowane zmiany
* wersja oprogramowania, biblioteki i ich wersje, materiały 
## krótko o programie
Ten program zawiera quizy, ciekawostki, rozpoznawanie śmieci (testy) i krótkie teksty o zanieczyszceniach powietrza.
## Instrukcja Użytkownika
1. Wejdź na serwer https://discord.com/channels/1421408649506590842/1421408650215297108,
2. Sprawdź, czy bot Goniec jest aktywny,
3. Jeżeli bot jest aktywny, wpisz komendę >pomoc, aby wyświetlić dalsze instrukcje
> Jeżeli bot nic nie wypisze lub powtórzy komendę, to jest uruchomiony właśnie inny kod.
## backend programu i zalecane zmiany
### ciekawostki
Gdy wywołujemy komendę trivies (po polsku ciekawostki) oraz po podaniu argumentu ilości ciekawostek dalej nazwyamy how_much w tej samej wiadomości (jeśli argument nie będzie uwzględniony w komendzie, to w konsoli wyrzuci błąd) program sprawdza, czy potrafi przekonwertować argument how_much do typu int, a jeżeli nie, to wysyła komunikat o tym. Jeżeli będzie mógł przekonwertować do typu integer (int) to uruchamia funkcję ciekawostki(itreacions), a w tym przypadku iteracions jest how_much. Funkcja ta służy do losowania tylu ciekawostek, ile było określonych w how_much.
### edukacja (krótkie teksty)
Gdy wywołujemy komendę edukacja, to bot Discord wyświetla nam akapit tekstu o zanieczyszczeniach powietrza i pyta o zgode na kontunuacje. Jeżeli użytkownik odpowie >tak, to bot kontynuuje i proces się powtarza aż do końca artykułu
### obliczanie kWh (kilo wato godzin) dla domów
Podzczas wpisywania na czacie serwera komendy home_emmis musimy wprowadzić jeszcze 3 argumenty: metraż domu w m2, ilość żarówek i ilość urządzeń korzystających z prądu wtej samej wiadomości. Potem program sprawdza, czy potrafi przekonwertować argumenty do typu int, a jeżeli nie, to wysyła komunikat o tym. Jeżeli będzie mógł przekonwertować do typu integer (int) to uruchamia sekwencje komend calcu., których wynikiem jest wynik roczne zużycie prądu w kWh. Program mówi jak dobra lub zła jest twoja efektywność energetyczna.
### quiz
Quiz składa się z 20 pytań, na każde z nich jest odpowiedź A lub B lub C lub D. Uwaga: Na jedno pytanie może być kilka odpowiedzi, wtedy wpisujemy tylko jedną.
### rozpoznawanie śmieci
(todo)
Po wywołaniu komendy program sprawdza, czy są jakieś załaczniki. Potem ten załącznik zapisuje w zmiennej i zapisuje załącznik na dysku twardym. Uruchamia funkcję get_class() z modelem keras, labelsami i linkiem do załączonego zdięcia. Funkcja get_class to funkcja w pliku model.py, która wykorzystuje bilitokekę keras (tf-keras) i uprzednio wytrenowany model Teachable Machine, która identyfikuje i zwraca kolor kosza, do którego ma być wrzucony obiekt na zdjęciu, jeżeli jego pewność, że ten obiekt powinno się wrzucić do tego kosza jest większa niż 40%. Gdy ten warunek się nie spełni, wtedy wysyła komunikat o nie rozpoznaniu zdjęcia. Jeżeli model AI zdięcie rozpoznał, to program daje nam informacje gdzie mamy wrzucić dany śmieć ze zdjęcua zdjęcie.
******* 
Zalecana jest zmiana modelu .h5, ponieważ ta wersja modelu, nie zawiera odpadów bio, ubrań
## Wersja oprogramowania i bibliotek
* Python             3.11
* absl-py            2.4.0
* aiohappyeyeballs   2.6.1
* aiohttp            3.13.5
* aiosignal          1.4.0
* astrunparse        1.6.3
* attrs              26.1.0
* certifi            2026.4.22
* charset-normalizer 3.4.7
* discord            2.3.2
* discord.py         2.7.1
* flatbuffers        25.12.19
* frozenlist         1.8.0
* gast               0.7.0
* google-pasta       0.2.0
* grypcio            1.80.0
* h5py               3.14.0
* idna               3.13
* keras              3.14.0
* libclang           18.1.1
* markdown-it-py     4.0.0
* mdurl              0.1.2
* ml_dtypes          0.5.4
* multidict          6.7.1
* namex              0.1.0
* numpy              2.4.4
* opt_einsum         3.4.0
* optree             0.19.0
* packaging          26.2
* pillow             12.2.0
* pip                24.0
* propcache          0.4.1
* protobuf           7.34.1
* Pygments           2.20.0
* requests           2.33.1
* rich               15.0.0
* setuptools         65.5.0
* six                1.17.0
* tensorflow         2.21.0
* termcolor          3.3.0
* tf_keras           2.21.0
* typing_extensions  4.15.0
* urllib3            2.6.3
* wheel              0.47.0
* wrapt              2.1.2
* yarl               1.23.0
