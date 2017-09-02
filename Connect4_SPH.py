# Connect Four
# Sebastian Puerta

def rules():
    print("\nRULES:")
    print("> You have the option to either play against the computer or a 2nd player")
    print("> The 1st player (user) is represented by 'O'")
    print("> The computer or 2nd player will be represented by 'X'")
    print("> Connect four 'O' in a row, column, or diagonally")
    print("> If the user inputs a wrong value, you will prompt again to input correct value or to exit the game")
    print("> You can restart the game by typing in the 'r'")
    print("> If you reset, the score goes back to 0 again, and the grid is empty again")
    print("> You can cheat and have the computer make a selection for you by typing in 'chance'")
    print("> You can exit the game when it's your turn by typing in keyword 'end'")
    print("> For every game, you will receive 1 point if you win or a 0 if you lose.")
    print("> User always goes first against the computer")
    print("> If position, is already filled choose another, otherwise you will prompt again for new values")
    print("> Ready? Good luck!")

# connect four checker algorithm (naive method)
def connect_four(G,x,y,c): 
    left = 0
    right = 0
    up = 0
    down = 0
    upleft_diag = 0
    lowleft_diag = 0
    upright_diag = 0
    lowright_diag = 0
    
    for i in range(4):
        # checks down
        if((x+i) >= 0 and (x+i) < 7):
            if(G[x + i][y] == c):
                down += 1
                if(down == 4): return True
        # checks up
        if((x-i) >= 0 and (x-i) < 7):
            if(G[x-i][y] == c):
                up += 1
                if(up == 4): return True
        # checks right
        if((y+i) >= 0 and (y+i) < 7):
            if(G[x][y+i] == c):
                right += 1
                if(right == 4): return True
        # checks left
        if((y-i) >= 0 and (y-i) < 7):
            if(G[x][y-i] == c):
                left += 1
                if(left == 4): return True
        # checks upper left diag
        if((x-i) >= 0 and (x-i) < 7 and (y-i) >= 0 and (y-i) < 7):
            if(G[x-i][y-i] == c):
                upleft_diag += 1
                if(upleft_diag == 4): return True
        # checks lower left diag
        if((x+i) >= 0 and (x+i) < 7 and (y-i) >= 0 and (y-i) < 7):
            if(G[x+i][y-i] == c):
                lowleft_diag += 1
                if(lowleft_diag == 4): return True
        # checks upper right diag
        if((x-i) >= 0 and (x-i) < 7 and (y+i) >= 0 and (y+i) < 7):
            if(G[x-i][y+i] == c):
                upright_diag += 1
                if(upright_diag == 4): return True
        # checks lower right diag
        if((x+i) >= 0 and (x+i) < 7 and (y+i) >= 0 and (y+i) < 7):
            if(G[x+i][y+i] == c):
                lowright_diag += 1
                if(lowright_diag == 4): return True

    return False


def main():
    print("\t========== CONNECT FOUR: Sebastian Version ==========")
    rules()
    player1 = ""
    player2 = ""
    score1 = 0
    score2 = 0
    x = 0
    y = 0
    count_X = 0
    count_O = 0
    win = False
    
    # creating a 7X7 Grid Table
    Grid = [['-' for i in range(7)] for j in range(7)]

    # number of players
    while(True):
        number = input("\nNumber of players (max is 2): ")
        if(number == '1' or number == '2'): break
        else: continue

    # player vs computer
    if(number == '1'):
        print("\n ===== PLAYER VS CPU ===== ")
        while(True):
            from random import randrange
            print("\nGAME OPTIONS")
            print("play: 'p'")
            print("rules: 'b'")
            print("chance: 'c'")
            print("reset: 'r'")
            print("exit: 'e'")

            print("\t\t CONNECT FOUR \n")
            print('\t', end="")
            print("   ", end="")
            for i in range(7):
                print(i, "  ",end="")
            print('\n')
            for i in range(7):
                print('\t', end="")
                print(i, " ",end="")
                for j in range(7):
                     print(Grid[i][j]," ", end=" ")
                print('\n')
            
            # user input prompt
            while(True):
                user_input = input("\nEnter a prompt: ")
                user_input = user_input.lower()
                if(user_input == 'b' or user_input == 'c' or user_input == 'r'
                   or user_input == 'e' or user_input == 'p'): break;
                else:
                    print("Wrong input, try again")
                    continue
            # rules of game
            if(user_input == 'b'): rules()
            # reset game
            elif(user_input == 'r'):
                print("Resetting game")
                score1 = 0
                score2 = 0
                Grid = [['-' for i in range(7)] for j in range(7)]
                continue

            # exit game
            elif(user_input == 'e'):
                print("Exiting game")
                break
            # automatic input (chance)
            elif(user_input == 'c'):
                while(True):
                    x = randrange(0,7,1)
                    y = randrange(0,7,1)
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'O'
                        break
            # player input
            elif(user_input == 'p'):
                print("Take a look at the game, find a position where you would like to place your piece")
                print("X are the ROW values, Y are the COLUMN values")
                while(True):
                    # Obtaining x value
                    while(True):
                        x_axis = input("Enter integer values for the x-axis: ")
                        if(x_axis == '0' or x_axis == '1' or x_axis == '2' or x_axis == '3' or x_axis == '4' or x_axis == '5' or x_axis == '6'):
                            x = ord(x_axis) % ord('0')
                            break
                        else: continue
                    # Obtaining y value
                    while(True):
                        y_axis = input("Enter integer values for the y-axis: ")
                        if(y_axis == '0' or y_axis == '1' or y_axis == '2' or y_axis == '3' or y_axis == '4' or y_axis == '5' or y_axis == '6'):
                            y = ord(y_axis) % ord('0')
                            break
                        else: continue
                    # Checking if position is already filled
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'O'
                        break
            win = connect_four(Grid,x,y,'O')
            if(win == True):
                score1 += 1
                break
            # computer's turn
            while(True):
                x = randrange(0,7,1)
                y = randrange(0,7,1)
                if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                else:
                    Grid[x][y] = 'X'
                    break
            win = connect_four(Grid,x,y,'X')
            if(win == True):
                score2 += 1
                break
    # Player vs Player
    elif(number == '2'):
        while(True):
            print("\n ===== PLAYER VS PLAYER =====")
            from random import randrange
            # PLAYER #1
            print("\n\t ======== PLAYER #1 ======== ")
            # keeping the score
            print("\nSCORES")
            print("Player 1: ", score1)
            print("Player 2: ", score2)

            print("\nGAME OPTIONS")
            print("play: 'p'")
            print("rules: 'b'")
            print("chance: 'c'")
            print("reset: 'r'")
            print("exit: 'e'")

            print("\t\t CONNECT FOUR \n")
            print('\t', end="")
            print("   ", end="")
            for i in range(7):
                print(i, "  ",end="")
            print('\n')
            for i in range(7):
                print('\t', end="")
                print(i, " ",end="")
                for j in range(7):
                    print(Grid[i][j]," ", end=" ")
                print('\n')
                
            # player 1 input prompt
            while(True):
                user_input = input("\nEnter a prompt: ")
                user_input = user_input.lower()
                if(user_input == 'b' or user_input == 'c' or user_input == 'r'
                    or user_input == 'e' or user_input == 'p'): break;
                else:
                    print("Wrong input, try again")
                    continue
            # rules of game
            if(user_input == 'b'): rules()
            # reset game
            elif(user_input == 'r'):
                print("Resetting game")
                score1 = 0
                score2 = 0
                Grid = [['-' for i in range(7)] for j in range(7)]
                continue
            # exit game
            elif(user_input == 'e'):
                print("Exiting game")
                break
            # automatic input (chance)
            elif(user_input == 'c'):
                while(True):
                    x = randrange(0,7,1)
                    y = randrange(0,7,1)
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'O'
                        break
            # player1 input
            elif(user_input == 'p'):
                print("Take a look at the table, find a position where you would like to place your piece")
                print("X are the ROW values, Y are the COLUMN values")
                while(True):
                    # Obtaining x value
                    while(True):
                        x_axis = input("PLAYER 1 Enter an integer value for the x-axis: ")
                        if(x_axis == '0' or x_axis == '1' or x_axis == '2' or x_axis == '3' or x_axis == '4' or x_axis == '5' or x_axis == '6'):
                            x = ord(x_axis) % ord('0')
                            break
                        else: continue
                    # Obtaining y value
                    while(True):
                        y_axis = input("PLAYER 1 Enter an integer value for the y-axis: ")
                        if(y_axis == '0' or y_axis == '1' or y_axis == '2' or y_axis == '3' or y_axis == '4' or y_axis == '5' or y_axis == '6'):
                            y = ord(y_axis) % ord('0')
                            break
                        else: continue
                    # Checking if position is already filled
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'O'
                        break
            win = connect_four(Grid,x,y,'O')
            if(win == True):
                score1 += 1
                break
            # PLAYER #2
            print("\n\t ======== PLAYER #2 ======== ")
            # keeping the score
            print("\nSCORES")
            print("Player 1: ", score1)
            print("Player 2: ", score2)

            print("\nGAME OPTIONS")
            print("play: 'p'")
            print("rules: 'b'")
            print("chance: 'c'")
            print("reset: 'r'")
            print("exit: 'e'")        
            print("\t\t CONNECT FOUR \n")
            print('\t', end="")
            print("   ", end="")
            for i in range(7):
                print(i, "  ",end="")
            print('\n')
            for i in range(7):
                print('\t', end="")
                print(i, " ",end="")
                for j in range(7):
                    print(Grid[i][j]," ", end=" ")
                print('\n')
            # player 2 input prompt
            while(True):
                user_input = input("\nEnter a prompt: ")
                user_input = user_input.lower()
                if(user_input == 'b' or user_input == 'c' or user_input == 'r'
                   or user_input == 'e' or user_input == 'p'): break;
                else:
                    print("Wrong input, try again")
                    continue
            # rules of game
            if(user_input == 'b'): rules()
            # reset game
            elif(user_input == 'r'):
                print("Resetting game")
                score1 = 0
                score2 = 0
                Grid = [['-' for i in range(7)] for j in range(7)]
                continue

            # exit game
            elif(user_input == 'e'):
                print("Exiting game")
                break
            # automatic input (chance)
            elif(user_input == 'c'):
                while(True):
                    x = randrange(0,7,1)
                    y = randrange(0,7,1)
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'X'
                        break
            # player2 input
            elif(user_input == 'p'):
                print("Take a look at the game, find a position where you would like to place your piece")
                print("X are the ROW values, Y are the COLUMN values")
                while(True):
                    # Obtaining x value
                    while(True):
                        x_axis = input("PLAYER 2: Enter integer values for the x-axis: ")
                        if(x_axis == '0' or x_axis == '1' or x_axis == '2' or x_axis == '3' or x_axis == '4' or x_axis == '5' or x_axis == '6'):
                            x = ord(x_axis) % ord('0')
                            break
                        else: continue
                    # Obtaining y value
                    while(True):
                        y_axis = input("PLAYER 2: Enter integer values for the y-axis: ")
                        if(y_axis == '0' or y_axis == '1' or y_axis == '2' or y_axis == '3' or y_axis == '4' or y_axis == '5' or y_axis == '6'):
                            y = ord(y_axis) % ord('0')
                            break
                        else: continue
                    # Checking if position is already filled
                    if(Grid[x][y] == 'O' or Grid[x][y] == 'X'): continue
                    else:
                        Grid[x][y] = 'X'
                        break
            win = connect_four(Grid,x,y,'X')
            if(win == True):
                score2 += 1
                break
    
    print("\t\t CONNECT FOUR \n")
    print('\t', end="")
    print("   ", end="")
    for i in range(7):
        print(i, "  ",end="")
    print('\n')
    for i in range(7):
        print('\t', end="")
        print(i, " ",end="")
        for j in range(7):
            print(Grid[i][j]," ", end=" ")
        print('\n')
    # results
    if(score1 > score2):
        print("You won! Congratulations")
    elif(score2 > score1):
        print("You lose! Better luck next time")
    else: print("It's a Draw!")
    print("To replay again, run the program again")

    print("\n - End of program...")
main()



