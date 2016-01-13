"""
    To try this out, run interface-graphic.py or interface-text.py

    Simulation Functions:
  
    1. create_wire
    
        Create a wire of the given size, with initial wire_temperature as given
    
    2. simulate_wire
  
        Simulate one second of time for a 1-cm thick metal wire, using a 1-cm grid.
        
        Parameters are:
            wire_temperatures    a 1-dimensional array of temperatures (in degrees Kelvin) of each square centimeter
            hot_spot             the location of the heated spot (in centimeters)
            hot_temp             the temperature of the heated spot (in degrees Kelvin)
            air_temp             the temperature of the air (in degrees Kelvin)
            htc                  the heat transfer constant of the metal, in Calories/degree_Kelvin/square_centimeter
            hcc                  the heat capacity constant of the metal, in degrees_Kelvin/Calorie/cubic_centimeter
            ahtc                 the heat transfer constant of the air/metal boundary, in Calories/degree_Kelvin/square_centimeter
            
        Note that hcc is measured by volume, not mass, which is somewhat unusual, but we do not actually care about the mass
        
    3. simulate_wire_N_steps
    
        Call on simulate_wire N times, return a list of average temperatures of the plate at each time.

Here's an example:

First, we create the set of temperatures with "create_wire", like so:

>>> wire_temperatures = create_wire(10,295.0)
>>> set_printoptions(linewidth=120)
>>> set_printoptions(precision=2)   # print only 2 figures after decimal point
>>> wire_temperatures
array([ 295.,  295.,  295.,  295.,  295.,  295.,  295.,  295.,  295.,  295.])

Then, we can simulate a single time step with each call to "simulate_wire":

>>> simulate_wire(wire_temperatures, 2,450.0, 280, 0.2,1.0,0.05)
>>> wire_temperatures
array([ 292.,  323.,  450.,  323.,  292.,  292.,  292.,  292.,  292.,  292.])
>>> simulate_wire(wire_temperatures, 2,450.0, 280, 0.2,1.0,0.05)
>>> wire_temperatures
array([ 295.8,  333.6,  450. ,  333.6,  295.8,  289.6,  289.6,  289.6,  289.6,  289.6])

To do lots of steps in one call and print average temperatures:

>>> simulate_wire_N_steps(wire_temperatures, 2,450.0, 280, 0.2,1.0,0.05, 12)    # doctest: +ELLIPSIS
Completed 12 simulated time steps; end-step average temps were: [316..., 317.1..., 317.4..., 317.6..., 317.7..., 317.8..., 317.8..., 317.8..., 317.8..., 317.8..., 317.8..., 317.7...]
>>> wire_temperatures
array([ 313.6 ,  347.75,  450.  ,  344.92,  304.81,  289.56,  283.83,  281.73,  281.  ,  280.78])

Note we may want to move the heating spot somewhere else:

>>> simulate_wire_N_steps(wire_temperatures, 5,600.0, 280, 0.2,1.0,0.05,4)    # doctest: +ELLIPSIS
Completed 4 simulated time steps; end-step average temps were: [353.7..., 355.1..., 355.2..., 354.9...]
>>> wire_temperatures
array([ 306.65,  312.21,  319.67,  338.03,  404.49,  600.  ,  390.01,  310.83,  286.18,  280.96])

"""
# make Python look in the right place for logic.py, or complain if it doesn't
try:
    import sys
    sys.path.append('/home/courses/python')
    from logic import *
except:
    print "Can't find logic.py; if this happens in the CS teaching lab, tell your instructor"
    print "   If you are using a different computer, add logic.py to your project"
    print "   (You can download logic.py from http://www.cs.haverford.edu/resources/software/logic.py)"
    sys.exit(1)


# Hopefully the following will stop any infinite loops without killing anything correct
import resource
resource.setrlimit(resource.RLIMIT_CPU, [1000, 1000])

try:
    from numpy import *
except:
    print "Can't seem to find numpy (Numeric Python) library on this computer"
    sys.exit(1)



def create_wire(size, wire_temperature):
    wire_temperatures = zeros(size)
    wire_temperatures[0:] = wire_temperature  # fill the array
    return wire_temperatures

def average_temp(wire_temperatures):
    precondition(len(wire_temperatures) > 0)
    total = 0
    for temp in wire_temperatures:
        total = total + temp  # not physically meaningful, but gets the right answer...
    return total/len(wire_temperatures)

def simulate_wire(wire_temperatures,hot_spot, hot_temp,air_temp, htc,hcc,ahtc):
    """ Simulate one time step on the wire, given array of temperatures, etc. """
    wire_temperatures[hot_spot] = hot_temp
    
    # First, calculate heat flow _into_ every element of wire
    heat_in = zeros_like(wire_temperatures)
    for place in range(len(wire_temperatures)):
        faces = 4   # Number of faces exposed to the air
        if(place!=0):
            from_left = (wire_temperatures[place-1] - wire_temperatures[place]) * htc # heat from left
        else:
            from_left = 0
    
        if(place<(len(wire_temperatures)-1)):
            from_right = (wire_temperatures[place+1] - wire_temperatures[place]) * htc # heat from right
        else:
            from_right = 0
                    
        from_air = (air_temp - wire_temperatures[place]) * faces*ahtc # heat from air
        
        heat_in[place] = from_left + from_right + from_air
    
    # Now, add the heat we found above to the old temperatures
    for place in range(len(wire_temperatures)):
        wire_temperatures[place] = wire_temperatures[place] + heat_in[place] * hcc
        
    # Finally, restore the temperature of the heated spot, and we're done!
    wire_temperatures[hot_spot] = hot_temp


def simulate_wire_N_steps(wire_temperatures,hot_spot, hot_temp,air_temp, htc,hcc,ahtc, N):
    """ Just call the one-time-step function N times... """
    all_averages = []  # log of temperatures at end of time steps
    for t in range(N):
        simulate_wire(wire_temperatures,hot_spot, hot_temp,air_temp, htc,hcc,ahtc)
        all_averages.append(average_temp(wire_temperatures))
    print "Completed", N, "simulated time steps; end-step average temps were:", all_averages
#    import matplotlib
#    matplotlib.plot(all_averages)



# copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
