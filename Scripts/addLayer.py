import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd, "Population")[0]
addLayer = arcpy.mapping.Layer("C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Data\\Communities")
arcpy.mapping.AddLayer(df, addLayer, "BOTTOM")
mxd.saveACopy(r"C:\Project\addLayer.mxd")
del mxd, addLayer
