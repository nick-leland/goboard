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
        print(self.x,self.y, self.state, self.statep)

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
        return "+"
    elif piece.status == 1:
        # White
        return '\u25CB'
    elif piece.status == 2:
        # Black
        return '\u25CF'

def printBoard():
    """Function used to print the fresh board state after each turn"""
    # Has to call each individual position class to get the current state
    w = '\u25CB'
    b = '\u25CF'
    for x in range(game_size):
        for y in range(game_size):
            pass
    pass

def requery():
    """Function to refresh the turn of the game, including piece removal"""
    pass

if __name__ == "__main__":
    game_size = sizeinput()
    for x in range(game_size):
        for y in range(game_size):
            xmod = x + 1
            ymod = y + 1
            str(str(modx)+str(mody)) = position(xmod, ymod, game_size)
            # Need to use something else for this, maybe a dictionary? 
    printBoard()

