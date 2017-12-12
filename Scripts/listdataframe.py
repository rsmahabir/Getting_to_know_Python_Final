import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Exercise6.mxd")
for df in arcpy.mapping.ListDataFrames(mxd):
    print df.name
    