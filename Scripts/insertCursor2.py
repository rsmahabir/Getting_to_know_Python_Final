import arcpy
# Create insert cursor for table
#
rows = arcpy.InsertCursor(r"C:\Users\Me\Desktop\GIS Programming\Training\Data\Hospitals.shp")
x = 1

# Create 25 new rows. Set the initial row ID and distance values
#
while x <= 25:
    row = rows.newRow()
    row.rowid = x
    row.distance = 100
    rows.insertRow(row)
    x = x + 1