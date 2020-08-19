# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pomodoro.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
import time, datetime, os
from pathlib import Path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("Timer")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("Settings")
        self.tabWidget.addTab(self.tab_2, "")
        self.pomoLabel = QtWidgets.QLabel(self.tab)
        self.pomoLabel.setGeometry(QtCore.QRect(260, 30, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.pomoLabel.setFont(font)
        self.pomoLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pomoLabel.setObjectName("pomoLabel")
        self.startButton = QtWidgets.QPushButton(self.tab)
        self.startButton.setGeometry(QtCore.QRect(70, 400, 161, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 170, 0))
        self.startButton.setPalette(palette)
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(self.tab)
        self.stopButton.setGeometry(QtCore.QRect(320, 400, 161, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.stopButton.setPalette(palette)
        self.stopButton.setObjectName("stopButton")
        self.resetButton = QtWidgets.QPushButton(self.tab)
        self.resetButton.setGeometry(QtCore.QRect(570, 400, 161, 91))
        self.resetButton.setObjectName("resetButton")
        self.pomoLabel_2 = QtWidgets.QLabel(self.tab)
        self.pomoLabel_2.setGeometry(QtCore.QRect(70, 190, 661, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.pomoLabel_2.setFont(font)
        self.pomoLabel_2.setAlignment(QtCore.Qt.AlignCenter)
        self.pomoLabel_2.setObjectName("pomoLabel_2")
        self.pomoButton = QtWidgets.QPushButton(self.tab)
        self.pomoButton.setGeometry(QtCore.QRect(270, 120, 93, 28))
        self.pomoButton.setObjectName("pomoButton")
        self.shortButton = QtWidgets.QPushButton(self.tab)
        self.shortButton.setGeometry(QtCore.QRect(360, 120, 93, 28))
        self.shortButton.setObjectName("shortButton")
        self.longButton = QtWidgets.QPushButton(self.tab)
        self.longButton.setGeometry(QtCore.QRect(450, 120, 93, 28))
        self.longButton.setObjectName("longButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        font2 = QtGui.QFont()
        font2.setPointSize(18)
        self.setCustomTime = QtWidgets.QLabel(self.tab_2)
        self.setCustomTime.setGeometry(QtCore.QRect(0, 0, 450, 100))
        self.setCustomTime.setFont(font2)
        self.setCustomTime.setAlignment(QtCore.Qt.AlignCenter)
        self.setCustomTime.setObjectName("customTimeLabel")
        font3 = QtGui.QFont()
        font3.setPointSize(12)
        self.setPomo = QtWidgets.QLabel(self.tab_2)
        self.setPomo.setGeometry(QtCore.QRect(30, 50, 100, 100))
        self.setPomo.setFont(font3)
        self.setPomo.setAlignment(QtCore.Qt.AlignCenter)
        self.setPomo.setObjectName("setPomoLabel")
        self.setShortBreak = QtWidgets.QLabel(self.tab_2)
        self.setShortBreak.setGeometry(QtCore.QRect(230, 50, 105, 100))
        self.setShortBreak.setFont(font3)
        self.setShortBreak.setAlignment(QtCore.Qt.AlignCenter)
        self.setShortBreak.setObjectName("setSBreakLabel")
        self.setLongBreak = QtWidgets.QLabel(self.tab_2)
        self.setLongBreak.setGeometry(QtCore.QRect(430, 50, 100, 100))
        self.setLongBreak.setFont(font3)
        self.setLongBreak.setAlignment(QtCore.Qt.AlignCenter)
        self.setLongBreak.setObjectName("setLBreakLabel")
        self.spinPomo = QtWidgets.QSpinBox(self.tab_2)
        self.spinPomo.setGeometry(QtCore.QRect(30, 120, 100, 30))
        self.spinPomo.setObjectName("spinPomo")
        self.spinPomo.setValue(25)
        self.spinSBreak = QtWidgets.QDoubleSpinBox(self.tab_2)
        self.spinSBreak.setGeometry(QtCore.QRect(230, 120, 100, 30))
        self.spinSBreak.setObjectName("spinSBreak")
        self.spinSBreak.setValue(5)
        self.spinLBreak = QtWidgets.QSpinBox(self.tab_2)
        self.spinLBreak.setGeometry(QtCore.QRect(430, 120, 100, 30))
        self.spinLBreak.setObjectName("spinLBreak")
        self.spinLBreak.setValue(10)
        self.saveButton = QtWidgets.QPushButton(self.tab_2)
        self.saveButton.setGeometry(QtCore.QRect(10, 500, 93, 28))
        self.saveButton.setObjectName("saveButton")
        self.soundList = QtWidgets.QListWidget(self.tab_2)
        self.soundList.setGeometry(QtCore.QRect(550, 75, 200, 200))
        self.soundList.setObjectName("soundList")
        self.setSound = QtWidgets.QLabel(self.tab_2)
        self.setSound.setGeometry(QtCore.QRect(550, 10, 120, 100))
        self.setSound.setFont(font3)
        self.loadSounds()

        self.pomoButton.clicked.connect(self.reset)
        self.shortButton.clicked.connect(self.shortBreak)
        self.longButton.clicked.connect(self.longBreak)
        self.startButton.clicked.connect(self.begin)
        self.stopButton.clicked.connect(self.stop)
        self.resetButton.clicked.connect(self.reset)    
        self.saveButton.clicked.connect(self.saveSettings)
        self.timePomo = 25 * 60
        self.timeShort = 5 * 60
        self.timeLong = 10 * 60
        self.timeLeft = time.strftime('%H:%M:%S', time.gmtime(self.timePomo))
        self.timeLeftInt = self.timePomo
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.begin)
        self.alarmFile = QtMultimedia.QSound('Sounds/pauwi.wav')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PomoTime"))
        self.pomoLabel.setText(_translate("MainWindow", "Pomodoro Timer"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))
        self.resetButton.setText(_translate("MainWindow", "Reset"))
        self.pomoLabel_2.setText(_translate("MainWindow", str(self.timeLeft)))
        self.pomoButton.setText(_translate("MainWindow", "Pomodoro"))
        self.shortButton.setText(_translate("MainWindow", "Short Break"))
        self.longButton.setText(_translate("MainWindow", "Long Break"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Timer"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Settings"))
        self.setCustomTime.setText(_translate("MainWindow", "Set Custom Times (in minutes)"))
        self.setPomo.setText(_translate("MainWindow", "Pomodoro"))
        self.setShortBreak.setText(_translate("MainWindow", "Short Break"))
        self.setLongBreak.setText(_translate("MainWindow", "Long Break"))
        self.setSound.setText(_translate("MainWindow", "Select Sound"))
        self.saveButton.setText(_translate("MainWindow", "Save"))

    def begin(self):
        if (self.tabWidget.currentIndex() == 1):
            self.timer.stop()
        self.pomoLabel_2.setText(str(self.timeLeft))
        MainWindow.setWindowTitle('PomoTime (%s)' %(str(self.timeLeft)))
        self.timeLeftInt -= 1
        self.timeLeft = time.strftime('%H:%M:%S', time.gmtime(self.timeLeftInt))
        if self.timeLeft != time.strftime('%H:%M:%S', time.gmtime(0)):
            self.timer.start(1000)
        else:
            QtCore.QTimer.singleShot(1000, lambda: self.pomoLabel_2.setText('Time\'s up! Time for a break!'))
            self.timer.stop()
            QtCore.QTimer.singleShot(1000, lambda: self.alarmFile.play())
            QtCore.QTimer.singleShot(1000, lambda: MainWindow.setWindowTitle('PomoTime (%s)' %('Pomo Done!')))

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timeLeft = time.strftime('%H:%M:%S', time.gmtime(self.timePomo))
        self.pomoLabel_2.setText(str(self.timeLeft))
        self.timeLeftInt = self.timePomo
        self.timer.stop()

    def shortBreak(self):
        self.timeLeft = time.strftime('%H:%M:%S', time.gmtime(self.timeShort))
        self.pomoLabel_2.setText(str(self.timeLeft))
        self.timeLeftInt = self.timeShort
        self.timer.stop()

    def longBreak(self):
        self.timeLeft = time.strftime('%H:%M:%S', time.gmtime(self.timeLong))
        self.pomoLabel_2.setText(str(self.timeLeft))
        self.timeLeftInt = self.timeLong
        self.timer.stop()

    def saveSettings(self):
        self.timePomo = self.spinPomo.value() * 60
        self.timeShort = self.spinSBreak.value() * 60
        self.timeLong = self.spinLBreak.value() * 60
        self.alarmFile = QtMultimedia.QSound('Sounds/'+self.soundList.selectedItems()[0].text())
        self.reset()
        self.tabWidget.setCurrentIndex(0)

    def loadSounds(self):
        for soundFile in os.listdir('.\\Sounds'):
            self.soundList.addItem(str(os.path.basename(Path('./Sounds') / soundFile)))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
