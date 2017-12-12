import os
import sys
import arcpy
import arcpy.mapping as mapping

# get input parameters 
outDir = arcpy.GetParameterAsText(0)
packageMap = arcpy.GetParameter(1)
checkBrokenLayers = arcpy.GetParameter(2)

# get the map document in which this code is running ("Current" keyword)
mxd = mapping.MapDocument('Current')

# build a pathname to the output report (text file)
reportPath = outDir + '\\' + mxd.title + '.txt'
# open the file (will be created if it doesn't exist)
reportFile = open(reportPath, 'w')
arcpy.AddMessage('Writing report to ' + reportPath)

# start writing report text to a string variable
reportText = 'Title: ' + mxd.title + '\n'
reportText += 'Author: ' + mxd.author + '\n'
reportText += 'Description: ' + mxd.description + '\n'
reportText += '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~' + '\n'

# if the user chose to do so, create map package
if packageMap:
    packagePath = outDir + '\\' + mxd.title.replace('.', '_') + '.mpk'
    if (os.path.exists(packagePath)):
	arcpy.AddMessage('Map package already exists (' + packagePath + ')')
    else:
	arcpy.AddMessage('Creating map package (' + packagePath + ')' )
	arcpy.PackageMap_management(mxd.filePath, packagePath)

# loop thru all data frames in the map
dataFrames = mapping.ListDataFrames(mxd, '')
for frame in dataFrames:
    # report data frame name and spatial reference
    reportText += '\nData Frame: ' + frame.name + '\n'
    reportText += 'Spatial Reference: ' + frame.spatialReference.name + '\n'
    # get all layers in this data frame
    layers = mapping.ListLayers(mxd, '', frame)
    i = 0 # layer index position
    # loop thru all layers in the data frame
    for lyr in layers:
        # report index position and name
	reportText += '\tLayer ' + str(i) + ': ' + lyr.name + '\n'
	i += 1 # same as i = i + 1

# if the user has requested it, check for layers with a missing data source
if checkBrokenLayers:
    arcpy.AddMessage('Checking for missing data sources')
    brokenList = mapping.ListBrokenDataSources(mxd)
    # report the count of broken layers
    reportText += '\nFound ' + str(len(brokenList)) + ' layers with missing data.'
    # loop thru all broken layers in the list
    for broken in brokenList:
        # report broken layer name
	reportText += '\t- ' + broken.name + '\n'

# write the text stored in the reportText variable to the output file
reportFile.write(reportText)
reportFile.close() # close the file
del mxd # delete the mxd object
