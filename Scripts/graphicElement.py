import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
for elm in arcpy.mapping.ListLayoutElements(mxd, "GRAPHIC_ELEMENT"):
    if elm.name == "Title Block":
        elm.elementPositionX = 4.75
        elm.elementPositionY = 10.5
mxd.save()
del mxd
