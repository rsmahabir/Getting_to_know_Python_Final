class LicenseError(Exception):
    pass

import arcpy
from arcpy import env

try:
    if arcpy.CheckExtension("3D") == "Available":
        arcpy.CheckOutExtension("3D")
    else:
        # Raise a custom exception
        #
        raise LicenseError
    
    env.workspace = "D:/GrosMorne"
    arcpy.HillShade_3d("WesternBrook", "westbrook_hill", 300)
    arcpy.Aspect_3d("WesternBrook", "westbrook_aspect")

except LicenseError:
    print "3D Analyst license is unavailable"  
except:
    print arcpy.GetMessages(2)
finally:
    # Check in the 3D Analyst extension
    #
    arcpy.CheckInExtension("3D")
