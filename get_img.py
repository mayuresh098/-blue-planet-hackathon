
#12.837469, 77.655863
import shutil

#12.837469, 77.655863
import requests
import shutil
import geopy
import time
import geopy.distance

### Define starting point.
##start = geopy.Point(12.837469,77.655863)


import math


def down_image(lat,lng):
    '''
    the def downlaod the image of given lat and lng with size of 1000 * 1000 with name of lat and lng in current diretory
    '''
    # with key=
    #https://maps.googleapis.com/maps/api/staticmap?center=17.053828,+-96.700116&zoom=17&scale=1&size=600x300&maptype=satellite&format=png&visual_refresh=true&key=YOUR_KEY_API

    lat=str(lat)
    lng=str(lng)
    url="https://maps.googleapis.com/maps/api/staticmap?center="+(lat)+","+(lng)+"&zoom=17&scale=1&size=800x800&maptype=satellite&format=png&visual_refresh=true&key=AIzaSyAoJHHE11wDXiLzU6AqQFOh3WbIqxfzjIA"
    #url="https://maps.googleapis.com/maps/api/staticmap?center="+(lat)+","+(lng)+"&zoom=17&scale=1&size=1000x1000&maptype=satellite&format=png&visual_refresh=true"
    str_imag_name=(lat)+"-"+(lng)+".jpg"
    response = requests.get(url, stream=True)
    with open(str_imag_name, 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    return str_imag_name

## caucluate ditance
from math import radians, sin, cos, acos
def calcuate_distance():
    print "a"
    # work in progress
##
##    print("Input coordinates of two points:")
##    slat = radians(float(input("Starting latitude: ")))
##    slon = radians(float(input("Ending longitude: ")))
##    elat = radians(float(input("Starting latitude: ")))
##    elon = radians(float(input("Ending longitude: ")))
##
##    dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
##    print("The distance is %.2fkm." % dist)


def get_lcoation_east(distance,lat,lng):
    
    R =3.1416 #Radius of the Earth
    # rememner below points
    # decimal degree 90 Radina 1.5708
    #Decimal degrees 180 Radians 3.1416
    #Decimal degrees 270 Radians 4.7124
    #Decimal degrees 36 Radians 6.2832
    brng = 1.5708 #Bearing is 90 degrees converted to radians.
    d = distance #Distance in km
    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lng) #Current long point converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    lat2=round(lat2,6)
    lon2=round(lon2,6)
    return([lat2,lon2])
def get_lcoation_north(distance,lat,lng):
    
    R =3.1416  #Radius of the Earth
    # rememner below points
    # decimal degree 90 Radina 1.57
    #Decimal degrees 180 Radians 3.1416
    #Decimal degrees 270 Radians 4.7124
    #Decimal degrees 36 Radians 6.2832
    brng = 4.7124 #Bearing is 90 degrees converted to radians.
    d = distance #Distance in km
    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lng) #Current long point converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    lat2=round(lat2,6)
    lon2=round(lon2,6)
    return([lat2,lon2])

def get_lcoation_west(distance,lat,lng):
    
    R =3.1416  #Radius of the Earth
    # rememner below points
    # decimal degree 90 Radina 1.57
    #Decimal degrees 180 Radians 3.1416
    #Decimal degrees 270 Radians 4.7124
    #Decimal degrees 36 Radians 6.2832
    brng =3.1416#Bearing is 90 degrees converted to radians.
    d = distance #Distance in km
    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lng) #Current long point converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    lat2=round(lat2,6)
    lon2=round(lon2,6)
    return([lat2,lon2])

def get_lcoation_south(distance,lat,lng):
    
    R =6.2832 #Radius of the Earth
    # rememner below points
    # decimal degree 90 Radina 1.57
    #Decimal degrees 180 Radians 3.1416
    #Decimal degrees 270 Radians 4.7124
    #Decimal degrees 36 Radians 6.2832
    brng =3.1416#Bearing is 90 degrees converted to radians.
    d = distance #Distance in km
    lat1 = math.radians(lat) #Current lat point converted to radians
    lon1 = math.radians(lng) #Current long point converted to radians
    lat2 = math.asin( math.sin(lat1)*math.cos(d/R) +
         math.cos(lat1)*math.sin(d/R)*math.cos(brng))
    lon2 = lon1 + math.atan2(math.sin(brng)*math.sin(d/R)*math.cos(lat1),
                 math.cos(d/R)-math.sin(lat1)*math.sin(lat2))
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)
    
    lat2=round(lat2,6)
    lon2=round(lon2,6)
    return([lat2,lon2])

###################################################################################################
lat_start=12.837469
lng_start=77.655863

while(1):
    
    print down_image(lat_start, lng_start)
    # getting location eact 1 km
    new_loc=get_lcoation_east(2,lat_start,lng_start)
    print new_loc
    lat_start= new_loc[0]
    lng_start= new_loc[1]
    time.sleep(10)
     
    




    


