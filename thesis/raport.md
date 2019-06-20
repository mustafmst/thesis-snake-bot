# Raport postępu prac (2019-06-20)

## Stan aktualny projektu

W katalogu `geneticAI/geticAlgorithm` znajduje się implementacja genetycznego algorytmu uczącego sieci neuronowe. Na samym początku generowana jest losowa populacja kandydatów (sieci neuronowych o podaje strukturze z losowymi wartościami wag i bias). Potem w pętli powtarzana jest sekwencja operacji na wygenerowanej populacji.

Tymi operacjami są:
- selekcja najlepiej przystosowanych osobników
- losowe krzyżowanie osobników
- poddanie mutacjom nowego pokolenia

## Opis działania poszczególnych operacji na populacji

### Selekcja

Selekcja odbywa się w sposób turniejowy. Z całej populacji losowane są pary kandydatów. Następnie każdy oceniany jest za pomocą funkcji oceny (w tym wypadku jest to gra `snake` [opisana poniżej](#funkcja-oceny)). Kandydat, który zostanie oceniony lepiej w parze przechodzi do następnego kroku a gorszy zostaje odrzucony. W przypadku takich samych wyników o przejściu i odrzuceniu decyduje losowanie.

---

### Krzyżowanie

Genotypem kandydatów jest po prostu zestaw wag więc krzyżowanie odbywa się na zasadzie losowego połączenia tych współczynników z dwóch kandydatów.

Przykładowo jeśli mamy kandydatów o genotypie(celowo uproszczony na potrzeby przykładu):

1. `[ [1,1,1,1] , [1,1,1,1] ]`
2. `[ [2,2,2,2] , [2,2,2,2] ]`

Po przeprowanieniu na nich operacji krzyżowania możemy otrzymać:

1. `[ [1,1,2,2] , [2,1,1,1] ]`
2. `[ [2,2,2,1] , [2,2,1,1] ]`

---

### Mutowanie

W konfiguracji algorytmu podawane jest ile mutacji ma być zaaplikowane do każdego nowego pokolenia. Jeśli współczynnkin ten ustawiony jes na 10 to dzisięć razy zostanie przeprowadzona operacja wylosowania osobnika nowego pokolenia i modyfikacji jednego losowego genu.

Przykładowo osobnik:

1. `[ [2,2,2,1] , [2,2,1,1] ]`

Po mutacji może wyglądać:

2. `[ [2,2,2,1] , [2,2,1,0] ]`

---

## Funkcja oceny

Funkcją oceny w projekcie jest gra `snake` i znajduje się w katalogu o tej samej nazwie. Jest to samodzielna aplikacja napisana w pythonie z wykorzystaniem biblioteki `pygame`. Na wejścjiu w konfiguracji dostaje model sieci neuronoweej stworzony za pomocą bibliotek `tensorflow` i `keras`, który jako wejście otrzymuje zapis stanu gry w formie obrazu planszy a na wyjściu podaje w którą stronę się chce przemieścić głową węża.

Celem gry jest zdobyć jak najwięcej punktów (jeden zjedzony owoc to jeden punkt).

Zasady gry:
- wąż umiera kiedy:
  - wyjdzie poza dostępną planszę
  - wejdzie na swój ogon
  - wykona ilość ruchów równą ilości pól na planszy bez zjedzenia owocu
- wąż może się porzuszać w 4 kierunkach (góra, dół, prawo, lewo) o jedno pole na raz
- gra kończy się wraz ze śmiercią węża i wtedy zwracany jest jego wynik 