#return discounted price
def DuckType(price, discount):
    finalPrice = price - (price * (discount / 100))
    return finalPrice
    
