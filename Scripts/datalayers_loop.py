import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\\Users\\Me\\Desktop\\GIS Programming\\Training\\Exercise3.mxd")
df = arcpy.mapping.ListDataFrames(mxd)[0] #First dataframe
#print the name of all layers in top most dataframe
for lstLys in arcpy.mapping.ListLayers(mxd, "", df):
    print lstLys
#del mxd
