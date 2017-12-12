import arcpy

# Create a Describe object from the GDB Feature Class
#
desc = arcpy.Describe(r"C:\Users\Me\Desktop\GIS Programming\Training\Data\Exercise2.gdb\Communities")

# Print GDB FeatureClass properties
print "Area Field Name  : " + desc.areaFieldName
print "Length Field Name: " + desc.lengthFieldName
