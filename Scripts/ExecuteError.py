import arcpy

try:
    result = arcpy.GetCount_management("C:/invalid.shp")
  
# Return geoprocessing specific errors
#
except arcpy.ExecuteError:    
    arcpy.AddError(arcpy.GetMessages(2))    
    print "Geoprocessing tool failed"
# Return any other type of error
except:    
    arcpy.AddError("Non-tool error occurred")
    print "It was not the geoprocessing tool!"