# -*- coding: utf-8 -*-
"""
/***************************************************************************
 addandzoom
                                 A QGIS plugin
 Add in tiger road data by name and zoom to a coordinate
                              -------------------
        begin                : 2015-10-04
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Wayne Enterprise
        email                : samkguerrero@gmail.com
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
from qgis.core import QgsFeature
from qgis.core import QgsMapLayerRegistry, QgsVectorLayer
from qgis.gui import QgisInterface
import qgis.core
import qgis.gui
import qgis.utils
import zipfile
import sys
import os.path
import os
import glob
from PyQt4.QtCore import QSettings, QTranslator, qVersion, QCoreApplication
from PyQt4.QtGui import QAction, QIcon
# Initialize Qt resources from file resources.py
import resources
# Import the code for the dialog
from addandzoom_dialog import addandzoomDialog
import os.path


class addandzoom:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        """Constructor.

        :param iface: An interface instance that will be passed to this class
            which provides the hook by which you can manipulate the QGIS
            application at run time.
        :type iface: QgsInterface
        """
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        # initialize locale
        locale = QSettings().value('locale/userLocale')[0:2]
        locale_path = os.path.join(
            self.plugin_dir,
            'i18n',
            'addandzoom_{}.qm'.format(locale))

        if os.path.exists(locale_path):
            self.translator = QTranslator()
            self.translator.load(locale_path)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = addandzoomDialog()

        # Declare instance attributes
        self.actions = []
        self.menu = self.tr(u'&addandzoom')
        # TODO: We are going to let the user set this up in a future iteration
        self.toolbar = self.iface.addToolBar(u'addandzoom')
        self.toolbar.setObjectName(u'addandzoom')

    # noinspection PyMethodMayBeStatic
    def tr(self, message):
        """Get the translation for a string using Qt translation API.

        We implement this ourselves since we do not inherit QObject.

        :param message: String for translation.
        :type message: str, QString

        :returns: Translated version of message.
        :rtype: QString
        """
        # noinspection PyTypeChecker,PyArgumentList,PyCallByClass
        return QCoreApplication.translate('addandzoom', message)


    def add_action(
        self,
        icon_path,
        text,
        callback,
        enabled_flag=True,
        add_to_menu=True,
        add_to_toolbar=True,
        status_tip=None,
        whats_this=None,
        parent=None):
        """Add a toolbar icon to the toolbar.

        :param icon_path: Path to the icon for this action. Can be a resource
            path (e.g. ':/plugins/foo/bar.png') or a normal file system path.
        :type icon_path: str

        :param text: Text that should be shown in menu items for this action.
        :type text: str

        :param callback: Function to be called when the action is triggered.
        :type callback: function

        :param enabled_flag: A flag indicating if the action should be enabled
            by default. Defaults to True.
        :type enabled_flag: bool

        :param add_to_menu: Flag indicating whether the action should also
            be added to the menu. Defaults to True.
        :type add_to_menu: bool

        :param add_to_toolbar: Flag indicating whether the action should also
            be added to the toolbar. Defaults to True.
        :type add_to_toolbar: bool

        :param status_tip: Optional text to show in a popup when mouse pointer
            hovers over the action.
        :type status_tip: str

        :param parent: Parent widget for the new action. Defaults None.
        :type parent: QWidget

        :param whats_this: Optional text to show in the status bar when the
            mouse pointer hovers over the action.

        :returns: The action that was created. Note that the action is also
            added to self.actions list.
        :rtype: QAction
        """

        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        action.triggered.connect(callback)
        action.setEnabled(enabled_flag)

        if status_tip is not None:
            action.setStatusTip(status_tip)

        if whats_this is not None:
            action.setWhatsThis(whats_this)

        if add_to_toolbar:
            self.toolbar.addAction(action)

        if add_to_menu:
            self.iface.addPluginToMenu(
                self.menu,
                action)

        self.actions.append(action)

        return action

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""

        icon_path = ':/plugins/addandzoom/icon.png'
        self.add_action(
            icon_path,
            text=self.tr(u'addandzoom'),
            callback=self.run,
            parent=self.iface.mainWindow())


    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu(
                self.tr(u'&addandzoom'),
                action)
            self.iface.removeToolBarIcon(action)
        # remove the toolbar
        del self.toolbar


    def run(self):
        """Run method that performs all the real work"""
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result:
            # Do something useful here - delete the line containing pass and
            # substitute with your code.

            locale_path = os.path.dirname(__file__)

            from qgis.core import QgsFeature
            from qgis.core import QgsMapLayerRegistry, QgsVectorLayer
            from qgis.gui import QgisInterface
            import qgis.core
            import qgis.gui
            import qgis.utils

            coordinatez = self.dlg.coordinatestxt.text()

            coordinates = str(coordinatez)
            comma = coordinates.find(",")
            ylat = coordinates[:comma]
            xlong = coordinates[comma + 1:]
            ylat = float(ylat)
            xlong = float(xlong)
            print ylat
            print xlong

            if not coordinatez:
                return

            from qgis.core import QgsMapLayerRegistry, QgsVectorLayer
            from qgis.gui import QgisInterface
            import qgis.core
            import qgis.utils
            import qgis.gui
            from PyQt4 import QtGui, QtCore
            from qgis.core import QgsFeature
            from qgis.core import QgsMapLayerRegistry, QgsVectorLayer
            from qgis.gui import QgisInterface

            canvas = qgis.utils.iface.mapCanvas()

            def zoomi(xlong,ylat):
                    from qgis import core
                    import qgis.core
                    import qgis.utils
                    import qgis.gui
                    canvas = qgis.utils.iface.mapCanvas()
                    scale = 1
                    rect = qgis.core.QgsRectangle(float(xlong)-scale,float(ylat)-scale,float(xlong)+scale,float(ylat)+scale)
                    canvas.setExtent(rect)
                    canvas.zoomScale(3500)
                    canvas.refresh()

                
            def sym(countylayer):
                countylayer.loadNamedStyle(locale_path + '/symbol.qml')
                countylayer.loadNamedStyle(locale_path + '/label.qml')
                canvas.refresh()
                countylayer.triggerRepaint()

            def addVectorLayer(uri, provider, name):
                vl = QgsVectorLayer(uri, name, provider)
                QgsMapLayerRegistry.instance().addMapLayer(vl)
                return vl, name

            class MyIface(QgisInterface):
                def __init__(self):
                    QgisInterface.__init__(self)
                def addVectorLayer(self, path, name, provider):
                    return addVectorLayer(path, provider, name)

            canvas = qgis.utils.iface.mapCanvas()

            try:
                inputLayer = QgsMapLayerRegistry.instance().mapLayersByName("esri_imagery")[0]
            except IndexError:
                import qgis.core
                import qgis.utils
                qgis.utils.iface.addRasterLayer("http://server.arcgisonline.com/ArcGIS/rest/services/ESRI_Imagery_World_2D/MapServer?f=json&pretty=true","esri_imagery")

            try:
                inputLayer = QgsMapLayerRegistry.instance().mapLayersByName("esri_street")[0]
            except IndexError:
                import qgis.core
                import qgis.utils
                qgis.utils.iface.addRasterLayer("http://server.arcgisonline.com/ArcGIS/rest/services/ESRI_StreetMap_World_2D/MapServer?f=json&pretty=true","esri_street")
                

            try:
                inputLayer = QgsMapLayerRegistry.instance().mapLayersByName("County_Index")[0]
            except IndexError:
                import qgis.core
                import qgis.utils
                qgis.utils.iface.addVectorLayer(locale_path + '/TIGER2015_county_index/tl_2015_us_county.shp','County_Index','ogr')
                QgsMapLayerRegistry.instance().mapLayersByName("County_Index")[0].loadNamedStyle(locale_path + '/cindexsymbol.qml')

            from qgis.core import QgsMapLayerRegistry, QgsVectorLayer
            from qgis.gui import QgisInterface

            try:
                inputLayer = QgsMapLayerRegistry.instance().mapLayersByName("You are here")[0]
            except IndexError:
                print "making a point"
                mlr = QgsMapLayerRegistry.instance()
                mlr.mapLayers()
                luyer =  QgsVectorLayer('Point?crs=EPSG:4269','You are here',"memory")
                pr = luyer.dataProvider() 
                pt = QgsFeature()
                point1 = qgis.core.QgsPoint(xlong,ylat)
                pt.setGeometry(qgis.core.QgsGeometry.fromPoint(point1))
                pr.addFeatures([pt])
                luyer.updateExtents()
                QgsMapLayerRegistry.instance().addMapLayers([luyer])
                luyer.loadNamedStyle(locale_path + '/pointsym.qml')
                print "point made"

            try:
                mapcanvas = qgis.utils.iface.mapCanvas()
                layers = mapcanvas.layers()
                if layers[1].name() == "County_Index" and layers[0].name() == 'You are here':
                    import processing
                    mapcanvas = qgis.utils.iface.mapCanvas()
                    layers = mapcanvas.layers()
                    countyindex = layers[1]
                    point = layers[0]
                    #countyindex on left, point on right. the mapcanvas counts down from 0.
                    processing.runalg('qgis:selectbylocation',countyindex,point, u'contains', 0)
                    print "selected"
                elif layers[2].name() == "County_Index" and layers[0].name() == 'You are here':
                    import processing
                    mapcanvas = qgis.utils.iface.mapCanvas()
                    layers = mapcanvas.layers()
                    countyindex = layers[2]
                    point = layers[0]
                    #countyindex on left, point on right. the mapcanvas counts down from 0.
                    processing.runalg('qgis:selectbylocation',countyindex,point, u'contains', 0)
                    print "selected"
                else:
                    print "i don't know man"

                layer = QgsMapLayerRegistry.instance().mapLayersByName('County_Index')[0]
                selected_features = layer.selectedFeatures()
                for i in selected_features:
                    print i['GEOID']
                    fips = i['GEOID'] 
                    print i['NAME']
                    nombre = i['NAME']
                    countpath = locale_path + '/TigerRoads/tl_2015_%s_roads/tl_2015_%s_roads.shp' % (fips,fips)
                    try:
                        inputLayer = QgsMapLayerRegistry.instance().mapLayersByName(nombre)[0]
                    except:
                        try:
                            zipped = zipfile.PyZipFile(locale_path + '/TigerRoads/tl_2015_%s_roads.zip' % (fips)) 
                            zipped.extractall(locale_path + '/TigerRoads/tl_2015_%s_roads' % (fips)) 
                            myiface = MyIface()
                            myiface.addVectorLayer(countpath,nombre,'ogr')
                            sym(qgis.utils.iface.activeLayer())
                            canvas.refresh()
                            zoomi(xlong,ylat)
                        except:
                            myiface = MyIface()
                            myiface.addVectorLayer(countpath,nombre,'ogr')
                            sym(qgis.utils.iface.activeLayer())
                            canvas.refresh()
                            zoomi(xlong,ylat)
                mlr = QgsMapLayerRegistry.instance()
                mlr.mapLayers()
                for i in mlr.mapLayers():
                    if not nombre in i.replace("_", " "):
                        if not i.startswith('County_Index'):
                            if not i.startswith('apple'):
                                if not i.startswith('esri'):
                                    mlr.removeMapLayer(i)
                layer.setSelectedFeatures([])
            except:
                print "I can't do it."

            

            # figure out how to access layer by name, call a layer object by a name
            # globally delcare so variables can be used throughout the code
            # force the order by aranging things on map canvas/toc













