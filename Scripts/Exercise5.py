import arcpy
try:
    arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data\\Exercise4.mdb"
    arcpy.MakeFeatureLayer_management("Communities","Communities_copy")
    arcpy.SelectLayerByAttribute_management("Communities_copy","NEW_SELECTION"," [COMM_NAME] = '     Tamana' ")
    arcpy.CopyFeatures_management("Communities_copy","test")
except:
    print "There was a problem"

