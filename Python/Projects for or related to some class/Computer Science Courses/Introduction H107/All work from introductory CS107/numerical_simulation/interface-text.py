from plate import *

def print_plate(message, plate):
    def round_to_tenths(number):
        return int(10.0*number+0.5)/10.0
    
    print message
    for row in range(len(plate)):
        print "\t",
        for across in range(len(plate[row])):
            print round_to_tenths(plate[across][row]), "\t",
        print " "
    
    
def text_ui():
    # It would we nice to use "input" to get lots of numbers here, but I haven't got time or energy
    init_T = 300
    hot_x  = 3
    hot_y  = 1
    hot_T  = 1300
    air_T  = 290
    htc    = 0.1
    hcc    = 1.0
    ahtc   = 0.001
    size   = 8
    N      = 10

    ## AT THIS POINT WE SHOULD CHECK FOR BAD VALUES

    print "Simulating plate with values: "
    print "  init_T  = ", init_T 
    print "  hot_x   = ", hot_x  
    print "  hot_y   = ", hot_y  
    print "  hot_T   = ", hot_T  
    print "  air_T   = ", air_T  
    print "  htc     = ", htc    
    print "  hcc     = ", hcc    
    print "  ahtc    = ", ahtc   
    print "  size    = ", size   
    print "  N       = ", N      
    print " "  # blank line
    
    test_plate = create_plate(size, 300)
    print_plate("Initial plate", test_plate)
    simulate_plate(test_plate,hot_x,hot_y, hot_T,air_T, htc, hcc, ahtc)
    print_plate("After 1 second", test_plate)
    simulate_plate(test_plate,hot_x,hot_y, hot_T,air_T, htc, hcc, ahtc)
    print_plate("After 2 seconds", test_plate)
    simulate_plate_N_steps(test_plate,hot_x,hot_y, hot_T,air_T, htc,hcc, ahtc,  N-2)
    print_plate("After " + str(N) + " seconds", test_plate)
    
text_ui()


