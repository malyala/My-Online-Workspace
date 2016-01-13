"""

The functions used to implement Lab 8 should be written here.
As usual, you'll need to include a test suite as well as your well-commented
functions.  In addition, you'll need to find any necessary code for doctest to
work (see past assignments) and import any needed libraries yourself.  After all,
other than this comment and a few tests below, this is a blank file!

A sample test for part 1 of the lab:
>>> dot_matrix("hello", "jello")
array([[0, 0, 0, 0, 0],
       [0, 1, 0, 0, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 1, 1, 0],
       [0, 0, 0, 0, 1]])
       
A sample test for part 2 of the lab.  The dictionary output order is not
guaranteed, so we test equality instead of directly testing the dictionary.
>>> amino_acids("tttttttggaga") == {'R': 1, 'W': 1, 'F': 2}
True
       
A sample test for part 3 of the lab, run on a small set of test fragments.
The final function should be able to run on the full set of fragments available
in genome_lib.get_fragments().
>>> put_fragments_together(genome_lib.get_test_fragments())
'ttttttggagacgcggg'

"""


