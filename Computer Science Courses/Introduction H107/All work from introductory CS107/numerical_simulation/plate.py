"""
    To try this out, run interface-graphic.py or interface-text.py

    Simulation Functions:
  
    1. create_plate
    
        Create a plate of the given size in the X and Y dimensions, with initial plate_temperature as given
    
    2. simulate_plate
  
        Simulate one second of time for a 1-cm thick metal plate, using a 1-cm grid.
        
        Parameters are:
            plate_temperatures    a 2-dimensional array of temperatures (in degrees Kelvin) of each square centimeter
            hot_x and hot_y       the location of the heated spot (in centimeters)
            hot_temp              the temperature of the heated spot (in degrees Kelvin)
            air_temp              the temperature of the air (in degrees Kelvin)
            htc                   the heat transfer constant of the metal, in Calories/degree_Kelvin/square_centimeter
            hcc                   the heat capacity constant of the metal, in degrees_Kelvin/Calorie/cubic_centimeter
            ahtc                  the heat transfer constant of the air/metal boundary, in Calories/degree_Kelvin/square_centimeter
            
        Note that hcc is measured by volume, not mass, which is somewhat unusual, but we do not actually care about the mass
        
    3. simulate_plate_N_steps
    
        Call on simulate_plate N times, return a list of average temperatures of the plate at each time

An example:


>>> set_printoptions(linewidth=120)
>>> set_printoptions(precision=2)   # print only 2 figures after decimal point

>>> temps = create_plate(6, 295.0)
>>> temps
array([[ 295.,  295.,  295.,  295.,  295.,  295.],
       [ 295.,  295.,  295.,  295.,  295.,  295.],
       [ 295.,  295.,  295.,  295.,  295.,  295.],
       [ 295.,  295.,  295.,  295.,  295.,  295.],
       [ 295.,  295.,  295.,  295.,  295.,  295.],
       [ 295.,  295.,  295.,  295.,  295.,  295.]])

>>> simulate_plate(temps, 1,3,450.0, 280, 0.2,1.0,0.05)
>>> temps
array([[ 293.5,  293.5,  293.5,  324.5,  293.5,  293.5],
       [ 293.5,  293.5,  324.5,  450. ,  324.5,  293.5],
       [ 293.5,  293.5,  293.5,  324.5,  293.5,  293.5],
       [ 293.5,  293.5,  293.5,  293.5,  293.5,  293.5],
       [ 293.5,  293.5,  293.5,  293.5,  293.5,  293.5],
       [ 293.5,  293.5,  293.5,  293.5,  293.5,  293.5]])

>>> simulate_plate(temps, 1,3,450.0, 280, 0.2,1.0,0.05)
>>> temps
array([[ 292.15,  292.15,  304.55,  332.75,  304.55,  292.15],
       [ 292.15,  298.35,  326.55,  450.  ,  326.55,  298.35],
       [ 292.15,  292.15,  304.55,  326.55,  304.55,  292.15],
       [ 292.15,  292.15,  292.15,  298.35,  292.15,  292.15],
       [ 292.15,  292.15,  292.15,  292.15,  292.15,  292.15],
       [ 292.15,  292.15,  292.15,  292.15,  292.15,  292.15]])
           
>>> simulate_plate_N_steps(temps, 1,3,450.0, 280, 0.2,1.0,0.05,100)    # doctest: +ELLIPSIS
Completed 100 simulated time steps; end-step average temps were: [303.36..., 304.07..., 304.66..., 305.14..., 305.54..., 307.8785..., 307.8785..., 307.8785...]

>>> temps
array([[ 297.04,  306.21,  327.09,  356.4 ,  330.31,  314.41],
       [ 296.38,  307.61,  342.22,  450.  ,  345.26,  315.72],
       [ 292.69,  299.41,  315.29,  339.31,  317.63,  305.36],
       [ 288.62,  291.77,  297.87,  303.96,  299.41,  295.42],
       [ 285.71,  287.08,  289.39,  291.24,  290.35,  289.18],
       [ 284.27,  284.98,  286.07,  286.87,  286.74,  286.37]])

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
    

def create_plate(size, plate_temperature):
    plate_temperatures = empty([size, size])
    plate_temperatures[:,:] = plate_temperature
    return plate_temperatures

def simulate_plate(plate_temperatures,hot_x,hot_y, hot_temp,air_temp, htc,hcc,ahtc):
    """ Simulate one time step on the plate, given array of temperatures, etc. """


def simulate_plate_N_steps(plate_temperatures,hot_x,hot_y, hot_temp,air_temp, htc,hcc,ahtc, N):
    """ Just call the one-time-step function N times... """



# copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test()
