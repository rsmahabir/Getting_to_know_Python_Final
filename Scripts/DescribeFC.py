import arcpy
try:
    arcpy.env.workspace = r"C:\Users\Me\Desktop\GIS Programming\Training\Data"
    descFC = arcpy.Describe("Hospitals.shp")
    print "The shape type is: "+ descFC.ShapeType
    flds = descFC.Fields
    for fld in flds:
        print "Field: " +fld.Name
        print "Type: " +fld.Type
        print "Length: " +str(fld.Length)
    ext = descFC.Extent
    print "XMin: %f" % (ext.xmin)
    print "YMin: %f" % (ext.ymin)
    print "XMax: %f" % (ext.xmax)
    print "YMax: %f" % (ext.ymax)
except:
    print arcpy.GetMessages()
    