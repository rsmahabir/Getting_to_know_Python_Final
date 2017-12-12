import arcpy, os
path = r"C:\\Users\\Me\\Desktop\\GIS Programming\\Training"
for fileName in os.listdir(path):
    fullPath = os.path.join(path, fileName)
    if os.path.isfile(fullPath):
        basename, extension = os.path.splitext(fullPath)
        if extension == ".mxd":
            mxd = arcpy.mapping.MapDocument(fullPath)
            print "MXD: " + fileName
            brknList = arcpy.mapping.ListBrokenDataSources(mxd)
            for brknItem in brknList:
                print "\t" + brknItem.name
del mxd
