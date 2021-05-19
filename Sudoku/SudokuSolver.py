class Solver:
    '''
    Solver( int[][] board ) >> create a new sudoku solver with a given starting state
    Solver.go() >> solve the board, for some reason leaving the last cell unsolved
    Solver.display() >> print the board in a nice fashion
    '''
    def __init__(self, board):
        self.board = board
        self.count = 0
        for i in board:
            for j in i:
                self.count+= (0 if j == 0 else 1)
        #print(self.count)
        self.calls = 0

    
        self.boxes = [[(i//3 + j//3*3, i%3 + 3*j%9) for i in range(9)]for j in range(9)]
    
    def display(self, mode="visual"):
        if mode == "visual":
            print("")
            for row in range(9):
                print("" + ("\n"+("---"*9) if row%3==0 else ""),end="\n")
                for col in range(9):
                    print((" | " if col%3==0 else " ") + str(self.board[row][col]), end = "")
                print(" |",end="")
            print("\n"+("---"*9))
        if mode == "listed":
            output=""
            for row in self.board:
                for cell in row:
                    output+= str(cell)
            print(output)
        print(f"This code took {self.calls} calls to finish!")

    def go(self):
        for i in range(9):
            for j in range(9):
                if(self.board[i][j]==0):
                    for k in range(1,10):
                        print(f"checking pos:{(i,j)}")
                        if(self.solve((i,j), self.count+1,k)):
                           return True
                    return False
        return False
    def solve(self, cor=None, counter=-1, val=1):
        self.calls += 1
        if cor==None:
          return self.go()
        r,c = cor
        
        #check for full solve
        if(counter == 81 and self.checkConflicts(r,c,val)):
            print("counter end")
            self.setValue(r,c,val)
            return True
        #check for conflicts
        if(not self.checkConflicts(r,c, val)):
            return False
        #set value at r, c
        self.setValue(r, c, val)
        #check next positions (9^3 at depth 1 you mongoose **lol jk its not im dumb)
        for i in range(9):
            for j in range(9):
                if((i,j)!= (r,c) and self.board[i][j]==0):
                    for k in range(1,10):
                        if(self.solve((i,j), counter+1,k)):
                           return True
                    self.setValue(r,c,0)
                    return False
        
        #if positions fail, unset value
        self.setValue(r,c,0)
        #return false
        return False
    
    
    def getBox(self,r,c):
        return r//3 * 3 + c//3
    def checkConflicts(self, r, c, val):
        """
        returns true if the given point is valid
        """
        #if the square is not empty, cannot work
        if self.board[r][c] != 0:
            print("this one")
            #return False
        #check column for conflict
        for i in range(len(self.board)):
            if self.board[i][c] == val and i != r:
                return False
        #check row
        for i in range(len(self.board[i])):
            if self.board[r][i] == val and i != c:
                return False
        #check box
        for i in self.boxes[self.getBox(r,c)]:
            if self.board[i[0]][i[1]] == val and i != (r,c):
                return False
        return True

    def setValue(self, r, c, val):
        self.board[r][c] = val

def takePuzzle(mode="fast"):
    if(mode=="slow"):
        output = [[0 for i in range(9)]for j in range(9)]
        for i in range(9):
            for j in range(9):
                intake = input(f"What goes at ({i}, {j})?: ")
                output[i][j] = 0 if intake=="" else int(intake)
        return output
    intake = input("Please input the board starting state: ")
    output = [[0 for i in range(9)]for j in range(9)]
    for i in range(9):
        for j in range(9):
            val = int(intake[0])
            intake = intake[1:]
            output[i][j] = val
    return output


def main():
    board = [[0 for i in range (9)]for j in range(9)]
    '''
    board = [[2,0,5,4,0,0,0,0,0],
         [0,0,0,0,0,0,0,1,0],
         [9,4,0,0,7,1,0,0,0],
         [4,0,9,0,6,0,0,3,7],
         [0,3,0,5,4,2,0,9,0],
         [6,2,0,0,9,0,4,0,8],
         [0,0,0,9,1,0,0,4,2],
         [0,7,0,0,0,0,9,0,0],
         [0,0,0,0,0,4,5,0,1]]
         '''
    board = [[0, 5, 2, 0, 0, 0, 7, 1, 0],
         [0, 1, 8, 6, 5, 0, 0, 4, 0],
         [0, 0, 0, 0, 0, 8, 0, 6, 0],
         [4, 0, 0, 0, 8, 6, 5, 0, 7],
         [0, 0, 6, 0, 7, 0, 2, 0, 0],
         [5, 0, 3, 4, 9, 0, 0, 0, 1],
         [0, 6, 0, 8, 0, 0, 0, 0, 0],
         [0, 4, 0, 0, 6, 3, 1, 2, 0],
         [0, 3, 1, 0, 0, 0, 8, 5, 0]]
    s = Solver(takePuzzle(mode="fast"))
    #s.takePuzzle()
    print(s.go())
    s.display()
    print(s.board)
if __name__ == '__main__':
    main()
    
