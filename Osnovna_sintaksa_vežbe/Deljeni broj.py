delilac = int(input())
granica = int(input())
trenutni_max = 0
konacni_max = 0

for i in range(1, granica + 1):
    if i % delilac == 0:
        trenutni_max = i
        if trenutni_max > konacni_max:
            konacni_max = trenutni_max
print(konacni_max)