import arcpy
insertCurs = arcpy.InsertCursor(r"C:\Users\Me\Desktop\GIS Programming\Training\Data\Hospitals.shp")
row = insertCurs.newRow()
row.NAME = "Ron"
row.ADDRESS = "Test"
insertCurs.insertRow(row)
del row
del insertCurs