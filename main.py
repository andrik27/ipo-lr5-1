str = input("Введите строку на русском: ")

glas = "аеёиоуыэюя"
soglas = "бвгджзйклмнпрстфхцчшщ"

noprob = str.replace(" ", "")

glas_count = 0
soglas_count = 0

for char in noprob.lower():
    if char in glas:
        glas_count += 1
    elif char in soglas:
        soglas_count += 1

print("Длина строки без пробелов:", len(noprob))
print("Количество гласных:", glas_count)
print("Количество согласных:", soglas_count)