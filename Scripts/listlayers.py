import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Exercise6.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0]

for lyr in arcpy.mapping.ListLayers(mxd,"Communities", df):
    if lyr.description == "Community 1":
        print "Test"
        lyr.visible = True
        lyr.transparency = 50
mxd.save()
del mxd
