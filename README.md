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
Po wywołaniu komendy program sprawdza, czy są jakieś załaczniki. Potem ten załącznik zapisuje w zmiennej i zapisuje załącznik na dysku twardym. Uruchamia funkcję get_class() z modelem keras, labelsami i linkiem do załączonego zdięcia. Funkcja get_class to funkcja w pliku model.py, która wykorzystuje bilitokekę keras (tf-keras) i uprzednio wytrenowany model Teachable Machine, która identyfikuje i zwraca kolor kosza, do którego ma być wrzucony obiekt na zdięciu, jeżeli jego pewność, że ten obiekt powinno się wrzucić do tego kosza jest większa niż 40%. Gdy ten warunek się nie spełni, wtedy wysyła komunikat o nie rozpoznaniu zdięcia. Jeżeli model AI zdięcie rozpoznał, to program porównuje dane swoje z danymi użytkownika. Jeżeli dane się powielają, to program dodaje dane do listy users, w przeciwnym wypadku do listy oszustów.
Dodatkowo, program informuje nas w konsoli, że mamy dużo podejrzanych o oszustwo.
******* 
Zalecana jest zmiana modelu .h5, ponieważ jest to wczesna wersja modelu, która zawiera tylko identyfikację mężczyzn i wprowadzenie rozróżniania AI od prawdziwych.
## Wersja oprogramowania i bibliotek
* Python: 3.11
* discord: 2.3.2
* discord.py: 2.7.1
* google-pasta: 0.2.0
* h5py: 3.14.0
* keras: 3.13.2
* numpy: 2.4.3
* pillow: 12.1.1
* pip: 24.0
* rich: 14.3.3
* tensorflow: 2.21.0
* tf_keras: 2.21.0
