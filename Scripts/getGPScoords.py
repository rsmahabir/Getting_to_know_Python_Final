# Reads a GPS-produced text file and writes the lat and long values
#  to a list of coordinates
gpsTrack = open("C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data\\gps_track.txt", "r")

# Figure out position of lat and long in the header
headerLine = gpsTrack.readline()
valueList = headerLine.split(",")

latValueIndex = valueList.index("lat")
lonValueIndex = valueList.index("long")

# Read lines in the file and append to coordinate list
coordList = []

for line in gpsTrack.readlines():
    segmentedLine = line.split(",")
    coordList.append([segmentedLine[lonValueIndex], segmentedLine[latValueIndex]])
   
print coordList