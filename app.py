# project 1 : tamrin 1 : f"string"

# name = "Ali"
# age = 20
# city = "Tehran"
# print(f"Hello, my name is {name}.\nI am {age} years old. \nI live in {city}.")

# ____________________________________________________________________________

# project 1 : tamrin 2 : f"string"

# a = 17
# b = 5
# c = a+b
# d = a-b
# e = a*b
# f = a//b
# print(f"17 + 5 = {c} \n17 - 5 = {d} \n17 * 5 = {e} \n17 / 5 = {f}")

# project 1 : tamrin 3 : f"string"

# price = 1234567.89123
# print(f"price: {price} \nprice: {price:,.2f} \nprice: {price:.3f}")

# ____________________________________________________________________________

# project 2 : tamrin 1 : String Methods

# name = "   aLI   "
# print(name.upper())
# print(name.lower())
# print(name.title())

# project 2 : tamrin 2 : String Methods

# text = "i love javascript. javascript is very popular."
# print(text.replace("javascript","python"))

# ____________________________________________________________________________

# project 2 : tamrin 3 : String Methods

# full_name = "   aLI reZAEi   "
# email = "  ALI.REZAEI@GMAIL.COM "
# full_name_strip = full_name.strip()
# email_strip = email.strip()
# print(f"{full_name_strip} \n{email_strip}")
# full_name_title = full_name_strip.title()
# full_name_strip = email_strip.lower()
# print(full_name_strip)
# email_split = email_strip.split('@')
# print(email_split)
# full_name_length = len(full_name_strip)
# print(f"Name length: {full_name_length}")

# ____________________________________________________________________________

# project 3 : tamrin 1 : Numbers

# score1 = 17.5
# score2 = 19
# score3 = 14.75
# score4 = 18.25

# print (score1+score2+score3+score4)
# print(sum([score1,score2,score3,score4]))
# import math
# import statistics
# x = [score1,score2,score3,score4]
# print(statistics.mean(x))
# min = (min(x))
# max = (max(x))
# print(min - max)

# ____________________________________________________________________________

# project 3 : tamrin 2 : Working with Mathematical Operators

# weight = 7.5
# price_per_kg = 12000
# packaging_fee = 15000

# transportation_cost = weight * price_per_kg
# print(transportation_cost)
# final_cost = transportation_cost + packaging_fee
# print(final_cost)

# ____________________________________________________________________________

# project 4 : tamrin 1 : Type Conversion

# product = input("product: ")
# unit_price = input("unit price: ")
# quantity = input("Quantity: ")

# unit_price = float(unit_price)
# quantity = int(quantity)

# total = unit_price * quantity
# print(f"total: {total}$")

# ____________________________________________________________________________

# project 5 : tamrin 1 : Comparison Operators

# price = int(input("price: "))

# print(price > 0)
# print(price <= 100000000)
# print(price > 0 , price <= 100000000)

# ____________________________________________________________________________

# project 6 : tamrin 1 : if / elif / else

# Customer = input("Customer: ")
# Purchase_amount = int(input("Purchase_amount: "))

# if Purchase_amount < 500000:
#     print("Low Purchase")
# elif 500000 <= Purchase_amount < 2000000:
#     print("Average Purchase")
# elif 2000000 <= Purchase_amount < 5000000:
#     print("Good Purchase")
# else:
#     print("Special Purchase")

# ____________________________________________________________________________

# project 6 : tamrin 2 : Ternary Operator

# product_name = "Laptop"
# stock = 5
# Price = 10000000
# Discount = 20000000

# Status = "Available" if stock > 0 else "Out of Stock"

# Discount = "Discount Available" if Discount > 10000000 else "No Discount"

# print(f"product_name: {product_name} \nstock: {stock} \n Status: {Status} \nDiscount: {Discount}")

# ____________________________________________________________________________

# project 6 : tamrin 3 : Logical Operators

# age = int(input("age: "))
# monthly_income = int(input("monthly_income: "))
# credit_score = input("credit_score (True/False): ").upper() == "TRUE"

# if age >= 18 and monthly_income>= 20000000 and credit_score==True:
#     Loan_eligibility = True
# elif age >= 18 and monthly_income >= 50000000 and credit_score == False:
#     Loan_eligibility = True
# else:
#     Loan_eligibility = False


# print(f"age: {age}\nmonthly_income: {monthly_income}\ncredit_score: {credit_score} \nLoan_eligibility: {Loan_eligibility}")

# ____________________________________________________________________________

# project 6 : tamrin 4 : Short-Circuit Evaluation

# username = "admin"
# password = "123456"

# # len(username) >= 1 and len(password) >= 1 and username == "admin" and len(password) >= 6
# # print(len(username) >= 1 and len(password) >= 1 and username == "admin" and len(password) >= 6)
# # print(username != "" and len(password) >= 1 and username == "admin" and len(password) >= 6)

# if len(username) >= 1:
#     print(len(password) >= 1 and username == "admin" and len(password) >= 6)
# else:
#     print("The username field is empty; please enter a value.")
    
# ____________________________________________________________________________

# project 6 : tamrin 5 : Between Condition

# temperature = 100

# if 20 <= temperature <=80:
#     Normal_temperature = True
# elif temperature < 20:
#     Normal_temperature = "Temperature is below the allowable range."
# else:
#     Normal_temperature = "The temperature is above the permitted range."

# print(f"temperature: {temperature} \nNormal_temperature: {Normal_temperature}")

# ____________________________________________________________________________

# project 6 : tamrin 6 : for

# sales = [1200000, 2500000, 1800000, 3000000, 1500000, 4000000, 2200000]
# Dayes = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5", "Day 6", "Day 7"]


# Total_sales = 0
# Days_above_2M = 0

# for number in sales:
#     Total_sales += number
#     Average_sales = Total_sales/2
#     if number >= 2000000:
#         Days_above_2M += 1

# for i in range(len(sales)):
#     print(f"{Dayes[i]}: {sales[i]:,}")


# print(f"Total_sales: {Total_sales} \nAverage_sales: {Average_sales} \nDays_above_2M: {Days_above_2M}")

# ____________________________________________________________________________

# project 6 : tamrin 6 : for-else

# products = ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphone"]

# product_name = input("Enter product name: ").upper()

# for i in products:
#     if product_name == i.upper():
#         print("Product Found")
#         break
# else:
#     print("Product Not Found")    
