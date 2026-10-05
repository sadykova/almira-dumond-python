#Section 1: Variables and Types
name = "Almira"
age = 35
height = 5.4
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

#Section 2: User input and math
user_name = input("What is your name?")
birth_year = int(input ("What is your birth year?"))

print(f"Hi,{user_name}! You are approximately {2026-birth_year} years old.")

#Section 3: Type conversion and f-strings
number1 = float(input("Enter a number:"))
number2 = float(input("Enter a second number:"))

print(f"{number1} x {number2} = {number1 * number2}")

#Section 4: Formatted Receipt
item_name = "Python Cookbook"
item_price = 64.99
quantity = 2
sales_tax = item_price*quantity*.04

print(f'''
=====================================
|                                   |
|               RECEIPT             |
|                                   |
=====================================
Item:          {item_name}
Price:         {item_price}
Quantity:      {quantity}

_____________________________________
Subtotal:      {item_price*quantity:.2f}
Sales tax(4%): {sales_tax:.2f}

Total:         {item_price*quantity+sales_tax:.2f}
''')

#Section 5: Mini-Project — Profile Card

profile_name = input("What is your name?")
hometown = input("What is your hometown?")
hobby = input("What is your hobby?")
fun_fact = input("Tell us one fun fact about yourselve.")
b_year = int(input("What year were you born?"))

print(f'''
=====================================

        PROFILE: {profile_name}
=====================================
Hometown:      {hometown}
Hobby:         {hobby}
Fun fact:      {fun_fact}
Age:           {2026 - b_year}
_____________________________________

''')
