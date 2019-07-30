
import turtle
import random 

turtle.tracer(1,0)

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y)
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 4
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
    pos_list.append(snake_pos)        
    snake_stamp = snake.stamp()
    stamp_list.append(snake_stamp)

def remove_tail():
    old_stamp = stamp_list.pop(0) # last piece of tail
    snake.clearstamp(old_stamp) # erase last piece of tail
    pos_list.pop(0) # remove last piece of tail's positio


snake.direction = None

def up():
    snake.direction="Up" #Change direction to up
    move_snake() #Update the snake drawing 
    print("You pressed the up key!")

def down():
    snake.direction="Down" 
    move_snake()  
    print("You pressed the down key!")

def left():
    snake.direction="Left" 
    move_snake()  
    print("You pressed the left key!")

def right():
    snake.direction="Right"
    move_snake()  
    print("You pressed the right key!")

UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400



turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    #If snake.direction is up, then we want the snake to change
    #it’s y position by SQUARE_SIZE
    if snake.direction == "Up":
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif snake.direction=="Down":
        snake.goto(x_pos, y_pos - SQUARE_SIZE)

    if snake.direction == "Left":
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved Left!")
    elif snake.direction=="Right":
        snake.goto(x_pos + SQUARE_SIZE, y_pos)

    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    ######## SPECIAL PLACE - Remember it for Part 5

    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()
    


#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for size_turtle  in range(0,START_LENGTH) :
    x_pos = snake.xcor() #Get x-position with snake.pos()[0]
    y_pos = snake.ycor() 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos += SQUARE_SIZE 

    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Now draw the new snake part on the screen (hint, you have a 
    #function to do this
    new_stamp()



#Now go add code to the end of your  move_snake() function

def move_snake():
    
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_x_pos >= UP_EDGE:
        print("You hit the UP EDGE! Game over!")
        quit()
    elif new_x_pos >= DOWN_EDGE:
        print("You hit the DOWN EDGE! Game over!")
        quit()
    elif new_x_pos >= LEFT_EDGE:
        print("You hit the LEFT EDGE! Game over!")
        quit()
#quiting right away....




    turtle.mainloop()





