# Analizator tekstu
# Napisz program, który analizuje tekst wprowadzony przez użytkownika, liczy słowa, znaki, zdania, a także wyszukuje najczęściej występujące słowo.
# Operacje na ciągach znaków (str) Praca z modułem collections (np. Counter) Obsługa plików tekstowych

### a001 ###
############

# Witaj w programie do analizy tekstu!
# Czy dane znajdują się  w pliku .txt? [Y/n]
# >>

# Pobierz i przygotuj dane
# Policz litery i znaki
# Policz słowa
# Policz zdania
# Określ najczęściej występujące słowa (maks. 3)

import shlex

txt = 'To jest przykładowy tekst wprowadzony przez użytkownika. Jest on stworzony na potrzeby tworzenia programu do analizy tekstu. Tekst może być wprowadzony bezpośrednio do programu lub pobrany z pliku txt. Słowo tekst występuje tu 4 razy.'

new = txt.split()

print (txt)
print (new)
print (len(new))
for i in new:
      print (len(i), end=', ')
