
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import  loadUiType
#import mysql.connector as mc
import MySQLdb as mdb


ui, _ = loadUiType('EmployeeInformationSystem.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        #To show first loginpage
        self.tabWidget.setCurrentIndex(0)

        
        self.b01.clicked.connect(self.login)
        self.b12.clicked.connect(self.insertData)

       

        ##Login  Form#
    def login(self):
        un=self.tb01.text()
        pw=self.tb02.text()
        if (un=='admin' and pw=='admin'):
            self.menubar.setVisible(True)#if both  r correct im enabiling the menubar
            #setting
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.information(self,"Employee Information System","Invalid Admin login details, Try Again!")

    
    def insertData(self):
        con = mdb.connect("localhost", "root", "", "employee information system")

        with con:
            cur = con.cursor()

            cur.execute("INSERT INTO employee(Employee_id, Name, Gender, Date_of_birth,	Age, Address, Email, Phn_No, Salary, Role)"
                        "VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(''.join(self.tb11.text()),
                                                                                       ''.join(self.tb12.text()),
                                                                                       ''.join(self.cb11.currentText()),
                                                                                       ''.join(self.tb13.text()),
                                                                                       ''.join(self.tb14.text()),
                                                                                       ''.join(self.tb15.text()),
                                                                                       ''.join(self.tb16.text()),
                                                                                       ''.join(self.tb17.text()),
                                                                                       ''.join(self.tb18.text()),
                                                                                       ''.join(self.cb12.currentText())))
            QMessageBox.about(self,"Employee Information System","Information added Successfully!")
            self.close()
           
def main():
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    app.exec_()

if __name__ == "__main__":
    main()
