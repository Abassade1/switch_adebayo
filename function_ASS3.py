def food_order (cost):
    food = int(input("What is the cost per pack?"))
    drinks = int(input("what is the cost per bottle?"))
    amount = food + drinks
    if amount >= cost:
        print ("The", amount, "is too expensive buy from Chicken Republic!")
    else:
        print ("Buy from Mr Biggs")

food_order(300)
