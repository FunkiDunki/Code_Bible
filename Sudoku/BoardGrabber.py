import mechanicalsoup
from Sudoku import *

def grabSudoku(id=9706885399, difficulty=4):
	#change the difficulty as needed: {easy: 1, medium: 2, hard:3, evil: 4}
	url = f"https://nine.websudoku.com/?level={difficulty}&set_id={id}"
	browser = mechanicalsoup.Browser()

	page=browser.get(url)

	board = [[0 for i in range(9)] for j in range(9)]

	for row in range(9):
		for col in range(9):
			cell = page.soup.find("input",id=f"f{col}{row}")
			if(cell["class"]==["d0"]):
				board[row][col] = 0
			else:
				board[row][col] = int(cell["value"][0])
	print(board)
	return board

if __name__ == '__main__':
	id = int(input("What is the id number of your puzzle?: "))
	board=grabSudoku(id=id)
	s = Solver(board)
	print("Here is the unsolved puzzle:")
	s.display()
	s.go()
	print("\nHere is the solved version of the puzzle:")
	s.display()
	print("\nHere is the listed version to put into the autohotkey script: ")
	s.display(mode="listed")
