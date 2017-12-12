import arcpy

try:
    # Execute the Buffer tool
    #
    result = arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
except: 
	result.GetMessages()
