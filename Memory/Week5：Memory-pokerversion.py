# implementation of card game - Memory
import simplegui
import random
interval = 800 // 16
image = []
blackground = simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/4efb/536499be0a7de.jpg")
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/b0fa/5364a7455d52b.png"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/8cfc/5364a75ea9410.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/d558/5364a772f2fb7.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/e89c/5364a78bc3dd4.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/1e0d/5364a7a2d3fa4.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/786e/5364a7bc7776a.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/6545/5364a7db920f2.jpg"))
image.append(simplegui.load_image("http://a1.eoe.cn/www/home/201405/03/c176/5364a7efb094b.jpg"))
image = image * 2
# helper function to initialize globals
def new_game():
    global exposed, state, Turns
    random.shuffle(image )
    exposed = [False] * 16
    state = Turns = 0
    label.set_text('Turns = ' + str(Turns))
    
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, interval, state, image_pos1, image_pos2, Turns
    i = pos[0] // interval 
    if exposed[i] == False:
        exposed[i] = True 
        if state == 0:
            state = 1
            Turns += 1
            image_pos1 = i
            
        elif state == 1:
           state = 2
           image_pos2 = i

        elif state == 2:
            state = 1
            Turns += 1
            if image[image_pos1] != image[image_pos2]:
                exposed[image_pos1] = exposed[image_pos2] = False

            image_pos1 = i
            image[image_pos1] = image[i]    
                
    label.set_text('Turns = ' + str(Turns))
                       
# image are logically 50x100 pixels in size    
def draw(canvas):
    global exposed
    for i in range(len(image)):
        if exposed[i] == False:
            canvas.draw_image(blackground, (25, 37.5), (50, 75), (25 + interval * i, 37.5), (50, 75))
        else:    
            canvas.draw_image(image[i], (25, 37.5), (50, 75), (25 + interval * i, 37.5), (50, 75))
            
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 75)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
