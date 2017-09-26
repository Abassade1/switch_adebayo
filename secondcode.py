print ("===welcome to my second program===")
print ()
age = input("Whats your age?")
balance = int(input("whats your account balance:"))
name = input ("whats your name?")
print()
max_allow_bal = 1000

if balance > max_allow_bal:
    print ("Hey", name, "at this", age , "you need to invest more")
else:
    print("Thank you for contacting us")


