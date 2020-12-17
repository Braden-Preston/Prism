# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'default_ImportFile.ui',
# licensing of 'default_ImportFile.ui' applies.
#
# Created: Sun Dec 15 19:03:30 2019
#      by: pyside2-uic  running on PySide2 5.9.0a1.dev1528389443
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_wg_ImportFile(object):
    def setupUi(self, wg_ImportFile):
        wg_ImportFile.setObjectName("wg_ImportFile")
        wg_ImportFile.resize(340, 706)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wg_ImportFile.sizePolicy().hasHeightForWidth())
        wg_ImportFile.setSizePolicy(sizePolicy)
        wg_ImportFile.setMinimumSize(QtCore.QSize(340, 0))
        wg_ImportFile.setMaximumSize(QtCore.QSize(340, 16777215))
        self.verticalLayout = QtWidgets.QVBoxLayout(wg_ImportFile)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.f_name = QtWidgets.QWidget(wg_ImportFile)
        self.f_name.setObjectName("f_name")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.f_name)
        self.horizontalLayout_2.setContentsMargins(9, 0, 18, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.l_name = QtWidgets.QLabel(self.f_name)
        self.l_name.setObjectName("l_name")
        self.horizontalLayout_2.addWidget(self.l_name)
        self.e_name = QtWidgets.QLineEdit(self.f_name)
        self.e_name.setMinimumSize(QtCore.QSize(0, 0))
        self.e_name.setMaximumSize(QtCore.QSize(9999, 16777215))
        self.e_name.setObjectName("e_name")
        self.horizontalLayout_2.addWidget(self.e_name)
        self.l_class = QtWidgets.QLabel(self.f_name)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.l_class.setFont(font)
        self.l_class.setObjectName("l_class")
        self.horizontalLayout_2.addWidget(self.l_class)
        self.verticalLayout.addWidget(self.f_name)
        self.gb_import = QtWidgets.QGroupBox(wg_ImportFile)
        self.gb_import.setObjectName("gb_import")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.gb_import)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.f_importPath = QtWidgets.QWidget(self.gb_import)
        self.f_importPath.setObjectName("f_importPath")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.f_importPath)
        self.horizontalLayout.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l_file = QtWidgets.QLabel(self.f_importPath)
        self.l_file.setObjectName("l_file")
        self.horizontalLayout.addWidget(self.l_file)
        self.e_file = QtWidgets.QLineEdit(self.f_importPath)
        self.e_file.setReadOnly(False)
        self.e_file.setObjectName("e_file")
        self.horizontalLayout.addWidget(self.e_file)
        self.b_browse = QtWidgets.QPushButton(self.f_importPath)
        self.b_browse.setMinimumSize(QtCore.QSize(22, 0))
        self.b_browse.setMaximumSize(QtCore.QSize(22, 16777215))
        self.b_browse.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_browse.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.b_browse.setObjectName("b_browse")
        self.horizontalLayout.addWidget(self.b_browse)
        self.verticalLayout_2.addWidget(self.f_importPath)
        self.f_importButton = QtWidgets.QWidget(self.gb_import)
        self.f_importButton.setObjectName("f_importButton")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.f_importButton)
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b_import = QtWidgets.QPushButton(self.f_importButton)
        self.b_import.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_import.setObjectName("b_import")
        self.horizontalLayout_3.addWidget(self.b_import)
        self.verticalLayout_2.addWidget(self.f_importButton)
        self.groupBox = QtWidgets.QGroupBox(self.gb_import)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.w_currentVersion = QtWidgets.QWidget(self.groupBox)
        self.w_currentVersion.setObjectName("w_currentVersion")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.w_currentVersion)
        self.horizontalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.w_currentVersion)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.l_curVersion = QtWidgets.QLabel(self.w_currentVersion)
        self.l_curVersion.setObjectName("l_curVersion")
        self.horizontalLayout_5.addWidget(self.l_curVersion)
        self.verticalLayout_3.addWidget(self.w_currentVersion)
        self.w_autoUpdate = QtWidgets.QWidget(self.groupBox)
        self.w_autoUpdate.setObjectName("w_autoUpdate")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.w_autoUpdate)
        self.horizontalLayout_14.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.l_autoUpdate = QtWidgets.QLabel(self.w_autoUpdate)
        self.l_autoUpdate.setObjectName("l_autoUpdate")
        self.horizontalLayout_14.addWidget(self.l_autoUpdate)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem1)
        self.chb_autoUpdate = QtWidgets.QCheckBox(self.w_autoUpdate)
        self.chb_autoUpdate.setText("")
        self.chb_autoUpdate.setChecked(False)
        self.chb_autoUpdate.setObjectName("chb_autoUpdate")
        self.horizontalLayout_14.addWidget(self.chb_autoUpdate)
        self.verticalLayout_3.addWidget(self.w_autoUpdate)
        self.w_latestVersion = QtWidgets.QWidget(self.groupBox)
        self.w_latestVersion.setObjectName("w_latestVersion")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.w_latestVersion)
        self.horizontalLayout_6.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.w_latestVersion)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.l_latestVersion = QtWidgets.QLabel(self.w_latestVersion)
        self.l_latestVersion.setObjectName("l_latestVersion")
        self.horizontalLayout_6.addWidget(self.l_latestVersion)
        self.verticalLayout_3.addWidget(self.w_latestVersion)
        self.w_importLatest = QtWidgets.QWidget(self.groupBox)
        self.w_importLatest.setObjectName("w_importLatest")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.w_importLatest)
        self.horizontalLayout_7.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.b_importLatest = QtWidgets.QPushButton(self.w_importLatest)
        self.b_importLatest.setMinimumSize(QtCore.QSize(0, 0))
        self.b_importLatest.setMaximumSize(QtCore.QSize(99999, 16777215))
        self.b_importLatest.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_importLatest.setObjectName("b_importLatest")
        self.horizontalLayout_7.addWidget(self.b_importLatest)
        self.verticalLayout_3.addWidget(self.w_importLatest)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.gb_options = QtWidgets.QGroupBox(self.gb_import)
        self.gb_options.setObjectName("gb_options")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.gb_options)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.f_keepRefEdits = QtWidgets.QWidget(self.gb_options)
        self.f_keepRefEdits.setObjectName("f_keepRefEdits")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.f_keepRefEdits)
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.l_keepRefEdits = QtWidgets.QLabel(self.f_keepRefEdits)
        self.l_keepRefEdits.setObjectName("l_keepRefEdits")
        self.horizontalLayout_10.addWidget(self.l_keepRefEdits)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem3)
        self.chb_keepRefEdits = QtWidgets.QCheckBox(self.f_keepRefEdits)
        self.chb_keepRefEdits.setText("")
        self.chb_keepRefEdits.setChecked(True)
        self.chb_keepRefEdits.setObjectName("chb_keepRefEdits")
        self.horizontalLayout_10.addWidget(self.chb_keepRefEdits)
        self.verticalLayout_6.addWidget(self.f_keepRefEdits)
        self.f_nameSpaces = QtWidgets.QWidget(self.gb_options)
        self.f_nameSpaces.setObjectName("f_nameSpaces")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.f_nameSpaces)
        self.horizontalLayout_12.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.l_keepRefEdits_2 = QtWidgets.QLabel(self.f_nameSpaces)
        self.l_keepRefEdits_2.setObjectName("l_keepRefEdits_2")
        self.horizontalLayout_12.addWidget(self.l_keepRefEdits_2)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.chb_autoNameSpaces = QtWidgets.QCheckBox(self.f_nameSpaces)
        self.chb_autoNameSpaces.setChecked(False)
        self.chb_autoNameSpaces.setObjectName("chb_autoNameSpaces")
        self.horizontalLayout_12.addWidget(self.chb_autoNameSpaces)
        spacerItem5 = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.b_nameSpaces = QtWidgets.QPushButton(self.f_nameSpaces)
        self.b_nameSpaces.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_nameSpaces.setObjectName("b_nameSpaces")
        self.horizontalLayout_12.addWidget(self.b_nameSpaces)
        self.verticalLayout_6.addWidget(self.f_nameSpaces)
        self.f_unitConversion = QtWidgets.QWidget(self.gb_options)
        self.f_unitConversion.setObjectName("f_unitConversion")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.f_unitConversion)
        self.horizontalLayout_13.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.l_keepRefEdits_3 = QtWidgets.QLabel(self.f_unitConversion)
        self.l_keepRefEdits_3.setObjectName("l_keepRefEdits_3")
        self.horizontalLayout_13.addWidget(self.l_keepRefEdits_3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
        self.b_unitConversion = QtWidgets.QPushButton(self.f_unitConversion)
        self.b_unitConversion.setFocusPolicy(QtCore.Qt.NoFocus)
        self.b_unitConversion.setObjectName("b_unitConversion")
        self.horizontalLayout_13.addWidget(self.b_unitConversion)
        self.verticalLayout_6.addWidget(self.f_unitConversion)
        self.f_abcPath = QtWidgets.QWidget(self.gb_options)
        self.f_abcPath.setObjectName("f_abcPath")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.f_abcPath)
        self.horizontalLayout_11.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.l_abcPath = QtWidgets.QLabel(self.f_abcPath)
        self.l_abcPath.setObjectName("l_abcPath")
        self.horizontalLayout_11.addWidget(self.l_abcPath)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem7)
        self.chb_abcPath = QtWidgets.QCheckBox(self.f_abcPath)
        self.chb_abcPath.setText("")
        self.chb_abcPath.setChecked(True)
        self.chb_abcPath.setObjectName("chb_abcPath")
        self.horizontalLayout_11.addWidget(self.chb_abcPath)
        self.verticalLayout_6.addWidget(self.f_abcPath)
        self.w_preferUnit = QtWidgets.QWidget(self.gb_options)
        self.w_preferUnit.setObjectName("w_preferUnit")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.w_preferUnit)
        self.horizontalLayout_8.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.l_preferUnit = QtWidgets.QLabel(self.w_preferUnit)
        self.l_preferUnit.setObjectName("l_preferUnit")
        self.horizontalLayout_8.addWidget(self.l_preferUnit)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem8)
        self.chb_preferUnit = QtWidgets.QCheckBox(self.w_preferUnit)
        self.chb_preferUnit.setText("")
        self.chb_preferUnit.setObjectName("chb_preferUnit")
        self.horizontalLayout_8.addWidget(self.chb_preferUnit)
        self.verticalLayout_6.addWidget(self.w_preferUnit)
        self.w_trackObjects = QtWidgets.QWidget(self.gb_options)
        self.w_trackObjects.setObjectName("w_trackObjects")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.w_trackObjects)
        self.horizontalLayout_9.setContentsMargins(9, 0, 9, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.l_trackObjects = QtWidgets.QLabel(self.w_trackObjects)
        self.l_trackObjects.setObjectName("l_trackObjects")
        self.horizontalLayout_9.addWidget(self.l_trackObjects)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem9)
        self.chb_trackObjects = QtWidgets.QCheckBox(self.w_trackObjects)
        self.chb_trackObjects.setText("")
        self.chb_trackObjects.setChecked(True)
        self.chb_trackObjects.setObjectName("chb_trackObjects")
        self.horizontalLayout_9.addWidget(self.chb_trackObjects)
        self.verticalLayout_6.addWidget(self.w_trackObjects)
        self.verticalLayout_2.addWidget(self.gb_options)
        self.gb_objects = QtWidgets.QGroupBox(self.gb_import)
        self.gb_objects.setObjectName("gb_objects")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.gb_objects)
        self.verticalLayout_4.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lw_objects = QtWidgets.QListWidget(self.gb_objects)
        self.lw_objects.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.lw_objects.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lw_objects.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.lw_objects.setObjectName("lw_objects")
        self.verticalLayout_4.addWidget(self.lw_objects)
        self.b_selectAll = QtWidgets.QPushButton(self.gb_objects)
        self.b_selectAll.setObjectName("b_selectAll")
        self.verticalLayout_4.addWidget(self.b_selectAll)
        self.verticalLayout_2.addWidget(self.gb_objects)
        self.verticalLayout.addWidget(self.gb_import)

        self.retranslateUi(wg_ImportFile)
        QtCore.QMetaObject.connectSlotsByName(wg_ImportFile)
        wg_ImportFile.setTabOrder(self.e_name, self.e_file)

    def retranslateUi(self, wg_ImportFile):
        wg_ImportFile.setWindowTitle(QtWidgets.QApplication.translate("wg_ImportFile", "ImportFile", None, -1))
        self.l_name.setText(QtWidgets.QApplication.translate("wg_ImportFile", "State name:", None, -1))
        self.l_class.setText(QtWidgets.QApplication.translate("wg_ImportFile", "ImportFile", None, -1))
        self.gb_import.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Import", None, -1))
        self.l_file.setText(QtWidgets.QApplication.translate("wg_ImportFile", "File:", None, -1))
        self.b_browse.setText(QtWidgets.QApplication.translate("wg_ImportFile", "...", None, -1))
        self.b_import.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Import", None, -1))
        self.groupBox.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Version", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Current Version:", None, -1))
        self.l_curVersion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "-", None, -1))
        self.l_autoUpdate.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Auto load latest version:", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Latest Version:", None, -1))
        self.l_latestVersion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "-", None, -1))
        self.b_importLatest.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Import latest Version", None, -1))
        self.gb_options.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Options", None, -1))
        self.l_keepRefEdits.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Keep Reference Edits:", None, -1))
        self.l_keepRefEdits_2.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Maya Namespaces:", None, -1))
        self.chb_autoNameSpaces.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Auto", None, -1))
        self.b_nameSpaces.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Remove", None, -1))
        self.l_keepRefEdits_3.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Unit conversion:", None, -1))
        self.b_unitConversion.setText(QtWidgets.QApplication.translate("wg_ImportFile", "cm -> m", None, -1))
        self.l_abcPath.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Alembic - Update path only (if exists)", None, -1))
        self.l_preferUnit.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Prefer versions in meter:", None, -1))
        self.l_trackObjects.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Keep track of connected objects:", None, -1))
        self.gb_objects.setTitle(QtWidgets.QApplication.translate("wg_ImportFile", "Objects", None, -1))
        self.b_selectAll.setText(QtWidgets.QApplication.translate("wg_ImportFile", "Select all", None, -1))

