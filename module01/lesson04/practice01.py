#Вам известен номер квартиры, этажность дома и количество квартир на этаже. Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.

apartment = int(input("Enter apartment number: "))

entrance = str((apartment - 1) // 20 + 1)
print("The apartment is in the " + entrance + "th entrance")

floor = str((apartment - 1) % 20 // 4 + 1)
print("The apartment is on the " + floor + "th floor")