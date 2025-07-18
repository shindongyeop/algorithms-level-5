coffee = 10
while True:
    money = int(input("Enter the amount of money you have: "))
    
    if money == 300:
        print("You can buy a coffee!")
        coffee -= 1
    elif money > 300:
        print("You can buy a coffee and have %d change left!" % (money - 300))
        coffee -= 1
    elif money < 300:
        print("You don't have enough money to buy a coffee.")
    else:
        print("Invalid input. No coffee is given.")
        print("Remaining coffee: %d" % coffee)
    if coffee == 0:
        break
    