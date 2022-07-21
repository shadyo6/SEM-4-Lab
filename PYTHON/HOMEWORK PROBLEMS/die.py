#develop a python program to simulate the rolling of a die

import random

class Die:
	def __init__(self):
		self.value = 1
	
	def roll(self):
		self.value = random.randint(1,7)
		return self.value

class Dice(Die):
	def __init__(self):
		self.dielist = []

	def addDie(die):
		self.dielist.append(die)

	def rollAll():
		for i in range()	
	
def main():

	die1 = Die()
	while True:
		y = input("\nPress y to roll and n to exit: ")
		if(y=='y'):
			print(Die1.roll())
		elif(y=="n"):
			exit()
		else:
			print("\ninvalid input, please try again")

if __name__=='__main__':
	main()