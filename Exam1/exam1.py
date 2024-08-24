pizzas = int(0)
salads = int(0)
drinks = int(0)

delivery = int(50)

def price(amount, price):
    return int(amount) * int(price)

def calculate_vat(x):
    return format(x * 0.12, '.2f')

def calc_tot(net, vat, delivery):
    return format(int(net) + float(vat) + int(delivery), '.2f')

print("----------------------")
print("  What food to order  ")
print("----------------------")

persons = int(input("How many persons? "))

if persons != 0:
    for i in range(persons):
        done = False
        pizzas_curr = int(0)
        salads_curr = int(0)
        drinks_curr = int(0)
        while not done:
            print("--------")
            print(f"Person {i+1}")
            print("--------")
            print(f"1. Add/remove pizza ({pizzas_curr} selected)")
            print(f"2. Add/remove salad ({salads_curr} selected)")
            print(f"3. Add/remove drink ({drinks_curr} selected)")
            print(f"4. Finish")
            choice = int(input("Choice: "))
            if choice == 1:
                if pizzas_curr == 1:
                    pizzas_curr -= 1
                else:
                    pizzas_curr = 1
            elif choice == 2:
                if salads_curr == 1:
                    salads_curr -= 1
                else:
                    salads_curr = 1
            elif choice == 3:
                if drinks_curr == 1:
                    drinks_curr -= 1
                else:
                    drinks_curr = 1
            else:
                done = True
        pizzas += pizzas_curr
        salads += salads_curr
        drinks += drinks_curr
        print(drinks)
else:
    print("No order")

total_price = int(price(pizzas, 85) + price(salads, 65) + price(drinks, 20))

if pizzas + salads + drinks < 1:
    print("No order")
else:
    print("------------------------------")
    print("         Your order:")
    print("------------------------------")
    if pizzas > 0:
        print(f"{str(pizzas) + ' pizza(s) x 85 kr: ':<20}{str(price(pizzas, 85)) + '.00 kr':>10}")
    if salads > 0:
        print(f"{str(salads) + ' salad(s) x 65 kr: ':<20}{str(price(salads, 65)) + '.00 kr':>10}")
    if drinks > 0:
        print(f"{str(drinks) + ' drink(s) x 20 kr: ':<20}{str(price(drinks, 20)) + '.00 kr':>10}")
    print("")
    print(f"{'VAT (12%)':<18}{': ':<2}{str(calculate_vat(total_price)) + ' kr':>10}")
    print(f"{'Delivery':<18}{': ':<2}{str(delivery) + '.00 kr':>10}")
    print("")
    print(f"{'Total price':<18}{': ':<2}{str(calc_tot(total_price, calculate_vat(total_price), delivery)) + ' kr':>10}")