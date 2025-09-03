def goodMorningMSg():
    username = input("what is your name?")
    print('good morning '+ username)

#goodMorningMSg()

def compoundInterest():
    investAmount = 100
    investAmount *= .05
    moneyGained = investAmount
    print(moneyGained)


#compoundInterest()

def totalCost(itemName, itemPrice):
    tax = 0.10
    totalTax = itemPrice * tax
    totalPrice = totalTax + itemPrice
    print(totalPrice)

totalCost('artic Coat',150)
"Atric coat total is $275.000"  
"Snow boots total is $165.00"
"Googles total is 110.000"

myNumbers = [10,8,3, 28,300,57]

myNumbers.sort()

print(myNumbers)   