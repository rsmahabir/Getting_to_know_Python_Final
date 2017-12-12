import arcpy
try:
    arcpy.env.workspace = r"C:\Users\Administrator\Desktop\GIS Programming\Training\Data"
    arcpy.AddField_management ("Hospitals.shp","FullAddr","TEXT", "50")
    updCursor = arcpy.UpdateCursor("Hospitals.shp")
    for row in updCursor:
        name = row.NAME
        addr = row.ADDRESS
        FullAddress = name + "," + addr
        row.setValue("FullAddr",FullAddress)
        updCursor.updateRow(row)
    print "Finish updating"
    del updCursor
except:
    arcpy.GetMessages()