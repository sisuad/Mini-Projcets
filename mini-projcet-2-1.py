import simplegui
import random
import math
# initialize global variables used in your code
num_range = 100


# helper function to start and restart the game
def new_game():
	global num_range, secret_num, guess_time
	guess_time = math.ceil(math.log(num_range, 2))
	secret_num = random.randrange(0, num_range)
	print "New game. Range is from 0 to", num_range
	print "Number of remaining guesses is ",int(guess_time)
	print ""
    
# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global num_range
    num_range = 100
    return new_game()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global num_range
    num_range = 1000
    return new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global guess_time
    count = 0
    count += 1
    remain_time = guess_time - count
    print "Guess was ", guess
    if remain_time > 0:
    	print "Number of remaining guesses is", int(remain_time)
    elif remain_time == 0:
    	print "Number of remaining guesses is", int(remain_time)
    	print "You ran out of guesses. The number was", secret_num

    

    if guess > secret_num:
    	print "Lower!"
    elif guess < secret_num:
    	print "Higher!"
    elif guess == secret_num:
    	print "Correct!"
    	return new_game()
    print ""

    
# create frame

frame = simplegui.create_frame("input", 200, 200)

# register event handlers for control elements
inp = frame.add_input("Guess a number", input_guess, 200)
button1 = frame.add_button("range100", range100, 200)
button2 = frame.add_button("range1000", range1000, 200)


# call new_game and start frame

frame.start()

# always remember to check your completed program against the grading rubric
new_game()