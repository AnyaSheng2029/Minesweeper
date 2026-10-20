
#welcome to Minesweeper!

import random
import time


global state
state = True
global win
win = False
global lose
lose = False
global stuck
stuck = False
global AImode
AImode = False

global height
height = 0
global width
width = 0


global display
display = [[]]
global dispKey
dispKey = [[]]
global key
key = [[]]

global moves
moves = 0

print("press command + option + plus to zoom in on the console, trust me")
print("I suggest making boards that are 20 percent bombs, such as 4,4,3 or 8,8,13 or 10,10,20")
print("btw my current best record for 4,4,3 is 7 seconds, for 8,8,13 it's 37 seconds, for 10,10,20 it's 1:55 minutes, and for 18,30,99, it's 14:30 minutes")
print("maybe the real AI was the font selection we made along the way")
print()
print()
print("basically the smarter AI (press a) will take the best chances of guessing to avoid 1 bomb in at least 4 possible places.")
print("otherwise, it gets stuck, and passes play back to the user")
print("but if it's called upon even while its stuck, it will take any guess it has with a 50% chance or better")
print("without any human input, in a 10,10,20 game this has an astounding win rate of 7 out of 50 (14%), getting stuck 3 times (6%)")
print("for contrast, playing 10,10,20 by myself, I win about 5/8 (63%)")
print("meanwhile, the dumber AI (press b) is just a convenience filler that will mark all remaining bombs around a slot if there are exactly that many spaces left")


print("call hostGame to start. try: hostGame(8,8,13)")

def setKey(bombs):
    """ creates board key with given size, width and height, then randomly assigns bombs number of bombs throughout
        returns the board
    """
    global display
    global dispKey
    global key

    global height
    global width

    bmbleft = bombs
    key = [['']*width for row in range(height)]
    for i in range(height):
        for j in range(width):
            squaresleft = width*height - i*width - j
            prob = bmbleft/squaresleft

            if random.random() <= prob and not bmbleft == 0:
                key[i][j] = 1
                bmbleft -= 1
            else:
                key[i][j] = 0

def printBoard(A):
    """ prints board A, works for both keys and actual display boards
        so much chaos, don't try to parse it
    """

    global height
    global width

    horiz = "     " + "0" + "   "
    for i in range(1,height-1):
        horiz += str(i) + "   " 
    horiz+= str(height-1)
    print(horiz)

    print("   " + "----" * width + "-")

    for i in range(height):
        if A[i][0] == '':
            vert = str(i) + " |" + "  •" + "   "
        else:
            vert = str(i) + " |" + "  " + translate(A,i,0) +  "  "
        
        for j in range(1,width-1):
            if A[i][j] == '':
                vert += "•   "
            else:
                vert += translate(A,i,j) + "  "
        vert+= translate(A,i,width-1)
        vert += " |"
        print(vert)
        if i < height - 1:
            print("  |" + "    " * (width-1) + "     |")
    print("   " + "----" * width + "-")
    print()


def translate(A,x,y):
    """ accepts x and y locations in the matrix A, and A, and 
        returns the emoji/visual representation for 0 through 8, bombs, and pins 
    """
    elem = str(A[x][y])
    """ cute font but strains
    if elem == "0":
        return "𝟘 "
    elif elem == "1":
        return "𝟙 "
    elif elem == "2":
        return "𝟚 "
    elif elem == "3":
        return "𝟛 "
    elif elem == "4":
        return "𝟜 "
    elif elem == "5":
        return "𝟝 "
    elif elem == "6":
        return "𝟞 "
    elif elem == "7":
        return "𝟟 "
    elif elem == "8":
        return "𝟠 "
    elif elem == "*":
        return "💣"
    elif elem == "!":
        return "📍"
    elif elem == "":
        return "• "
    """

    """ slightly less eye strain
    if elem == "0":
        return "𝟎 "
    elif elem == "1":
        return "𝟏 "
    elif elem == "2":
        return "𝟐 "
    elif elem == "3":
        return "𝟑 "
    elif elem == "4":
        return "𝟒 "
    elif elem == "5":
        return "𝟓 "
    elif elem == "6":
        return "𝟔 "
    elif elem == "7":
        return "𝟕 "
    elif elem == "8":
        return "𝟖 "
    elif elem == "*":
        return "💣"
    elif elem == "!":
        return "📍"
    elif elem == "":
        return "• "
    """

    if elem == "0":
        return "0️⃣ "
    elif elem == "1":
        return "1️⃣ "
    elif elem == "2":
        return "2️⃣ "
    elif elem == "3":
        return "3️⃣ "
    elif elem == "4":
        return "4️⃣ "
    elif elem == "5":
        return "5️⃣ "
    elif elem == "6":
        return "6️⃣ "
    elif elem == "7":
        return "7️⃣ "
    elif elem == "8":
        return "8️⃣ "
    elif elem == "*":
        return "💣"
    elif elem == "!":
        return "📍"
    elif elem == "":
        return "• "


def setDisplayKey():
    """ takes key and creates the display key board of the same dimension, with appropriate number denoting how many bomb neighbors that square has
        returns that display key board
    """
    global display
    global dispKey
    global key

    global height
    global width

    dispKey = [['']*width for row in range(height)]
    
    for i in range(height):
        for j in range(width):
            if key[i][j] == 1:
                dispKey[i][j] = "*" #it's a bomb!
            else:
                dispKey[i][j] = countNeighbors(key,i,j,1)

    return dispKey

def countNeighbors(A,x,y,check):
    """ Accepts matrix A, which is used to check the neighbors
        also accepts coordinates in A, and check, the value it is checking for in the neighbors
        returns the number of neighbors of the coordinates (x,y) in A that are the check
    """ 
    global height
    global width

    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            if i+x < 0 or i+x >= height or j+y < 0 or j+y >= width: #in case out of bounds, on the edges
                pass
            elif A[i+x][j+y] == check:
                count += 1
            else:
                pass
    return count

def checkWin():
    """ tests win condition
        returns nothing but changes global variable win if either all bombs are correctly marked or if all safe slots are opened
    """
    global state
    global display
    global dispKey
    global key
    global win
    global lose

    global height
    global width

    allSafe = True
    allMarked = True
    for i in range(height):
        for j in range(width):
            if dispKey[i][j] == "*":
                allMarked = allMarked and display[i][j] == "!"
            else:
                allSafe = allSafe and display[i][j] == dispKey[i][j]

    win = allSafe or allMarked




def hostGame(h,w,bombs):
    """ starts up a game with the inputted dimensions and bombs
    """
    global state
    global display
    global dispKey
    global key
    global win
    global lose

    global height
    global width
    height = h
    width = w
    
    global moves
    start_time = time.time()


    setKey(bombs)
    printBoard(key)
    setDisplayKey()
    printBoard(dispKey)

    display = [['']*width for row in range(height)]
    printBoard(display)

    print()
    print("Welcome to Minesweeper!")
    print('Your goal: Open every safe slot without clicking on a mine!')

    while not win and not lose: 

        printBoard(display)                # show the board
        print("Current state:")
        if state:
            print("      TEST NEW SLOTS")
        else:
            print("      MARK BOMBS")
        print("Enter c to change state")

        x = promptUser("x")   # prompt the user
        if not x < 0:
            y = promptUser("y")   # prompt the user

        if x >= 0 and y >= 0:
            if state:
                if display[x][y] == '':
                    test(x,y)
                elif display[x][y] == "!":
                    print()
                    print("That's already a flag! Press 'c' to switch to the bomb marking state to unmark it")
                else:
                    openRest(x,y)
            else:
                if display[x][y] == '' or display[x][y] == '!':
                    mark(x,y)
                else:
                    openRest(x,y)
            moves+=1
        print("       Moves:", moves)
        print()
        checkWin()
    end_time = time.time() # Record the ending time

    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)

    if win:
        for i in range(height):
            for j in range(width):
                if display[i][j] == '':
                    display[i][j] = dispKey[i][j]
        printBoard(display) 
        print()
        print("YOU WON!")
    elif lose:
        #print everything exploding for aesthetics
        print()
        print("YOU LOSE!")
    print("Stats")
    print("moves: ", moves)
    print("time:"f"\r{int(minutes):02d}:{seconds:05.2f}", end="")
    
    #resetting
    state = True
    win = False
    lose = False
    moves = 0


def AI(type):
    """ Simple AI that will mark bombs if there's only the exact number of spots left that are needed to fulfill the rest of the bomb count
        type should be either "a" or "b" string, that denotes how smart the ai should be (a is smartest b is dumbest)
    """
    global display
    global dispKey
    global win
    global lose
    global AImode
    global stuck
    AImode = True

    global height
    global width
    #start_time = time.time()
    
    empty = True
    first = True

    for e in range(height):         #update everything
        for f in range(width):
            openRest(e,f)
            empty = empty and display[e][f] == ""
    
    if empty:
        test(0,0)
        first = False
    
    while not win and not lose and not (stuck and not first):
        endTurn = False
        for x in range(height): #if same, this is the baseline, aka b, but will also run for a
            for y in range(width): 
                #print("checking",x,y,"for same spaces as bombs")
                if not endTurn: #so that once we have checked the remaining bombs and spaces successfully and updated once, we can check for winning again
                    if not dispKey[x][y] == "*" and not display[x][y] == "":
                        currentFlags= countNeighbors(display,x,y,"!")
                        goal = dispKey[x][y]
                        remainingBombs = goal - currentFlags
                        remainingSpaces = countNeighbors(display,x,y,"")
                        endTurn = ifSame(remainingSpaces, remainingBombs,x,y)
                        if endTurn:
                            first = False
        if type == "a" and not win and not lose and not (stuck and not first): #will only check for a's condition of guessing 1 bomb's location if there's nothing to do this cycle with b, which is more secure
            for x in range(height):
                for y in range(width): 
                    #print("checking",x,y,"for guessing one")
                    if not endTurn: #so that once we have checked the remaining bombs and spaces successfully and updated once, we can check for winning again
                        if not dispKey[x][y] == "*" and not display[x][y] == "":
                            currentFlags= countNeighbors(display,x,y,"!")
                            goal = dispKey[x][y]
                            remainingBombs = goal - currentFlags
                            remainingSpaces = countNeighbors(display,x,y,"")
                            endTurn = guess(remainingSpaces, remainingBombs,x,y,1,3)
                            if endTurn:
                                first = False
                        elif x == height - 1 and y == width - 1:
                            stuck = True
        if stuck and first:
            stuck = False
            for i in range(height):
                for j in range(width):
                    if not endTurn: #so that once we have checked the remaining bombs and spaces successfully and updated once, we can check for winning again
                        if not display[i][j] == "!" and not display[i][j] == "":
                            currentFlags= countNeighbors(display,i,j,"!")
                            goal = dispKey[i][j]
                            remainingBombs = goal - currentFlags
                            remainingSpaces = countNeighbors(display,i,j,"")
                            endTurn = guess(remainingSpaces, remainingBombs,i,j,1,2)
                            if endTurn:
                                first = False
                            elif not endTurn:
                                endTurn = guess(remainingSpaces, remainingBombs,i,j,1,1)
                            elif endTurn:
                                first = False
                            elif not endTurn:
                                endTurn = guess(remainingSpaces, remainingBombs,i,j,2,3)
                            elif endTurn:
                                first = False
                            elif not endTurn:
                                endTurn = guess(remainingSpaces, remainingBombs,i,j,3,5)
                            elif endTurn:
                                first = False
                            elif not endTurn:
                                endTurn = guess(remainingSpaces, remainingBombs,i,j,4,7)
                        elif i == height - 1 and j == width - 1:
                            stuck = True
                            first = False
    print()
    printBoard(display) 
    print()

    if win:
        for i in range(height):
            for j in range(width):
                if display[i][j] == '':
                    display[i][j] = dispKey[i][j]
        print()
        printBoard(display) 
        print()
        print("THE AI WON!")
    elif stuck:
        #print everything exploding for aesthetics
        print()
        print("The AI is stuck!")
    elif lose:
        print()
        print("Sorry! Looks like the AI guessed wrong")
    print("Stats")
    #end_time = time.time() # Record the ending time


    stuck = False
    




def guess(remainingSpaces, remainingBombs,x,y,bombs,limit):
    """ takes the remaining spaces and remaining bombs of the safe slot at x and y coordinates, 
        as well as the requirements of bombs and requirement of spaces left
        returns True if something is done and the turn should end and while loop conditions need to be checked again
    """
    global display
    global dispKey
    global win
    global lose
    global height
    global width
    global stuck
    if remainingBombs == bombs and remainingSpaces > limit: #smarter part, will make a guess if there's only one bomb and 3 or more options
        index = int(random.uniform(0,remainingSpaces))
        count = -1
        for i in range(-1,2):
            for j in range(-1,2):
                if i+x < 0 or i+x >= height or j+y < 0 or j+y >= width: #in case out of bounds, on the edges
                    pass
                elif display[i+x][j+y] == "":
                    count+=1
                    if index == count:
                        test(i+x,j+y) #this is the guess
                else:
                    pass

        for e in range(height):         #update everything
            for f in range(width):
                openRest(e,f)
        
        checkWin()
        return True
    elif x == height - 1 and y == width - 1:
        stuck = True
    return False


        

def ifSame(remainingSpaces, remainingBombs,x,y):
    """ takes the remaining spaces and remaining bombs of the item at x and y coordinates and marks all the surrounding empty spaces of x and y
        if the spaces and bombs are an equal number
        corresponding to just AI b
    """
    global display
    global dispKey
    global win
    global lose
    global height
    global width
    global stuck
    if remainingSpaces == remainingBombs and not remainingSpaces == 0: #simplest doing stuff condition
        for i in range(-1,2):
            for j in range(-1,2):
                if i+x < 0 or i+x >= height or j+y < 0 or j+y >= width: #in case out of bounds, on the edges
                    pass
                elif display[i+x][j+y] == "":
                    mark(i+x,j+y) #mark every remaining space since it must be a bomb
                else:
                    pass

        for e in range(height):         #update everything
            for f in range(width):
                openRest(e,f)
        
        checkWin()
        return True
    return False



                        



def promptUser(coord):
    """ promptUser should ask the user for a valid index (location) to toggle 
            it should keep asking until a valid index is entered (not yet implemented)
    """
    user_index = -1    # start with an intentionally invalid index
    global state
    global display
    user_string = input("Choose your " + coord +" coordinate to change:")
    global moves
    global height
    global width
    
    if user_string == "a" or user_string == "A":
        AI("a")
        return -1
    elif user_string == "b" or user_string == "B":
        AI("b")
        return -1
    else:
        try:                                                # Python error handling
            user_index = int(user_string)
        except ValueError:                                  # if it's not an integer
            if user_string == "c":
                state = not state
                print()
                print ("   Changed state! New state:")
                if state:
                    print("      MARK BOMBS")
                else:
                    print ("      TEST NEW SLOTS")
                user_index = -2
            else:
                print ("   Invalid index, please try again!")
                user_index = -1


        if user_index == -2 or user_index == -1:
            pass
        elif coord == "x" and (user_index >= height or user_index< 0):
            print ("   Invalid index, please try again!")
            user_index = -1
        elif coord == "y" and (user_index >= width or user_index< 0):
            print ("   Invalid index, please try again!")
            user_index = -1

            

        return user_index  




def test(x,y):
    """ only leads to if state is true, and the index has not been tested before
        gonna be kinda complicated, will code later
    """ 
    global display
    global dispKey
    global key
    global lose

    if dispKey[x][y] == "*":
        lose = True
        print()
        print("Oops! You clicked a bomb! Better luck next time!") #replace with actual losing menu in host game
    else:
        display[x][y] = dispKey[x][y] #reveal
        if display[x][y] == 0:
            openRest(x,y)



def openRest(x,y):
    """ only leads to if state is true, and the index has already been tested before
        to be implemented
    """
    global display
    global dispKey
    global key

    global height
    global width

    marked = countNeighbors(display,x,y,"!")
    if marked == display[x][y]: #if the marked bombs around x,y in the current user display version matches what it's supposed to be,
        for i in range(-1,2):
            for j in range(-1,2):
                if i+x < 0 or i+x >= height or j+y < 0 or j+y >= width: #in case out of bounds, on the edges
                    pass
                elif display[i+x][j+y] == '':
                    test(i+x,j+y)
                    

    elif not dispKey[x][y] == "*" and marked >= int(dispKey[x][y]) and not AImode:
        print("There's too many bombs marked around this slot!")
    elif not AImode:
        print("There's too little bombs marked around this slot!")

def mark(x,y):
    """ only leads to if state is false, in marking bombs state
        to be implemented
    """
    global display
    global dispKey
    global key

    if display[x][y] == "!":
        display[x][y] = ''
    else:
        display[x][y] = "!"
    
