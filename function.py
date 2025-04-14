def calculate_discount(price, discount_percent):
    if (discount_percent >= 0.2):
        if (discount_percent > 1):
            if (discount_percent > 100):
                return print("Discount can not be more than 100%")
            discount_percent = discount_percent/ 100
            if(discount_percent < 0.2):
                return print("Price is: ", price)
        return print(price * discount_percent)
    else:
        return print("Price is: ", price)
    

inputPrice = float(input("Please Enter the Orignal price of the Item: "))
inputDiscount = float(input("Please Enter the "))

calculate_discount(inputPrice, inputDiscount)