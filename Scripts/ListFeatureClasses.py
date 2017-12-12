import arcpy
try:
    arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data"
    fcList = arcpy.ListFeatureClasses("","Polygon")
    for fc in fcList:
        print fc
except:
    print arcpy.GetMessages()


   