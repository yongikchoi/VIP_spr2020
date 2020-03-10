# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'autograders2.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutograderS2(object):
    def setupUi(self, AutograderS2):
        AutograderS2.setObjectName("AutograderS2")
        AutograderS2.resize(800, 600)
        AutograderS2.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.centralwidget = QtWidgets.QWidget(AutograderS2)
        self.centralwidget.setObjectName("centralwidget")
        self.exportButton = QtWidgets.QPushButton(self.centralwidget)
        self.exportButton.setGeometry(QtCore.QRect(640, 450, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.exportButton.setFont(font)
        self.exportButton.setStyleSheet("background-color: rgb(170, 255, 255)")
        self.exportButton.setObjectName("exportButton")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 0, 801, 131))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(36)
        self.titleLabel.setFont(font)
        self.titleLabel.setStyleSheet("background-color: rgb(85, 255, 255)")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.scoreLabel = QtWidgets.QLabel(self.centralwidget)
        self.scoreLabel.setGeometry(QtCore.QRect(590, 150, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.scoreLabel.setFont(font)
        self.scoreLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.scoreLabel.setObjectName("scoreLabel")
        self.score = QtWidgets.QLabel(self.centralwidget)
        self.score.setGeometry(QtCore.QRect(590, 210, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.score.setFont(font)
        self.score.setFrameShape(QtWidgets.QFrame.Box)
        self.score.setObjectName("score")
        self.confusionMatrixLabel = QtWidgets.QLabel(self.centralwidget)
        self.confusionMatrixLabel.setGeometry(QtCore.QRect(300, 150, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.confusionMatrixLabel.setFont(font)
        self.confusionMatrixLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.confusionMatrixLabel.setObjectName("confusionMatrixLabel")
        self.signCategoriesLabel = QtWidgets.QLabel(self.centralwidget)
        self.signCategoriesLabel.setGeometry(QtCore.QRect(10, 150, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(16)
        self.signCategoriesLabel.setFont(font)
        self.signCategoriesLabel.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.signCategoriesLabel.setObjectName("signCategoriesLabel")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 210, 241, 341))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.signCategories = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.signCategories.setContentsMargins(0, 0, 0, 0)
        self.signCategories.setObjectName("signCategories")
        self.regulatoryVBOX = QtWidgets.QVBoxLayout()
        self.regulatoryVBOX.setObjectName("regulatoryVBOX")
        self.regulatoryContainer = QtWidgets.QHBoxLayout()
        self.regulatoryContainer.setObjectName("regulatoryContainer")
        self.regulatorySign = QtWidgets.QHBoxLayout()
        self.regulatorySign.setObjectName("regulatorySign")
        self.regulatoryLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.regulatoryLabel.setFont(font)
        self.regulatoryLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.regulatoryLabel.setObjectName("regulatoryLabel")
        self.regulatorySign.addWidget(self.regulatoryLabel)
        self.regulatoryContainer.addLayout(self.regulatorySign)
        self.regulatoryPercentage = QtWidgets.QHBoxLayout()
        self.regulatoryPercentage.setObjectName("regulatoryPercentage")
        self.regulatoryPercentValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.regulatoryPercentValue.setFrameShape(QtWidgets.QFrame.Box)
        self.regulatoryPercentValue.setText("")
        self.regulatoryPercentValue.setObjectName("regulatoryPercentValue")
        self.regulatoryPercentage.addWidget(self.regulatoryPercentValue)
        self.regulatoryContainer.addLayout(self.regulatoryPercentage)
        self.regulatoryVBOX.addLayout(self.regulatoryContainer)
        self.signCategories.addLayout(self.regulatoryVBOX)
        self.guidingVBOX = QtWidgets.QVBoxLayout()
        self.guidingVBOX.setObjectName("guidingVBOX")
        self.guidingContainer = QtWidgets.QHBoxLayout()
        self.guidingContainer.setObjectName("guidingContainer")
        self.guidingSign = QtWidgets.QHBoxLayout()
        self.guidingSign.setObjectName("guidingSign")
        self.guidingLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.guidingLabel.setFont(font)
        self.guidingLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.guidingLabel.setObjectName("guidingLabel")
        self.guidingSign.addWidget(self.guidingLabel)
        self.guidingContainer.addLayout(self.guidingSign)
        self.guidingPercentage = QtWidgets.QHBoxLayout()
        self.guidingPercentage.setObjectName("guidingPercentage")
        self.guidingPercentValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.guidingPercentValue.setFrameShape(QtWidgets.QFrame.Box)
        self.guidingPercentValue.setText("")
        self.guidingPercentValue.setObjectName("guidingPercentValue")
        self.guidingPercentage.addWidget(self.guidingPercentValue)
        self.guidingContainer.addLayout(self.guidingPercentage)
        self.guidingVBOX.addLayout(self.guidingContainer)
        self.signCategories.addLayout(self.guidingVBOX)
        self.warningVBOX = QtWidgets.QVBoxLayout()
        self.warningVBOX.setObjectName("warningVBOX")
        self.warningContainer = QtWidgets.QHBoxLayout()
        self.warningContainer.setObjectName("warningContainer")
        self.warningSign = QtWidgets.QHBoxLayout()
        self.warningSign.setObjectName("warningSign")
        self.warningLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.warningLabel.setFont(font)
        self.warningLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.warningLabel.setObjectName("warningLabel")
        self.warningSign.addWidget(self.warningLabel)
        self.warningContainer.addLayout(self.warningSign)
        self.warningPercentage = QtWidgets.QHBoxLayout()
        self.warningPercentage.setObjectName("warningPercentage")
        self.warningPercentValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.warningPercentValue.setFrameShape(QtWidgets.QFrame.Box)
        self.warningPercentValue.setText("")
        self.warningPercentValue.setObjectName("warningPercentValue")
        self.warningPercentage.addWidget(self.warningPercentValue)
        self.warningContainer.addLayout(self.warningPercentage)
        self.warningVBOX.addLayout(self.warningContainer)
        self.signCategories.addLayout(self.warningVBOX)
        self.constructionVBOX = QtWidgets.QVBoxLayout()
        self.constructionVBOX.setObjectName("constructionVBOX")
        self.constructionContainer = QtWidgets.QHBoxLayout()
        self.constructionContainer.setObjectName("constructionContainer")
        self.constructionSign = QtWidgets.QHBoxLayout()
        self.constructionSign.setObjectName("constructionSign")
        self.constructionLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(11)
        self.constructionLabel.setFont(font)
        self.constructionLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.constructionLabel.setObjectName("constructionLabel")
        self.constructionSign.addWidget(self.constructionLabel)
        self.constructionContainer.addLayout(self.constructionSign)
        self.constructionPercentage = QtWidgets.QHBoxLayout()
        self.constructionPercentage.setObjectName("constructionPercentage")
        self.constructionPercentValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.constructionPercentValue.setFrameShape(QtWidgets.QFrame.Box)
        self.constructionPercentValue.setText("")
        self.constructionPercentValue.setObjectName("constructionPercentValue")
        self.constructionPercentage.addWidget(self.constructionPercentValue)
        self.constructionContainer.addLayout(self.constructionPercentage)
        self.constructionVBOX.addLayout(self.constructionContainer)
        self.signCategories.addLayout(self.constructionVBOX)
        self.otherVBOX = QtWidgets.QVBoxLayout()
        self.otherVBOX.setObjectName("otherVBOX")
        self.otherContainer = QtWidgets.QHBoxLayout()
        self.otherContainer.setObjectName("otherContainer")
        self.otherSign = QtWidgets.QHBoxLayout()
        self.otherSign.setObjectName("otherSign")
        self.otherLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.otherLabel.setFont(font)
        self.otherLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.otherLabel.setObjectName("otherLabel")
        self.otherSign.addWidget(self.otherLabel)
        self.otherContainer.addLayout(self.otherSign)
        self.otherPercentage = QtWidgets.QHBoxLayout()
        self.otherPercentage.setObjectName("otherPercentage")
        self.otherPercentValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.otherPercentValue.setFrameShape(QtWidgets.QFrame.Box)
        self.otherPercentValue.setText("")
        self.otherPercentValue.setObjectName("otherPercentValue")
        self.otherPercentage.addWidget(self.otherPercentValue)
        self.otherContainer.addLayout(self.otherPercentage)
        self.otherVBOX.addLayout(self.otherContainer)
        self.signCategories.addLayout(self.otherVBOX)
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(300, 210, 271, 241))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.confusionMatrix = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.confusionMatrix.setContentsMargins(0, 0, 0, 0)
        self.confusionMatrix.setObjectName("confusionMatrix")
        self.confusionContainer = QtWidgets.QVBoxLayout()
        self.confusionContainer.setObjectName("confusionContainer")
        self.positiveVBOX = QtWidgets.QVBoxLayout()
        self.positiveVBOX.setObjectName("positiveVBOX")
        self.positiveContainer = QtWidgets.QHBoxLayout()
        self.positiveContainer.setObjectName("positiveContainer")
        self.truePositive = QtWidgets.QHBoxLayout()
        self.truePositive.setObjectName("truePositive")
        self.tpLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tpLabel.setFont(font)
        self.tpLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.tpLabel.setObjectName("tpLabel")
        self.truePositive.addWidget(self.tpLabel)
        self.positiveContainer.addLayout(self.truePositive)
        self.falsePositive = QtWidgets.QHBoxLayout()
        self.falsePositive.setObjectName("falsePositive")
        self.fpLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.fpLabel.setFont(font)
        self.fpLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.fpLabel.setObjectName("fpLabel")
        self.falsePositive.addWidget(self.fpLabel)
        self.positiveContainer.addLayout(self.falsePositive)
        self.positiveVBOX.addLayout(self.positiveContainer)
        self.confusionContainer.addLayout(self.positiveVBOX)
        self.negativeVBOX = QtWidgets.QVBoxLayout()
        self.negativeVBOX.setObjectName("negativeVBOX")
        self.negativeContainer = QtWidgets.QHBoxLayout()
        self.negativeContainer.setObjectName("negativeContainer")
        self.falseNegative = QtWidgets.QHBoxLayout()
        self.falseNegative.setObjectName("falseNegative")
        self.fnLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.fnLabel.setFont(font)
        self.fnLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.fnLabel.setObjectName("fnLabel")
        self.falseNegative.addWidget(self.fnLabel)
        self.negativeContainer.addLayout(self.falseNegative)
        self.trueNegative = QtWidgets.QHBoxLayout()
        self.trueNegative.setObjectName("trueNegative")
        self.tnLabel = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        self.tnLabel.setFont(font)
        self.tnLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.tnLabel.setObjectName("tnLabel")
        self.trueNegative.addWidget(self.tnLabel)
        self.negativeContainer.addLayout(self.trueNegative)
        self.negativeVBOX.addLayout(self.negativeContainer)
        self.confusionContainer.addLayout(self.negativeVBOX)
        self.confusionMatrix.addLayout(self.confusionContainer)
        AutograderS2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AutograderS2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        AutograderS2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AutograderS2)
        self.statusbar.setObjectName("statusbar")
        AutograderS2.setStatusBar(self.statusbar)

        self.retranslateUi(AutograderS2)
        QtCore.QMetaObject.connectSlotsByName(AutograderS2)

    def retranslateUi(self, AutograderS2):
        _translate = QtCore.QCoreApplication.translate
        AutograderS2.setWindowTitle(_translate("AutograderS2", "AutograderS2"))
        self.exportButton.setText(_translate("AutograderS2", "Export"))
        self.titleLabel.setText(_translate("AutograderS2", "3D Point Cloud Autograder"))
        self.scoreLabel.setText(_translate("AutograderS2", "Aggregate Score:"))
        self.score.setText(_translate("AutograderS2", "100%"))
        self.confusionMatrixLabel.setText(_translate("AutograderS2", "Confusion Matrix:"))
        self.signCategoriesLabel.setText(_translate("AutograderS2", "Sign Categories:"))
        self.regulatoryLabel.setText(_translate("AutograderS2", "Regulatory:"))
        self.guidingLabel.setText(_translate("AutograderS2", "Guiding:"))
        self.warningLabel.setText(_translate("AutograderS2", "Warning:"))
        self.constructionLabel.setText(_translate("AutograderS2", "Construction:"))
        self.otherLabel.setText(_translate("AutograderS2", "Other:"))
        self.tpLabel.setText(_translate("AutograderS2", "True Positive"))
        self.fpLabel.setText(_translate("AutograderS2", "False Positive"))
        self.fnLabel.setText(_translate("AutograderS2", "False Negative"))
        self.tnLabel.setText(_translate("AutograderS2", "True Negative"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutograderS2 = QtWidgets.QMainWindow()
    ui = Ui_AutograderS2()
    ui.setupUi(AutograderS2)
    AutograderS2.show()
    sys.exit(app.exec_())