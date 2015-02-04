from random import randint
print "\nLet's play 2-player Battleship!\n"
numWins1=0
numWins2=0
numGames=0
numRounds=0
startPlayer=2
player1=""
player2=""

player1=str(raw_input("Name of Player1: "))
player2=str(raw_input("Name of Player2: "))
while True:
    numRounds = int(raw_input("How many rounds do you want to play: "))
    if numRounds<=0:
        print "Please enter a number greater than 0!"
    else:
        break

for r in range(numRounds):
    print "\nRound%s Starts!" % (int(r)+1)
    startPlayer=1 if startPlayer==2 else 2
    while True:
        sideLen = int(raw_input("Please enter grid size(number of rows/cols): "))
        if sideLen<=0:
            print "The number of rows must be greater than 0!"
        else:
            board = []
            for x in range(sideLen):
                board.append(["O"] * sideLen)

            def print_board(board):
                for row in board:
                    print " ".join(row)

            
            print_board(board)

            def random_row(board):
                return randint(0, len(board) - 1)

            def random_col(board):
                return randint(0, len(board[0]) - 1)

            ship_row = random_row(board)
            ship_col = random_col(board)


            # Everything from here on should go in your for loop!
            # Be sure to indent four spaces!
            curPlayer=startPlayer;
            while True:
                guess_row = int(raw_input("%s guess row: " % player1)) if curPlayer==1 else int(raw_input("%s guess row: " % player2))
                guess_col = int(raw_input("%s guess col: " % player1)) if curPlayer==1 else int(raw_input("%s guess col: " % player2))
                
                if guess_row == ship_row and guess_col == ship_col:
                    print "Congratulations %s! You sunk my battleship!" % player1 if curPlayer==1 else "Congratulations %s! You sunk my battleship!" % player2
                    if curPlayer==1:
                        numWins1+=1
                    else:
                        numWins2+=1
                    numGames+=1
                    break
                elif (guess_row < 0 or guess_row > len(board)-1) or (guess_col < 0 or guess_col > len(board[0])-1):
                        print "Oops, that's not even in the ocean."
                elif(board[guess_row][guess_col] == "X"):
                    print "You guessed that one already."
                else:
                    print "You missed my battleship!"
                    board[guess_row][guess_col] = "X"

                    # Print (turn + 1) here!
                    print_board(board)
                curPlayer=1 if curPlayer==2 else 2
            print "%s has won %s games(%s%%)" % (player1, numWins1, numWins1/float(numGames)*100)
            print "%s has won %s games(%s%%)" % (player2, numWins2, numWins2/float(numGames)*100)
            break
winner = player1 if numWins1>numWins2 else player2
print "\nGame Over!\nWinner is %s! Congratulations!" % winner
