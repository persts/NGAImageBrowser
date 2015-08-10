"""
/***************************************************************************
Name                 : NGA Image Browser
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
import webbrowser

class NGABrowserWindow(QWidget, Ui_NGABrowserWidget):
  def __init__(self):
    QWidget.__init__(self)
    self.setupUi(self);
    self.layer = None
    self.featureSet = {}
    self.objectIdUrlMap = {}
    self.frameUsable.setDisabled(True)
    self.pButtonCatalog.clicked.connect(self.openCatalog)
    self.tabWidget.currentChanged.connect(self.tabSelected)
    self.rButtonNo.toggled.connect(self.toggledNo)
    self.rButtonMaybe.toggled.connect(self.toggledMaybe)
    self.rButtonYes.toggled.connect(self.toggledYes)

  def addFeature(self, url, feature):
    self.featureSet[url] = feature
    self.objectIdUrlMap[str(feature.attribute('objectid'))] = url

  def loadImage(self, networkReply):
    data = networkReply.readAll()
    pixmap = QPixmap()
    pixmap.loadFromData(data)
    label = QLabel()
    label.setPixmap(pixmap)
    self.tabWidget.addTab(label, str(self.featureSet[networkReply.url().toString()].attribute('objectid')))

  def openCatalog(self):
    objectid = self.tabWidget.tabText(self.tabWidget.currentIndex())
    if objectid != "":
      feature = self.featureSet[self.objectIdUrlMap[objectid]]
      if feature.fieldNameIndex('browseurl') == -1:
        webbrowser.open(feature.attribute('previewurl'))
      else :
        webbrowser.open(feature.attribute('browseurl'))

  def reset(self):
    while self.tabWidget.count() > 0:
      self.tabWidget.removeTab(self.tabWidget.count() - 1)
    self.featureSet.clear()
    self.objectIdUrlMap.clear()

  def setLayer(self, layer):
    self.layer = layer

  def tabSelected(self, index):
    if index < 0:
      return 
    objectid = self.tabWidget.tabText(index)
    feature = self.featureSet[self.objectIdUrlMap[objectid]]
    if feature.fieldNameIndex('order') != -1:
      self.frameUsable.setEnabled(True)
      attr = feature.attribute('order')
      if attr == 'no':
        self.rButtonNo.setChecked(True)
      elif attr == 'maybe':
        self.rButtonMaybe.setChecked(True)
      elif attr == 'yes':
        self.rButtonYes.setChecked(True)
      else:
        self.rButtonYes.setChecked(False)
        self.rButtonMaybe.setChecked(False)
        self.rButtonNo.setChecked(False)
    else:
      self.frameUsable.setDisabled(True)

  def toggledNo(self, checked):
    if checked:
      self.updateAttribute('no')

  def toggledMaybe(self, checked):
    if checked:
      self.updateAttribute('maybe')

  def toggledYes(self, checked):
    if checked:
      self.updateAttribute('yes')

  def updateAttribute(self, value):
    objectid = self.tabWidget.tabText(self.tabWidget.currentIndex())
    feature = self.featureSet[self.objectIdUrlMap[objectid]]
    if value != feature.attribute('order'):
      attributes = {feature.fieldNameIndex('order'): value}
      self.layer.dataProvider().changeAttributeValues({feature.id(): attributes})
      feature.setAttribute('order', value)

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
    layer = self.canvas.currentLayer()
    if layer is None or QGis.vectorGeometryType(layer.geometryType()) != 'Polygon':
      QMessageBox.information(self.iface.mainWindow(),"Info",'Your active layer must be a polygon layer')
    else:
      self.display.reset()
      self.display.setLayer(layer)
      for feature in layer.getFeatures():
        if feature.fieldNameIndex('browseurl') == -1 and feature.fieldNameIndex('previewurl') == -1:
          QMessageBox.information(self.iface.mainWindow(),"Info",'Your active layer does not appear to be a NGA footprint layer')
          return
        if feature.geometry().contains(point):
          if feature.fieldNameIndex('browseurl') == -1:
            url = "https://browse.digitalglobe.com/imagefinder/showBrowseImage?" + feature.attribute('previewurl').split('?')[1]
          else:  
            url = "https://browse.digitalglobe.com/imagefinder/showBrowseImage?" + feature.attribute('browseurl').split('?')[1]
          self.display.addFeature(url, feature)
          request = QtNetwork.QNetworkRequest(QUrl(url))
          self.network.get(request)
      self.display.show()
      self.display.raise_()

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
    