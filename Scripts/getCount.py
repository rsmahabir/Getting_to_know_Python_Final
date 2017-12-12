import arcpy

# Execute the GetCount tool
#
arcpy.GetCount_management("C:\\Users\\Administrator\\Desktop\\GIS Programming\\Training\\Data\\Exercise4.mdb\\Schools") 

# Get the resulting messages and print them
#
print arcpy.GetMessages()
