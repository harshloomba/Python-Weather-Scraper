import os
import json
import urllib2
import time
import datetime
#scriptpath = "/Users/harshloomba/Documents/BlueBottle-Assignment/forecastio.py"
import sys
import getpass
# Add the directory containing your module to the Python path (wants absolute paths)
#sys.path.append(os.path.abspath(scriptpath))

# Do the import
from forecastio import Forecastio


city_lat  = 37.831106
city_long = -122.254110

# We can do real-time feed by passing the data directly into table
#Key generated by the API
forecast = Forecastio("8aa0dadbf2a543f28dca16c9304b678b")
result = forecast.load_forecast(city_lat,city_long)
#print result
#time duration for which we need the data
start_date = datetime.datetime(2015,1,1)
end_date = datetime.datetime(2015,2,28)
d = start_date
delta = datetime.timedelta(hours=1)
out = open('/Users/harshloomba/Documents/BlueBottle-Assignment/out1.csv', 'a')
while d <= end_date:
    result = forecast.load_forecast(city_lat,city_long,d,lazy=True)
    current = forecast.get_currently()
    days_list = []
    item = current
    time = item.time
    temperature = item.temperature
#   print time.strftime("%Y-%m-%d %H:%M")
#    print "%.2f" %temperature
    out.write(time.strftime("%Y-%m-%d %H:%M"))
    out.write(";")
    out.write("%.3f" %temperature)
    out.write('\n')
    d += delta
out.close()
print "sucessful"
#conn.commit()
