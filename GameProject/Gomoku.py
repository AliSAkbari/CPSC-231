#Group 76 
#Members: Navjeet, Ali, Justine
#Game: Gomoku 

#This function prints all introduction statements and instructions
#for the game on the terminal.
def introduction():
	#ASCII art title
	print("""
  _    _        _  _                 
 | |  | |      | || |                               
 | |__| |  ___ | || |  ___   
 |  __  | / _ \| || | / _ \                                        
 | |  | ||  __/| || || (_) |                                    
 |_|  |_| \___||_||_| \___/                                      
                             
 __    __     _                                                
/ / /\ \ \___| | ___ ___  _ __ ___   ___                  
\ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \                    
 \  /\  /  __/ | (_| (_) | | | | | |  __/                        
  \/  \/ \___|_|\___\___/|_| |_| |_|\___|                                
 _         
| |                                    
| |_  ___                                        
| __|/ _ \                                     
| |_| (_) |                                 
 \__|\___/  
                                                 
   _____                           _            _  _ 
  / ____|                         | |          | || |
 | |  __   ___   _ __ ___    ___  | | __ _   _ | || |
 | | |_ | / _ \ | '_ ` _ \  / _ \ | |/ /| | | || || |
 | |__| || (_) || | | | | || (_) ||   < | |_| ||_||_|
  \_____| \___/ |_| |_| |_| \___/ |_|\_\ \__,_|(_)(_)
""")


#All import modules.
import turtle
import random


#Creating all turtles required. "welcome" for the board on the turtle
#screen, "jim" for the stones placed by the players.
welcome = turtle.Turtle()
jim = turtle.Turtle()
tess = turtle.Turtle()
jake = turtle.Turtle()
leo = turtle.Turtle()
luke = turtle.Turtle()
blueberry = turtle.Turtle()

#Creating and setting up the window screen
wn = turtle.Screen()	
wn.bgcolor("AntiqueWhite")

#These global variables are for the the board drawn on the turtle screen.
#Each cell has the length and width of 50 pixels, thus, the length
#and the height are adjusted accordingly to the number of rows and columns 
#chosen for the game.
#ROWS = int(input("Please choose between 9 and 18, 9 for a 10x10 board, 18 for a 19x19 board: ")) + 1
gridsize = 10
ROWS = gridsize
COLUMNS = ROWS

CELL_SIZE = 50
HALF_CELL_LENGTH = CELL_SIZE / 2

START_X = 0  
START_Y = 0 

LENGTH_OF_BOARD = (COLUMNS * CELL_SIZE)
HEIGHT_OF_BOARD = (ROWS * CELL_SIZE) 

LABLE_LOCATIONX = (START_X)
LABLE_LOCATIONY = (START_Y)

#The margin allows some space between the edges of the board on the turtle
#screen, to the edges of the window screen. The screen height and width are 
#also adjusted accordingly to the number of rows and columns for the board, 
#and may also adjust according to the cell size.
MARGIN = 120
SCREEN_HEIGHT = (2*MARGIN) + (CELL_SIZE * ROWS)
SCREEN_WIDTH= (2*MARGIN) + (CELL_SIZE * COLUMNS)

#The game state of the game, kept in a 2D list.
GRID = [['-'] * ROWS for x in range(ROWS)]

#Intializes a truth value for the function isGameDone.
isGameDone = False

#Initializes variable to 0, where 'COLOR' is a choice for the player to choose
#whether they would like to play with a white or a black stone. 0 is assigned
#to white, and 1 is assigned to black.
COLOR = 0
TURN = 0

filename = "gomokuSaved.txt"

def UpdateGlobalVariable():
	global ROWS
	global gameState
	global gridsize
	global COLUMNS
	global LENGTH_OF_BOARD
	global HEIGHT_OF_BOARD
	global SCREEN_HEIGHT
	global SCREEN_WIDTH
	global GRID

	ROWS = gridsize
	COLUMNS = ROWS
	
	LENGTH_OF_BOARD = (COLUMNS * CELL_SIZE)
	HEIGHT_OF_BOARD = (ROWS * CELL_SIZE) 

	SCREEN_HEIGHT = (2*MARGIN) + (CELL_SIZE * ROWS)
	SCREEN_WIDTH= (2*MARGIN) + (CELL_SIZE * COLUMNS)
		
	GRID = [['-'] * ROWS for x in range(ROWS)]

	gameState = GRID

def optionsForBoardSize():
	blueberry.up()
	blueberry.goto(-250, 90)
	blueberry.down()
	blueberry.speed(0)
	for i in range(0, 10):
		for t in range(4):
			blueberry.forward(50)
			blueberry.right(90)
		blueberry.forward(50)
	blueberry.up()

#To choose the color
def optionsForColour():
	blueberry.goto(-150, -20)
	blueberry.down()
	for drawWhiteOrBlackButton in range(2):
		for draw in range(2):
			blueberry.forward(100)
			blueberry.right(90)
			blueberry.forward(50)
			blueberry.right(90)
		blueberry.up()
		blueberry.forward(200)
		blueberry.down()
	blueberry.up()


def startButton():
	blueberry.goto(-100, -100)
	blueberry.down()
	for drawingTwo in range(4):
		blueberry.forward(200)
		blueberry.right(90)
		blueberry.forward(80)
		blueberry.right(90)
	blueberry.up()


#To write all labels
def writingForIntro():
	blueberry.color("DodgerBlue")
	blueberry.pensize(5)
	blueberry.speed(20)
	blueberry.up()
	blueberry.goto(0, 210)
	blueberry.down()
	blueberry.write("Gomoku!", align="center", font=("Arial",50, "normal")) 

	blueberry.up()
	blueberry.goto(0, 175)
	blueberry.down()
	blueberry.write("Welcome to this amazing game called Gomoku!",align="center", font=("Arial",15, "normal")) 

	blueberry.up()
	blueberry.goto(-255, 100)
	blueberry.write("How many rows and columns would you like to play on?", font=("Bauhaus 93", 16, "normal"))
	startWriting = -230
	for integers in range(10, 20, 1):
		blueberry.goto(startWriting, 60)
		blueberry.write(integers)
		startWriting = startWriting + 50

	blueberry.up()
	blueberry.goto(-248, -10)
	blueberry.write("Please choose the colour you would like to play with", font=("Bauhaus 93", 16, "normal"))

	blueberry.up()
	blueberry.goto(-115, -50)
	blueberry.write("White")

	blueberry.goto(88, -50)
	blueberry.write("Black")

	blueberry.up()
	blueberry.goto(-25, -150)
	blueberry.write("Start!", font=("Bauhaus 93", 16, "normal"))

	blueberry.up()
	blueberry.goto(-300, -230)
	blueberry.write("This is a 2 player game where you use either a black or a white stone. The objective is to", font=("Candara", 12, "normal"))
	blueberry.goto(-320, -260)
	blueberry.write(" connect 5 of your stones in a line to win. Connecting 6 or more in a line will not count as a win.", font=("Candara", 12, "normal"))
	blueberry.goto(-320, -290)
	blueberry.write("To pick a correct value, please click between the board boundaries and at the row and column ", font=("Candara", 12, "normal"))
	blueberry.goto(-25, -320)
	blueberry.write("intersections.", font=("Candara", 12, "normal"))

	blueberry.ht()

def startOfGameClicks(x,y):
	global COLOR	
	global gridsize
	start_x = -250
	#This loop is to handle board size 
	for i in range(0, 11):
		if ( (x >= (start_x+(i*50))) and (x <= start_x + (50*(i+1))) and ((y <= 90) and (y >= 40)) ):
			gridsize = (i+10)
			print ("grid size is: ", gridsize)
			UpdateGlobalVariable()
			return gridsize

	#To handle black or white stones
	if ( (x >= -150) and (x <= -50) and (y <= -20) and (y >= -70) ):
		print("White Stone")
		COLOR = 0
	if ( (x >= 50) and (x <= 150) and (y <= -20) and (y >= -70) ):
		print("Black Stone")
		COLOR = 1

	#Handle start button
	if ( (x >= -100) and (x <= 100) and (y <= -100) and (y >= -180) ):
		print("Game has started")
		officialGame()








#This function draws the game board on the turtle screen. It takes in no
#parameters, but includes two for loops. The outer for loop will draw the 
#columns, whereas the inner for loops will draw the rows. Nothing is returned.
def GameBoard():
	RowNum = START_Y
	for i in range(COLUMNS - 1):
		ColumnNum = START_X	
		for j in range(ROWS - 1):
			draw_square(ColumnNum, RowNum)
			ColumnNum = ColumnNum + CELL_SIZE
		RowNum = RowNum + CELL_SIZE

#The turtle 'welcome' draws the size of each cell for the number of rows and
#columns for the function GameBoard(). 
#This function takes two parameters:
#START_X and START_Y, which are values located at 0,0 as pixels on the turtle
#screen. These parameters are class int. 
def draw_square(START_X, START_Y):
	turtle.tracer(0)
	welcome.up()
	welcome.speed(10)
	welcome.goto(START_X, START_Y)
	welcome.down()
	for h in range(4):
		welcome.forward(CELL_SIZE)
		welcome.left(90)
	welcome.ht()
	turtle.update()
	turtle.tracer(0)					
	

#Writes the row numbers and column numbers on the turtle screen. No parameters
#are used.
def labels():
	global LABLE_LOCATIONY
	global LABLE_LOCATIONX
	#Turtle 'welcome' writes y-values for all values starting at 0 and
	#incrementing by 1 according to the number of rows.
	for yValueLabels in range(0, ROWS):
		welcome.up()
		welcome.goto(LABLE_LOCATIONX - 5, LABLE_LOCATIONY - 50)
		welcome.down
		welcome.write(str(yValueLabels), font=("Arial",15,"normal"))
		welcome.up()
		LABLE_LOCATIONX = LABLE_LOCATIONX + CELL_SIZE
		welcome.ht()
	#Resets the location of x to 0
	LABLE_LOCATIONX = 0
	#Turtle 'welcome' writes all x-values starting at 0 and
	#incrementing by 1 according to the number of rows.
	for xValueLabels in range(0, COLUMNS):
		welcome.up()
		welcome.goto(LABLE_LOCATIONX - 35, LABLE_LOCATIONY - 10)
		welcome.down
		welcome.write(str(xValueLabels), font=("Arial",15,"normal"))
		welcome.up()
		LABLE_LOCATIONY = LABLE_LOCATIONY + CELL_SIZE
		welcome.ht()

#This function uses the random module to determine whether the computer or the
#player will go first. 
#No parameters are required.
def whichPlayerGoesFirst():
	global TURN
	TURN = random.randint(0,1)
	if TURN == 0:
		screenWriting("Computer will go first")
	else:
		screenWriting("Player will go first")
	return TURN

#This function is for the computer to use the randomly generated integer and
#make it into a real, valid move on the board. This function will check if the
#computer move is valid, will draw the stone on the board, and will update the 
#2D list, with the right color of stone the computer must play with.
def AI_movement():
	(col, row)= random_move_generate()
	print(col, row)
	if not check_board_full():
		return
	if isMoveValid(row, col):
		drawItemOnBoard(col, row)
		updatetwoDlistGamestate(row, col)
		changeColor()
	else:
		AI_movement()


#This function will generate a random move for the computer to make. A random
#integer for the x and y pixel values will be chosen for the computer. Those 
#pixel values are then converted to column and row values to be successfully 
#placed on the board.
#No parameters are required.
#Returns: col, row. Class int.
def random_move_generate():
	global ROWS
	global COLUMNS
	row = random.randint(0, (ROWS - 1))
	col = random.randint(0, (COLUMNS - 1))
	return(col, row)

#This function creates the 2D list and incorporates the game state.
#There are no parameters.
#Returns: GRID, class list.
def twoDlistGamestate():
	for i in range (ROWS):
		print(GRID[i][0:])
	return GRID

#Assigns the variable gameState to the global variable GRID.
gameState = GRID

#This function updates the list whenever a white or black stone is placed on
#the board. 'W' represents write, 'B' represents black.
#Parameters: col, row. Converted to class int, from (x,y) pixels.
#Returns: the gameState, class list. 
def updatetwoDlistGamestate(row, col):
	global COLOR
	global gameState
	if (COLOR == 0):
		gameState[row][col] = 'W'
	else:
		gameState[row][col] = 'B'
	return gameState

#Checks whether the spot is taken or if it's empty.
#Parameters: col, row. Class int.
#Returns: gameState truth value of index, class list.
def isMoveValid(row, col):
	global gameState
	return gameState[row][col] == '-'

def check_board_full():
	for i in range(ROWS):
		for j in range(COLUMNS):
			if gameState[i][j] == '-':
				return True
			else:
				return False

		
#Checks the winning states hoizontally, vertically, or diagonally.
#Parameters: col, row. Class int.
#Returns: 
def isWinning(row, col):
	return isWinningVertical(row, col) or isWinningHorizontal(row, col) or isWinningDiagonal(row, col)

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones horizontally, but no more than 5.
#Parameters: col, row. Class int.
#Returns: True if winning state meets all conditions, false otherwise.
def isWinningHorizontal(row, col): 
	global gameState
	global COLOR

	counter = 0
	
	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'
	#This for loop checks the list in both directions, reading from left to
	#right and right to left.

	for direction in [1, -1]:
		i = 0
		curPos = col
		while ( 0 <= curPos < COLUMNS and  gameState[row][curPos] == str_variable):
			counter += 1	
			i += 1				
			curPos = col + i*direction
	counter -= 1
	
	if counter == 5: 
		return True 
	else:	
		return False  

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones vertically, but no more than 5.
#Parameters: col, row. Class int.
#Returns: True if winning state meets all conditions, false otherwise.
def isWinningVertical(row, col):
	global gameState
	global COLOR
    
	counter = 0

	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'
	for direction in [1, -1]:
		i = 0
		curPos = row
		while ( 0 <= curPos < ROWS and  gameState[curPos][col] == str_variable):
			counter += 1	
			i += 1				
			curPos = row + i*direction
	counter -= 1
	
	if counter == 5: 
		return True 
	else:	
		return False  

#This function iterates through the gameState to determine whether there are 
#5 consecutive same colored stones diagonally in either direction, but no 
#more than 5.
#Parameters: col, row. Class int.
#Returns: True if winning state meets all conditions, false otherwise.

def isWinningDiagonal(row, col):
	global gameState
	global COLOR
	global ROWS
	global COLUMNS
	
	counter1 = 0
	counter2 = 0

	if COLOR == 0:
		str_variable = 'W'
	else:
		str_variable = 'B'	

	'''left = False
	right = False
	y_change = 0
	x_change = 0
	Counter = 1
	if (((row + 4) >= 0) and ((row + 4) <= (ROWS - 1)) and ((col - 4) >= 0) and ((col - 4) <= (COLUMNS-1))):				#there is room for a diagonal"
		if gameState[row+4][col-4] == str_variable:
			left = True			#each end of diagonals are there and true
			while (left and (Counter <= 4)): #since this is true, check next spot
				y_change += 1
				x_change += 1
				Counter += 1
				if (gameState[row + y_change][col - x_change] != str_variable):
					left = False	#there is no stone on the second last diagonal
					break
			if (row + 5 <= (ROWS - 1)) and ((COLUMNS - 1) - 5 >= 0):
				if gameState[row + 5][col - 5] == str_variable:
					left = False

	if ( (((row + 4) >= 0) and ((row + 4) <= (ROWS - 1))) and ((col + 4) >= 0) and ((col + 4) <= (COLUMNS - 1))):
		if gameState[row+4][col+4] == str_variable:
			right = True
			while (right and (Counter <= 4)):
				y_change += 1
				x_change += 1
				Counter += 1
				if (gameState[row + y_change][col + x_change] != str_variable):
					right = False
					break
			if (row + 5 <= (ROWS - 1)) and ((COLUMNS - 1) - 5 >= 0):
				if gameState[row + 5][col + 5] == str_variable:
					right = False 

	if left or right: 
		return True 
	else:
		return False '''

	curRow = row
	curCol = col
	print("ROWS", ROWS, "curRow", curRow, "COLUMNS", COLUMNS, "curCol", curCol)
	#checks top and left
	while( 0<= curRow < ROWS and 0 <= curCol < COLUMNS and gameState[curRow][curCol] == str_variable):
		curRow += 1
		curCol -= 1
		print("ROWS", ROWS, "curRow", curRow, "COLUMNS", COLUMNS, "curCol", curCol)
	
	#down and right
	curRow2 = row
	curCol2 = col
	while( 0<= curRow2 < ROWS and 0 <= curCol2 < COLUMNS and gameState[curRow2][curCol2] == str_variable):
		curRow2 -= 1
		curCol2 += 1
		print("ROWS", ROWS, "curRow", curRow, "COLUMNS", COLUMNS, "curCol", curCol)

	curRow3 = row
	curCol3 = col
	#up and right
	while( 0<= curRow3 < ROWS and 0 <= curCol3 < COLUMNS and gameState[curRow3][curCol3] == str_variable):
		curRow3 += 1
		curCol3 += 1
		print("ROWS", ROWS, "curRow", curRow, "COLUMNS", COLUMNS, "curCol", curCol)
			
	#down and left
	curRow4 = row
	curCol4 = col
	while( 0<= curRow4 < ROWS and 0 <= curCol4 < COLUMNS and gameState[curRow4][curCol4] == str_variable):
		curRow4 -= 1
		curCol4 -= 1
		print("ROWS", ROWS, "curRow", curRow, "COLUMNS", COLUMNS, "curCol", curCol)

	counter1 = curRow - curRow2 - 1
	counter2 = curRow3 - curRow4 - 1

	print("C1: ",counter1)
	print("C2: ", counter2)
	if (counter1 == 5) or( counter2 == 5): 
		return True 
	else:
		return False  


#Checks and prints which player wins if they have met all conditions
def gameOver():
	global isGameDone
	isGameDone = True
	if COLOR == 0:
		luke.undo()
		screenWriting("White, wins!")
	else:
		luke.undo()
		screenWriting("Black, wins!")
	return isGameDone

#This function converts the pixel coordinates into coordinates shown on the 
#game board.
#Parameters: x,y. Class float. Taken from function clicked(x,y)
#Parameter x: uses the x values of pixels and makes them into board columns
#Parametere y: uses y-values of pixels and makes them into board rows
#Returns: Nothing
def screenCoordToBoardCoord(x, y):
	#This is the range of the board, print invalid if click outside of the range
	#There is a 15 pixel margin of error
	if (((x >= (START_X - 15)) and (x <= (START_X + 15 +(LENGTH_OF_BOARD))) and (y <= (START_Y + 15) + (HEIGHT_OF_BOARD) and (y >= (START_Y - 15))))):   
		col = (int((x + HALF_CELL_LENGTH)/ CELL_SIZE))
		row = (int((y + HALF_CELL_LENGTH)/  CELL_SIZE))
		return(col, row)
	else:
		luke.undo()
		screenWriting("Invalid!")
		return 



def screenDrawing():
	global COLOR

	jake.speed(10)
	jake.up()
	jake.goto(-165, 100)
	jake.down()
	for drawing in range(2):
		jake.pencolor("red")
		jake.forward(100)
		jake.right(90)
		jake.forward(50)
		jake.right(90)
	jake.up()
	jake.goto(-135, 65)
	jake.write("Save")
	jake.ht()
		
	leo.up()
	leo.speed(10)
	leo.goto(-165, 35)
	leo.down()

	for drawing in range(2):
		leo.pencolor("black")
		leo.forward(100)
		leo.right(90)
		leo.forward(50)
		leo.right(90)
	leo.up()
	leo.goto(-135, 0)
	leo.write("Load")
	leo.ht()

	tess.color("OrangeRed")
	tess.shape("circle")
	tess.speed(10)
	tess.up()
	tess.goto(-165, HEIGHT_OF_BOARD - 50)
	tess.down()
	for i in range(2):
		tess.forward(115)
		tess.left(90)
		tess.forward(50)
		tess.left(90)
	tess.color("black")
	tess.up()
	tess.goto(-155, HEIGHT_OF_BOARD - 45)
	tess.pensize(5)
	tess.write("Turn:", align = "left", font = ("Arial",15, "normal"))
	tess.ht()

	if COLOR == 0:
		jim.color("white")
	else:
		jim.color("black")
	jim.up()
	jim.shape("circle")
	jim.goto(-75, HEIGHT_OF_BOARD - 25)
	jim.stamp()
	jim.ht()


	luke.speed(10)
	luke.up()
	luke.goto(-150, -85)
	luke.down()
	luke.pencolor("black")
	luke.pensize(5)
	for drawing in range(2):
		luke.forward(700)
		luke.right(90)
		luke.forward(175)
		luke.right(90)
	luke.ht()


def screenWriting(writes_this):
	luke.up()
	luke.goto(-115, -175)
	luke.write(writes_this, align = "left", font = ("Arial",15, "normal"))


def handleSaveOrLoadButton(x,y):
	if ( ((x >= -165) and (x <= -65)) and ((y <= 100) and (y >= 50)) ) : 
		wn.onclick(saveFile(), btn=1, add=None)
		return True
	elif ( ((x >= -165) and (x <= -65)) and ((y <= 35) and (y >= -15)) ): 
		wn.onclick(loadFile(), btn=1, add=None)
		for u in range(ROWS * COLUMNS):
			jim.undo()
		for k in range(ROWS):
			for l in range(COLUMNS):
				if GRID[k][l] == 'B':
					jim.color('black')
					jim.up()
					jim.goto((l * 50),(k * 50))
					jim.stamp()
				elif GRID[k][l] == 'W':
					jim.color('white')
					jim.up()
					jim.goto((l * 50),(k * 50))
					jim.stamp()
		return True
	return False


#event handlers
def saveFile():
	with open(filename, 'w') as f:
		f.writelines(str(ROWS) + '\n')
		f.writelines(''.join(str(j) for j in i) + '\n' for i in GRID)
	luke.undo()
	screenWriting("Save Completed!"	)

def loadFile():	
	global GRID
	global ROWS
	i = 0
	j = 0
	try:
		with open(filename) as f:
			luke.undo()
			screenWriting("The file is now loaded.")
			newSize = f.readline()
			ROWS = int(newSize)
			COLUMNS = ROWS
			GRID = [['-'] * ROWS for x in range(ROWS)]
			while True:
				character = f.readline().rstrip('\n')             
				if not character:
					break
				while j < ROWS:
					GRID[i][j] = character[j]
					j = j + 1
				j = 0
				i = i + 1
				if i >= ROWS:
					break

	except IOError:
		luke.undo()
		screenWriting("gomokuSaved.txt could not be opened")
	twoDlistGamestate()

			


#Uses the turtle module to stamp a stone wherever the user clicks or the 
#computer moves.
#Parameters: col, row. Class int
#	parameter col: from x value pixels, is the x values on the board
#	parameter row: from y value pixels, is the y values on the board
def drawItemOnBoard(col, row):
	global COLOR
	global isGameDone
	if not isGameDone:
		if COLOR == 0:
			jim.color("white")
		else:
			jim.color("black")
		jim.shape("circle")
		jim.shapesize(1)
		jim.speed(10)
		jim.up()
		jim.goto((col * CELL_SIZE), (row * CELL_SIZE))
		jim.stamp()
		jim.ht()
	else:
		return  


def changeColor():
	global COLOR
	if (COLOR == 0):
		COLOR = 1
	else:
		COLOR = 0
	return COLOR

#Will take user clicks and change pixels to board coordinates, check if every
#move made is valid, if so, draws the item on the board, then updates the 2D list.
#Parameters: x,y. Class float
#Returns: Nothing / null
def clicked(x,y):
	global turn	
	global gameState
	global isGameDone
	global COLOR

	if (isGameDone):
		return

	handler = handleSaveOrLoadButton(x,y)

	if not handler:
		results = screenCoordToBoardCoord(x,y)
		if results == None:
			return
		(col, row) = results

		if not isMoveValid(row, col):
			luke.undo()
			screenWriting("Someone has moved there already pick again!")
			return

		drawItemOnBoard(col, row)
		updatetwoDlistGamestate(row, col)

		for line in reversed(gameState):
			print(line)

		if isWinning(row,col):
			gameOver()
			return

		changeColor() 
		AI_movement()
	else:
		wn.onscreenclick(clicked, btn=1, add=None)
	

#This function calls to other functions to set up the board and the 2D list. 
#These functions will draw the titles, labels, make the screensize, and complete
#the 2D list.
def setup():
	global ROWS
	global COLUMNS
	ROWS = gridsize
	COLUMNS = ROWS
	wn.setworldcoordinates(-500, -500, 750, 750)		#Setting World Coordinates
	wn.setup(SCREEN_HEIGHT, SCREEN_WIDTH)				#Adjusting Screen Setup
	#GameBoard Setup:
	labels()
	screenDrawing()
	GameBoard()
	
	
def officialGame():
	global COLOR
	introduction()
	setup()
	whichPlayerGoesFirst()
	
	if TURN == 0:
		if COLOR ==0:
			COLOR =1
		else:
			COLOR = 0
		AI_movement()

	wn.onscreenclick(clicked, btn=1, add=None)
	wn.mainloop()

'''def toPlayAgain():'''
	

def main():
	global COLOR

	writingForIntro()
	optionsForBoardSize()
	optionsForColour()
	startButton()
	wn.onscreenclick(startOfGameClicks, btn=1, add=None)

	wn.mainloop()


main()
