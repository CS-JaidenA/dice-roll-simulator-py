import random

def roll2Dice():
	"""
	:returns: The sum of rolling the two dice.
	"""

	roll1: int = random.randint(1, 6)
	roll2: int = random.randint(1, 6)
	
	sum: int = roll1 + roll2
	print(f"{roll1}, {roll2} (sum: {sum})")
	
	return sum

print() # blank line

while True:
	print("Dice Roll Simulator Menu")
	print("1. Roll Dice Once")
	print("2. Roll Dice 5 Times")
	print("3. Roll Dice 'n' times")
	print("4. Roll Dice until Snake Eyes")
	print("5. Exit")

	option: int = int(input("Select an option (1-5): "))
	print() # blank line

	match option:
		case 1:
			roll2Dice()
		case 2:
			for i in range(5):
				roll2Dice()
		case 3:
			n = int(input("How many rolls would you like? "))
			print()
			
			for i in range(n):
				roll2Dice()
		case 4:
			count: int = 0

			while True:
				count += 1

				if roll2Dice() == 2:
					print(f"SNAKE EYES! It took {count} rolls to get snake eyes.")
					break
		case 5:
			break
		case _:
			print("Invalid option. Try again...")
	
	print() # blank line
