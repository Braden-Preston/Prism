# -*- coding: utf-8 -*-
#
####################################################
#
# PRISM - Pipeline for animation and VFX projects
#
# www.prism-pipeline.com
#
# contact: contact@prism-pipeline.com
#
####################################################
#
#
# Copyright (C) 2016-2020 Richard Frangenberg
#
# Licensed under GNU GPL-3.0-or-later
#
# This file is part of Prism.
#
# Prism is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Prism is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Prism.  If not, see <https://www.gnu.org/licenses/>.


import os
import logging

try:
    from PySide2.QtCore import *
    from PySide2.QtGui import *
    from PySide2.QtWidgets import *
except:
    from PySide.QtCore import *
    from PySide.QtGui import *

from PrismUtils.Decorators import err_catcher as err_catcher

import hou

logger = logging.getLogger(__name__)


class Prism_Houdini_ImportFile(object):
    def __init__(self, plugin):
        self.plugin = plugin
        self.core = self.plugin.core

    @err_catcher(name=__name__)
    def onNodeCreated(self, kwargs):
        self.plugin.onNodeCreated(kwargs)
        kwargs["node"].setColor(hou.Color(0.451, 0.369, 0.796))

    @err_catcher(name=__name__)
    def getStateFromNode(self, kwargs):
        return self.plugin.getStateFromNode(kwargs)

    @err_catcher(name=__name__)
    def showInStateManagerFromNode(self, kwargs):
        self.plugin.showInStateManagerFromNode(kwargs)

    @err_catcher(name=__name__)
    def openInExplorerFromNode(self, kwargs):
        self.plugin.openInExplorerFromNode(kwargs)

    @err_catcher(name=__name__)
    def openProductBrowserFromNode(self, kwargs):
        state = self.getStateFromNode(kwargs)
        state.ui.browse()
        self.refreshUiFromNode(kwargs, state)

    @err_catcher(name=__name__)
    def refreshUiFromNode(self, kwargs, state=None):
        state = state or self.getStateFromNode(kwargs)
        path = state.ui.getImportPath()
        kwargs["node"].parm("filepath").set(path)

        data = self.core.paths.getCachePathData(path)
        if data["entityType"]:
            date = self.core.getFileModificationDate(os.path.dirname(path))
            task = data.get("task", "")
            versionDir = os.path.basename(os.path.dirname(os.path.dirname(path)))
            versionData = versionDir.split(self.core.filenameSeparator)
            if len(versionData) == 3:
                _, comment, user = versionData
            else:
                comment = data.get("comment", "")
                user = data.get("user", "")
        else:
            expandedPath = hou.expandString(path)
            if os.path.exists(expandedPath):
                date = self.core.getFileModificationDate(expandedPath)
            else:
                date = ""
            task = ""
            comment = ""
            user = ""

        kwargs["node"].parm("entity").set(data.get("fullEntity"))
        kwargs["node"].parm("task").set(task)
        kwargs["node"].parm("version").set(data.get("version", ""))
        kwargs["node"].parm("comment").set(comment)
        kwargs["node"].parm("user").set(user)
        kwargs["node"].parm("date").set(date)

    @err_catcher(name=__name__)
    def setPathFromNode(self, kwargs):
        state = self.getStateFromNode(kwargs)
        state.ui.e_file.setText(kwargs["script_value"])
        state.ui.importObject()
        state.ui.updateUi()
        self.refreshUiFromNode(kwargs)
