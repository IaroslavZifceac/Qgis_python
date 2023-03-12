# This script creates a polygon from a txt file
# Import necessary modules
from qgis.core import (QgsProject, QgsPointXY, QgsGeometry, QgsFeature,
                       QgsField, QgsFields, QgsVectorLayer)

# Specify the text file path and field separator
# This script asume that the file has no other values than x and y value without any head of columns
txt_file = 'pathofthefile'
# Specify the separator between the x and y

separator = ','

# Create a new memory layer for the polygon feature
layer_name = 'Polygon from Points'
fields = QgsFields()
fields.append(QgsField('id', QVariant.Int))
polygon_layer = QgsVectorLayer('Polygon?crs=EPSG:4326', layer_name, 'memory')
polygon_layer.dataProvider().addAttributes(fields)
QgsProject.instance().addMapLayer(polygon_layer)

# Open the text file and read each line to create a QgsPointXY object
with open(txt_file, 'r') as file:
    points = []
    for line in file:
        x, y = line.strip().split(separator)
        x = float(x)
        y = float(y)
        point = QgsPointXY(x, y)
        points.append(point)

# Create the polygon geometry from the QgsPointXY objects
if len(points) > 2:
    polygon = QgsGeometry.fromPolygonXY([[point for point in points]])

    # Create a new feature for the polygon and add it to the memory layer
    feature = QgsFeature()
    feature.setGeometry(polygon)
    feature.setFields(fields)
    feature.setAttribute('id', 1)
    polygon_layer.dataProvider().addFeature(feature)