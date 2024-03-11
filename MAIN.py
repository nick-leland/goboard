import string

class position:
    """The baseline class for the definition of a space"""
    def __init__(self, x, y, board):
        self.x = x
        self.y = y

        # 0 if Empty
        # 1 if White
        # 2 if Black
        self.status = 0
        
        count = 0
        if abs(x) == 1 or abs(x) == board:
            count+=1
        if abs(y) == 1 or abs(y) == board:
            count+=1
        
        # This whole section is just for debugging, use the count to determine the positions
        if count == 0:
            self.statep ="center"
        if count == 1:
            self.statep ="edge"
        if count == 2:
            self.statep ="corner"
        self.state = count
        # print(self.x,self.y, self.state, self.statep)

def sizeinput():
    """Function to query the board size at the start of the game"""
    size = None
    while size == None:
        input_size = input("What is the size of the game board? Answer 9x9[1], 13x13[2] or 19x19[3]")
        if input_size == "1":
            size = 9
        elif input_size == "2":
            size = 13
        elif input_size == "3":
                size = 19
        else:
            print("Please input one of the 3 numbers.")
            continue
    print(f"The board is a {size}x{size} board.")
    return size

def c(piece):
    if piece.status == 0:
        # Empty
        return "+ "
    elif piece.status == 1:
        # White
        return '\u25CB '
    elif piece.status == 2:
        # Black
        return '\u25CF '

def printBoard(game_size, piece_list):
    """Function used to print the fresh board state after each turn"""
    # Has to call each individual position class to get the current state
    count = 0
    for x in range(game_size):
        print("")
        for y in range(game_size):
            print(c(piece_list[count]), end="")
            count +=1
    print("\n")
    pass

def verification(chars, game_size):
    """Function to verify that the input for a move is within acceptable board range"""
    x = list(chars)
    x[0] = str.capitalize(x[0]) #This can probably be optimized in the future check time constraints
    accep_chars = []
    accep_num = []
    for _ in range(game_size):
        accep_chars.append(string.ascii_uppercase[_])
        accep_num.append(str(_+1))
    if x[0] in accep_chars and x[1] in accep_num:
        print("Valid entry")
        return
    else:
        print("Not a valid entry")
        pass

    """Function to refresh the turn of the game, including piece removal"""
    printBoard(game_size, positions)
    pass

def passcount(pm, cm):
    """Used to determine if both players pass to conclude the match."""
    if pm == cm:
        return True
    else:
        return False

if __name__ == "__main__":
    game_size = sizeinput()
    positions = []
    for x in range(game_size):
        for y in range(game_size):
            xmod = x + 1
            ymod = y + 1
            positions.append(position(xmod, ymod, game_size))
    wincon = False
    print("If help is required type 'help'.")
    while wincon == False:
        requery(game_size, positions)
        move = input("Input move in A1 notation.", "\n")
        if move == 'pass':
            continue
        elif move == 'help':
            "You don't need help"
        else:
            verification(move, game_size)
            

    print("\n", "Game has been concluded.", "\n")
