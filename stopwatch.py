# "Stopwatch: The Game"

import simplegui

# define global variables
time = 0
time_text = ''
counter = 0
seconds_unit = 0
seconds_ten = 0
minutes = 0
total_stops = 0
total_wins = 0
game_start = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
   global time_text
   global counter
   global seconds_unit
   global seconds_ten
   global minutes
   counter = t%10
   seconds_unit = int(t/10)%10
   seconds_ten = int(t/100)%6
   minutes = int(t/600)%600
   time_text = str(minutes) + ':' + str(seconds_ten) + str(seconds_unit) + '.' + str(counter)
   return time_text

# define event handlers for buttons: "Start", "Stop", "Reset"
def start():
    global game_start
    timer.start()
    #set a flag for the game start
    game_start = True
    sound_loose.rewind()
    sound_win.rewind()

def stop():
   global total_wins
   global total_stops
   global game_start
   timer.stop()
   if game_start == True:
        if counter == 0:
            total_wins += 1
            sound_win.play()
        else:
            total_stops += 1
            sound_loose.play()
        game_start = False
        
def reset():
    global time
    global total_stops
    global total_wins
    timer.stop()
    time = 0
    format(time)
    total_stops = 0
    total_wins = 0
    sound_loose.pause()
    sound_win.pause()
    
def draw(canvas):
     canvas.draw_text(str(minutes) + ':' + str(seconds_ten) + str(seconds_unit) + '.' + str(counter),(120,85),30, "Red")
     canvas.draw_text(str(total_wins) + '/' + str(total_stops), (250,30), 20, "Green")
        
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    format(time)

# create timer
timer = simplegui.create_timer(100, timer_handler)
    
# create frame
frame = simplegui.create_frame("Stopwatch: The game", 300, 150)

frame.set_draw_handler(draw)
frame.add_button("Start", start, 70)
frame.add_button("Stop", stop, 70)
frame.add_button("Reset", reset, 70)

sound_loose = simplegui.load_sound("http://static1.grsites.com/archive/sounds/people/people136.wav")
sound_win = simplegui.load_sound("http://static1.grsites.com/archive/sounds/recreation/recreation006.wav")

# start frame
frame.start()

