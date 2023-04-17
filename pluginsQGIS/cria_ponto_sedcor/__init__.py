# -*- coding: utf-8 -*-
"""
/***************************************************************************
 CriaPontoSedcor
                                 A QGIS plugin
 Crai pontos de coleta a partir de DEM
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-03-19
        copyright            : (C) 2023 by Andre Costa
        email                : andre.costa@grupoge21.com
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
    """Load CriaPontoSedcor class from file CriaPontoSedcor.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cria_ponto_sedcor import CriaPontoSedcor
    return CriaPontoSedcor(iface)
