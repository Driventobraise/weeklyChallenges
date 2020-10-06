

def Profit(costPrice,sellPrice,Inventory):
    truePrice = (sellPrice - costPrice)
    totalprofit = (truePrice * Inventory)
    print(totalprofit)

if __name__ == "__main__":
    Profit(2.77, 7.95, 8500)
    
