
class Board:
    def __init__(self, rows, cols):
        self.board = [[-1 for i in range(rows)] for j in range(cols)]#fill board with negative ones
        self.order = [(2, -1), (2, 1), (1, 2), (-2, 1), (-1, 2), (-1, -2), (1, -2), (-2, -1)]
        self.rows = len(self.board)
        self.cols = len(self.board[0])

    def display(self):
        print("\n")
        for row in self.board:
            print("\n")
            for col in row:
                print((" " if col < 10 else "") + str(col), end = "  ")
        print("\n")

    def placeKnight(self,row,col,val):
        #return true if board is filled
        if(val == self.rows *self.cols):
            return True

        #if spot full >> return false
        if(row >= self.rows or row < 0 or col >= self.cols or col<0 or self.board[row][col]!= -1):
            return False
        
        #else >> place knight
        self.board[row][col] = val
        
        #check all possible next placements
        for spot in self.order:
            (newR,newC) = spot
            #if they work >> return true
            if(self.placeKnight(newR+row,newC+col,val+1)):
                return True

        #unplace Knight and return false
        self.board[row][col] = -1
        return False
    
    def go(self):
        self.placeKnight(0,0,0)
        self.display()
b=Board(8,8)
b.go()
