customer_name="jhon"
customer_age=35
membership_status="True"
number_of_products_purchased=5
price=[350,400,500,230,150]
names_of_products=('soap','rice','shampoo','rice','ghee')
nam_price={'soap':350,'rice':400,'shampoo':500,'creame':230,'ghee':150}
print('-----customer information-----')
print('cutomer_name:',customer_name,'\n','customer_age:',customer_age,'\n','membership_status:',membership_status)
print('avialable products')
print(nam_price)
print('avarge price')
avarge=sum(price)/len(price)
print(avarge)
print('highest priced')
print(max(price))
print('lowest priced')
print(min(price))



print(nam_price)

total_bill = 0

while True:
    product = input("Enter product name :")

    if product == names_of_products:
        break

    if product in nam_price:
        quantity = int(input("Enter quantity: "))

        price = nam_price[product]
        product_total = price * quantity

        total_bill += product_total



print("Total Bill:", total_bill)


# if:
# total_bill<=500:

# print('discount ')



#q4.
products=names_of_products

# display_products()

