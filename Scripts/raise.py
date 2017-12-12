class NoFeatures(Exception):
    pass

import arcpy
import os

arcpy.env.overwriteOutput = 1
fc = arcpy.GetParameterAsText(0)

try:
    # Check that the input has features
    #
    result = arcpy.GetCount_management(fc)
    if int(result.getOutput(0)) > 0:
        arcpy.FeatureToPolygon_management(fc, os.path.dirname(fc) + os.sep + "out_poly.shp")
    else:
        # Raise custom exception
        #
        raise NoFeatures(result)

except NoFeatures:
    # The input has no features
    #
    print fc + " has no features."
except:
    # By default any other errors will be caught here
    #
    print arcpy.GetMessages(2)
