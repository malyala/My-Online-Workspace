"""

>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "CM CY MV MH MY VH VY")
True

If Ct and Ma are both red, there's trouble
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False

If Ma and NH are both blue, that's not good either:
>>> is_a_legal_coloring("Cr Mb Vr Hb Yg", "CM CY MV MH MY VH VY")
False

Test some legal colorings
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "MC CY MV MH MY VH VY")
True
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "YV YM YC VM VH MH MC")
True
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "CM CY VM HM YM VH VY")
True
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "MC CY VM MH MY HV YV")
True
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "CM CY MV MH MY VH YV")
True

First, some obscure cases

All states are the same color
>>> is_a_legal_coloring("Cr Mr Vr Hr Yr", "CM CY MV MH MY VH VY")
False

All states the same color, no borders
>>> is_a_legal_coloring("Cr Mr Vr Hr Yr", "")
True

Legal coloring, no borders
>>> is_a_legal_coloring("Cr Mb Vr Hg Yg", "")
True

Mixing up where the badly colored states are in sample_coloring
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CM CY MV MH MY VH VY")
False

Bad Colored states located in the middle
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CY MV MH CM MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CY MV MH MY VH VY CM")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "MC CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CY MV MH MC MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Cr Mr Yg", "CY MV MH MY VH VY MC")
False

Bad Colored states located at the beginning and the end
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CY MV MH CM MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CY MV MH MY VH VY CM")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "MC CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CY MV MH MC MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Hg Yg Mr", "CY MV MH MY VH VY MC")
False

Bad Colored states located at the end
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CY MV MH CM MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CY MV MH MY VH VY CM")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "MC CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CY MV MH MC MY VH VY")
False
>>> is_a_legal_coloring("Vb Hg Yg Cr Mr", "CY MV MH MY VH VY MC")
False

Bad Colored states located at the beginning
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CY MV MH CM MY VH VY")
False
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CY MV MH MY VH VY CM")
False
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "MC CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CY MV MH MC MY VH VY")
False
>>> is_a_legal_coloring("Cr Mr Vb Hg Yg", "CY MV MH MY VH VY MC")
False

Bad Colored states located at the beginning and the middle
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CM CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CY MV MH CM MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CY MV MH MY VH VY CM")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "MC CY MV MH MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CY MV MH MC MY VH VY")
False
>>> is_a_legal_coloring("Cr Vb Mr Hg Yg", "CY MV MH MY VH VY MC")
False

Corner cases:
>>> is_a_legal_coloring("", "")
True
>>> is_a_legal_coloring("Cr", "")
True
>>> is_a_legal_coloring("", "CY")
True

"""
from is_legal import *

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
