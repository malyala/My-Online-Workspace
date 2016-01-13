"""
   A python class to represent time on the planet Regulus,
       as described in the lab assignment.

Examples:

>>> t1 = Time(03 + 60 * (25 + 60 * (01 + 24 * ((01-1) + 30 * ((04-1) + 12 * (12-1))))))
>>> print t1    # 04/01/12 01:25:03 AM RST     (or, if you like, 12-04-01 1:15:03 RST)
4/1/12 1:25:3 RST

>>> t1_original = deepcopy(t1)
>>> t1.add_minutes(-120)
>>> print t1                    # 120 minutes before 04/01/12 01:25:03 AM RST
3/30/12 23:25:3 RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(-60)
>>> print t1                    #  60 minutes before 04/01/12 01:25:03 AM RST which is hour 0 in military time
4/1/12 0:25:3 RST
>>> t1 = deepcopy(t1_original)

>>> t1.add_minutes(60)
>>> print t1                    #  60 minutes after  04/01/12 01:25:03 AM RST, i.e. into DST
4/1/12 3:25:3 RDT
>>> t1 = deepcopy(t1_original)


>>> Time(344775540).minutes_until(Time(344775900))  # from the assignment
6

# t2 is "10/01/12 01:55:57 AM RDT"
#  that's a total of 57 seconds plus 60*55 seconds ... minus 1 hour
>>> t2 = Time(57 + 60 * (55 + 60 * (01 + 24 * ((01-1) + 30 * ((10-1) + 12 * (12-1))))) - 3600)
>>> print t2  # "1:55:57 AM on October 1, year 12 prints as: "
10/1/12 1:55:57 RDT

>>> print t1.minutes_until(t2)    # 10/01/12 01:55:57 AM RDT   vs.   04/01/12 01:25:03 AM RST
259170
>>> print t2.minutes_until(t1)    # 04/01/12 01:25:03 AM RST   vs.   10/01/12 01:55:57 AM RDT  # note -259171 is fine too
-259171

>>> t2.add_minutes(60)
>>> print t2    # 1 hour  after "1:55:57 AM on October 1, year 12"
10/1/12 2:55:57 RDT
>>> t2.add_minutes(60)
>>> print t2    # 2 hours after "1:55:57 AM on October 1, year 12"
10/1/12 2:55:57 RST
>>> t2.add_minutes(60)
>>> print t2    # 3 hours after "1:55:57 AM on October 1, year 12"
10/1/12 3:55:57 RST

>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  3)
>>> t1.minutes_until(t3)
3
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t1.minutes_until(t3)
-60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(-60)
>>> t3.minutes_until(t1)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(  0)
>>> t1.minutes_until(t3)
0
>>> t3 = deepcopy(t1)
>>> t3.add_minutes( 60)
>>> t1.minutes_until(t3)
60
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(120)
>>> t1.minutes_until(t3)
120
>>> t3 = deepcopy(t1)
>>> t3.add_minutes(180)
>>> t1.minutes_until(t3)
180

>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  3)
>>> t2.minutes_until(t3)
3
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(-60)
>>> t2.minutes_until(t3)
-60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(  0)
>>> t2.minutes_until(t3)
0
>>> t3 = deepcopy(t2)
>>> t3.add_minutes( 60)
>>> t2.minutes_until(t3)
60
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(120)
>>> t2.minutes_until(t3)
120
>>> t3 = deepcopy(t2)
>>> t3.add_minutes(180)
>>> t2.minutes_until(t3)
180

"""
from copy import deepcopy
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

#===============================================================
#
#                    The Two Classes:
#
#================================================================



#################################################################
#=====================The First Class===========================
#################################################################
class Time_represented_by_seconds:
    """Replace this with your definition of 'time' so that the test works"""
    def __init__(self, secs):
        precondition(type(secs) == int)
        #postcond: we just store the seconds under some name in self
        self.seconds = secs
    def minutes_until(self, other):
        #precondition(type(other)==Time_represented_by_seconds) #for some reason this causes problems!
        to_return = (other.seconds - self.seconds)/60
        #postcond: to_return is the number of minutes (int rounded down) to change from the time 'self' to the time 'other'
        return to_return
    def add_minutes(self, min_to_add):
        precondition(type(min_to_add)== int)
        sec_to_add = min_to_add *60
        #postcond:we change the time of self by 'min_to_add' minutes
        self.seconds += sec_to_add
    def __repr__(self):
        
        DST= False # intially assume it is not daylight savings time
        
        secs_yet_to_be_organized = self.seconds
        years = (secs_yet_to_be_organized / 31104000) + 1 #number of seconds in a year, we add one b/c we start with year 1
        secs_yet_to_be_organized %= 31104000 #now we have time less than a year
        
        if  7783200 <secs_yet_to_be_organized < 23335200: #if we are in the daylight saving time period
            DST = True
            secs_yet_to_be_organized += 3600
            
#Here I prefer the imperative method because it is clearer
        months = (secs_yet_to_be_organized / 2592000) +1 # number of months plus one b/c start with first month
        secs_yet_to_be_organized %= 2592000 #now we have time less than a month
        days = (secs_yet_to_be_organized/86400) +1 #number of days left, add one b/c start with day 1
        secs_yet_to_be_organized %= 86400 # now we have only hours left
        hours = secs_yet_to_be_organized /3600  #number of hours (we deal with 0th hour below)
        #hours = 12 if hours==0 else hours #the 0th hour is just 12
        secs_yet_to_be_organized %= 3600 #secs of minutes left.. etc
        minutes = secs_yet_to_be_organized/60 
        secs_yet_to_be_organized %= 60
        seconds = secs_yet_to_be_organized
        

        if DST:
            is_daylight_savings = "RDT"
        else:
            is_daylight_savings = "RST"
     
        
        to_return = str(months) + "/" + str(days) + "/" + str(years) + " " + \
        str(hours) +':'+ str(minutes) + ":" + str(seconds) + " "+ \
        is_daylight_savings
        #postcond: we have "mm/dd/yy hrs:mins:secs RS/DT" with the correct time
        return to_return
###########################################################################        
#=====================The Second Class====================================== 
###########################################################################  

#copied code that we make into a function; it makes seconds into the printable fields
def to_fields(secs): #this is copied from the first class
        DST = False
        secs_yet_to_be_organized = secs
        years = (secs_yet_to_be_organized / 31104000) + 1 #number of seconds in a year, we add one b/c we start with year 1
        secs_yet_to_be_organized %= 31104000 #now we have time less than a year
        
        if  7783200 <secs_yet_to_be_organized < 23335200: #if we are in the daylight saving time period
            DST = True
            secs_yet_to_be_organized += 3600
            
        months = (secs_yet_to_be_organized / 2592000) +1 # number of months plus one b/c start with first month
        secs_yet_to_be_organized %= 2592000 #now we have time less than a month
        days = (secs_yet_to_be_organized/86400) +1 #number of days left, add one b/c start with day 1
        secs_yet_to_be_organized %= 86400 # now we have only hours left
        hours = secs_yet_to_be_organized /3600  #number of hours (we deal with 0th hour below)
        #hours = 12 if hours==0 else hours #the 0th hour is just 12
        secs_yet_to_be_organized %= 3600 #secs of minutes left.. etc
        minutes = secs_yet_to_be_organized/60 
        secs_yet_to_be_organized %= 60
        seconds = secs_yet_to_be_organized
        
        if DST:
            is_daylight_savings = "RDT"
        else:
            is_daylight_savings = "RST"

        return [months, days, years, hours, minutes, seconds, is_daylight_savings]


     
class Time_represented_by_clock_and_calendar:
#note: we use the function to_fields above ^
    
    
    def __init__(self, secs):
        precondition(type(secs) == int)
        
#technique: convert the secs to years, months,... with the to_fields function and then make that 
#the data
#postcondition: we store the time as printable fields
        self.data = to_fields(secs)
        
    def to_seconds(self):
        """
        Returns the number of seconds since planet's founding of a given time object
        (Basically converts a time to seconds since start of recorded time)
        """
        d = self.data
        seconds = ((d[0]-1)*2592000)+((d[1]-1)*86400)+((d[2]-1)*31104000)+(d[3]*3600)+(d[4]*60)+d[5]
        if d[6] == "RDT":
            seconds -= 3600 
        #postcond: 'seconds' is the num of seconds since the founding of regulus and the time 'self'      
        return seconds
            
    def minutes_until(self, other):
        #precondition(type(other) == Time_represented_by_clock_and_calendar) #for some reason, this causes errors!
        #postcond: we return the change of minutes (int rounded down) from self to other
        return (other.to_seconds() - self.to_seconds())/60 
                       
        
    def add_minutes(self, minutes):
        precondition(type(minutes) == int)
#we convert self's time to seconds, add the seconds of the number of minutes and
#with to_fields reconvert it back to months, days ... and store that in self.data
#postcondition: we have self have its time changed by 'minutes' minutes
        self.data = to_fields(self.to_seconds() + (minutes*60))
        
    def __repr__(self):
        d = self.data
        #postcondition we return the string "mm/dd/yy hrs:mins:secs RS/DT" of the correct time
        return str(d[0])+"/"+str(d[1])+"/"+str(d[2])+" "+str(d[3])+":"+\
        str(d[4])+":"+str(d[5])+" "+d[6]
    
#================================================================
#
#                    End Of The Two Classes.
#
#================================================================





# by default, use the first representation, but this is changed in DocTest below
Time = Time_represented_by_seconds

# mostly copied from  http://docs.python.org/lib/module-doctest.html
def _test():
    import doctest
    global Time
    
    
    
    Time = Time_represented_by_seconds
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_seconds is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"

    print "\n\n\n\n"
    
#uncomment this for next testing...
    
    Time = Time_represented_by_clock_and_calendar
    result = doctest.testmod()
    print "Result of doctest for Time_represented_by_clock_and_calendar is:",
    if result[0] == 0:
        print "Wahoo! Passed all", result[1], "tests!"
    else:
        print "Rats!"
    Time = Time_represented_by_seconds
    
if __name__ == "__main__":
    _test()
