### Jak wymnozyc wszystkie liczby zbioru?
### [ a * b * c ... ]

# range (len())

#liczby = [10, 2, 2, 3]
#n = 0

#print ("zbior to: ", liczby)
#print (liczby[0] * liczby[1] * liczby[2] * liczby[3])


result = 1  # Inicjalizacja zmiennej
numbers = [2, 3, 4, 5]

for num in numbers:
    result *= num  # To samo co: result = result * num

print(result)  # Wynik: 120
