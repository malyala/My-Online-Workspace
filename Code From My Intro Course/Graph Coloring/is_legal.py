"""
    CS105 first graph_coloring lab:
     determining whether or not a proposed coloring for a graph is legal
    
    is_a_legal_coloring should return True if the coloring is legal, and False otherwise
    
    it takes two parameters,
        possible_coloring, a proposed coloring
            Each state will be represented by a single letter such as V for Vermont,
                and each color with a single letter such as r for red, and thus the
                coloring will be a space-separated set of pairs of state and color letters,
                e.g. "Cr Mb Vr Hg Yg" could mean Ct is red, Ma is blue, Vt is red, etc.
        borders, a set of borders, e.g. "CM CY MV MH MY VH VY" for Ct bordering Ma, etc.
        
Examples:
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "CM CY MV MH MY VH VY")
True

If Ct and Ma are both red, there's trouble
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False

##############################################################################
#
#        REPLACE THIS WITH YOUR TEST-SUITE
#


#Average valid coloring
>>> is_a_legal_coloring('Ob Fr Sb Rg Wg', 'OW FS FR FW SR')
True

#Average not valid coloring- few bad borders
>>> is_a_legal_coloring('Ar Dg Lg Fg Ir Hb', 'AD AI AH DF DI DH LF LI LH')
False

#two states, same color, obv false
>>> is_a_legal_coloring('Ar Br', 'BA')
False

#two states, same color but isolated, obv true
>>> is_a_legal_coloring('Ar Br', '')
True

#two states, diff colors, obv true
>>> is_a_legal_coloring('Ar Bg', 'BA')
True

#Many states, all the same color-obv false
>>> is_a_legal_coloring('Lg Og Yg Fg Xg', 'LO LF LX YF YX FX')
False

#Almost a legal coloring, one pair of same colors
>>> is_a_legal_coloring('Mb Jr Tg Kr Lg', 'MT MK ML JT JK TK KL')
False

#4 states with each state connected to other three- obv false
>>> is_a_legal_coloring('Ag Br Cb Dg', 'CD DB BC BA AC DA')
False


#almost correct, lots of correct links with one broken one:
#circle of alternating 2 colors- excpet one with color #3 and with one that is not the same color connecting to all others
>>> is_a_legal_coloring('Ab Bg Cb Dr Eb Fg Gb Hg Ib Jg Kb Lg Mb Ng Ob Pg Qr Rg Sb Tg Ub Vg Wb Xg Yb Zg', 'AB BC CD DE EF FG GH HI IJ JK KL LM MN NO OP PQ QR RS ST TU UV VW WX XY YZ ZA EQ QS QT QU QV QW QX QY QZ QA QB QC QD QF QG QH QI QJ QK QL QM QN QO')
False

#almost correct, one border fails- subclique of size four
>>> is_a_legal_coloring('Ig Wb Mr Ab', 'IW IM WM IA AM AW')
False

#Close to correct, has 2 bad borders
>>> is_a_legal_coloring('Kg Ub Ir Og Ab Bb', 'KI UI UO IO IA AK AB BU')
False

#===============================

#one state, obv true
>>> is_a_legal_coloring('Ar', '')
True




#It seems that only algorithms 1 and 4 are correct


##############################################################################
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



"""
###############is_a_legal_coloring design comment:

1. A legal coloring has within it a smaller problem of a legal coloring of one less state
ex:
this: 
>>> is_a_legal_coloring('Ob Fr Sb Rg Wg', 'OW FS FR FW SR')
has inside of it, the simpler problem
this:
>>> is_a_legal_coloring('Fr Sb Rg Wg', 'OW FS FR FW SR')

2.  We solve the general problem by combining the truth value of the smaller problem using the and operation with the truth value of the ommitted state
and all the non ommited states.

With the previous example:
>>> is_a_legal_coloring('Ob Fr Sb Rg Wg', 'OW FS FR FW SR')
is like asking: 
>>> is_a_legal_coloring('Fr Sb Rg Wg', 'OW FS FR FW SR') AND 

#This combination below would be the func call onetoall("Ob", "Fr Sb Rg Wg",'OW FS FR FW SR' ) 

is_a_legal_coloring('Ob Fr', 'OW FS FR FW SR')AND
is_a_legal_coloring('Ob Sb', 'OW FS FR FW SR') AND
is_a_legal_coloring('Ob Rg', 'OW FS FR FW SR') AND
is_a_legal_coloring('Ob Wg', 'OW FS FR FW SR')

To make all these combinations shown above, we use a function called onetoall which takes in one state, a string of all other states, 
and a string of the borders and returns the 'and' combination of booleans of {the one state paired with each other state} in the string of borders.





3. If we got down to two or less states- this would be too simple to pass the precondition. It would be a problem not worth asking. 

4. The base case is calling the function with two states. In this case we simply search if there exists a connection 
in the list of borders and if so, check if the states have different colors
ex:
>>> is_a_legal_coloring('Ob Wg', 'OW FS FR FW SR')
first we search for OW or WO in 'OW FS FW SR'
if there is a border, we check 'Ob'[1] != 'Wg'[1]
and if this test fails, we return false
otherwise true

5. Given the precondition that we must have at least two states, we can then say since the number of states decreases by one
in each recursive call, it must eventually reach 2- the base case. 

"""




"""
        # Design comment for onetoall:
just basic recursive design with checking if the one works with the first in rest 
then addting that truth value to the recursive call with 
the base case of there being just one other country left




        #test suite for onetoall:

this is just the test suite for is legal with the first element as a seperate argument...
      
"""

def onetoall(one, rest, borders):
    if len(rest) == 2:
        order1 = one[0] + rest[0]
        order2 = order1[::-1]
        if order1 in borders or order2 in borders:
            return one[1] != rest[1]
        else: return True
    else:
        order1 = one[0] + rest[0]
        order2 = order1[::-1]
        
        return onetoall(one, rest[:2], borders) and \
        onetoall(one, rest[3:], borders)




def is_a_legal_coloring(possible_coloring, borders):
    precondition(len(possible_coloring) >= 2)
    want_to_print_stuff = not are_we_doing_doctest() and not are_we_doing_coloring_enumeration()
    if want_to_print_stuff:
        print "Calling is_a_legal_coloring..."
        print ">>> is_a_legal_coloring('"+ possible_coloring + "', '" + borders + "')"

    MODE='mine'  # set to 'test samples', 'answer key', or 'mine'
    
    if MODE=='mine':
        """
        if len(possible_coloring) == 5:
            check1 = possible_coloring[0] + possible_coloring[3]
            check2 = check1[::-1]
            
            if check1 in borders or check2 in borders:
                return not possible_coloring[1] == possible_coloring[4]
            else:
                return True
        
        """
        if len(possible_coloring) == 2:
            return True
        
        else:
            return onetoall(possible_coloring[:2], possible_coloring[3:], borders) and \
            is_a_legal_coloring(possible_coloring[3:], borders)
        
        
          
    elif MODE=='test samples' or MODE=='answer key':
        try:
            from sample_answers.cs105.graph_coloring.testing_samples import is_a_legal_coloring_samples_correct, is_a_legal_coloring_samples_all
        
            # set the following to only use the correct one!
            coloring_testing_samples_just_do_the_right_ones = (MODE=='answer key' or are_we_doing_coloring_enumeration())
        
            if coloring_testing_samples_just_do_the_right_ones:
                answer = is_a_legal_coloring_samples_correct(possible_coloring, borders)
            else:
                answer = is_a_legal_coloring_samples_all(possible_coloring, borders)
            
        except:
            print "Hmmmm... can't find sample answers. This shouldn't happen on the CS teaching lab computers"
            print " If you are running this program on another computer, you'll have to wait to check"
            print " your test suite against the sample answers when you're back in the lab."
            print " (Remember to Team->Commit on your computer and Team->Update in the lab.)"
    
            answer= False  # Well, sometimes this is the right answer!
    else:
        answer = 'ERROR: You need to set MODE correctly in is_legal.py'


    if want_to_print_stuff:
        print answer
    return answer  


#
# The stuff below makes sure the two files can communicate about things
#  like whether or not we're doing doctest,
#  to control whether things are printed
#
doing_doctest_for_graph_coloring = False  # This is automatically reset to True when we do doctest tests; it controls printing
doing_coloring_enum              = False  # This is automatically reset to True for Lab 3 but not Lab 4

INSANE_DEBUGGING = False  # can't get the debugger to play nice with doctest, AND I'm trying to debug doctest :-(
def are_we_doing_doctest():  # I can import a function but not a variable into Lab 4
    global doing_doctest_for_graph_coloring
    if INSANE_DEBUGGING:
        print("In are_we_doing_doctest? returning " + str(doing_doctest_for_graph_coloring))
    return doing_doctest_for_graph_coloring

def we_are_doing_doctest(well_are_we = True):
    global doing_doctest_for_graph_coloring
    if INSANE_DEBUGGING:
        print("in we_are_doing_doctest, setting to " + str(well_are_we))
    doing_doctest_for_graph_coloring = well_are_we

def are_we_doing_coloring_enumeration():  # I can import a function but not a variable into Lab 4
    global doing_coloring_enum
    return doing_coloring_enum

def we_are_doing_coloring_enumeration(well_are_we = True):
    global doing_coloring_enum
    doing_coloring_enum = well_are_we


# The following gets the "doctest" system to check test cases in the documentation comments
# see  http://docs.python.org/lib/module-doctest.html
def _test_is_legal():
    print "Running 'doctest' tests for graph coloring testing function."
    print " To use the graphical interface, run A_graphical_user_interface.py"
    we_are_doing_doctest()
    import doctest
    result = doctest.testmod()
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], __file__.split('/')[-1], "tests!"
    else:
        print "Rats!"

if __name__ == "__main__": _test_is_legal()
