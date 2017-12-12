import arcpy
try:
    arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data"
    fieldList = arcpy.ListFields("Hospitals.shp")
    for fld in fieldList:
        print "%s is a type of %s with a length of %i" %(fld.name,fld.type,fld.length)
except:
    print arcpy.GetMessages()
    

