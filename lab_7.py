
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
snake.shape("circle")
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
        


snake.direction = "Up"


UP_EDGE = 250
DOWN_EDGE = -250
RIGHT_EDGE = 400
LEFT_EDGE = -400

def up():
    snake.direction="Up" #Change direction to up 
    print("You pressed the up key!")

def down():
    snake.direction="Down" 
    print("You pressed the down key!")

def left():
    snake.direction="Left" 
    print("You pressed the left key!")

def right():
    snake.direction="Right"
    print("You pressed the right key!")

turtle.onkeypress(up, "Up") # Create listener for up key
turtle.onkeypress(down, "Down")
turtle.onkeypress(left, "Left")
turtle.onkeypress(right, "Right")

turtle.listen()

turtle.register_shape("trash.gif")

food = turtle.clone()

food.shape("trash.gif")

food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

for this_food_pos in food_pos :
    food.goto(this_food_pos)
    v = food.stamp()
    food_stamps.append(v)
    food.hideturtle()


def make_food():
    min_x=-int(SIZE_X/2/SQUARE_SIZE)+1
    max_x=int(SIZE_X/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_Y/2/SQUARE_SIZE)+1
    max_y=int(SIZE_Y/2/SQUARE_SIZE)-1

    
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

    food.goto(food_x, food_y)
    food_pos.append(food.pos())
    s = food.stamp()
    food_stamps.append(s)








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

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]



    if new_x_pos >= RIGHT_EDGE:
         print("You hit the right edge! Game over!")
         quit()
    elif new_y_pos >= UP_EDGE:
        print("You hit the UP EDGE! Game over!")
        quit()
    elif  DOWN_EDGE >= new_y_pos :
        print("You hit the DOWN EDGE! Game over!")
        quit()
    elif  LEFT_EDGE >=new_x_pos :
        print("You hit the LEFT EDGE! Game over!")
        quit()

    for po in pos_list:
        if snake.pos() == po:
            print("You hit youref! Game over!")
            quit()


        

        


    #Make the snake stamp a new square on the screen
    #Hint - use a single function to do this
    new_stamp()

    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_index=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_index]) #Remove eaten food stamp
        food_pos.pop(food_index) #Remove eaten food position
        food_stamps.pop(food_index) #Remove eaten food stamp
        print("You have eaten the food!")
        new_stamp()



    #remove the last piece of the snake (Hint Functions are FUN!)
    remove_tail()

    if len(food_stamps) <= 4 :
        make_food()

    turtle.ontimer(move_snake,TIME_STEP)

    

    
    


move_snake()
    


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


    
#quiting right away!!!!!!!!!!!!!!!!!!!!!!!!!




turtle.mainloop()



