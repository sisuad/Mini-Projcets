# implementation of card game - Memory
import simplegui
import random
interval = 800 // 16

# helper function to initialize globals
def new_game():
    global cards, exposed, state, card_pos, Turns
    cards = range(0, 8) * 2
    random.shuffle(cards)
    exposed = [False] * 16
    state = Turns = 0
    label.set_text('Turns = ' + str(Turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, interval, state, card_pos1, card_pos2, Turns
    i = pos[0] // interval 
    if exposed[i] == False:
        exposed[i] = True 
        if state == 0:
            state = 1
            Turns += 1
            card_pos1 = i
            
        elif state == 1:
           state = 2
           card_pos2 = i

        elif state == 2:
            state = 1
            Turns += 1
            if cards[card_pos1] != cards[card_pos2]:
                exposed[card_pos1] = exposed[card_pos2] = False

            card_pos1 = i
            cards[card_pos1] = cards[i]    
                
    label.set_text('Turns = ' + str(Turns))
                       
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    num_pos = [15, 70]
    polyline_pos = [25, 0, 25, 100]
    for i in range(len(cards)):
        if exposed[i] == False:
            canvas.draw_polygon([[polyline_pos[0] + interval * i, polyline_pos[1]], [polyline_pos[2] + interval * i, polyline_pos[3]]], 50, "Green")
            canvas.draw_polyline([[polyline_pos[0] + 25 + interval * i, polyline_pos[1]], [polyline_pos[2] + 25 + interval * i, polyline_pos[3]]], 2, "black")
        else:    
            canvas.draw_text(str(cards[i]), (num_pos[0] + interval * i, num_pos[1]), 48, "White")
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
