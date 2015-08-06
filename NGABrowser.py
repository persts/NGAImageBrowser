"""
/***************************************************************************
Name			 	         : NGA Image Browser
Description          : A simple plugin to help browse through NGA images.
Date                 : 2015-07-27 
copyright            : (C) 2015 by Peter J. Ersts
email                : ersts@amnh.org 
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import * 
from PyQt4.QtGui import *
from qgis.core import *
from qgis.gui import *
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from Ui_NGABrowser import Ui_NGABrowserWidget

from PyQt4 import QtNetwork

class NGABrowserWindow(QWidget, Ui_NGABrowserWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self);
    self.identifyResults = {}

  def addFeature(self, url, feature):
    self.identifyResults[url] = feature

  def loadImage(self, networkReply):
    data = networkReply.readAll()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    label = QLabel()
    label.setPixmap(pixmap)
    self.tabWidget.addTab(label, str(self.identifyResults[networkReply.url().toString()].attribute('objectid')))

  def reset(self):
    self.identifyResults.clear()
    while self.tabWidget.count() > 0:
      self.tabWidget.removeTab(0)

class NGABrowser: 
  def __init__(self, iface):
    # Save reference to the QGIS interface
    self.iface = iface
    self.canvas = self.iface.mapCanvas()
    self.clickTool = QgsMapToolEmitPoint(self.canvas)
    self.network = QtNetwork.QNetworkAccessManager()
    self.network.finished.connect(self.imageDownloaded)
    self.network.sslErrors.connect(self.sslErrorHandler)

  def initGui(self):  
    # Create action that will start plugin configuration
    self.action = QAction(QIcon(":/NGABrowser/icon.png"), \
        "NGA Image Browser", self.iface.mainWindow())
    # connect the action to the run method
    QObject.connect(self.action, SIGNAL("activated()"), self.run) 

    # Add toolbar button and menu item
    self.iface.addToolBarIcon(self.action)

    QObject.connect(self.clickTool, SIGNAL("canvasClicked(const QgsPoint &, Qt::MouseButton)"), self.mouseDown)

  def imageDownloaded(self, networkReply):
    self.display.loadImage(networkReply)

  def mouseDown(self, point, button):
    self.display.show()
    self.display.raise_()
    layer = self.canvas.currentLayer()
    if layer is None or QGis.vectorGeometryType(layer.geometryType()) != 'Polygon':
      QMessageBox.information(self.iface.mainWindow(),"Info",'Your active layer must be a polygon layer')
    else:
      self.display.reset()
      for feature in layer.getFeatures():
        if feature.geometry().contains(point):
          url = "https://browse.digitalglobe.com/imagefinder/showBrowseImage?" + feature.attribute('browseurl').split('?')[1]
          self.display.addFeature(url, feature)
          request = QtNetwork.QNetworkRequest(QUrl(url))
          self.network.get(request)

  def sslErrorHandler(self, networkReply):
    networkReply.ignoreSslErrors()

  def unload(self):
    # Remove the plugin menu item and icon
    self.iface.removeToolBarIcon(self.action)

  # run method that performs all the real work
  def run(self): 
    self.canvas.setMapTool(self.clickTool)
    # create and show the dialog 
    self.display = NGABrowserWindow() 
    
