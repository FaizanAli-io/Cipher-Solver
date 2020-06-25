# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cipher.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from hashing import encode

class Ui_Dialog(object):
        def setupUi(self, Dialog):
                Dialog.setObjectName("Dialog")
                Dialog.resize(320, 280)
                self.groupBox = QtWidgets.QGroupBox(Dialog)
                self.groupBox.setGeometry(QtCore.QRect(10, 10, 300, 260))
                self.groupBox.setObjectName("groupBox")
                self.encodeButton = QtWidgets.QPushButton(self.groupBox)
                self.encodeButton.setGeometry(QtCore.QRect(190, 160, 100, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.encodeButton.setFont(font)
                self.encodeButton.setStyleSheet("")
                self.encodeButton.setObjectName("encodeButton")
                self.decodeButton = QtWidgets.QPushButton(self.groupBox)
                self.decodeButton.setGeometry(QtCore.QRect(190, 210, 100, 40))
                font = QtGui.QFont()
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.decodeButton.setFont(font)
                self.decodeButton.setStyleSheet("")
                self.decodeButton.setObjectName("decodeButton")
                self.textInput = QtWidgets.QLineEdit(self.groupBox)
                self.textInput.setGeometry(QtCore.QRect(110, 60, 150, 20))
                self.textInput.setStyleSheet("border-radius:8px;\n"
                "border-color:rgb(12, 12, 12);\n"
                "border-width:1px;\n"
                "border-style:solid")
                self.textInput.setObjectName("textInput")
                self.textOut = QtWidgets.QTextBrowser(self.groupBox)
                self.textOut.setGeometry(QtCore.QRect(20, 160, 160, 90))
                self.textOut.setObjectName("textOut")
                self.keyInput = QtWidgets.QLineEdit(self.groupBox)
                self.keyInput.setGeometry(QtCore.QRect(110, 90, 150, 20))
                self.keyInput.setStyleSheet("border-radius:8px;\n"
                "border-color:rgb(12, 12, 12);\n"
                "border-width:1px;\n"
                "border-style:solid")
                self.keyInput.setClearButtonEnabled(False)
                self.keyInput.setObjectName("keyInput")
                self.cipherTypes = QtWidgets.QComboBox(self.groupBox)
                self.cipherTypes.setGeometry(QtCore.QRect(110, 30, 150, 20))
                self.cipherTypes.setObjectName("cipherTypes")
                self.cipherTypes.addItem("")
                self.cipherTypes.addItem("")
                self.cipherTypes.addItem("")
                self.cipherTypes.addItem("")
                #self.cipherTypes.addItem("")
                self.type = QtWidgets.QLabel(self.groupBox)
                self.type.setGeometry(QtCore.QRect(20, 30, 80, 20))
                font = QtGui.QFont()
                font.setFamily("Perpetua")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.type.setFont(font)
                self.type.setObjectName("type")
                self.hashkeyInput = QtWidgets.QLineEdit(self.groupBox)
                self.hashkeyInput.setGeometry(QtCore.QRect(110, 120, 150, 20))
                self.hashkeyInput.setStyleSheet("border-radius:8px;\n"
                "border-color:rgb(12, 12, 12);\n"
                "border-width:1px;\n"
                "border-style:solid")
                self.hashkeyInput.setObjectName("hashkeyInput")
                self.textLabel = QtWidgets.QLabel(self.groupBox)
                self.textLabel.setGeometry(QtCore.QRect(20, 60, 80, 20))
                font = QtGui.QFont()
                font.setFamily("Perpetua")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.textLabel.setFont(font)
                self.textLabel.setObjectName("textLabel")
                self.keyLabel = QtWidgets.QLabel(self.groupBox)
                self.keyLabel.setGeometry(QtCore.QRect(20, 90, 80, 20))
                font = QtGui.QFont()
                font.setFamily("Perpetua")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.keyLabel.setFont(font)
                self.keyLabel.setObjectName("keyLabel")
                self.hashkeyLabel = QtWidgets.QLabel(self.groupBox)
                self.hashkeyLabel.setGeometry(QtCore.QRect(20, 120, 80, 20))
                font = QtGui.QFont()
                font.setFamily("Perpetua")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.hashkeyLabel.setFont(font)
                self.hashkeyLabel.setObjectName("hashkeyLabel")

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

                #
                self.encodeButton.clicked.connect(self.encodeMethod)
                self.decodeButton.clicked.connect(self.decodeMethod)
                #

        def retranslateUi(self, Dialog):
                _translate = QtCore.QCoreApplication.translate
                Dialog.setWindowTitle(_translate("Dialog", "Cipher Solver by Faizan"))
                self.groupBox.setTitle(_translate("Dialog", "Text Encoder"))
                self.encodeButton.setText(_translate("Dialog", "Encode Text"))
                self.decodeButton.setText(_translate("Dialog", "Decode Text"))
                self.cipherTypes.setItemText(0, _translate("Dialog", "Caeser\'s Cipher"))
                self.cipherTypes.setItemText(1, _translate("Dialog", "Vigenere\'s Cipher"))
                self.cipherTypes.setItemText(2, _translate("Dialog", "Matrix Cipher"))
                self.cipherTypes.setItemText(3, _translate("Dialog", "Porta Cipher"))
                #self.cipherTypes.setItemText(4, _translate("Dialog", "ADVGF (German) Cipher"))
                self.type.setText(_translate("Dialog", "Cipher Type"))
                self.textLabel.setText(_translate("Dialog", "Text"))
                self.keyLabel.setText(_translate("Dialog", "Key"))
                self.hashkeyLabel.setText(_translate("Dialog", "Hash"))
        
        def encodeMethod(self):
                index = self.cipherTypes.currentIndex()
                text = encode(self.textInput.text())
                if index==0:
                        key = int(self.keyInput.text())
                        ciphertext = text.caesar(key)
                elif index==1:
                        key = self.keyInput.text()
                        ciphertext = text.vigenere(key)
                elif index==2:
                        key = int(self.keyInput.text())
                        ciphertext = text.matrix(key)
                elif index==3:
                        key = self.keyInput.text()
                        ciphertext = text.porta(key)
                elif index==4:
                        key = self.keyInput.text()
                        ciphertext = f"{text.ADFGVX(key)[0]}\n{text.ADFGVX(key)[1]}"
                else:
                        ciphertext = ''
                self.textOut.setText(ciphertext)
        
        def decodeMethod(self):
                index = self.cipherTypes.currentIndex()
                text = encode(self.textInput.text())
                if index==0:
                        key = int(self.keyInput.text())
                        ciphertext = text.decode_caesar(key)
                elif index==1:
                        key = self.keyInput.text()
                        ciphertext = text.decode_vigenere(key)
                elif index==2:
                        key = int(self.keyInput.text())
                        ciphertext = text.decode_matrix(key)
                elif index==3:
                        key = self.keyInput.text()
                        ciphertext = text.decode_porta(key)
                elif index==4:
                        key = self.keyInput.text()
                        hask = self.hashkeyInput.text()
                        ciphertext = text.decode_ADFGVX(hask, key)
                else:
                        ciphertext = ''
                self.textOut.setText(ciphertext)

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
