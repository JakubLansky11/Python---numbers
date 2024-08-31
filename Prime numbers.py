# Python - numbers
# Author - Jakub Lánský

# Funkce je_delitelne umí vyhodnotit, zda zadané číslo je dělitelné číslem označeným jako delitel. 
# Musí být zadány oba argumenty v tomto pořadí (číslo, dělitel).
def je_delitelne(cislo, delitel):
    if cislo % delitel == 0:
        return True
    else:
        return False

# Funkce je_prvocislo umí vyhodnotit, zda zadané číslo je prvočíslem. 
def je_prvocislo(cislo):
    if cislo < 2:
        return False
    elif cislo == 2:
        return True
    for i in range(2, cislo - 1):
        if not je_delitelne(cislo, i):
            continue
        else:
            return False
    return True

# Funkce vypis_prvocisla vypíše prvočísla v zadaném intervalu od do a to včetně horního limitu. 
# Musí být zadány oba argumenty v tomto pořadí (spodní limit, horní limit).
prvocisla = []
def vypis_prvocisla(spodni_limit, horni_limit):
    for cislo in range(spodni_limit, horni_limit + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
        else:
            continue
    return prvocisla

print("Ahoj. Tento program ti vypíše prvočísla v zadaném intervalu.")
while True:
    spodni_limit = int(input("Zadej spodní limit intervalu: "))
    horni_limit = int(input("Zadej horní limit intervalu: "))
    vypis_prvocisla(spodni_limit, horni_limit)
    print(prvocisla)
    prvocisla = []
    continue

