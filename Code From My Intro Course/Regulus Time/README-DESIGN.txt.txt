Here I explain the general concepts of the implementation of the methods
Time1 will be used in place of Time_represented_by_seconds
Time2 will be used in place of Time_represented_by_clock_and_calendar


1. Intializing

Time1 just stores the seconds
Time2 converts the time into all the nessesary printing fields
comments have been given as to how this is done

2.minutes_until

Time1 just subtracts the seconds of the latter from the former 
and does integer division by 60
Time2 does the same by using a helper method called seconds which returns
the seconds of each time2 object

3. add_minutes

Time1 converts the 'minutes to add' to seconds and adds those to 
the given time object
Time2 first gets the number of seconds to the time oject
using a helper method and then adds the (minutes*60). Then, 
it converts these seconds back into the seperate fields and 
rebinds the time object's data to these fields. 

4. __repr__

Time1 converts the seconds to the fields for printing 
by repeatedly finding the number of [years, months, etc.] and updating
the reminaing seconds as the remainder of the seconds in a [year, month, etc.]

It also takes into account daylight savings time by seeing if the number of seconds
that remain after all complete years have been subtracted 
are within the RDT time range and adding an hour if so.
It then concatenates these fields with / and :

NOTE:
This piece of code is used a couple times in Time2 to convert seconds to the fields needed
for a Time2 object

Time2 implements this by simply printing the fields with the proper concatenation