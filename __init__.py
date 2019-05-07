# -*- coding: utf-8 -*-
"""
/***************************************************************************
 addandzoom
                                 A QGIS plugin
 Add in tiger road data by name and zoom to a coordinate
                             -------------------
        begin                : 2015-10-04
        copyright            : (C) 2015 by Wayne Enterprise
        email                : samkguerrero@gmail.com
        git sha              : $Format:%H$
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


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load addandzoom class from file addandzoom.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .addandzoom import addandzoom
    return addandzoom(iface)
