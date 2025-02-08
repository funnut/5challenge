# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### _lisq_ ###
############## by funnut

import sys
import re # reiteracja id
import shlex
import shutil # szerokość terminalu
import readline # historia poleceń
from datetime import datetime
from random import randrange

notesfilename = '/data/data/com.termux/files/home/notes/notes.txt'

def glowna_funkcja(command):
    cmd, arg = command  # Rozpakowanie tuple
### ADD
    if cmd == 'add':
        if not arg:
            arg = input("Wpisz notatkę: ").strip()
            if not arg:
                print ("Anulowano dodawanie – nie podano treści notatki.")
                return
        if arg:
            write_file(arg)
        return
### DELETE
    elif cmd == 'del':
        if not arg:
            arg = input("Wpisz ID: ").strip().lower()
            if not arg:
                print("Anulowano usuwanie – nie podano ID.")
                return
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
### REITERATE
    elif cmd == 'reiterate()':
        reiterate()
        print ('\nreiterate _done_\n')
        return
### HELP
    elif cmd in ['help', 'h']:
        print("\n>> liseq is a free and OpenSource notes app for you <<\n\n"
            ": quit, q, exit\n"
            ": cls, clear   - clear screen\n"
            ": show, s      - show the last set of notes (default: 10)\n"
            ": show [N]     - show N notes\n"
            ": show [str]   - show notes containing [str]\n"
            ": show all     - show all notes\n"
            ": del [id]     - delete a note containing [id]\n"
            ": del L        - delete the last note\n"
            ": del all      - delete all notes\n"
            ": reiterate()  - function that reiterate iXXX\n")
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
    terminal_width = shutil.get_terminal_size().columns
    print('\n _id _data','::','=' * (terminal_width-14))
    try:
        with open(notesfilename, 'r', encoding='utf-8') as plik:
            linie = plik.readlines()
            if a == 'all':
                do_wyswietlenia = linie
            elif a == 'last':
                do_wyswietlenia = linie[-10:] # sets nr of lines shown by 'show'
            elif a.isdigit():
                do_wyswietlenia = linie[-int(a):]
            else:
                znalezione = [linia for linia in linie if a.lower() in linia.lower()]
                if znalezione:
                    do_wyswietlenia = znalezione
                else:
                    return print("Nie znaleziono pasujących elementów!\n")
            for linia in do_wyswietlenia:
                parts = linia.split()
                formatted_date = "/".join(parts[1].split("/")[1:])  # Usunięcie roku
                print(f"{parts[0]} {formatted_date} {' '.join(parts[2:]).strip()}")
            print(f'\nZnaleziono {len(do_wyswietlenia)} pasujących elementów.')
    except FileNotFoundError:
        print("Plik nie został znaleziony!")

def write_file(a):
    """Dodaje nową notatkę do pliku."""
    try:
        with open(notesfilename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        if lines:
            last_line = lines[-1]
            last_id = int(last_line.split()[0][2:])  # Extract the numeric part of the ID (after 'id')
            id_ = last_id + 1
        else:
            id_ = 1
    except FileNotFoundError:
        id_ = 1
    formatted_id = f"i{str(id_).zfill(3)}"
    data_ = datetime.now().strftime("%Y/%m/%d")
    with open(notesfilename, 'a', encoding='utf-8') as file:
        file.write(f"{formatted_id} {data_} :: {a}\n")
    print('\nNotatka została dodana.')

def delete(arg):
    """Usuwa notatki na podstawie podanego argumentu:
    - 'id' (np. '123') - usuwa notatki zawierające identyfikator,
    - 'l' - usuwa ostatnią notatkę,
    - 'all' - usuwa wszystkie notatki.
    """
    with open(notesfilename, "r", encoding="utf-8") as plik:
        linie = plik.readlines()
    if arg == "all":
        yesno = input("\nCzy na pewno chcesz usunąć wszystkie notatki? (y/n): ")
        if yesno.lower() == 'y':
            open(notesfilename, "w", encoding="utf-8").close()  # Czyścimy plik
            print("\nWszystkie notatki zostały usunięte.")
        else:
            print("\nOperacja anulowana.")
    elif arg == "l":
        if linie:
            yesno = input("\nCzy na pewno chcesz usunąć ostatnią notatkę? (y/n): ")
            if yesno.lower() == 'y':
                with open(notesfilename, "w", encoding="utf-8") as plik:
                    plik.writelines(linie[:-1])  # Zapisujemy plik bez ostatniej linii
                print("\nOstatnia notatka została usunięta.")
            else:
                print("\nOperacja anulowana.")
        else:
            print("\nBrak notatek do usunięcia.")
    else:
        nowe_linie = [linia for linia in linie if arg not in linia]
        numer = len(linie) - len(nowe_linie)

        if numer > 0:
            yesno = input(f"\nCzy usunąć {numer} notatki zawierające identyfikator {arg}? (y/n): ")
            if yesno.lower() == 'y':
                with open(notesfilename, "w", encoding="utf-8") as plik:
                    plik.writelines(nowe_linie)
                reiterate()
                print(f"\nUsunięto {numer} notatki zawierające identyfikator {arg}.")
            else:
                print("\nOperacja anulowana.")
        else:
            print("\nNie znaleziono notatek do usunięcia.")


def reiterate():
    with open(notesfilename, "r", encoding="utf-8") as f:
        linie = f.readlines()

    nowy_numer = 1
    poprawione_linie = []

    for linia in linie:
        # Sprawdzenie, czy linia zaczyna się od iXXX
        dopasowanie = re.match(r"i\d{1,}", linia)
        if dopasowanie:
            nowa_linia = f"i{nowy_numer:03d}{linia[dopasowanie.end():]}"
            nowy_numer += 1
        else:
            nowa_linia = linia  # Zachowaj linię bez zmian

        poprawione_linie.append(nowa_linia)

    # Nadpisanie pliku poprawionymi danymi
    with open(notesfilename, "w", encoding="utf-8") as f:
        f.writelines(poprawione_linie)


def pobierz_input():
    """Pobiera polecenie użytkownika w trybie interaktywnym."""
    while True:
        print("add / del / show")
        usr_input = shlex.split(input(">> ").strip())
        glowna_funkcja(sprawdz_input(usr_input))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        note = " ".join(sys.argv[1:])
        write_file(note)
        sys.exit()


    readline.set_history_length(100)
    print(fr"""
 _ _
| (_)___  __ _
| | / __|/ _` |
| | \__ \ (_| |
|_|_|___/\__, |WELCOME
quit - help |_|{randrange(0,1000)}""")
    pobierz_input()

