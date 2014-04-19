import simplegui
# define global variables
count = 0
message = "0:00.0"
stop_time = 0
interval = 100
correct_time = 0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(count):
    global message
    A = int( count // 600)
    B = int( count % 600 / 10 // 10)
    C = int( count % 600 / 10 % 10)
    D = int( count % 600 % 10 % 10)
    message = str(A) + ":" + str(B) + str(C) + "." + str(D)       
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global stop_time, correct_time
    if not timer.is_running():
        timer.stop()   
    else:
        stop_time += 1
        timer.stop()
        if count % 10 == 0:
            correct_time += 1

def reset_handler():
    global count, correct_time, stop_time
    timer.stop()
    count = 0
    stop_time = 0
    correct_time =0
    format(count)

# define event handler for timer with 0.1 sec interval
def tick():
    global  count
    count += 1
    if count == 6000:
        count = 0
    format(count)

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(message), (65, 80), 30, "white")
    canvas.draw_text(str(correct_time) + "/" + str(stop_time), (163, 20), 20, "green")

# create frame
frame = simplegui.create_frame("Stopwatch", 200, 150)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, tick)

# register event handlers
button1 = frame.add_button("Start", start_handler, 100,)
button2 = frame.add_button("Stop", stop_handler, 100)
button3 = frame.add_button("Reset", reset_handler, 100)

# start frame
frame.start()