#5. Банкомат видає суму дрібними, але не більше 10 штук кожної дрібної купюри

amount_to_withdraw = int(input("Enter the amount of money you want to withdraw: ")) #введення бажаної суми КРАТНА 10
available_denominations = [10, 20, 50, 100, 200, 500, 1000]  #доступні номінали 
remaining_amount = amount_to_withdraw    #залишилось видати
max_bills_denomination = 10  #максимальна кількість кожного номіналу

for denomination in available_denominations:
    if remaining_amount >= denomination:
        number_of_notes = remaining_amount // denomination  #кількість купюр = залишилось видати / номінал
        remaining_amount %= denomination   #залишок від залишилось видати / номінал /
        print(f"{number_of_notes} x {denomination} UAH")
        
        #як задати максимальну кількість кожного номіналу?????