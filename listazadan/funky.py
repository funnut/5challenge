### l001 ###
############

def sprawdz_input(usr_input):
	if len(usr_input) == 1:
		polecenie = usr_input[0]
		return polecenie
	elif len(usr_input) == 2:
		polecenie = usr_input[0], usr_input[1]
		return polecenie
	else:
		return False

