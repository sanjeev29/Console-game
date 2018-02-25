import random
from tabulate import tabulate

class ConsoleGame(object):

	def __init__(self):
		self.list_name=[[random.randrange(1,100) for i in range(8)] for y in range(8)]
		self.input_from_user=int(input('Enter one number between 1 and 100: '))
	
	def run(self):
		for rows in self.list_name:
			if self.input_from_user in rows:
				print(tabulate(self.list_name, tablefmt="fancy_grid"))
				print('You lost!:P')
				break
			else:
				print(tabulate(self.list_name, tablefmt="fancy_grid"))				
				print('Yay! You won!:)')
				break
					

#if __name__ == "__main__":
	#game=ConsoleGame()
	#game.run()