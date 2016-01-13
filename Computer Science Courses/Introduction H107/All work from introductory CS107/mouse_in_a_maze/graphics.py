"""

THIS IS THE GRAPHICAL INTERFACE FOR THE MOUSE IN A MAZE PROJECT

IN CMSC 105, YOU DO NOT NEED TO READ OR UNDERSTAND IT.

"""

from Tkinter import *
import random
import math
import time
import sys

class App:

    def __init__(self, master):
        self.size = 10
        self.maze_debug = False
        self.mouse_position = (0,0)
        self.cat_position = (-1, -1)
        self.mouse_direction = "right"
        self.cheese_position = (self.size-1,self.size-1)
        self.path = []
        
        self.multiplier = int(500/self.size)
        self.window_size = self.multiplier*self.size
        self.maze = [[[1,1,0] for y in range(self.size)] for x in range(self.size)] # create a maze with no walls [right,bottom,ischeese]
        self.visited = []
        self.build_maze()     
          
        self.frame = Frame(master)
        self.frame.pack()
        
        self.canvas = Canvas(self.frame, height=(self.window_size+1), width=(self.window_size+1), highlightthickness=0, cursor="crosshair")
        self.sideframe = Frame(self.frame, height=self.window_size, width=200, bg="light blue")
        self.canvas.pack(side=LEFT)
        self.sideframe.pack(side=LEFT, expand=1, fill=BOTH)
                
        self.display_maze()
        self.display_mouse()
        self.display_cheese()
            
    def neighbors(self,x,y):
        temp = []
        if(x>0):
            temp.append((x-1,y))     
        if(y>0):
            temp.append((x,y-1))
        if(x<(self.size-1)):
            temp.append((x+1,y))     
        if(y<(self.size-1)):
            temp.append((x,y+1))
        return temp
        
    def delete_wall_between(self,node1,node2):
        assert node1[0] == node2[0] or node1[1] == node2[1]
        if(node1[0] == node2[0]): 
            if(node1[1] > node2[1]):
                self.maze[node2[0]][node2[1]][1] = 0 # delete the bottom wall of the node closest to the top
            else:
                self.maze[node1[0]][node1[1]][1] = 0
        else: # node1[1] == node2[1]
            if(node1[0] > node2[0]):
                self.maze[node2[0]][node2[1]][0] = 0 # delete the right wall of the node closest to the left
            else:
                self.maze[node1[0]][node1[1]][0] = 0
            
    def build_maze(self):
        pending_cells = [(0,0)]
        while(len(pending_cells)!=0):
            if(random.random()>0.2): # make the maze more random
                point_in_list = int(random.random()*len(pending_cells))
                temp1 = pending_cells[0:point_in_list]
                temp2 = pending_cells[point_in_list:len(pending_cells)]
                temp1.reverse()
                pending_cells = temp1 + temp2
            x = pending_cells[-1][0]
            y = pending_cells[-1][1]
            neighbors = self.neighbors(x,y)
            if(len(neighbors)!=0):
                to_be_deleted = []
                for i in range(len(neighbors)):
                    if(neighbors[i] in self.visited):
                        to_be_deleted.append(neighbors[i])
                for i in to_be_deleted:
                    neighbors.remove(i)        
            if(len(neighbors)!=0):
                node = neighbors[int(random.random()*len(neighbors))]
                self.visited.append((x,y))
                pending_cells.append(node)
                self.delete_wall_between((x,y),node)
            else:
                self.visited.append((x,y))
                pending_cells.remove((x,y))
                            
    def display_maze(self):
        self.canvas.create_line([0,0,0,self.window_size],fill="black")
        self.canvas.create_line([self.window_size,0,self.window_size,self.window_size],fill="black")
        self.canvas.create_line([0,0,self.window_size,0],fill="black")
        self.canvas.create_line([0,self.window_size,self.window_size,self.window_size],fill="black")
        for x in range(len(self.maze)):
            for y in range(len(self.maze)):
                if(self.maze[x][y][0] == 1):
                    self.canvas.create_line([(x+1)*self.multiplier,y*self.multiplier,(x+1)*self.multiplier,(y+1)*self.multiplier],fill="black")
                if(self.maze[x][y][1] == 1):
                    self.canvas.create_line([x*self.multiplier,(y+1)*self.multiplier,(x+1)*self.multiplier,(y+1)*self.multiplier],fill="black")

    def display_mouse(self):
        self.photo = PhotoImage(file="mouse.gif")
        self.photo = self.photo.zoom(25)
        self.photo = self.photo.subsample(self.size*2+4)
        
        self.photoup = PhotoImage(file="mouseup.gif")
        self.photoup = self.photoup.zoom(25)
        self.photoup = self.photoup.subsample(self.size*2+4)
        
        self.photoleft = PhotoImage(file="mouseleft.gif")
        self.photoleft = self.photoleft.zoom(25)
        self.photoleft = self.photoleft.subsample(self.size*2+4)
        
        self.photodown = PhotoImage(file="mousedown.gif")
        self.photodown = self.photodown.zoom(25)
        self.photodown = self.photodown.subsample(self.size*2+4)
        
        self.item = self.canvas.create_image(self.mouse_position[0]*self.multiplier+1, self.mouse_position[1]*self.multiplier, anchor=NW, image=self.photo)
        
    def display_cheese(self):    
        self.photo2 = PhotoImage(file="cheese.gif")
        self.photo2 = self.photo2.zoom(25)
        self.photo2 = self.photo2.subsample(self.size*2)
        
        self.item2 = self.canvas.create_image(self.cheese_position[0]*self.multiplier, self.cheese_position[1]*self.multiplier, anchor=NW, image=self.photo2)
        self.canvas.tag_lower(self.item2)
    
    def update_mouse_position(self):
        self.canvas.coords(self.item,self.mouse_position[0]*self.multiplier+1, self.mouse_position[1]*self.multiplier)
    
    def update_mouse_rotation(self):
        self.canvas.delete(self.item)
        if(app.mouse_direction == "right"):
            self.item = self.canvas.create_image(self.mouse_position[0]*self.multiplier, self.mouse_position[1]*self.multiplier+1, anchor=NW, image=self.photo)
        elif(app.mouse_direction == "left"):
            self.item = self.canvas.create_image(self.mouse_position[0]*self.multiplier, self.mouse_position[1]*self.multiplier+1, anchor=NW, image=self.photoleft)
        elif(app.mouse_direction == "up"):
            self.item = self.canvas.create_image(self.mouse_position[0]*self.multiplier, self.mouse_position[1]*self.multiplier+1, anchor=NW, image=self.photoup)
        elif(app.mouse_direction == "down"):
            self.item = self.canvas.create_image(self.mouse_position[0]*self.multiplier, self.mouse_position[1]*self.multiplier+1, anchor=NW, image=self.photodown)
        root.update_idletasks()
    
    def clear_maze(self):
        stufftoclear = self.canvas.find_all()
        for i in stufftoclear:
            self.canvas.delete(i)
            
    def restart_maze(self):
        app.mouse_position = (0,0)
        app.mouse_direction = "right"
        app.cheese_position = (app.size-1,app.size-1)
        app.path = []
        app.visited = []
        app.canvas.delete("line")
        app.display_mouse()
        app.display_cheese()  
        
    def cat_attack(self):
        print "Oh, no! The cat!"
        self.cat = PhotoImage(file="cat.gif")
        self.item8 = self.canvas.create_image(self.mouse_position[0]*self.multiplier-60, self.mouse_position[1]*self.multiplier-60, anchor=NW, image=self.cat)
        root.update_idletasks()
        time.sleep(2)
        self.canvas.delete(self.item8)
        self.mouse_position = self.cat_position
        self.update_mouse_position()
        sys.exit()
            
root = Tk()

app = App(root)

def maze_debug_on():
    app.maze_debug = True

def maze_debug_off():
    app.maze_debug = False

def maze_debug(string):
    if (app.maze_debug):
        print string
        
def maze_print(string):
    print string

def turn_left():
    maze_debug("Turning left")
    if(app.mouse_direction == "right"):
        app.mouse_direction = "up"
    elif(app.mouse_direction == "left"):
        app.mouse_direction = "down"
    elif(app.mouse_direction == "up"):
        app.mouse_direction = "left"
    elif(app.mouse_direction == "down"):
        app.mouse_direction = "right"
    app.update_mouse_rotation()   
    
def turn_right():
    maze_debug("Turning right")
    if(app.mouse_direction == "right"):
        app.mouse_direction = "down"
    elif(app.mouse_direction == "left"):
        app.mouse_direction = "up"
    elif(app.mouse_direction == "up"):
        app.mouse_direction = "right"
    elif(app.mouse_direction == "down"):
        app.mouse_direction = "left"
    app.update_mouse_rotation()

def what_is_ahead():
    if (app.mouse_position == app.cat_position):
        return "cat's stomach"
    elif (app.mouse_position == app.cheese_position):
        return "c"
    else:
        if(app.mouse_direction == "right"):
            if(app.mouse_position[0] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "left"):
            if(app.mouse_position[0] <= 0 or app.maze[app.mouse_position[0]-1][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "up"):
            if(app.mouse_position[1] <= 0 or app.maze[app.mouse_position[0]][app.mouse_position[1]-1][1] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "down"):
            if(app.mouse_position[1] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][1] == 1):
                return "w"
            else:
                return ""

def what_is_right():
    if (app.mouse_position == app.cat_position):
        return "cat's stomach"
    elif (app.mouse_position == app.cheese_position):
        return "c"
    else:
        if(app.mouse_direction == "up"):
            if(app.mouse_position[0] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "down"):
            if(app.mouse_position[0] <= 0 or app.maze[app.mouse_position[0]-1][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "left"):
            if(app.mouse_position[1] <= 0 or app.maze[app.mouse_position[0]][app.mouse_position[1]-1][1] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "right"):
            if(app.mouse_position[1] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][1] == 1):
                return "w"
            else:
                return ""
                
def what_is_left():
    if (app.mouse_position == app.cat_position):
        return "cat's stomach"
    elif (app.mouse_position == app.cheese_position):
        return "c"
    else:
        if(app.mouse_direction == "down"):
            if(app.mouse_position[0] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "up"):
            if(app.mouse_position[0] <= 0 or app.maze[app.mouse_position[0]-1][app.mouse_position[1]][0] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "right"):
            if(app.mouse_position[1] <= 0 or app.maze[app.mouse_position[0]][app.mouse_position[1]-1][1] == 1):
                return "w"
            else:
                return ""
        elif(app.mouse_direction == "left"):
            if(app.mouse_position[1] >= (app.size-1) or app.maze[app.mouse_position[0]][app.mouse_position[1]][1] == 1):
                return "w"
            else:
                return ""
            
def look_ahead():
    result = what_is_ahead()
    maze_debug("Looking ahead ... seeing " + result)
    return result

def look_right():
    result = what_is_right()
    maze_debug("Looking right ... seeing " + result)
    return result

def look_left():
    result = what_is_left()
    maze_debug("Looking left ... seeing " + result)
    return result

def move_forward():
    if(what_is_ahead() != "w" and what_is_ahead() != "cat's stomach"):
        maze_debug("Moving forward")
        old_position = app.mouse_position
        if(app.mouse_direction == "right"):
            app.mouse_position = (app.mouse_position[0]+1,app.mouse_position[1])
        elif(app.mouse_direction == "left"):
            app.mouse_position = (app.mouse_position[0]-1,app.mouse_position[1])
        elif(app.mouse_direction == "up"):
            app.mouse_position = (app.mouse_position[0],app.mouse_position[1]-1)
        elif(app.mouse_direction == "down"):
            app.mouse_position = (app.mouse_position[0],app.mouse_position[1]+1)
        app.update_mouse_position()    
        if((app.mouse_position,old_position) in app.path):
            app.canvas.delete(app.latest)
            app.path.remove((app.mouse_position,old_position))
            app.canvas.create_line([old_position[0]*app.multiplier + int(app.multiplier/2),old_position[1]*app.multiplier + int(app.multiplier/2),app.mouse_position[0]*app.multiplier + int(app.multiplier/2),app.mouse_position[1]*app.multiplier + int(app.multiplier/2)],fill="yellow",tags="line")
        else:
            app.latest = app.canvas.create_line([old_position[0]*app.multiplier + int(app.multiplier/2),old_position[1]*app.multiplier + int(app.multiplier/2),app.mouse_position[0]*app.multiplier + int(app.multiplier/2),app.mouse_position[1]*app.multiplier + int(app.multiplier/2)],fill="red",tags="line")
            app.path.append((old_position,app.mouse_position))
    elif (what_is_ahead() == "w"):
        maze_print("Trying to move through a wall!")
        app.cat_attack()
    # else do nothing!
    root.update_idletasks()
    
def eat_cheese():
    if(what_is_ahead()=="c"):
        maze_print("Eating cheese ... yum yum!")
        return True
    else:
        maze_print("Trying to eat cheese when there's none there!")
        app.cat_attack()
        return False
