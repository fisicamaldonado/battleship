from random import randint 

def create_board():
    board=[]
    for j in range(5):
        board.append(["O"]*5)
    return board

board=create_board()

def print_board(board_in):
  for lst in board_in:
    print (" ".join(lst))

print_board(board)

#Hidding our ship
def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#debugger print (use it carefully)
#print(ship_row,ship_col)

#Guessing where is our ship
for turn in range(5):
    print ("Turn ",turn+1)
    guess_row = int(input("Input your Guess Row: "))
    guess_col = int(input("Input your Guess Col: "))

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You hit the ship!")
        break
    else:
        if guess_row not in range(5) or \
        guess_col not in range(5):
            print ("Hey! That's out of board's range.")
        elif board[guess_row][guess_col] == "X":
            print ("You already guessed that!")
        else:
            print ("Sorry, you missed the ship!")
            board[guess_row][guess_col]="X"
    print_board(board)
    if turn == 4:
      print ("Game Over")
      break
    else:
      print ("Try again!)
