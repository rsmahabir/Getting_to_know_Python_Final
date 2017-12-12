import arcpy
mxd = arcpy.mapping.MapDocument("C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\XY.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Layers")[0]
table = arcpy.mapping.ListTableViews(mxd, "XY", df)[0]
table.definitionQuery = "ID = 1"
mxd.save()
del mxd
