"""
/***************************************************************************
Name			 	 : NGA Image Browser
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
 This script initializes the plugin, making it known to QGIS.
"""
def name(): 
  return "NGA Image Browser" 
def description():
  return "A simple plugin to help browse through NGA images."
def version(): 
  return "Version 1.0" 
def qgisMinimumVersion():
  return "2.8"
def classFactory(iface): 
  # load NGABrowser class from file NGABrowser
  from NGABrowser import NGABrowser 
  return NGABrowser(iface)
