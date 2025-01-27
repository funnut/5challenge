def sprawdz_odleglosc (a, b):
	return abs(a-b)

def komentator (a):
	if a <= 5:
		return "Jestes juz bardzo blisko!"
	elif a <= 10:
		return "Blisko, blisko..."
	elif a <= 20:
		return "Bunkrow nie ma ale niedaleko"
	elif a <= 50:
		return "Kazdy miewa gorsze dni"
	elif a <= 75:
		return "Bardzo, bardzo zimno"
