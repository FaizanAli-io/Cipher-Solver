from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
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
                self.cipherTypes.addItem("")
                self.type = QtWidgets.QLabel(self.groupBox)
                self.type.setGeometry(QtCore.QRect(20, 30, 80, 20))
                font = QtGui.QFont()
                font.setFamily("Perpetua")
                font.setPointSize(10)
                font.setBold(True)
                font.setWeight(75)
                self.type.setFont(font)
                self.type.setObjectName("type")
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

                self.retranslateUi(Dialog)
                QtCore.QMetaObject.connectSlotsByName(Dialog)

                #
                self.encodeButton.clicked.connect(self.encodeMethod)
                self.decodeButton.clicked.connect(self.decodeMethod)
                self.cipherTypes.activated.connect(self.changeLabels)
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
                self.cipherTypes.setItemText(4, _translate("Dialog", "ADVGF (German) Cipher"))
                self.type.setText(_translate("Dialog", "Cipher Type"))
                self.textLabel.setText(_translate("Dialog", "Text"))
                self.keyLabel.setText(_translate("Dialog", "Key"))
        
        #
        def encodeMethod(self):
                index = self.cipherTypes.currentIndex()
                text = encode(self.textInput.text())
                key = self.keyInput.text()
                if index==0:
                        if not key.isnumeric(): self.popError('Specify an Integer Key please')
                        else: ciphertext = text.caesar(int(key))
                elif index==1:
                        if not key.isalpha(): self.popError('Specify a valid KeyWord please')
                        else: ciphertext = text.vigenere(key)
                elif index==2:
                        if not key.isnumeric(): self.popError('Specify an Integer Key please')
                        else: ciphertext = text.matrix(int(key))
                elif index==3:
                        if not key.isalpha(): self.popError('Specify a valid KeyWord please')
                        else: ciphertext = text.porta(key)
                elif index==4:
                        if key: 
                                if not key.isalnum() or not len(key) == 36: self.popError('Specify a valid (36 digit) HashKey please')
                                else: ciphertext, hashmap = text.ADFGVX(key)
                        else: ciphertext, hashmap = text.ADFGVX()
                        self.keyInput.setText(hashmap)
                else:
                        ciphertext = ''
                try:
                        self.textOut.setText(ciphertext)
                except:
                        pass
        
        def decodeMethod(self):
                index = self.cipherTypes.currentIndex()
                text = encode(self.textInput.text())
                key = self.keyInput.text()
                if index==0:
                        if not key.isnumeric(): self.popError('Specify an Integer Key please')
                        else: ciphertext = text.decode_caesar(int(key))
                elif index==1:
                        if not key.isalpha(): self.popError('Specify a valid KeyWord please')
                        else: ciphertext = text.decode_vigenere(key)
                elif index==2:
                        if not key.isnumeric(): self.popError('Specify an Integer Key please')
                        else: ciphertext = text.decode_matrix(int(key))
                elif index==3:
                        if not key.isalpha(): self.popError('Specify a valid KeyWord please')
                        else: ciphertext = text.decode_porta(key)
                elif index==4:
                        if not key.isalnum() or not len(key) == 36: self.popError('Specify a valid (36 digit) HashKey please')
                        else: ciphertext = text.decode_ADFGVX(key)
                else:
                        ciphertext = ''
                try:
                        self.textOut.setText(ciphertext)
                except:
                        pass

        def changeLabels(self, cur):
                if cur == 0 or cur == 2:
                        self.keyLabel.setText("Key")
                elif cur == 1 or cur == 3:
                        self.keyLabel.setText("KeyWord")
                elif cur == 4:
                        self.keyLabel.setText("HashKey")
        
        def popError(self, errorText):
                mb = QMessageBox()
                mb.setWindowTitle("Invalid Input")
                mb.setText(errorText)
                mb.setIcon(QMessageBox.Warning)

                x = mb.exec_()
        #

if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        Dialog.show()
        sys.exit(app.exec_())
