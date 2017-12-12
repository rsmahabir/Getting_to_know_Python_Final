import arcpy
# Set workspace
arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data"
# Set overwrite option
#arcpy.overwriteOutput = true
#Create lyr file
arcpy.MakeFeatureLayer_management("Hospitals.shp", "Hospitals_lyr")
# Write the selected features to a new featureclass
arcpy.CopyFeatures_management("Hospitals_lyr", "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data\H")
