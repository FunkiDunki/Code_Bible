#include <iostream>
int board[8][8];
bool place(int row, int col, int val, int board[8][8])
{
    if(val == 64)
    {
        return true;
    }
    
    if(row<0 || col<0 || row>=8 || col>=8 || board[row][col] != -1)
    {
        return false;
    }
    //(2, -1), (2, 1), (1, 2), (-2, 1), (-1, 2), (-1, -2), (1, -2), (-2, -1)
    board[row][col] = val;
    if(place(row+2,col-1,val+1, board)){return true;}
    if(place(row+2,col+1,val+1, board)){return true;}
    if(place(row+1,col+2,val+1, board)){return true;}
    if(place(row-2,col+1,val+1, board)){return true;}
    if(place(row-1,col+2,val+1, board)){return true;}
    if(place(row-1,col-2,val+1, board)){return true;}
    if(place(row+1,col-2,val+1, board)){return true;}
    if(place(row-2,col-1,val+1, board)){return true;}
    board[row][col] = -1;
    return false;
    
}

void print(int param[8][8])
{
    for(int i = 0; i < 8; i++)
    {
        std::cout << "\n";
        for(int j = 0; j < 8; j++)
        {
            std::cout << " " << ((param[i][j]<10)?"0":"") << param[i][j];
        }
    }
}

int main() {
    // Write C++ code here
    std::cout << "Knight's Journey:";
    int i,j;
    for(i=0; i < 8; i++)
    {
        for(j=0; j < 8; j++)
        {
            board[i][j] = -1;
        }
    }
    place(0,0,0,board);
    print(board);
    return 0;
}
