# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/taboowords.ui'
#
# Created: Mon Aug 26 23:13:53 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_TabooWords(object):
    def setupUi(self, TabooWords):
        TabooWords.setObjectName("TabooWords")
        TabooWords.resize(804, 751)
        self.centralwidget = QtGui.QWidget(TabooWords)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_8 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.glCard = QtGui.QGridLayout()
        self.glCard.setObjectName("glCard")
        self.qteCard = QtGui.QTextEdit(self.groupBox_3)
        self.qteCard.setReadOnly(True)
        self.qteCard.setObjectName("qteCard")
        self.glCard.addWidget(self.qteCard, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pbSkip = QtGui.QPushButton(self.groupBox_3)
        self.pbSkip.setObjectName("pbSkip")
        self.horizontalLayout_2.addWidget(self.pbSkip)
        self.pbWin = QtGui.QPushButton(self.groupBox_3)
        self.pbWin.setObjectName("pbWin")
        self.horizontalLayout_2.addWidget(self.pbWin)
        self.glCard.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.glCard, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.tlRemainingCards = QtGui.QLabel(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tlRemainingCards.setFont(font)
        self.tlRemainingCards.setObjectName("tlRemainingCards")
        self.gridLayout.addWidget(self.tlRemainingCards, 0, 0, 1, 1)
        self.lcdRemainingCards = QtGui.QLCDNumber(self.groupBox_3)
        self.lcdRemainingCards.setNumDigits(3)
        self.lcdRemainingCards.setProperty("intValue", 5)
        self.lcdRemainingCards.setObjectName("lcdRemainingCards")
        self.gridLayout.addWidget(self.lcdRemainingCards, 0, 1, 1, 1)
        self.pbNewCardsRound = QtGui.QPushButton(self.groupBox_3)
        self.pbNewCardsRound.setObjectName("pbNewCardsRound")
        self.gridLayout.addWidget(self.pbNewCardsRound, 1, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout, 1, 1, 1, 1)
        self.twDiscardedCards = QtGui.QTableWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.twDiscardedCards.setFont(font)
        self.twDiscardedCards.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twDiscardedCards.setAlternatingRowColors(True)
        self.twDiscardedCards.setObjectName("twDiscardedCards")
        self.twDiscardedCards.setColumnCount(1)
        self.twDiscardedCards.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.twDiscardedCards.setHorizontalHeaderItem(0, item)
        self.twDiscardedCards.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_5.addWidget(self.twDiscardedCards, 0, 0, 2, 1)
        self.twGuessedCards = QtGui.QTableWidget(self.groupBox_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.twGuessedCards.setFont(font)
        self.twGuessedCards.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.twGuessedCards.setAlternatingRowColors(True)
        self.twGuessedCards.setShowGrid(True)
        self.twGuessedCards.setGridStyle(QtCore.Qt.SolidLine)
        self.twGuessedCards.setObjectName("twGuessedCards")
        self.twGuessedCards.setColumnCount(1)
        self.twGuessedCards.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.twGuessedCards.setHorizontalHeaderItem(0, item)
        self.twGuessedCards.horizontalHeader().setStretchLastSection(True)
        self.twGuessedCards.verticalHeader().setVisible(True)
        self.gridLayout_5.addWidget(self.twGuessedCards, 0, 2, 2, 1)
        self.gridLayout_7.addLayout(self.gridLayout_5, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_3, 0, 0, 1, 2)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pbProcessRound = QtGui.QPushButton(self.groupBox)
        self.pbProcessRound.setObjectName("pbProcessRound")
        self.gridLayout_2.addWidget(self.pbProcessRound, 0, 2, 3, 1)
        self.leGuessedCards = QtGui.QLineEdit(self.groupBox)
        self.leGuessedCards.setAlignment(QtCore.Qt.AlignCenter)
        self.leGuessedCards.setObjectName("leGuessedCards")
        self.gridLayout_2.addWidget(self.leGuessedCards, 0, 1, 1, 1)
        self.tlDiscardedCards = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tlDiscardedCards.setFont(font)
        self.tlDiscardedCards.setObjectName("tlDiscardedCards")
        self.gridLayout_2.addWidget(self.tlDiscardedCards, 1, 0, 1, 1)
        self.tlGuessedCards = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tlGuessedCards.setFont(font)
        self.tlGuessedCards.setObjectName("tlGuessedCards")
        self.gridLayout_2.addWidget(self.tlGuessedCards, 0, 0, 1, 1)
        self.leDiscardedCards = QtGui.QLineEdit(self.groupBox)
        self.leDiscardedCards.setAlignment(QtCore.Qt.AlignCenter)
        self.leDiscardedCards.setObjectName("leDiscardedCards")
        self.gridLayout_2.addWidget(self.leDiscardedCards, 1, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        self.glScores = QtGui.QGridLayout()
        self.glScores.setObjectName("glScores")
        self.tlScoreTeamB = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tlScoreTeamB.setFont(font)
        self.tlScoreTeamB.setObjectName("tlScoreTeamB")
        self.glScores.addWidget(self.tlScoreTeamB, 1, 1, 1, 1)
        self.tlScoreTeamA = QtGui.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.tlScoreTeamA.setFont(font)
        self.tlScoreTeamA.setObjectName("tlScoreTeamA")
        self.glScores.addWidget(self.tlScoreTeamA, 0, 1, 1, 1)
        self.lcdScoreTeamA = QtGui.QLCDNumber(self.groupBox)
        self.lcdScoreTeamA.setNumDigits(3)
        self.lcdScoreTeamA.setObjectName("lcdScoreTeamA")
        self.glScores.addWidget(self.lcdScoreTeamA, 0, 2, 1, 1)
        self.lcdScoreTeamB = QtGui.QLCDNumber(self.groupBox)
        self.lcdScoreTeamB.setNumDigits(3)
        self.lcdScoreTeamB.setObjectName("lcdScoreTeamB")
        self.glScores.addWidget(self.lcdScoreTeamB, 1, 2, 1, 1)
        self.rbPlayingA = QtGui.QRadioButton(self.groupBox)
        self.rbPlayingA.setChecked(True)
        self.rbPlayingA.setObjectName("rbPlayingA")
        self.glScores.addWidget(self.rbPlayingA, 0, 0, 1, 1)
        self.rbPlayingB = QtGui.QRadioButton(self.groupBox)
        self.rbPlayingB.setObjectName("rbPlayingB")
        self.glScores.addWidget(self.rbPlayingB, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.glScores, 3, 0, 1, 2)
        self.gridLayout_6 = QtGui.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_4.addLayout(self.gridLayout_6, 0, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 4, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.glTimer = QtGui.QGridLayout()
        self.glTimer.setObjectName("glTimer")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbTimerStart = QtGui.QPushButton(self.groupBox_2)
        self.pbTimerStart.setObjectName("pbTimerStart")
        self.horizontalLayout.addWidget(self.pbTimerStart)
        self.pbTimerPause = QtGui.QPushButton(self.groupBox_2)
        self.pbTimerPause.setObjectName("pbTimerPause")
        self.horizontalLayout.addWidget(self.pbTimerPause)
        self.pbTimerReset = QtGui.QPushButton(self.groupBox_2)
        self.pbTimerReset.setObjectName("pbTimerReset")
        self.horizontalLayout.addWidget(self.pbTimerReset)
        self.glTimer.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.lcdTimer = QTimerWidget(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdTimer.sizePolicy().hasHeightForWidth())
        self.lcdTimer.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.lcdTimer.setFont(font)
        self.lcdTimer.setNumDigits(3)
        self.lcdTimer.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdTimer.setProperty("intValue", 60)
        self.lcdTimer.setObjectName("lcdTimer")
        self.glTimer.addWidget(self.lcdTimer, 0, 0, 1, 1)
        self.gridLayout_3.addLayout(self.glTimer, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_2, 1, 1, 1, 1)
        TabooWords.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TabooWords)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 804, 21))
        self.menubar.setObjectName("menubar")
        TabooWords.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TabooWords)
        self.statusbar.setObjectName("statusbar")
        TabooWords.setStatusBar(self.statusbar)

        self.retranslateUi(TabooWords)
        QtCore.QMetaObject.connectSlotsByName(TabooWords)

    def retranslateUi(self, TabooWords):
        TabooWords.setWindowTitle(QtGui.QApplication.translate("TabooWords", "Taboo words", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_3.setTitle(QtGui.QApplication.translate("TabooWords", "Cartas", None, QtGui.QApplication.UnicodeUTF8))
        self.qteCard.setHtml(QtGui.QApplication.translate("TabooWords", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">PALABRA #1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* TABOO #1</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* TABOO #2</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* TABOO #3</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* TABOO #4</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">* TABOO #5</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.pbSkip.setText(QtGui.QApplication.translate("TabooWords", "<< Saltear", None, QtGui.QApplication.UnicodeUTF8))
        self.pbWin.setText(QtGui.QApplication.translate("TabooWords", "Ganada >>", None, QtGui.QApplication.UnicodeUTF8))
        self.tlRemainingCards.setText(QtGui.QApplication.translate("TabooWords", "Tarjetas restantes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbNewCardsRound.setText(QtGui.QApplication.translate("TabooWords", "Dar nueva ronda de cartas", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.verticalHeaderItem(0).setText(QtGui.QApplication.translate("TabooWords", "#1", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.verticalHeaderItem(1).setText(QtGui.QApplication.translate("TabooWords", "#2", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.verticalHeaderItem(2).setText(QtGui.QApplication.translate("TabooWords", "#3", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.verticalHeaderItem(3).setText(QtGui.QApplication.translate("TabooWords", "#4", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.verticalHeaderItem(4).setText(QtGui.QApplication.translate("TabooWords", "#5", None, QtGui.QApplication.UnicodeUTF8))
        self.twDiscardedCards.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TabooWords", "Tarjetas Salteadas", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.verticalHeaderItem(0).setText(QtGui.QApplication.translate("TabooWords", "#1", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.verticalHeaderItem(1).setText(QtGui.QApplication.translate("TabooWords", "#2", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.verticalHeaderItem(2).setText(QtGui.QApplication.translate("TabooWords", "#3", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.verticalHeaderItem(3).setText(QtGui.QApplication.translate("TabooWords", "#4", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.verticalHeaderItem(4).setText(QtGui.QApplication.translate("TabooWords", "#5", None, QtGui.QApplication.UnicodeUTF8))
        self.twGuessedCards.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("TabooWords", "Tarjetas Ganadas", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("TabooWords", "Puntajes", None, QtGui.QApplication.UnicodeUTF8))
        self.pbProcessRound.setText(QtGui.QApplication.translate("TabooWords", "Procesar Ronda", None, QtGui.QApplication.UnicodeUTF8))
        self.leGuessedCards.setText(QtGui.QApplication.translate("TabooWords", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tlDiscardedCards.setText(QtGui.QApplication.translate("TabooWords", "Tarjetas Salteadas", None, QtGui.QApplication.UnicodeUTF8))
        self.tlGuessedCards.setText(QtGui.QApplication.translate("TabooWords", "Tarjetas Ganadas", None, QtGui.QApplication.UnicodeUTF8))
        self.leDiscardedCards.setText(QtGui.QApplication.translate("TabooWords", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.tlScoreTeamB.setText(QtGui.QApplication.translate("TabooWords", "Puntaje grupo B:", None, QtGui.QApplication.UnicodeUTF8))
        self.tlScoreTeamA.setText(QtGui.QApplication.translate("TabooWords", "Puntaje grupo A:", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPlayingA.setText(QtGui.QApplication.translate("TabooWords", "Jugando", None, QtGui.QApplication.UnicodeUTF8))
        self.rbPlayingB.setText(QtGui.QApplication.translate("TabooWords", "Jugando", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("TabooWords", "Tiempo", None, QtGui.QApplication.UnicodeUTF8))
        self.pbTimerStart.setText(QtGui.QApplication.translate("TabooWords", "Iniciar!", None, QtGui.QApplication.UnicodeUTF8))
        self.pbTimerPause.setText(QtGui.QApplication.translate("TabooWords", "Pausar", None, QtGui.QApplication.UnicodeUTF8))
        self.pbTimerReset.setText(QtGui.QApplication.translate("TabooWords", "Resetear", None, QtGui.QApplication.UnicodeUTF8))

from qtimerwidget import QTimerWidget