import arcpy.mapping
mxdDoc = arcpy.mapping.MapDocument("CURRENT")
for elms in arcpy.mapping.ListLayoutElements(mxdDoc):
    print elms.name

