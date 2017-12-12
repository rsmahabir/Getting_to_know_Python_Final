import arcpy

fc = arcpy.GetParameterAsText(0)
result = arcpy.GetCount_management(fc)

# Get the count from GetCount's Result object
#
featurecount = int(result.getOutput(0))

if featurecount == 0:
    arcpy.AddError(fc + " has no features.")		
else:
    arcpy.AddMessage(fc + " has " + str(featurecount))