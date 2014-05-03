# Implementation of classic arcade game Pong
import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_vel = [60.0 / 60.0, -60.0 / 60.0]
ball_pos = [WIDTH / 2, HEIGHT / 2]
paddle_move = 5
score1 = 0
score2 = 0
acc = .1

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_vel[0] = random.randrange(120, 240) / 60.0
    ball_vel[1] = - random.randrange(60, 180) / 60.0
    if direction == LEFT:
        ball_vel[0] = -ball_vel[0]
    elif direction == RIGHT:
        ball_vel[0] = ball_vel[0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2, direction 
    paddle2_vel = paddle1_vel = score1 = score2 = 0
    paddle1_pos = paddle2_pos = HEIGHT / 2
    direction = random.choice([LEFT, RIGHT])
    spawn_ball(direction)

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, paddle1_vel, paddle2_vel, acc, direction

    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1] 
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT - 1) - BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]

    if 0 <= ball_pos[0] - BALL_RADIUS <= PAD_WIDTH:
        if paddle1_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * (1 + acc)
        else:
            spawn_ball(RIGHT)
            score2 += 1

    if WIDTH - PAD_WIDTH <= ball_pos[0] + BALL_RADIUS <= WIDTH - 1:
        if paddle2_pos - HALF_PAD_HEIGHT <= ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel[0] = - ball_vel[0] * (1 + acc)
        else:
            spawn_ball(LEFT)
            score1 +=1   
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, "White", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel 
    if paddle1_pos < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif HEIGHT -HALF_PAD_HEIGHT < paddle1_pos:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
        
    paddle2_pos += paddle2_vel 
    if paddle2_pos < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif HEIGHT -HALF_PAD_HEIGHT < paddle2_pos:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT

    # draw paddles
    canvas.draw_polyline([(PAD_WIDTH / 2, (paddle1_pos - PAD_HEIGHT / 2)), (PAD_WIDTH / 2, (paddle1_pos + PAD_HEIGHT / 2 ))], PAD_WIDTH, "White")
    canvas.draw_polyline([(WIDTH - PAD_WIDTH / 2, paddle2_pos - PAD_HEIGHT / 2), (WIDTH - PAD_WIDTH / 2, paddle2_pos + PAD_HEIGHT / 2)], PAD_WIDTH, "White")
    
    # draw scores
    canvas.draw_text(str(score1), ((WIDTH - PAD_WIDTH * 2) / 4, 50), 36, "White")
    canvas.draw_text(str(score2), (WIDTH -(WIDTH - PAD_WIDTH * 2) / 4, 50), 36, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle_move
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel += paddle_move
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel += paddle_move
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel -= paddle_move
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel -= paddle_move

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button = frame.add_button("Restart the game", new_game, 150)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
