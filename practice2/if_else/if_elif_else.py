# if-elif-else statement examples

# Example 1: Grading system
score = 85
if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
elif score >= 60:
    print("Grade D")
else:
    print("Grade F")

# Example 2: Time greeting
hour = 14
if hour < 12:
    print("Good morning")
elif hour < 18:
    print("Good afternoon")
elif hour < 22:
    print("Good evening")
else:
    print("Good night")

# Example 3: Temperature check
temp = 25
if temp > 30:
    print("Hot weather")
elif temp > 20:
    print("Warm weather")
elif temp > 10:
    print("Cool weather")
else:
    print("Cold weather")

# Example 4: Discount calculation
purchase = 200
if purchase > 500:
    discount = 20
elif purchase > 200:
    discount = 10
elif purchase > 100:
    discount = 5
else:
    discount = 0
print("Discount:", discount, "%")

# Example 5: BMI category
bmi = 22.5
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")