import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
for tabView in arcpy.mapping.ListTableViews(mxd):
    print tabView.name

