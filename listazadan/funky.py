### l001 ###
############

def sprawdz_input(usr_input):
	if len(usr_input) == 1:
		polecenie = usr_input[0].lower()
		return polecenie
	elif len(usr_input) == 2:
		polecenie = usr_input[0].lower(), usr_input[1]
		return polecenie
	elif len(usr_input) == 0:
		return 'add'
	else:
		polecenie = 'max_two_items_array'
		return polecenie

def cleanup():
	print ("\n\n\n"*15)

