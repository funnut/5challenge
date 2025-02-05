from datetime import datetime

id_ = 1 # niech id bedzie zawsze poprzedni nr id + 1 # stworz zmienna ktoa bedzie poprzednie id
data_ = datetime.now().strftime("%Y-%m-%d")
notatka = "To jest przykładowa notatka."

with open("notatki.txt", "a", encoding="utf-8") as plik:
    plik.write(f"{id_} {data_} {notatka}\n")
