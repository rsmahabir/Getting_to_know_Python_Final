import arcpy
try:
    arcpy.env.workspace = r"C:\Users\Administrator\Desktop\GIS Programming\Training\Data"
    searchCurs = arcpy.SearchCursor("Schools.shp","\"TYPE\" = \'Primary School\'")
    for row in searchCurs:
        print row.SCHOOL
except:
    arcpy.GetMessages()