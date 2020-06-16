Program z listy 2. wzbogacony o algorytmy: radix, quickSort oraz DualPivot z SELECTem 
(Zad 1 oraz 4)

Przykladowe uruchomienie programu:
        
python3 sort.py --type 'algorytm' --comp 'porzadek'


# --type przyjmuje parametry: insert, merge, quick, dual_pivot, hybrid, radix, select_dual oraz select_quick 

# --comp przyjmuje: '>=' oraz '<='

Mozliwe rowniez uruchomienie w trybie stat:

python3 sort.py --type 'algorytm' --comp 'porzadek' --stat 'nazwa_pliku' 'powtorzenia'

# program tworzy plik o podanej nazwie jezeli taki jeszcze nie istnieje


Struktura statystyk:

n ; swapy ; porownania ; czas ; zuzycie pamieci w [B] 


##### Komentarz #######

Radix dziala szybciej gdy liczby losujemy z mniejszego przedzialu.

Algorytm bada kazda cyfre liczby osobno (10^n), wiec im mniejsze n, 
tym mniej wykonanych instrukcji.


