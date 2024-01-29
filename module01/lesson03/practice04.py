#4. Банкомат видає суму максимально можливими купюрами

amount_to_withdraw = int(input("Enter the amount of money you want to withdraw: ")) #введення бажаної суми КРАТНА 10
available_denominations = [1000, 500, 200, 100, 50, 20, 10]  #доступні номінали 
remaining_amount = amount_to_withdraw    #залишилось видати

for denomination in available_denominations:
    if remaining_amount >= denomination:
        number_of_notes = remaining_amount // denomination  #кількість купюр = залишилось видати / номінал
        remaining_amount %= denomination   #залишок від залишилось видати / номінал /
        print(f"{number_of_notes} x {denomination} UAH")
        