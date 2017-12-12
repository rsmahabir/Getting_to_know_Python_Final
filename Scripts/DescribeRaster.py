import arcpy
try:
    arcpy.env.workspace = r"C:\Users\Me\Desktop\GIS Programming\Training\Data"
    descRaster = arcpy.Describe("Test.img")
    ext = descRaster.Extent
    print "XMin: %f" % (ext.xmin)
    print "YMin: %f" % (ext.ymin)
    print "XMax: %f" % (ext.xmax)
    print "YMax: %f" % (ext.ymax)
    sr = desRaster.SpatialReference
    print sr.Name
    print sr.Type
except:
    print arcpy.GetMessages()
    