import arcpy

try:
    # Execute the Buffer tool
    #
    arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
except: 
	print "Ok...hold up, you need to fix me"
