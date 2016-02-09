#
# To debug a Python function,
#  * make sure the class or function is imported into this file
#  * use the troublesome function or class method(s) in this file
#  * double-click on the left margin to get a green 'thumb tack' on the line you want to debug
#  * right-click on this file in the Navigator pane on the left of your Eclipse window,
#    and choose Debug As->Python Run
#  * click "ok" when asked about changing perspectives
#
#  then debug the program, as illustrated in lecture
#
#  When done, remember to:
#  * stop the program by clicking on the "red box" in the upper left pane
#    (if that box is grey rather than red, the program is already stopped)
#  * right-click on "Debug" in your perspectives menu and choose "close"
#

# for example, if we were debugging sqrt from the math library (which we can't actually see in the debugger), we would write

from math import sqrt

print sqrt(9)
