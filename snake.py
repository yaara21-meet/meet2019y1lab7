
import turtle
import random 

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6
TIME_STEP = 100


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []


snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()



#Function to draw a part of the snake on the screen
def new_stamp():
    snake_pos = snake.pos()
    pos_lost.append(snake_pos)        
    snake_stanp = snake.stamp()
    stamp_list.append(snake_pos)


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for size_turtle  in range(START_LENGTH) :
    x_pos = snake.pos() #Get x-position with snake.pos()[0]
    y_pos = snake.pos() 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos += SQUARE_SIZE 

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new stamp()






