import calculations
import messages

messages.show_title()

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print(f"\nSum: {calculations.add(number1, number2)}")
print(f"Difference: {calculations.subtract(number1, number2)}")
print(f"Product: {calculations.multiply(number1, number2)}")
print(f"Quotient: {calculations.divide(number1, number2)}")

messages.show_goodbye()