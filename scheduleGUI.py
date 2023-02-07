'''
Author: Fahad Ali
Student ID: 3099218
Description: Create main GUI app
References: 
https://www.geeksforgeeks.org/pyqt5-input-dialog-python/
https://www.pythonguis.com/tutorials/pyqt-dialogs/
'''
from PyQt5.QtWidgets import *
from students import students
import sys

class MainWindow(QMainWindow):
    # main window class
    def __init__(self):
        # initialize main window
        super().__init__()
        self.resize(400, 250)
        self.setWindowTitle("Schedule")
        self.setupUI()

    def cohort_button(self):
        # create cohort dialog
        cohortDialog = CohortDialog()
        cohortDialog.exec()
    
    def schedule_button(self):
            #TODO: make scheudule functionality and dialog
            pass
        
    def setupUI(self):
        # create cohort button and execute dialog
        cohortButton = QPushButton("Setup Cohorts?", self)
        cohortButton.resize(150, 100)
        cohortButton.clicked.connect(self.cohort_button)
        
        #TODO: make scheudule functionality and dialog
        # scheduleButton = QPushButton("Schedules", self)
        # scheduleButton.resize(150, 200)
        # scheduleButton.clicked.connect(self.schedule_button)
        
class CohortDialog(QDialog):
    # create cohort dialog
	def __init__(self):
		# initialize the window
		super().__init__()
		self.resize(500, 400)
		self.formGroupBox = QGroupBox("Cohort")
  
		# creating a line edit texts for each program
		self.PCOM = QLineEdit()
		self.BCOM = QLineEdit()
		self.PM = QLineEdit()
		self.BA = QLineEdit()
		self.GLM = QLineEdit()
		self.FS = QLineEdit()
		self.DXD = QLineEdit()
		self.BK = QLineEdit()
		self.SCM = QLineEdit()

		# call method that inputs numbers
		self.setup_input()

		# creating a dialog button for ok and cancel
		self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
		self.buttonBox.rejected.connect(self.reject)
		# add action when "ok" clicked
		self.buttonBox.accepted.connect(self.creat_cohorts)

		# create a veritcal layout
		mainLayout = QVBoxLayout()
		mainLayout.addWidget(self.formGroupBox)
		# add button  to the layout
		mainLayout.addWidget(self.buttonBox)
		# set lay out
		self.setLayout(mainLayout)
  
	def creat_cohorts(self):
		# TODO: deal with inputs
		studentCohort = students()
		studentCohort._BCOMStudents = self.BCOM.text()
		studentCohort._PCOMStudents = self.PCOM.text()
		studentCohort._PMStudents = self.PM.text()
		studentCohort._BAStudents = self.BA.text()
		studentCohort._GLMStudents = self.GLM.text()
		studentCohort._FSStudents = self.FS.text()
		studentCohort._DXDStudents = self.DXD.text()
		studentCohort._BKStudents = self.BK.text()
		studentCohort._SCMStudents = self.SCM.text()
		print(studentCohort.cohorts_final())
    
	def setup_input(self):
		# create a form layout
		studentInput = QFormLayout()
  
		studentInput.addRow(QLabel("Business Communication (BCOM)"), self.BCOM)
		studentInput.addRow(QLabel("Professional Communication (PCOM)"), self.PCOM)
		studentInput.addRow(QLabel("Project Management (PM)"), self.PM) 
		studentInput.addRow(QLabel("Business Analysis (BA)"), self.BA) 
		studentInput.addRow(QLabel("Global Logistics Management (GLM)"), self.GLM) 
		studentInput.addRow(QLabel("Full Stack Web Development (FS)"), self.FS) 
		studentInput.addRow(QLabel("Digital Experience Design Foundation (DXD)"), self.DXD) 
		studentInput.addRow(QLabel("BookKeeping Certificate (BK)"), self.BK) 
		studentInput.addRow(QLabel("Supply Chain Management (SCM)"), self.SCM) 

		# set the layout
		self.formGroupBox.setLayout(studentInput)


def main():
    from PyQt5.QtCore import pyqtRemoveInputHook
    pyqtRemoveInputHook()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
 
if __name__ == '__main__':
    main()