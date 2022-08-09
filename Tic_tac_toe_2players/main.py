import random
tic_tac_toe_board=[]
for i in range(3):
    tic_tac_toe_board.append([])
    for j in range(3):
        tic_tac_toe_board[i].append("*")
def Display_board(board):
    for i in board:
        print()
        for j in i:
            print(j,end="")
    

def play(board):
    n=0
    while n<=8:
        rem=n%2
        
        player=input("\n Player %d turn. Choose a number between 0 and 8 inclusive: "%(rem+1))
        r=int(player)%3
        q=int(player)//3
        if board[q][r]
        if rem==0:
            board[q][r]="X"
        else:
            board[q][r]="O"
        Display_board(board)
        n+=1
        '''player2=input("\nChoose a number between 0 and 8 inclusive: ")
        r=int(player2)%3
        q=int(player2)//3
        board[q][r]="O"
        Display_board(board)
    '''
    
        
        
play(tic_tac_toe_board)
