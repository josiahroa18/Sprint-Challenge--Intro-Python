# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).
class City:
  def __init__(self, name, lat, lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"{self.name}, {self.lat}, {self.lon}"


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
  with open("./cities.csv") as csvfile:
    city = csv.reader(csvfile, delimiter=',')
    line_count = 0
    for row in city:
      if line_count > 0:
        cities.append(City(row[0], float(row[3]), float(row[4])))
      line_count += 1

    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
# print(len(cities))
# for c in cities:
#     print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user
# user_input_1 = input("Enter lat1,lon1: ")
# user_input_2 = input("Enter lat2,lon2: ")
# user_input_1 = user_input_1.split(',')
# user_input_2 = user_input_2.split(',')
# print(user_input_1)
# print(user_input_2)

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # Normalize input data to be a pair of lower-left,upper-right pair of coordinates
  lat1 = float(lat1)
  lon1 = float(lon1)
  lat2 = float(lat2)
  lon2 = float(lon2)

  lower_left = []
  upper_right = []
  upper_left = []
  lower_right = []
  if lat1 < lat2 and lon1 < lon2:
    lower_left = [lat1, lon1]
    upper_right = [lat2, lon2]
  elif lat1 > lat2 and lon1 > lon2:
    lower_left = [lat2, lon2]
    upper_right = [lat1, lon1]
  elif lat1 < lat2 and lon1 > lon2:
    upper_left = [lat1, lon1]
    lower_right = [lat2, lon2]
  elif lat1 > lat2 and lon1 < lon2:
    upper_left = [lat1, lon1]
    lower_right = [lat2, lon2]
  else:
    return "Error normalizing data"

  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.
  for city in cities:
    # Lower left and upper right
    if len(lower_left) > 0 and len(upper_right) > 0:
      lat1 = lower_left[0]
      lon1 = lower_left[1]
      lat2 = upper_right[0]
      lon2 = upper_right[1]

      if city.lat >= lat1 and city.lon >= lon1 and city.lat <= lat2 and city.lon <= lon2:
        within.append(city)
    # Upper left and lower right
    else:
      lat1 = upper_left[0]
      lon1 = upper_left[1]
      lat2 = lower_right[0]
      lon2 = lower_right[1]

      if city.lat <= lat1 and city.lon <= lon1 and city.lat >= lat2 and city.long >= lon2:
        within.append(city)

      
  

  return within

within_cities = cityreader_stretch(45, -100, 32.0, -120, cities)
for city in within_cities:
  print(city.name)
# cityreader_stretch(user_input_1[0], user_input_1[1], user_input_2[0], user_input_2[1], cities)

