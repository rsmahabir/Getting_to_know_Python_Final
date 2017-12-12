# Reads a GPS-produced text file and writes the lat and long values
#  to an already-created polyline shapefile. Handles multiple polylines.

import arcpy

# Hard-coded variables for GPS track text file and feature class
gpsTrack = open("C:\\Users\\Me\\Desktop\\Getting to know Python\\Data\\gps_track_multiple.txt", "r")
polylineFC = "C:\\Users\\Me\\Desktop\\Getting to know Python\\Data\\tracklines_multiple.shp"

# Functions to add a vertex and add a completed polyline to the shapefile
def addVertex(lat, lon, array):
   vertex = arcpy.CreateObject("Point")
   vertex.X = lon
   vertex.Y = lat
   array.add(vertex)

def addPolyline(cursor, array):
   feature = cursor.newRow()
   feature.shape = array
   cursor.insertRow(feature)
   array.removeAll()

# Figure out position of lat and long in the header
headerLine = gpsTrack.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index("lat")
lonValueIndex = valueList.index("long")
newTrackIndex = valueList.index("new_seg")

# Read lines in the file and append to coordinate list
cursor = arcpy.InsertCursor(polylineFC)
vertexArray = arcpy.CreateObject("Array")

# Read each line and split it
for line in gpsTrack.readlines():
   segmentedLine = line.split(",")
   isNew = segmentedLine[newTrackIndex].upper()

   # If starting a new line, write the completed
   #  line to the feature class
   if isNew == "TRUE":

       # This check is needed to handle the first GPS entry
       if vertexArray.count > 0:
           addPolyline(cursor, vertexArray)

   # Get the lat/lon values of the current GPS reading
   latValue = segmentedLine[latValueIndex]
   lonValue = segmentedLine[lonValueIndex]

   # Call the function we defined earlier to add a vertex
   addVertex(latValue, lonValue, vertexArray)

# Add the final polyline to the shapefile
addPolyline(cursor, vertexArray)

del cursor
