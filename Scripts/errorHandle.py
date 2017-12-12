#Name: John Doe
#Date: Aug, 2011
#Purpose: Working with errors in Python
import arcpy
try:
	arcpy.env.workspace = "C:\\Users\\Me\\Desktop\\GIS Programming\\Training"
	arcpy.Buffer_analysis("test.shp","sch_buff")
except:
	print "An Error has occured"
