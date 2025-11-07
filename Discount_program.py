name = input("Enter Product name ")
price = float(input("Enter Product Price "))

if price >= 10000 :
    discount = 0.20
elif price >= 5000 and price <= 9999 :
    discount = 0.1
else :
    discount = 0.0
discounted_price = price - (price * discount )    
    
print(f"The {name} now costs {discounted_price:.2f} after discount.")    