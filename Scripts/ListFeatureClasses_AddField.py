import arcpy
try:
    arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data"
    fcList = arcpy.ListFeatureClasses("","Polygon")
    for fc in fcList:
        print "Adding field to " + fc
        arcpy.AddField_management (fc,"Edited by", "text","25")
except:
    print arcpy.GetMessages()


   