# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/Nick/Desktop/untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(473, 582)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 90, 181, 16))
        self.label.setToolTipDuration(10000)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 171, 16))
        self.label_2.setToolTipDuration(10000)
        self.label_2.setObjectName("label_2")
        self.lineEdit_background = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_background.setGeometry(QtCore.QRect(240, 90, 161, 21))
        self.lineEdit_background.setObjectName("lineEdit_background")
        self.lineEdit_gear = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_gear.setGeometry(QtCore.QRect(240, 120, 161, 21))
        self.lineEdit_gear.setObjectName("lineEdit_gear")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 431, 121))
        self.groupBox.setWhatsThis("")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.toolButton_background = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_background.setGeometry(QtCore.QRect(390, 30, 26, 22))
        self.toolButton_background.setObjectName("toolButton_background")
        self.toolButton_gear = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_gear.setGeometry(QtCore.QRect(390, 60, 26, 22))
        self.toolButton_gear.setObjectName("toolButton_gear")
        self.pushButton_randomize = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_randomize.setGeometry(QtCore.QRect(240, 90, 131, 22))
        self.pushButton_randomize.setObjectName("pushButton_randomize")
        self.pushButton_imageFolder = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_imageFolder.setGeometry(QtCore.QRect(20, 90, 161, 22))
        self.pushButton_imageFolder.setObjectName("pushButton_imageFolder")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 190, 191, 111))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.checkBox_reviewer = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_reviewer.setGeometry(QtCore.QRect(20, 30, 131, 20))
        self.checkBox_reviewer.setToolTipDuration(10000)
        self.checkBox_reviewer.setChecked(True)
        self.checkBox_reviewer.setObjectName("checkBox_reviewer")
        self.checkBox_toolbar = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_toolbar.setGeometry(QtCore.QRect(20, 50, 131, 20))
        self.checkBox_toolbar.setToolTipDuration(10000)
        self.checkBox_toolbar.setChecked(True)
        self.checkBox_toolbar.setObjectName("checkBox_toolbar")
        self.checkBox_topbottom = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_topbottom.setGeometry(QtCore.QRect(20, 70, 151, 20))
        self.checkBox_topbottom.setToolTipDuration(10000)
        self.checkBox_topbottom.setChecked(True)
        self.checkBox_topbottom.setObjectName("checkBox_topbottom")
        self.Slider_main = QtWidgets.QSlider(Dialog)
        self.Slider_main.setGeometry(QtCore.QRect(300, 230, 131, 22))
        self.Slider_main.setToolTip("")
        self.Slider_main.setToolTipDuration(-1)
        self.Slider_main.setWhatsThis("")
        self.Slider_main.setMaximum(100)
        self.Slider_main.setPageStep(1)
        self.Slider_main.setProperty("value", 100)
        self.Slider_main.setSliderPosition(100)
        self.Slider_main.setTracking(True)
        self.Slider_main.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_main.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Slider_main.setTickInterval(1)
        self.Slider_main.setObjectName("Slider_main")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 230, 41, 16))
        self.label_5.setToolTip("")
        self.label_5.setToolTipDuration(-1)
        self.label_5.setStatusTip("")
        self.label_5.setWhatsThis("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(240, 270, 51, 16))
        self.label_6.setObjectName("label_6")
        self.Slider_review = QtWidgets.QSlider(Dialog)
        self.Slider_review.setGeometry(QtCore.QRect(300, 270, 131, 22))
        self.Slider_review.setMaximum(100)
        self.Slider_review.setPageStep(1)
        self.Slider_review.setProperty("value", 100)
        self.Slider_review.setSliderPosition(100)
        self.Slider_review.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_review.setInvertedAppearance(False)
        self.Slider_review.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Slider_review.setObjectName("Slider_review")
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(220, 190, 231, 111))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_attachment = QtWidgets.QComboBox(Dialog)
        self.comboBox_attachment.setGeometry(QtCore.QRect(120, 340, 104, 26))
        self.comboBox_attachment.setObjectName("comboBox_attachment")
        self.comboBox_attachment.addItem("")
        self.comboBox_attachment.addItem("")
        self.comboBox_position = QtWidgets.QComboBox(Dialog)
        self.comboBox_position.setGeometry(QtCore.QRect(120, 370, 104, 26))
        self.comboBox_position.setObjectName("comboBox_position")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.comboBox_position.addItem("")
        self.lineEdit_color_main = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_color_main.setGeometry(QtCore.QRect(70, 470, 91, 21))
        self.lineEdit_color_main.setObjectName("lineEdit_color_main")
        self.lineEdit_color_top = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_color_top.setGeometry(QtCore.QRect(310, 470, 91, 21))
        self.lineEdit_color_top.setObjectName("lineEdit_color_top")
        self.lineEdit_color_bottom = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_color_bottom.setGeometry(QtCore.QRect(310, 500, 91, 21))
        self.lineEdit_color_bottom.setObjectName("lineEdit_color_bottom")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 340, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(30, 370, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(240, 370, 81, 16))
        self.label_9.setObjectName("label_9")
        self.scaleBox = QtWidgets.QDoubleSpinBox(Dialog)
        self.scaleBox.setGeometry(QtCore.QRect(327, 369, 91, 24))
        self.scaleBox.setDecimals(1)
        self.scaleBox.setMinimum(0.1)
        self.scaleBox.setSingleStep(0.1)
        self.scaleBox.setProperty("value", 1.0)
        self.scaleBox.setObjectName("scaleBox")
        self.groupBox_4 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 299, 431, 121))
        self.groupBox_4.setTitle("")
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(220, 40, 81, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_size = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_size.setGeometry(QtCore.QRect(300, 40, 104, 26))
        self.comboBox_size.setObjectName("comboBox_size")
        self.comboBox_size.addItem("")
        self.comboBox_size.addItem("")
        self.groupBox_5 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 440, 431, 91))
        self.groupBox_5.setObjectName("groupBox_5")
        self.label_11 = QtWidgets.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(188, 30, 101, 20))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_5)
        self.label_13.setGeometry(QtCore.QRect(188, 60, 101, 20))
        self.label_13.setObjectName("label_13")
        self.toolButton_color_main = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_color_main.setGeometry(QtCore.QRect(150, 30, 26, 22))
        self.toolButton_color_main.setObjectName("toolButton_color_main")
        self.toolButton_color_top = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_color_top.setGeometry(QtCore.QRect(390, 30, 26, 22))
        self.toolButton_color_top.setObjectName("toolButton_color_top")
        self.toolButton_color_bottom = QtWidgets.QToolButton(self.groupBox_5)
        self.toolButton_color_bottom.setGeometry(QtCore.QRect(390, 60, 26, 22))
        self.toolButton_color_bottom.setObjectName("toolButton_color_bottom")
        self.OkButton = QtWidgets.QPushButton(Dialog)
        self.OkButton.setGeometry(QtCore.QRect(370, 540, 81, 22))
        self.OkButton.setObjectName("OkButton")
        self.toolButton_website = QtWidgets.QToolButton(Dialog)
        self.toolButton_website.setGeometry(QtCore.QRect(70, 20, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/CustomBackground/AnKingSmall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_website.setIcon(icon)
        self.toolButton_website.setIconSize(QtCore.QSize(31, 31))
        self.toolButton_website.setObjectName("toolButton_website")
        self.toolButton_youtube = QtWidgets.QToolButton(Dialog)
        self.toolButton_youtube.setGeometry(QtCore.QRect(110, 20, 31, 31))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/CustomBackground/YouTube.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_youtube.setIcon(icon1)
        self.toolButton_youtube.setIconSize(QtCore.QSize(31, 31))
        self.toolButton_youtube.setObjectName("toolButton_youtube")
        self.toolButton_facebook = QtWidgets.QToolButton(Dialog)
        self.toolButton_facebook.setGeometry(QtCore.QRect(370, 20, 31, 31))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/CustomBackground/Facebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_facebook.setIcon(icon2)
        self.toolButton_facebook.setIconSize(QtCore.QSize(31, 31))
        self.toolButton_facebook.setObjectName("toolButton_facebook")
        self.toolButton_instagram = QtWidgets.QToolButton(Dialog)
        self.toolButton_instagram.setGeometry(QtCore.QRect(330, 20, 31, 31))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/CustomBackground/Instagram.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_instagram.setIcon(icon3)
        self.toolButton_instagram.setIconSize(QtCore.QSize(31, 31))
        self.toolButton_instagram.setObjectName("toolButton_instagram")
        self.toolButton_patreon = QtWidgets.QToolButton(Dialog)
        self.toolButton_patreon.setGeometry(QtCore.QRect(150, 22, 171, 26))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/CustomBackground/Patreon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_patreon.setIcon(icon4)
        self.toolButton_patreon.setIconSize(QtCore.QSize(200, 31))
        self.toolButton_patreon.setObjectName("toolButton_patreon")
        self.pushButton_videoTutorial = QtWidgets.QPushButton(Dialog)
        self.pushButton_videoTutorial.setGeometry(QtCore.QRect(20, 540, 141, 22))
        self.pushButton_videoTutorial.setObjectName("pushButton_videoTutorial")
        self.RestoreButton = QtWidgets.QPushButton(Dialog)
        self.RestoreButton.setGeometry(QtCore.QRect(230, 540, 131, 22))
        self.RestoreButton.setObjectName("RestoreButton")
        self.groupBox_5.raise_()
        self.groupBox_4.raise_()
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit_background.raise_()
        self.lineEdit_gear.raise_()
        self.groupBox_2.raise_()
        self.Slider_main.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.Slider_review.raise_()
        self.comboBox_attachment.raise_()
        self.comboBox_position.raise_()
        self.lineEdit_color_main.raise_()
        self.lineEdit_color_top.raise_()
        self.lineEdit_color_bottom.raise_()
        self.label_4.raise_()
        self.label_7.raise_()
        self.label_9.raise_()
        self.scaleBox.raise_()
        self.OkButton.raise_()
        self.toolButton_website.raise_()
        self.toolButton_youtube.raise_()
        self.toolButton_facebook.raise_()
        self.toolButton_instagram.raise_()
        self.toolButton_patreon.raise_()
        self.pushButton_videoTutorial.raise_()
        self.RestoreButton.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Custom Background Settings"))
        self.label.setToolTip(_translate("Dialog", "<html><head/><body><p>Name of the background image file.</p><p>&quot;Random&quot; will shuffle through defaults</p></body></html>"))
        self.label.setText(_translate("Dialog", "Image name for background:"))
        self.label_2.setToolTip(_translate("Dialog", "<html><head/><body><p>Name of the file to replace the gear icon. </p><p>Anki default is gears.svg</p><p>&quot;Random&quot; will shuffle through defaults</p></body></html>"))
        self.label_2.setText(_translate("Dialog", "Image name for gear icon:"))
        self.toolButton_background.setText(_translate("Dialog", "..."))
        self.toolButton_gear.setText(_translate("Dialog", "..."))
        self.pushButton_randomize.setText(_translate("Dialog", "Random Images"))
        self.pushButton_imageFolder.setText(_translate("Dialog", "Open Image Folders"))
        self.checkBox_reviewer.setToolTip(_translate("Dialog", "<html><head/><body><p>Show the background image in the reviewer screen</p></body></html>"))
        self.checkBox_reviewer.setText(_translate("Dialog", "Show in reviewer"))
        self.checkBox_toolbar.setToolTip(_translate("Dialog", "<html><head/><body><p>Show the background image in the top and bottom toolbars in addition to the main screen</p></body></html>"))
        self.checkBox_toolbar.setText(_translate("Dialog", "Show in toolbar"))
        self.checkBox_topbottom.setToolTip(_translate("Dialog", "<html><head/><body><p>Set the background position of the toolbars to top and bottom (if the main background position is set to center, this will look cleaner for most images)<br/></p></body></html>"))
        self.checkBox_topbottom.setText(_translate("Dialog", "Toolbar top/bottom"))
        self.label_5.setText(_translate("Dialog", "Main"))
        self.label_6.setText(_translate("Dialog", "Review"))
        self.groupBox_3.setTitle(_translate("Dialog", "Background opacity"))
        self.comboBox_attachment.setItemText(0, _translate("Dialog", "fixed"))
        self.comboBox_attachment.setItemText(1, _translate("Dialog", "scroll"))
        self.comboBox_position.setCurrentText(_translate("Dialog", "left top"))
        self.comboBox_position.setItemText(0, _translate("Dialog", "left top"))
        self.comboBox_position.setItemText(1, _translate("Dialog", "center top"))
        self.comboBox_position.setItemText(2, _translate("Dialog", "right top"))
        self.comboBox_position.setItemText(3, _translate("Dialog", "right"))
        self.comboBox_position.setItemText(4, _translate("Dialog", "left"))
        self.comboBox_position.setItemText(5, _translate("Dialog", "center"))
        self.comboBox_position.setItemText(6, _translate("Dialog", "left bottom"))
        self.comboBox_position.setItemText(7, _translate("Dialog", "center bottom"))
        self.comboBox_position.setItemText(8, _translate("Dialog", "right bottom"))
        self.label_4.setText(_translate("Dialog", "Attachment:"))
        self.label_7.setText(_translate("Dialog", "Position:"))
        self.label_9.setText(_translate("Dialog", "Scale:"))
        self.label_8.setText(_translate("Dialog", "Size:"))
        self.comboBox_size.setItemText(0, _translate("Dialog", "cover"))
        self.comboBox_size.setItemText(1, _translate("Dialog", "contain"))
        self.groupBox_5.setTitle(_translate("Dialog", "Background color"))
        self.label_11.setText(_translate("Dialog", "Main:"))
        self.label_12.setText(_translate("Dialog", "Top toolbar:"))
        self.label_13.setText(_translate("Dialog", "Bottom toolbar:"))
        self.toolButton_color_main.setText(_translate("Dialog", "..."))
        self.toolButton_color_top.setText(_translate("Dialog", "..."))
        self.toolButton_color_bottom.setText(_translate("Dialog", "..."))
        self.OkButton.setText(_translate("Dialog", "OK"))
        self.toolButton_website.setText(_translate("Dialog", "..."))
        self.toolButton_youtube.setText(_translate("Dialog", "..."))
        self.toolButton_facebook.setText(_translate("Dialog", "..."))
        self.toolButton_instagram.setText(_translate("Dialog", "..."))
        self.toolButton_patreon.setText(_translate("Dialog", "..."))
        self.pushButton_videoTutorial.setText(_translate("Dialog", "Video Tutorial"))
        self.RestoreButton.setText(_translate("Dialog", "Restore Default"))
'''
import icons_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
'''