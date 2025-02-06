# Lista zadań (To-Do List)
# Stwórz aplikację do zarządzania zadaniami, która pozwala użytkownikowi dodawać, usuwać i wyświetlać zadania.

### l001 ###
############

# Witaj w l001!
# add / del / show
# >
# ostatnio dodane, id, data dodania, status

from random import randrange
from datetime import datetime
import shlex
import funky

id_ = 1 # niech id bedzie zawsze poprzedni nr id + 1 # stworz zmienna ktoa bedzie poprzednie id
data_ = datetime.now().strftime("%Y/%m/%d")

print (f"\nWitaj w lisqu!\n{randrange(0,1000)} <- q <- h")


def glowna_funkcja (polecenie):
			### ADD
	if polecenie == 'add':
		notatka_ = str(input("Wpisz notatke: ").strip())
		if len(notatka_) != 0:
			with open('dane.txt', 'a', encoding='utf-8') as notatki:
				notatki.write(f"{id_} {data_} {notatka_}\n")
				print('_done_\n')
			pobierz_input()
		else:
			pobierz_input()
	elif polecenie[0] == 'add' and polecenie[1]:
		print ("_DONE_\n### notatka zapisana")
		pobierz_input()
			### DELETE
	elif polecenie == 'del':
		DEL_ID = input("Wpisz id: ").strip().lower()
		print ("_DONE_")
		print ("### notatka usunieta")
		pobierz_input()
	elif polecenie[0] == 'del' and polecenie[1]:
		print ("_DONE_\n### notatka usunieta")
		pobierz_input()
			### SHOW
	elif polecenie in ['show', 's']:
		for line in read_data[-5:]:
			print (line, end='')
		pobierz_input()
	elif polecenie[0] in ['show', 's'] and polecenie[1] == 'all':
		read_file()
		pobierz_input()
	elif polecenie in ['show', 's'] and int(polecenie[1]):
		print ("show [a]")
		pobierz_input()
			###
	elif polecenie in ['cls', 'clear']:
		funky.cleanup()
		pobierz_input()
	elif polecenie in ['help', 'h', 'menu', 'info', 'commands']:
		print ("\n©liseq is a free and OpenSource notes app for you\n:: enter q for quit\n:: cls for screen cleanup\n:: show or s <- showing last 10 notes\n:: show [t] <- showing t number of notes\n:: show all <- listing all notes\n:: del 035 <- deliting a specific note\n:: del l <- deliting last note\n:: del all <- deleting all notes")
		pobierz_input()
	elif polecenie in ['hey', 'hi', 'hello', 'welcome','yo']:
		print ("\nNice having you here!\nShall we start?")
		pobierz_input()
	elif polecenie in ['end', 'exit', 'quit', 'q']:
		print ("### program_end ###")
	else:
		print ("### nieprawidlowe_polecenie! ###")
		print ("var ",polecenie)
		pobierz_input()


def pobierz_input():
	print ("add / del / show")
	usr_input = shlex.split(input(">> ").strip().lower())
	glowna_funkcja(funky.sprawdz_input(usr_input))

def read_file():
	with open('/data/data/com.termux/files/home/kod/5challenge/listazadan/dane.txt', 'r', encoding="utf-8") as DANE:
		read_all = DANE.read()
		print (read_all)

pobierz_input()

# id_nr =
# data_nr =
