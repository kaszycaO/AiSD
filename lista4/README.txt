W tym folderze znajduja sie zadanie 1. i 2. z Listy 4

******ZADANIE 1.*********
*************************

Wywolanie:

python3 zad1.py --type [typ] < data/pilk.txt

Dostepne typy:

- bst
- rbt
- hmap

--Przykladowe wywowalanie--


python3 zad1.py --type bst < data/input.txt





WAZNE!!!!!!!

W folderze data, znajduja sie wszystkie pliki wejsciowe i wyjsciowe. Aby uzyc wlasnego pliku wejsciowego
nalezy go umiescic w tym folderze, a w wywolaniu uzyc przekierowania w postaci < data/nazwa_pliku

WAZNE!!!!!!

W programach zostal zastosowany porzadek leksykograficzny wzgledem kodow ASCII.
W przypadku funkcji load tworzona jest nowa struktura!
Usuwanie powoduje usuniecie wszystkich duplikatow danego elementu!


Do zadania pierwszego nalezy takze plik experiments.py. 
Zapisuje on do folderu data, pomiary czasow dzialania poszczegolnych funkcji kazdej ze struktur w postaci:
# n; load; insert; delete; find; max; min; successor; inorder #

Wywolanie:




python3 experiments.py n





n -> liczba powtorzen przy kazdym rozmiarze danych ([100, 1000])


******ZADANIE 2.*********
*************************

Wywolanie:




python3 zad2.py





Program zapisuje do folderu data dane dotyczace badan nad procedura find, w kazdej strukturze.
Pobiera dane z data/experiment.txt (bez powtorzen) oraz z data/with_dupl.txt (z powtorzeniami)
Dane zapisuje w folderze data w plikach bst_limits.txt, hmap_limits.txt, rbt_limits.txt w postaci:
# n, minimum, maximum, random #



Opracowanie danych zostanie wyslane na maila, a same wykresy znajduja sie w folderze data w pliku wykresy.pdf

