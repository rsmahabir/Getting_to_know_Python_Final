# Reads a GPS-produced text file and writes the lat and long values
#  to an already-created polyline shapefile
import arcpy

# Hard-coded variables for GPS track text file and feature class
gpsTrack = open("C:\\Users\\Me\\Desktop\\Getting to know Python\\Data\\gps_track.txt", "r")
polylineFC = "C:\\Users\\Me\\Desktop\\Getting to know Python\Data\\tracklines.shp"
    
# Figure out position of lat and long in the header
headerLine = gpsTrack.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index("lat")
lonValueIndex = valueList.index("long")

# Create an array to store the points for the polyline
vertexArray = arcpy.CreateObject("Array")

# Read each line in the file
for line in gpsTrack.readlines():
    segmentedLine = line.split(",")

    # Get the lat/lon values of the current GPS reading                    
    latValue = segmentedLine[latValueIndex]
    lonValue = segmentedLine[lonValueIndex]

    # Create a point and add it to the array
    vertex = arcpy.CreateObject("Point")
    vertex.X = lonValue
    vertex.Y = latValue
    vertexArray.add(vertex)

# Write the array (which now makes a polyline) to the feature class
cursor = arcpy.InsertCursor(polylineFC)
feature = cursor.newRow()
feature.shape = vertexArray
cursor.insertRow(feature)    
  
del cursor