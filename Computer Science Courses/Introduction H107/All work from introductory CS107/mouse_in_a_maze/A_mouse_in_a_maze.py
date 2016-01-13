"""

THIS IS THE "GET THINGS STARTED" FILE FOR THE MOUSE IN A MAZE PROJECT

IN CMSC 105, YOU SHOULD RUN THIS FILE, BUT DO NOT NEED TO READ OR UNDERSTAND IT.

"""


from graphics import *
from find_the_cheese import *


def generate_maze():
    app.size = int(entry2.get())
    app.maze = [[[1,1,0] for y in range(app.size)] for x in range(app.size)]
    app.mouse_position = (0,0)
    app.mouse_direction = "right"
    app.cheese_position = (app.size-1,app.size-1)
    app.path = []
        
    app.multiplier = int(500/app.size)
    app.window_size = app.multiplier*app.size
    app.maze = [[[1,1,0] for y in range(app.size)] for x in range(app.size)] # create a maze with no walls [right,bottom,ischeese]
    app.visited = []
    app.clear_maze()
    app.build_maze()
    app.display_maze()
    app.display_mouse()
    app.display_cheese()  

button1 = Button(app.sideframe, text="Do 1 Step", highlightbackground="light blue", command=one_step_to_cheese)
button2 = Button(app.sideframe, text="Find the Cheese!", highlightbackground="light blue", command=move_to_cheese2)
button3 = Button(app.sideframe, text="Generate New Maze!", highlightbackground="light blue", command=generate_maze)
button4 = Button(app.sideframe, text="Reset Mouse and Cheese", highlightbackground="light blue", command=app.restart_maze)
# button5 = Button(app.sideframe, text="Eat the mouse", highlightbackground="light blue", command=app.cat_attack)
button_Debug_on = Button(app.sideframe, text="Debugging output ON", highlightbackground="light blue", command=maze_debug_on)
button_Debug_off = Button(app.sideframe, text="Debugging output OFF", highlightbackground="light blue", command=maze_debug_off)

v2 = StringVar()
v2.set("10")

frame2 = Frame(app.sideframe, bg="light blue")
label2 = Label(frame2, text="size of maze:", bg="light blue")
entry2 = Entry(frame2, textvariable=v2, width=3, highlightbackground="light blue")

button1.pack(side=TOP, anchor=W)
button2.pack(side=TOP, anchor=W)
button4.pack(side=TOP, anchor=W)
button_Debug_on.pack(side=TOP, anchor=W)
button_Debug_off.pack(side=TOP, anchor=W)
frame2.pack(side=TOP, anchor=W)
label2.pack(side=LEFT)
entry2.pack(side=LEFT)
button3.pack(side=TOP, anchor=W)
# button5.pack(side=TOP, anchor=W)

root.mainloop()