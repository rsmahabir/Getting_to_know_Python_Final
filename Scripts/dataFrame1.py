import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
for df in arcpy.mapping.ListDataFrames(mxd):
    df.rotation = 0
    df.scale = 24000
    outFile = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\" + df.name + ".tif"
    arcpy.mapping.ExportToTIFF(mxd, outFile, df)
del mxd
