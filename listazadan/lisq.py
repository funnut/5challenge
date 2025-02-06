# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >
# ostatnio dodane, id, data dodania, status

from datetime import datetime
from random import randrange
import shlex
import funky


print (f"\nWitaj w lisqu!\n{randrange(0,1000)} -> quit -> help")


def glowna_funkcja (polecenie):
			### ADD
	if polecenie == 'add':
		notatka = str(input("Wpisz notatke: "))
		if len(notatka) != 0:
			write_file(notatka)
		else:
			pobierz_input()
	elif polecenie[0] == 'add' and polecenie[1]:
		write_file(polecenie[1])
			### DELETE
	elif polecenie == 'del':
		id_str = input("Wpisz id: ").strip().lower()
		delete(id_str)
		pobierz_input()
	elif polecenie[0] == 'del' and polecenie[1]:
		delete(polecenie[1])
		pobierz_input()
			### SHOW
	elif polecenie in ['show', 's']:
		read_file('last')
	elif polecenie[0] in ['show', 's'] and polecenie[1] == 'all':
		read_file('all')
	elif polecenie[0] in ['show', 's'] and polecenie[1].isdigit():
		read_file(polecenie[1])
			###
	elif polecenie in ['cls', 'clear']:
		funky.cleanup()
		pobierz_input()
	elif polecenie in ['help', 'h']:
		print ("\n>> liseq is a free and OpenSource notes app for you <<\n:: enter q for quit\n:: cls for screen cleanup\n:: show or s <- showing last 10 notes\n:: show [N] <- showing N number of notes\n:: show all <- listing all notes\n:: del 035 <- deliting a specific note\n:: del l <- deliting last note\n:: del all <- deleting all notes\n")
		pobierz_input()
	elif polecenie in ['hey', 'hi', 'hello', 'welcome','yo']:
		print ("\nNice having you here!\nShall we start?")
		pobierz_input()
	elif polecenie in ['quit', 'q', 'exit']:
		print ("### program_end ###")
	else:
		print ("### nieprawidlowe_polecenie! ###")
		print ("var ",polecenie)
		pobierz_input()


def pobierz_input():
	print ("add / del / show")
	usr_input = shlex.split(input(">> ").strip())
	glowna_funkcja(funky.sprawdz_input(usr_input))

def read_file(a):
	print ("\n___id ______data")
	with open('/data/data/com.termux/files/home/kod/5challenge/listazadan/dane.txt', 'r', encoding="utf-8") as plik:
		if a=='all':
			read_all = plik.read()
			print (read_all)
		elif a=='last':
			ostatnie = plik.readlines()
			for i in ostatnie[-10:]:
				print (i.strip())
			print('')
		elif a.isdigit():
			N = int(a)
			for i in (plik.readlines() [-N:]):
				print (i.strip())
			print('')
	pobierz_input()

def write_file(a):
	id_ = 1 # niech id bedzie zawsze poprzedni nr id + 1 # stworz zmienna ktoa bedzie poprzednie id
	data_ = datetime.now().strftime("%Y/%m/%d")
	with open('dane.txt', 'a', encoding='utf-8') as file:
		file.write(f"{id_} {data_} | {a}\n")
		print('_done_\n### notatka zapisana')
	pobierz_input()


def delete(id_str):
	with open('dane.txt', "r", encoding="utf-8") as plik:
		linie = plik.readlines()  # Read all lines from the file
		nowe_linie = [linia for linia in linie if id_str not in linia]  # Filter out the lines containing id_str

	numer = len(linie) - len(nowe_linie)  # Calculate how many lines were removed
	if numer > 0:
		yesno = input(f"Czy usunąć {numer} notatki? (y/n): ")
		if yesno == 'y':
			with open('dane.txt', "w", encoding="utf-8") as plik:
				plik.writelines(nowe_linie)  # Write the remaining lines back to the file
			print(f"Usunięto {numer} notatki zawierające identyfikator {id_str}.")
		else:
			print("Operacja anulowana.")
	else:
		print("Nie znaleziono notatek do usunięcia.")

pobierz_input()
