"""

This is a graphical user interface for the graph_coloring project.

Students should _run_ it to try out their algoritthms,
 but students should _not_ need to look at it,
 and should not change it.

"""



from Tkinter import *
from math import sqrt
from is_legal import is_a_legal_coloring
from graph_coloring import collect_legal_colorings
import random
import time

def distance(x1,x2,y1,y2):
    return sqrt(pow((x1-x2),2)+pow((y1-y2),2))

class App:

    def __init__(self, master):
        self.states = []
        self.connections = []
        self.possible_states = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.possible_colors = [("r","red"),("b","blue"),("g","dark green")]
        self.current_states = ""
        self.current_connections = ""
        self.current_coloring = ""
        self.valid_coloring = []
        self.valid_color = 0
        
        self.frame = Frame(master)
        self.frame.pack()
        
        self.canvas = Canvas(self.frame, height=500, width=500, bg="light gray", highlightthickness=0, cursor="crosshair")
        self.canvas.pack(side=LEFT)
        
        self.frame_side = Frame(self.frame, height=500, width=300, bg="orange")
        self.frame_side.pack(side=LEFT, expand=1, fill=BOTH)
        
        self.frame2 = Frame(self.frame_side, height=400, width=300, bg="orange")
        self.frame2.pack(side=TOP, anchor=N, expand=1)
        self.frame3 = Canvas(self.frame_side, height=100, width=300, bg="orange", highlightthickness=0)
        self.frame3.pack()
        self.temptext = self.frame3.create_text(150,50,text="?")
               
        v = IntVar()
        self.button1 = Radiobutton(self.frame2, text="Create State", bg="orange", variable=v, value=1, command=self.bind_create_state)
        self.button2 = Radiobutton(self.frame2, text="Connect States", bg="orange", variable=v, value=2, command=self.bind_connect_states)
        self.button3 = Radiobutton(self.frame2, text="Move State", bg="orange", variable=v, value=3, command=self.bind_move_state)
        self.button4 = Radiobutton(self.frame2, text="Delete State", bg="orange", variable=v, value=4, command=self.bind_delete)
        self.button5 = Radiobutton(self.frame2, text="Change State Color", bg="orange", variable=v, value=5, command=self.bind_change_color)
        self.button6 = Button(self.frame2, text="Create the Northeast", highlightbackground="orange", command=self.create_northeast)
        self.button7 = Button(self.frame2, text="Add Random Country", highlightbackground="orange", command=self.random_create)
        self.button8 = Button(self.frame2, text="Alien Attack!", highlightbackground="orange", command=self.alienattack)
        self.button9 = Button(self.frame2, text="Delete Everything", highlightbackground="orange", command=self.delete_all)
        self.button10 = Button(self.frame2, text="Check if Coloring is Valid", highlightbackground="orange", command=self.valid_check)
        self.button11 = Button(self.frame2, text="Generate All Valid Colorings", highlightbackground="orange", command=self.generate_valid_colors)
        self.button12 = Button(self.frame2, text="Display Next Valid Coloring", highlightbackground="orange", command=self.display_valid_coloring)
        
        self.button1.pack(side=TOP, anchor=W)
        self.button2.pack(side=TOP, anchor=W)
        self.button3.pack(side=TOP, anchor=W)
        self.button4.pack(side=TOP, anchor=W)
        self.button5.pack(side=TOP, anchor=W)
        self.button6.pack(side=TOP, anchor=W)
        self.button7.pack(side=TOP, anchor=W)
        self.button8.pack(side=TOP, anchor=W)
        self.button9.pack(side=TOP, anchor=W)
        self.button10.pack(side=TOP, anchor=W)
        self.button11.pack(side=TOP, anchor=W)
        self.button12.pack(side=TOP, anchor=W)
    
    def delete_all(self):
        self.states = []
        self.connections = []
        self.possible_states = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        self.possible_colors = [("r","red"),("b","blue"),("g","dark green")]
        self.current_states = ""
        self.current_connections = ""
        self.current_coloring = ""
        stufftoclear = self.canvas.find_all()
        for i in stufftoclear:
            self.canvas.delete(i)
    
    def bind_change_color(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>", self.change_state_color)
        
    def bind_delete(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>", self.delete_state)
        
    def bind_create_state(self):
        self.canvas.bind("<Button-1>", self.start_state)
        self.canvas.bind("<B1-Motion>", self.preview_state)
        self.canvas.bind("<ButtonRelease-1>", self.create_state)
        
    def bind_connect_states(self):
        self.canvas.bind("<Button-1>", self.start_connect)
        self.canvas.bind("<B1-Motion>", self.preview_connect)
        self.canvas.bind("<ButtonRelease-1>", self.create_connect)
    
    def bind_move_state(self):
        self.canvas.bind("<Button-1>", self.start_move)
        self.canvas.bind("<B1-Motion>", self.preview_move)
        self.canvas.bind("<ButtonRelease-1>", self.move_state)
        
    def printdata(self):
        print "States:" + self.current_states
        print "Borders:" + self.current_connections
        print "Coloring:" + self.current_coloring
    
    def valid_check(self):
        self.frame3.delete(self.temptext)
        if(self.current_connections == ""):
            self.temptext = self.frame3.create_text(150,50,text="Coloring is Valid")
#            print "Coloring is Valid! --------------------------"
#            self.printdata()
#            print "--------------------------------------------"
        elif(is_a_legal_coloring(self.current_coloring.rstrip(" "), self.current_connections)):
            self.temptext = self.frame3.create_text(150,50,text="Coloring is Valid")
#            print "Coloring is Valid --------------------------"
#            self.printdata()
#            print "--------------------------------------------"
        else:
            self.temptext = self.frame3.create_text(150,50,text="Coloring is Not Valid")
#            print "Coloring is Not Valid ----------------------"
#            self.printdata()
#            print "--------------------------------------------"

    # not really a method, but not a global function either...
    def addspace(self, old, to_add):
        if old == "":
            return to_add
        else:
            return old + " " + to_add

    def generate_new_coloring(self):
        self.current_coloring = ""
        for i in self.states:
            self.current_coloring = self.addspace(self.current_coloring, i[4]+i[5])
            
    def generate_new_states(self):
        self.current_states = ""
        for i in self.states:
            self.current_states = self.current_states + i[4]
    
    def generate_new_connections(self):
        self.current_connections = ""
        for i in self.connections:
            self.current_connections = self.addspace(self.current_connections, i[7]+i[8])
    
    def change_state_color(self,event):
        if(self.states != []):
            tempdistance = 999
            to_change = -1
            current_color = ""
            for i in self.states:
                if(distance(event.x,i[1],event.y,i[2]) < tempdistance):
                    tempdistance = distance(event.x,i[1],event.y,i[2])
                    to_change = i[0]
                    current_color = i[5]
            new_color = ()
            for i in range(len(self.possible_colors)):
                if(self.possible_colors[i][0] == current_color):
                    new_color = self.possible_colors[i-1]
            for i in range(len(self.states)):
                if(self.states[i][0] == to_change):
                    self.states[i][5] = new_color[0]
            self.generate_new_coloring()
            self.canvas.itemconfigure(to_change,fill=new_color[1])
    
    def start_state(self,event):
        self.tempcolor = self.possible_colors[int(random.random()*3)]
        self.temp = self.canvas.create_oval([event.x-12,event.y-12,event.x+12,event.y+12],fill=self.tempcolor[1])
    
    def preview_state(self,event):
        self.canvas.delete(self.temp)
        self.temp = self.canvas.create_oval([event.x-12,event.y-12,event.x+12,event.y+12],fill=self.tempcolor[1])
    
    def create_state(self,event):
        self.canvas.delete(self.temp)
        if(self.possible_states != []):
            self.temp = self.canvas.create_oval([event.x-12,event.y-12,event.x+12,event.y+12],fill=self.tempcolor[1])
            self.temp2 = self.canvas.create_text([event.x,event.y],fill="white",text=self.possible_states[0],font=("Helvetica", 12, "bold"))
            self.current_states = self.current_states + self.possible_states[0]
            self.current_coloring = self.addspace(self.current_coloring, self.possible_states[0]+self.tempcolor[0])
            self.states.append([self.temp,event.x,event.y,self.temp2,self.possible_states[0],self.tempcolor[0]])
            self.possible_states.remove(self.possible_states[0])
        
    def start_connect(self,event):
        tempdistance = 999
        self.connect_to = 0
        self.connect_to_name = 0
        self.startx = -1
        self.starty = -1
        for i in self.states:
            if(distance(event.x,i[1],event.y,i[2]) < tempdistance):
                tempdistance = distance(event.x,i[1],event.y,i[2])
                self.connect_to = i[4]
                self.connect_to_name = i[0]
                self.startx = i[1]
                self.starty = i[2]
        if(self.startx != -1):
            self.temp = self.canvas.create_line([self.startx,self.starty,event.x,event.y],fill="black")
    
    def preview_connect(self,event):
        if(self.startx != -1):
            self.canvas.delete(self.temp)
            self.temp = self.canvas.create_line([self.startx,self.starty,event.x,event.y],fill="black")
    
    def create_connect(self,event):
        if(self.startx != -1):
            tempdistance = 999
            connect_to2 = 0
            connect_to_name2 = 0
            endx = 0
            endy = 0
            for i in self.states:
                if(distance(event.x,i[1],event.y,i[2]) < tempdistance):
                    tempdistance = distance(event.x,i[1],event.y,i[2])
                    connect_to2 = i[4]
                    connect_to_name2 = i[0]
                    endx = i[1]
                    endy = i[2]
            self.canvas.delete(self.temp)
            if(self.startx != endx and self.starty != endy):                
                temp2 = -1
                for i in self.connections:
                    if((i[5] == self.connect_to_name and i[6] == connect_to_name2) or (i[5] == connect_to_name2 and i[6] == self.connect_to_name)):
                        temp2 = 1
                if(temp2 == -1):
                    self.temp = self.canvas.create_line([self.startx,self.starty,endx,endy],fill="black")
                    self.canvas.tag_lower(self.temp)
                    self.connections.append([self.temp,self.startx,self.starty,endx,endy,self.connect_to_name,connect_to_name2,self.connect_to,connect_to2])
                    self.current_connections = self.addspace(self.current_connections, self.connect_to+connect_to2)
    
    def start_move(self,event):
        if(self.states != []):
            tempdistance = 999
            self.temp = -1
            self.temp2 = -1
            for i in self.states:
                if(distance(event.x,i[1],event.y,i[2]) < tempdistance):
                    tempdistance = distance(event.x,i[1],event.y,i[2])
                    self.temp = i[0]
                    self.temp2 = i[3]
            for i in self.connections:
                if(i[5]==self.temp):
                    self.canvas.coords(i[0],event.x,event.y,i[3],i[4])
                elif(i[6]==self.temp):
                    self.canvas.coords(i[0],i[1],i[2],event.x,event.y)
            self.canvas.coords(self.temp,event.x-12,event.y-12,event.x+12,event.y+12)
            self.canvas.coords(self.temp2,event.x,event.y)

    def preview_move(self,event):
        if(self.states != []):
            for i in self.connections:
                if(i[5]==self.temp):
                    self.canvas.coords(i[0],event.x,event.y,i[3],i[4])
                    i[1] = event.x
                    i[2] = event.y
                elif(i[6]==self.temp):
                    self.canvas.coords(i[0],i[1],i[2],event.x,event.y)
                    i[3] = event.x
                    i[4] = event.y
            self.canvas.coords(self.temp,event.x-12,event.y-12,event.x+12,event.y+12)
            self.canvas.coords(self.temp2,event.x,event.y)
        
    def move_state(self,event):
        if(self.states != []):
            for i in self.states:
                if(i[0] == self.temp):
                    i[1] = event.x
                    i[2] = event.y
            self.canvas.coords(self.temp,event.x-12,event.y-12,event.x+12,event.y+12)
            self.canvas.coords(self.temp2,event.x,event.y)
            
    def delete_state(self,event):
        if(self.states != []):
            tempdistance = 999
            self.temp = -1
            self.temp2 = -1
            for i in self.states:
                if(distance(event.x,i[1],event.y,i[2]) < tempdistance):
                    tempdistance = distance(event.x,i[1],event.y,i[2])
                    self.temp = i[0]
                    self.temp2 = i[3]
                    self.temp3 = i
            self.to_be_removed = []        
            for i in self.connections:
                if(i[5]==self.temp or i[6]==self.temp):
                    self.canvas.delete(i[0])
                    self.to_be_removed.append(i)
            
            for i in self.to_be_removed:
                self.connections.remove(i)
            self.canvas.delete(self.temp)
            self.canvas.delete(self.temp2)
            self.states.remove(self.temp3)
            self.possible_states.append(self.temp3[4])
            self.generate_new_coloring()
            self.generate_new_states()
            self.generate_new_connections()
        
    def random_create(self):
        new_states = []
        link_to_states = []
        for i in range(int(random.random()*5)+4):
            if(self.possible_states != []):
                new_states.append(self.create_random_state())
                link_to_states.append(new_states[-1])
        # link some of the states
        for i in new_states:
            link_to_states.remove(i) # dont link to itself
            for j in link_to_states:
                if(random.random() > 0.3):
                    self.connect_states(i,j)
                    
    def connect_states(self,state1,state2):
        self.temp = self.canvas.create_line([state1[1],state1[2],state2[1],state2[2]],fill="black")
        self.canvas.tag_lower(self.temp)
        self.connections.append([self.temp,state1[1],state1[2],state2[1],state2[2],state1[0],state2[0],state1[3],state2[3]])
        self.current_connections = self.addspace(self.current_connections, state1[3]+state2[3])
        
    def create_random_state(self):
        if(self.possible_states != []):
            state = self.possible_states[int(random.random()*len(self.possible_states))]
            x = int(random.random()*500)
            y = int(random.random()*500)
            self.tempcolor = self.possible_colors[int(random.random()*3)]
            self.temp = self.canvas.create_oval([x-12,y-12,x+12,y+12],fill=self.tempcolor[1])
            self.temp2 = self.canvas.create_text([x,y],fill="white",text=state,font=("Helvetica", 12, "bold"))
            self.current_states = self.current_states + state
            self.current_coloring = self.addspace(self.current_coloring, state+self.tempcolor[0])
            self.states.append([self.temp,x,y,self.temp2,state,self.tempcolor[0]])
            self.possible_states.remove(state)
            return (self.temp,x,y,state)
    
    def generate_valid_colors(self):
        self.frame3.delete(self.temptext)
        self.temptext = self.frame3.create_text(150,50,text="Colorings being generated...")

        self.valid_coloring = collect_legal_colorings(self.current_states, "rgb", self.current_connections)
        # print self.valid_coloring it should be printed automatically now

        self.frame3.delete(self.temptext)
        self.temptext = self.frame3.create_text(150,50,text="See Console for colorings (if any)")

        self.valid_coloring = self.valid_coloring.split("\n")
        self.to_be_removed = []
        for i in self.valid_coloring:
            if(len(i)<2):
                self.to_be_removed.append(i)
        for i in self.to_be_removed:
            self.valid_coloring.remove(i)
        self.valid_color = 0
    
    def display_valid_coloring(self):
        # print "mooo", self.valid_coloring, self.current_coloring
        if(len(self.valid_coloring)<=self.valid_color):
            print "No more Valid Colorings!"
            self.frame3.delete(self.temptext)
            self.temptext = self.frame3.create_text(150,50,text='Click "No more valid colorings')
        else:
            self.frame3.delete(self.temptext)
            self.temptext = self.frame3.create_text(150,50,text='Click "Check if Coloring is Valid" to test')
        
            self.current_coloring = self.valid_coloring[self.valid_color]
            temp_list = self.current_coloring
            temp_list = temp_list.split(" ")  ### will this work with addspace? I don't know
            for i in temp_list:
                if(len(i)==2):
                    for j in self.states:
                        if(j[4] == i[0]):
                            j[5] = i[1]
                            for k in range(len(self.possible_colors)):
                                if(i[1] in self.possible_colors[k]):
                                    self.canvas.itemconfigure(j[0],fill=self.possible_colors[k][1])
            self.valid_color = self.valid_color + 1
    
    # This seems to both draw a state and enter it into the "states" set
    # Tweaked 9/29/06 by davew to ensure only single-letter colors are recorded
    def draw_state(self,x,y,state,color):
        self.temp = self.canvas.create_oval([x-12,y-12,x+12,y+12],fill=color)
        self.temp2 = self.canvas.create_text([x,y],fill="white",text=state,font=("Helvetica", 12, "bold"))
        record_color = 0
        for c in range(len(self.possible_colors)):
            if color == self.possible_colors[c][0]:
                record_color = color
            elif color == self.possible_colors[c][1]:
                record_color = self.possible_colors[c][0]
        if record_color == 0:
            record_color = "b"
        self.states.append([self.temp,x,y,self.temp2,state,record_color])
        self.states2.append([self.temp,x,y,state])
        self.possible_states.remove(state)    
        
    def create_northeast(self):
        # Map for the six states
        #  new Hampshire, Vermont, Massachusetts,
        #  Rhode island, Connecticut, new York
        self.delete_all()
        self.states2 = []
        
        state = "M" # massachusetts -0
        x = 250
        y = 250
        color = "blue"
        
        self.draw_state(x,y,state,color)
        
        state = "Y" # new york -1
        x = 200
        y = 250
        
        self.draw_state(x,y,state,color)
        
        state = "V" # vermont -2
        x = 230
        y = 200
        
        self.draw_state(x,y,state,color)
        
        state = "H" # new hampshire -3
        x = 280
        y = 200
        
        self.draw_state(x,y,state,color)
        
        state = "C" # conneticut -4
        x = 230
        y = 300
        
        self.draw_state(x,y,state,color)
        
        state = "R" # rhode island -5
        x = 280
        y = 300
        
        self.draw_state(x,y,state,color)
        
        #NorthEast = "HV HM VM VY MR MC MY RC CY"
        self.connect_states(self.states2[3], self.states2[2])
        self.connect_states(self.states2[3], self.states2[0])
        self.connect_states(self.states2[2], self.states2[0])
        self.connect_states(self.states2[2], self.states2[1])
        self.connect_states(self.states2[0], self.states2[5])
        self.connect_states(self.states2[0], self.states2[4])
        self.connect_states(self.states2[0], self.states2[1])
        self.connect_states(self.states2[4], self.states2[5])
        self.connect_states(self.states2[4], self.states2[1])
        
        self.generate_new_coloring()
        self.generate_new_states()
        self.generate_new_connections()

    
    def alienattack(self):
        xpos = 0
        ypos = int(random.random()*400 + 50)
        ship1 = self.canvas.create_arc(xpos-50,ypos-45,xpos+50,ypos,fill="black",outline="red",start=0,extent=180)
        ship2 = self.canvas.create_arc(xpos-100,ypos-27,xpos+100,ypos+10,fill="dark red",outline="red",start=10,extent=160)
        ship3 = self.canvas.create_arc(xpos-100,ypos-34,xpos+100,ypos+3,fill="dark red",outline="red",start=190,extent=160)
        for xpos in range(-100,600):
            self.canvas.delete(ship1)
            self.canvas.delete(ship2)
            self.canvas.delete(ship3)
            ship1 = self.canvas.create_arc(xpos-50,ypos-45,xpos+50,ypos,fill="black",outline="red",start=0,extent=180)
            ship2 = self.canvas.create_arc(xpos-100,ypos-27,xpos+100,ypos+10,fill="dark red",outline="red",start=10,extent=160)
            ship3 = self.canvas.create_arc(xpos-100,ypos-34,xpos+100,ypos+3,fill="dark red",outline="red",start=190,extent=160)
            if(random.random()>0.99 and self.connections!=[]):
                connection_to_delete = self.connections[int(random.random()*len(self.connections))]
                self.connections.remove(connection_to_delete)             
                self.temp = self.canvas.create_line([xpos,ypos,(connection_to_delete[1]+connection_to_delete[3])/2,(connection_to_delete[2]+connection_to_delete[4])/2],fill="red",width=5)
                self.canvas.tag_lower(self.temp)
                root.update_idletasks()
                time.sleep(0.05)
                self.canvas.delete(connection_to_delete[0])
                self.canvas.delete(self.temp)
            root.update_idletasks()
        self.canvas.delete(ship1)
        self.canvas.delete(ship2)
        self.canvas.delete(ship3)
        self.generate_new_connections()
        
root = Tk()

app = App(root)

root.mainloop()