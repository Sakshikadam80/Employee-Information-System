
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from PyQt5.uic import  loadUiType
import mysql.connector as con
#import MySQLdb as mdb


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

    #mydb = mysql.connector.connect( host="localhost",user= "root",password= "",database= "employee information system")


    def insertData(self):
        try:
            mydb = con.connect( host="localhost",user= "root",password= "",database= "employee information system")
            mycursor = mydb.cursor()

            Employee_id = self.tb11.text()
            Name = self.tb12.text()
            Gender= self.cb11.currentText()
            Date_of_birth = self.tb13.text()
            Age= self.tb14.text()
            Address = self.tb15.text()
            Email= self.tb16.text()
            Phn_No= self.tb17.text()
            Salary = self.tb18.text()
            Role = self.cb12.currentText()

            

            
            qry ="INSERT INTO employee(Employee_id, Name, Gender, Date_of_birth, Age, Address, Email, Phn_No, Salary, Role)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            value= (Employee_id, Name, Gender, Date_of_birth, Age, Address, Email, Phn_No, Salary, Role)
            mycursor.execute(qry,value)
            mydb.commit()
            QMessageBox.about(self,"Employee Information System","Information added Successfully!")

        except con.Error as e:
            print("Error",e)
            




        
                   
def main():
    app = QApplication(sys.argv)
    Window = MainApp()
    Window.show()
    app.exec_()

if __name__ == "__main__":
    main()
