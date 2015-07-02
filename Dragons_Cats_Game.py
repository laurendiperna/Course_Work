from sys import exit
#this function exits the game and makes you start over completely
#I start with die() because I'm running these blocks separately in ipython notebook
#you need seven definitions to play this game
#die(), cat_room(), start(), infinite_loop(), ice_room(), treasure_trove(), dragon_room() (blocks also follow this order)

def die(why):
    print why #having "why" allows you to reprint whatever you have in die before saying Game over and exiting
    exit(0)

#This function is for the cat_room

#after you run start() you have the choice to go left or right in the game
#the cat_room() is the room to the right, start() should call this function 


def cat_room():
    print "There is a cat blocking the next door. What do you do?"
    
    cat_choice = raw_input('> ') #prompt the user to answer your question
    
    if cat_choice == "pet cat": #if they type in 'pet cat' the following should be executed
        print "the cat moves and you can open the next door."
        next_choice = raw_input("please type 'open next door' to continue > ")
        
        if next_choice == "open next door": #if they follow the raw_input instruction, the program should call ice_room()
                ice_room()
        else:
            cat_room()#added this in 3/18 so that the person doesn't get kicked out, and the function starts over
            #die("I know you know how to type. Guess you get to start over, sorry.")
            #USE the code below once you know the above works, in the meantime use die() to catch mistakes
            #print "I know you know how to type. Try again." #if they miss type they have to start over with cat_room() 
            #cat_room()
                
    elif cat_choice == "taunt cat": #if they type in 'taunt cat' then the following should be executed
        print "The cat scratches you and stays put"
        print "Not the greatest idea being a meanie. Try again."
        cat_room() #the cat_room() should start over if they choose 'taunt cat'
    else:          #this else statement is to catch anything else you do that isn't expected, and makes you start over
        cat_room() #added this in 3/18 so that the person doesn't get kicked out, and the function starts over
        #print "This game isnt' that sophisticated."
        #print "Your two choices were 'pet cat' or 'taunt cat'."
        #die("With that in mind, please try again. Guess you get to start over, sorry.")
        #ONCE YOU KNOW THE CODE WORKS just use the below instead of die
        #print "With that in mind, please try again."
        #cat_room() 

#let's start the game in the first block of code with start()

#actually I just realized since start calls other definitions I need to define
#those before I can run this to check if it works, so I'm going to start with cat_room()
def start():
    global position #just added this in to see if you would help not break the dragon room
    global hands
    position = "front door" #hopefully this variable can get overwritten
    hands = "warm"
    print "You approach a house. there are two doors."
    print "Do you take the left door or the right door?"
    
    door_choice = raw_input('> ')
    
    if "right" in door_choice:  #this should accept anything as long as you say 'right' within your raw_input for door_choice
        cat_room()              #this should call cat_room()
    elif "left" in door_choice: #this should accept anything as long as you say 'left' within your raw_input for door_choice
        position = "front door" #you need this variable for dragon_room(), to know from where the player enters
        dragon_room()           #this should call dragon_room()
    else:
        print "I don't understand, please type 'right' or 'left'"
        start() #I'm not sure I can call a definition within a def (I think you can,)
                #if not just use exit(0) to start the game over
        #you need a way to prompt the user for input again and let
        #them do through the if statement again/ I don't know how to do this without using a While statement

#this is the block of code for the infinite_loop
#it gets called in the ice_block function
#I don't know how to do this yet but I'd like to cause a prompt to take 2 seconds to appear
#WORK ON adding limit to how long this loop can run like while number = 4 is less then 5, so they can only do 5 iterations

def infinite_loop():
    print "okay you've wait long enough, do you still want to wait?"
    
    y_n_choice = True #set a yes no choice variable to True so you can make a while loop
                      #AT SOME POINT add counter so that the loop stops after 5 tries
    while True:       #you capitilized "while" don't do that 
        infinite_choice = raw_input('yes or no > ')
        if infinite_choice == "yes":
            print """
            Ice has melted a bit more, waiting could be good. 
            Do you want to keep waiting?
            """
            y_n_choice = True
            
        elif infinite_choice == "no":
            print "Be a little patient the ice seems to be melting."
            print "Are you willing to keep waiting?"
            y_n_choice = True
            
        elif infinite_choice == "@#$%! this": 
            print "I agree!"
            print "let's pick 1 or 2 as a choice next time."
            y_n_choice = False
            ice_room()
            
        else:
            print "I have no idea what that means."
            

#this is the block of code for the ice_room(), which is connected to the cat_room() and treasure_trove()
#when a player starts the game the cat_room is the first room and the ice_room is the second, the treasure_trove is third
#the dragon_room is the first door on the left when the player starts, and it connects diretly to the treasure_trove room

def ice_room():
    global hands #I just added this in to see if defining 'hands' globally will make treasure_trove work
    print """
    You enter the next room. There is a block of ice and through the ice you see
    the next door you need to go through. You can 1) push 2) stand or 3) just wait for
    the block to melt.
    """
    
    ice_choice = raw_input('please pick 1, 2, or 3 > ')
    
    if ice_choice == "1":
        print """
        The block slides away from the door. You can now go through the door,
        ta da!
        Though your hands are pretty frozen now...
        """
        hands = "frozen" #this will be an important variable in the treasure_trove()
        treasure_trove() #this should call the treasure_trove function
        
    elif ice_choice == "2":
        #move hands and print statement up over the bottom print statment
        hands = "warm" #this variable will be important for the treasure_trove function
        print hands #WHY IS THIS CAUSING AN ERROR? FOR SOME REASON the variable hands can't be assigned "warm"
        print "The ice block melts into a puddle and you can open the next door"
        treasure_trove()#this should call the treasure_trove function        
        
    elif ice_choice == "3":
        print "Wait until I check back with you"
        infinite_loop() #this should start the infinite loop
        hands = "warm"
    else:
        die('make sure to just type 1 2 or 3 next time. Guess you have to start over.')

#this is for the treasure_trove function

def treasure_trove(): #this didn't work so I removed hands:I just added 'hands' into the parantheses to see if argv works in the first cell
    global position   #and to see if 'hands' gets passed to treasure_trove from ice_room in the way I hoped for.
    position = "back door" #added this in see above reason
    print """
    In the next room you stumble upon a giant treasure trove,
    that has a note saying "Open me!"
    """
    treasure_trove_choice = raw_input("Type 'open box' > ")
    
    if treasure_trove_choice == "open box" and hands == "frozen":
        print "Your hands are too cold, you need to find a fire-breathing dragon" #you forgot to type print here
        hint_choice = raw_input("Hint: try the left door > ")
        
        if hint_choice == "left door":
            print "You're very wise to listen."
            dragon_room() #this calls the dragon_room function
            #position = "back door" removed this line #this variable is used for dragon_room, to knowing how the player came into the room
        else:
            die("Next time just type 'left door'. Time to begin again.")
            
    elif treasure_trove_choice == "open box" and hands == "warm":
        print "The box opens. Inside you find soooo much gold! AND a key to exit the door to the right"
        print "Yeah you didn't notice that door because you were too excited about the treasure trove."
        die("Congrats, you win. Game Over")
    else:
        die("Sorry I don't understand. Time to begin again.")

        
#this is for the dragon_room() function
#requires that you define position as a global function, but it will also be a global function in ice_box so I think it can 
#get overwritten

def dragon_room():
    print """
    In this room there is a dragon... SMACK IN THE MIDDLE OF THE ROOM!
    Do you try to sneak past to get to the door on the other side?
    Or do you poke the dragon?
    """
    dragon_choice = raw_input("type 'sneak past' or 'poke'> ")
    
    #YOU NEED TO CLEAN THESE IF STATMENTS UP SO THEY ARE NOT SO COMPLICATED
    if dragon_choice == "sneak past":
        print "The dragon wakes up and eats you!"
        die("What a way to go out.")
        
    elif dragon_choice == "poke" and hands == "frozen" and position == "back door":
        print "The dragon raises one eyelid and shoots a flame at your hands."
        print """
        Your hands thaw and you can go back to the treasure trove room,
        where you open the chest and find sooo much gold! 
        AND
        a key to exit through the final door!
        """
        die("Congrats, you win. Game over.")
        
    elif dragon_choice == "poke" and hands == "warm" and position == "back door":
        print "Your hands are burnt to a crisp."
        print "You run back to the room with a giant block of ice"
        ice_room() #I'm not sure what will happen if you go back to the ice room with this new set of variables attached
                   #to you. FIGURE THIS OUT, I think the variables should just be overwritten
    elif dragon_choice == "poke" and position == "front door":
        print "Your hands are burnt to a crisp."
        die("Those are some serious burns. Forget this game. Go get treated.")
            
    else:
        die("I don't understand what you entered. Guess you get to start over.")
        

#start the game by pressing enter
start()