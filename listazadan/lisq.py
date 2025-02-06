# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >
# ostatnio dodane, id, data dodania, status

import sys
import shlex
from datetime import datetime
from random import randrange

def glowna_funkcja(polecenie):
    cmd, arg = polecenie  # Rozpakowanie tuple
    ### ADD
    if cmd == 'add':
        if not arg:
            arg = input("Wpisz notatkę: ").strip()
        if arg:
            write_file(arg)
        return
    ### DELETE
    elif cmd == 'del':
        if not arg:
            arg = input("Wpisz ID: ").strip().lower()
        delete(arg)
        return
    ### SHOW
    elif cmd in ['show', 's']:
        read_file(arg if arg else 'last')
        return
    ### CLEAR SCREEN
    elif cmd in ['cls', 'clear']:
        print("\n" * 50)
        return
    ### HELP
    elif cmd in ['help', 'h']:
        print("\n>> liseq is a free and OpenSource notes app for you <<\n"
              ":: q - quit\n"
              ":: cls - screen cleanup\n"
              ":: show / s - show last 10 notes\n"
              ":: show [N] - show N notes\n"
              ":: show all - show all notes\n"
              ":: del [id] - delete a note\n"
              ":: del l - delete last note\n"
              ":: del all - delete all notes\n")
        return
    ### EXIT
    elif cmd in ['quit', 'q', 'exit']:
        print("Zamknięcie programu.")
        sys.exit()
    ### INVALID COMMAND
    print("### Nieprawidłowe polecenie! ###")

def sprawdz_input(usr_input):
    """Przetwarzanie wejścia od użytkownika na polecenie i argument."""
    if not usr_input:
        return ('add', None)
    elif len(usr_input) == 1:
        return (usr_input[0].lower(), None)
    else:
        return (usr_input[0].lower(), usr_input[1])

def read_file(a):
    """Odczytuje plik i wyświetla notatki."""
    print("\n___id _data _____________________________")
    try:
        with open('dane.txt', 'r', encoding='utf-8') as plik:
            linie = plik.readlines()
            if a == 'all':
                do_wyswietlenia = linie
            elif a == 'last':
                do_wyswietlenia = linie[-10:]
            elif a.isdigit():
                do_wyswietlenia = linie[-int(a):]
            else:
                return print("Niepoprawny parametr!\n")
            for linia in do_wyswietlenia:
                parts = linia.split()
                formatted_date = "/".join(parts[1].split("/")[1:])  # Usunięcie roku
                print(f"{parts[0]} {formatted_date} {' '.join(parts[2:]).strip()}")
            print('')
    except FileNotFoundError:
        print("Plik nie został znaleziony!")

def write_file(a):
    """Dodaje nową notatkę do pliku."""
    try:
        with open('dane.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if lines:
            last_line = lines[-1]
            last_id = int(last_line.split()[0][2:])  # Extract the numeric part of the ID (after 'id')
            id_ = last_id + 1
        else:
            id_ = 1
    except FileNotFoundError:
        id_ = 1
    formatted_id = f"id{str(id_).zfill(3)}"
    data_ = datetime.now().strftime("%Y/%m/%d")
    with open('dane.txt', 'a', encoding='utf-8') as file:
        file.write(f"{formatted_id} {data_} {a}\n")
    print(f'Notatka została dodana: {a}')

def delete(id_str):
    """Usuwa notatki na podstawie podanego ID."""
    with open('dane.txt', "r", encoding="utf-8") as plik:
        linie = plik.readlines()  # Read all lines from the file
        nowe_linie = [linia for linia in linie if id_str not in linia]  # Filter out the lines containing id_str

    numer = len(linie) - len(nowe_linie)  # Calculate how many lines were removed
    if numer > 0:
        yesno = input(f"Czy usunąć {numer} notatki? (y/n): ")
        if yesno.lower() == 'y':
            with open('dane.txt', "w", encoding="utf-8") as plik:
                plik.writelines(nowe_linie)  # Write the remaining lines back to the file
            print(f"Usunięto {numer} notatki zawierające identyfikator {id_str}.")
        else:
            print("Operacja anulowana.")
    else:
        print("Nie znaleziono notatek do usunięcia.")

def pobierz_input():
    """Pobiera polecenie użytkownika w trybie interaktywnym."""
    while True:
        print(":: add / del / show ::")
        usr_input = shlex.split(input(">> ").strip())
        glowna_funkcja(sprawdz_input(usr_input))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Jeśli przekazano argumenty, traktuj je jako notatkę do dodania
        note = " ".join(sys.argv[1:])
        write_file(note)
        sys.exit()  # Program kończy działanie po dodaniu notatki

    print(f"\nWitaj w lisqu!\n{randrange(0,1000)} -> quit -> help")
    pobierz_input()
