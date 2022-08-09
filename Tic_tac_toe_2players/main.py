position_board=[]
k=0
for i in range(3):
    position_board.append([])
    for j in range(3):
        position_board[i].append(k)
        k+=1
tic_tac_toe_board=[]
for i in range(3):
    tic_tac_toe_board.append([])
    for j in range(3):
        tic_tac_toe_board[i].append("*")
def Display_board(board):
    for i in board:
        for j in i:
            print(j,end=" ")
        print()
    
def check_win(board):
    flag=False
    for i in range(3):
        if (board[0][i]==board[1][i]==board[2][i] != "*") or (board[i][0]==board[i][1]==board[i][2]!="*"):
            flag=True
    if board[0][0]==board[1][1]==board[2][2]!="*" or board[0][2]==board[1][1]==board[2][0]!="*":
        flag=True
    return flag
    
    
def play(board):
    Display_board(position_board)
    n=0
    while n<=8:
        rem=n%2
        while True:
            player_num=input("\n Player %d turn. Choose a number between 0 and 8 inclusive: "%(rem+1))
            try :
                val=int(player_num)
            except ValueError:
                print("Input is not an integer")
                continue
            if val<9:
                r=val%3
                q=val//3
            else:
                print("Invalid input")
                continue
            if board[q][r]=="*":
                break
            else:
                print("Entered place is occupied or invalid input")
        if rem==0:
            board[q][r]="X"
        else:
            board[q][r]="O"
        Display_board(board)
        if check_win(board):
            print("Player %d wins"%(rem+1))
            break
        n+=1
        
play(tic_tac_toe_board)


