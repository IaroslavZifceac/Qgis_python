# Import necessary modules
from qgis.core import (QgsProject, QgsPointXY, QgsGeometry, QgsFeature,
                       QgsField, QgsFields, QgsVectorLayer)

# Specify the text file path and field separator
# This script asume that the file has no other values than x and y value without any head of columns
txt_file = 'path'

separator = ','

# Create a new memory layer for the line feature
layer_name = 'Line from Points'
fields = QgsFields()
fields.append(QgsField('id', QVariant.Int))
line_layer = QgsVectorLayer('LineString?crs=EPSG:4326', layer_name, 'memory')
line_layer.dataProvider().addAttributes(fields)
QgsProject.instance().addMapLayer(line_layer)

# Open the text file and read each line to create a QgsPointXY object
with open(txt_file, 'r') as file:
    points = []
    for line in file:
        x, y = line.strip().split(separator)
        x = float(x)
        y = float(y)
        point = QgsPointXY(x, y)
        points.append(point)

# Create the line geometry from the QgsPointXY objects
if len(points) > 1:
    line = QgsGeometry.fromPolylineXY(points)

    # Create a new feature for the line and add it to the memory layer
    feature = QgsFeature()
    feature.setGeometry(line)
    feature.setFields(fields)
    feature.setAttribute('id', 1)
    line_layer.dataProvider().addFeature(feature)