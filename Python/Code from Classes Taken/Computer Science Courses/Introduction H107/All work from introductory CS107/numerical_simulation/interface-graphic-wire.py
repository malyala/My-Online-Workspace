from Tkinter import *
from wire import *
import time


"""
    Warning --- the code below is quite functional but stylistically horrific.
    It started with some lame variable names of Kris',
    and then got much worse when Dave re-ordered them without renaming them.
"""

class App:

    def __init__(self, master):

        self.frame = Frame(master)
        self.frame.pack()
        
        self.canvas = Canvas(self.frame, height=500, width=500, highlightthickness=0, cursor="crosshair")
        self.canvas.pack(side=LEFT)
        
        self.frame_side = Frame(self.frame, height=500, width=400, bg="light blue")
        self.frame_side.pack(side=LEFT, expand=1, fill=BOTH)
        
        self.canvas.bind("<ButtonRelease-1>", self.apply_iron)
        self.canvas.bind(" <B1-Motion>", self.apply_iron)
        
        v1 = StringVar()
        v1.set("310")
        
        v2 = StringVar()
        v2.set("25")
        
        v3 = StringVar()
        v3.set("25")

        
        v4 = StringVar()
        v4.set("1200")

        v8 = StringVar()
        v8.set("280")
        

        
        v5 = StringVar()
        v5.set("0.2")
        
        v6 = StringVar()
        v6.set("0.9")
        
        v7 = StringVar()
        v7.set("0.1")


        v9 = StringVar()
        v9.set("5")
        
        va = StringVar()
        va.set("50")
        
        self.buttonframe = Frame(self.frame_side, bg="light blue")
        self.button1 = Button(self.buttonframe, text="Next Frame", highlightbackground="light blue", command=self.nextframe)
        self.button2 = Button(self.buttonframe, text="Start Over", highlightbackground="light blue", command=self.startover)
        
        self.frame1 = Frame(self.frame_side, bg="light blue")
        self.label1 = Label(self.frame1, text="Initial Temperature (deg. Kelvin):", bg="light blue")
        self.entry1 = Entry(self.frame1, textvariable=v1, width=5, highlightbackground="light blue")
        
        self.frame2 = Frame(self.frame_side, bg="light blue")
        self.label2 = Label(self.frame2, text="Hot X Coordinate (cm from left):", bg="light blue")
        self.entry2 = Entry(self.frame2, textvariable=v2, width=2, highlightbackground="light blue")
        
        self.frame3 = Frame(self.frame_side, bg="light blue")
        self.label3 = Label(self.frame3, text="Hot Y Coordinate (cm from top):", bg="light blue")
        self.entry3 = Entry(self.frame3, textvariable=v3, width=2, highlightbackground="light blue")

        
        self.frame4 = Frame(self.frame_side, bg="light blue")
        self.label4 = Label(self.frame4, text="Hot Temperature (deg. Kelvin):", bg="light blue")
        self.entry4 = Entry(self.frame4, textvariable=v4, width=5, highlightbackground="light blue")

        self.frame8 = Frame(self.frame_side, bg="light blue")
        self.label8 = Label(self.frame8, text="Air Temperature (degrees Kelvin):", bg="light blue")
        self.entry8 = Entry(self.frame8, textvariable=v8, width=10, highlightbackground="light blue")

        
        self.frame5 = Frame(self.frame_side, bg="light blue")
        self.label5 = Label(self.frame5, text="Heat Transfer Constant:", bg="light blue")
        self.entry5 = Entry(self.frame5, textvariable=v5, width=5, highlightbackground="light blue")
        
        self.frame6 = Frame(self.frame_side, bg="light blue")
        self.label6 = Label(self.frame6, text="Heat Capacity Constant:", bg="light blue")
        self.entry6 = Entry(self.frame6, textvariable=v6, width=5, highlightbackground="light blue")
        
        self.frame7 = Frame(self.frame_side, bg="light blue")
        self.label7 = Label(self.frame7, text="Air Heat Transfer Constant:", bg="light blue")
        self.entry7 = Entry(self.frame7, textvariable=v7, width=5, highlightbackground="light blue")
 
        
        self.framea = Frame(self.frame_side, bg="light blue")
        self.labela = Label(self.framea, text="size of wire (cm):", bg="light blue")
        self.entrya = Entry(self.framea, textvariable=va, width=5, highlightbackground="light blue")
        
        self.frame9 = Frame(self.frame_side, bg="light blue")
        self.label9 = Label(self.frame9, text="N (number of 1-second steps):", bg="light blue")
        self.entry9 = Entry(self.frame9, textvariable=v9, width=5, highlightbackground="light blue")
        
        
        
        self.button3 = Button(self.frame_side, text="Do N Steps", highlightbackground="light blue", command=self.donsteps)
        
        self.buttonframe2 = Frame(self.frame_side, bg="light blue")
        self.button4 = Button(self.buttonframe2, text="Do N Steps with Visuals", highlightbackground="light blue", command=self.startloop)
        
        self.buttonframe.pack(side=TOP, anchor=W)
        self.button1.pack(side=LEFT, anchor=W)
        self.button2.pack(side=LEFT, anchor=W)
        
        self.frame1.pack(side=TOP, anchor=W)
        self.label1.pack(side=LEFT, anchor=W)
        self.entry1.pack(side=LEFT, anchor=W)

        self.frame2.pack(side=TOP, anchor=W)
        self.label2.pack(side=LEFT, anchor=W)
        self.entry2.pack(side=LEFT, anchor=W)
        """        
        self.frame3.pack(side=TOP, anchor=W)
        self.label3.pack(side=LEFT, anchor=W)
        self.entry3.pack(side=LEFT, anchor=W)
        """

        self.frame4.pack(side=TOP, anchor=W)
        self.label4.pack(side=LEFT, anchor=W)
        self.entry4.pack(side=LEFT, anchor=W)
        
        self.frame8.pack(side=TOP, anchor=W)
        self.label8.pack(side=LEFT, anchor=W)
        self.entry8.pack(side=LEFT, anchor=W)

        
        self.frame5.pack(side=TOP, anchor=W)
        self.label5.pack(side=LEFT, anchor=W)
        self.entry5.pack(side=LEFT, anchor=W)
        
        self.frame6.pack(side=TOP, anchor=W)
        self.label6.pack(side=LEFT, anchor=W)
        self.entry6.pack(side=LEFT, anchor=W)
        
        self.frame7.pack(side=TOP, anchor=W)
        self.label7.pack(side=LEFT, anchor=W)
        self.entry7.pack(side=LEFT, anchor=W)
        
        
        self.framea.pack(side=TOP, anchor=W)
        self.labela.pack(side=LEFT, anchor=W)
        self.entrya.pack(side=LEFT, anchor=W)
        
        self.frame9.pack(side=TOP, anchor=W)
        self.label9.pack(side=LEFT, anchor=W)
        self.entry9.pack(side=LEFT, anchor=W)
        
        self.button3.pack(side=TOP, anchor=W)
        
        self.buttonframe2.pack(side=TOP, anchor=W)
        self.button4.pack(side=LEFT, anchor=W)
        
        self.wire = create_wire(int(self.entrya.get()), float(self.entry1.get()))
        self.draw_wire(self.wire)
    
    def startloop(self):
        for i in range(int(self.entry9.get())):
            self.nextframe()
            root.update_idletasks()
        
    def stoploop(self):
        self.loop = False
    
    def nextframe(self):
        simulate_wire(self.wire,int(self.entry2.get()),
                      int(self.entry4.get()),int(self.entry8.get()),
                      float(self.entry5.get()),float(self.entry6.get()),float(self.entry7.get()))
        self.update_wire()
    
    def donsteps(self):
        simulate_wire_N_steps(self.wire,int(self.entry2.get()),
                              int(self.entry4.get()),int(self.entry8.get()),
                              float(self.entry5.get()),float(self.entry6.get()),float(self.entry7.get()),
                              int(self.entry9.get()))
        self.update_wire()

    def update_wire(self):
        self.clear_wire()
        self.draw_wire(self.wire)
    
    def apply_iron(self, event):
        self.wire[int(event.x/10)][int(event.y/10)] = int(self.entry4.get())
        self.update_wire()
    
    def draw_wire(self, wire):
        self.photo = PhotoImage(width=len(wire), height=1)
        for x in range(len(wire)):
            self.photo.put(self.get_color(wire[x]), to=(x,0))
        self.photo = self.photo.zoom(500/len(wire),20)
        self.item = self.canvas.create_image(0, 250, anchor=NW, image=self.photo)
    
    def startover(self):
        self.wire = create_wire(int(self.entrya.get()), float(self.entry1.get()))
        self.update_wire()
        
    def get_color(self, number):
        number = (number-200.0)  # Dave hacks to make 300 look better
        if(number > (2551275)):
            number = (2551275)
        if(number < 0):
            number = 0
        if(number <= 255):
            (red, green, blue) = (0,0,number)
        elif(number <= 510):
            (red, green, blue) = (0,number-255,255)
        elif(number <= 765):
            (red, green, blue) = (0,255,255 - (number - 510))
        elif(number <= 1020):
            (red, green, blue) = (number - 765,255,0)
        elif(number <= 1275):
            (red, green, blue) = (255,255 - (number - 1020),0)
        elif(number <= 2551275):
            (red, green, blue) = (255,(number - 1275)/10000,(number - 1275)/10000)
        else:
            (red, green, blue) = (255,255,255)    
        tk_rgb = "#%02x%02x%02x" % (red, green, blue)
        return tk_rgb
    
    def clear_wire(self):
        self.canvas.delete(self.item)
        

root = Tk()

app = App(root)

root.mainloop()