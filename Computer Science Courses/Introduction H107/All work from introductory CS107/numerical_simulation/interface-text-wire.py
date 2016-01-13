from wire import *

def print_wire(message, wire):
    def round_to_tenths(number):
        return int(10.0*number+0.5)/10.0
    
    print message
    print "\t",
    for across in range(len(wire)):
        print round_to_tenths(wire[across]), "\t",
    print " "
    
    
def text_ui():
    # It would we nice to use "input" to get lots of numbers here, but I haven't got time or energy
    init_T = 300
    hot_x  = 3
    hot_T  = 1300
    air_T  = 290
    htc    = 0.1
    hcc    = 1.0
    ahtc   = 0.001
    size   = 12
    N      = 10
    
    print "Simulating wire with values: "
    print "  init_T  = ", init_T 
    print "  hot_x   = ", hot_x   
    print "  hot_T   = ", hot_T  
    print "  air_T   = ", air_T  
    print "  htc     = ", htc    
    print "  hcc     = ", hcc    
    print "  ahtc    = ", ahtc   
    print "  size    = ", size   
    print "  N       = ", N      
    print " "  # blank line
    
    test_wire = create_wire(size, 300)
    print_wire("Initial wire", test_wire)
    simulate_wire(test_wire,hot_x, hot_T,air_T, htc, hcc, ahtc)
    print_wire("After 1 second", test_wire)
    simulate_wire(test_wire,hot_x, hot_T,air_T, htc, hcc, ahtc)
    print_wire("After 2 seconds", test_wire)
    simulate_wire_N_steps(test_wire,hot_x, hot_T,air_T, htc,hcc, ahtc,  N-2)
    print_wire("After " + str(N) + " seconds", test_wire)
    
text_ui()


