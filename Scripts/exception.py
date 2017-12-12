import arcpy

try:
    # Execute the Buffer tool
    #
    arcpy.Buffer_analysis("c:/transport/roads.shp", "c:/transport/roads_buffer.shp")
except Exception as e:
    print e.message
    
    # If using this code within a script tool, AddError can be used to return messages 
    #   back to a script tool.  If not, AddError will have no effect.
    arcpy.AddError(e.message)
