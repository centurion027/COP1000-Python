import dice_tools

print("Custom Dice Roller\n")

sides = int(input("How many sides should each die have? "))
dice_count = int(input("How many dice would you like to roll? "))

total = 0

# Roll each die and calculate the total
for i in range(dice_count):
    roll = dice_tools.roll_die(sides)
    print(f"Roll {i + 1}: {roll}")
    total += roll

print(f"\nTotal: {total}")