#from tkinter import Tk, Label, Button

#class MyFirstGUI:
    #def __init__(self, master):
        #self.master = master
        #master.title("A simple GUI")

        #self.label = Label(master, text="This is our first GUI!")
        #self.label.pack()

        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack()

    #def greet(self):
        #print("Greetings!")
        
#for i in range(12):
    

#root = Tk()
#my_gui = MyFirstGUI(root)
#root.mainloop()


def time_find(dated, datem, datey, time, country):
    pass

from geopy import geocoders # $ pip  install geopy
from datetime import datetime,timedelta
import pytz
import calendar

#g = geocoders.GoogleV3 # set variable from Google
#place, (lat, lng) = g.geocode('Tokyo') # get country
#timezone = g.timezone((lat, lng)) # return pytz timezone object = get that country's timezone
#print(timezone.zone)

#now = datetime.now(pytz.timezone('Asia/Tokyo')) # you could pass `timezone` object here
#weekday = now.weekday() 
#print(calendar.day_name[weekday])

def countryFind(country):
    g = geocoders.GoogleV3() # set variable from Google
    place, (lat, lng) = g.geocode(country) # get country
    timezone = g.timezone((lat, lng)) # return pytz timezone object = get that country's timezone  
    
    now = datetime.now(timezone) # you could pass `timezone` object here
    return now
    #weekday = now.weekday() 
    #print(calendar.day_name[weekday])    

def pretty_print(now):
    print(now.month, now.day, now.year, now.hour, now.minute)
country = 'christchurch'
origin = countryFind(country)
country = ('los angeles')
destination = countryFind(country.lower())
print(origin)
print(destination)




fmt = '%Y-%m-%d %H:%M'
origin = origin.strftime(fmt)
destination = destination.strftime(fmt)
d1 = datetime.strptime(origin, fmt)
d2 = datetime.strptime(destination, fmt)

diff = d2 - d1

diff_minutes = ((diff.days * 24 * 60) + (diff.seconds/60))/60


print('+' + str(diff_minutes))
