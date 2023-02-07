'''
Author: Fahad Ali
Student ID: 3099218
Description: Create main GUI app
References: 
https://www.geeksforgeeks.org/pyqt5-input-dialog-python/
https://www.pythonguis.com/tutorials/pyqt-dialogs/
'''
import sys
import Students

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtRemoveInputHook


class MainWindow(QWidget):
    '''
    Description: This is the main window of the app, it will have buttons
    that have different dialogs for each UI element
    '''
    # main window class
    def __init__(self):
        # initialize main window
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Schedule")
        self.setupUI()
        
    def cohort_button(self):
        # create cohort dialog
        cohortDialog = CohortDialog()
        cohortDialog.exec()
    
    def schedule_button(self):
        scheduleDialog = ScheduleDialog()
        scheduleDialog.exec()
        
    def setupUI(self):
        # create layout
        mainlLayout = QHBoxLayout(self)
        
        # create cohort button and execute dialog
        cohortButton = QPushButton("Click to Setup Cohorts", self)
        cohortButton.resize(200, 100)
        cohortButton.clicked.connect(self.cohort_button)
        
        #TODO: make scheudule functionality and dialog
        scheduleButton = QPushButton("Click to see Schedules", self)
        scheduleButton.resize(200, 100)
        scheduleButton.clicked.connect(self.schedule_button)
        
        # add buttonts to layout
        mainlLayout.addWidget(cohortButton, 1)
        mainlLayout.addWidget(scheduleButton, 1)
        # set layout
        self.setLayout(mainlLayout)

class CohortDialog(QDialog):
    '''
    Description: This is the cohort dialog class, it will ask for input of the term
    and students in each program and output the cohorts
    '''
    def __init__(self):
        # initialize the window
        super().__init__()
        self.resize(500, 400)
        self.formGroupBox = QGroupBox("Cohort")

        # creating a line edit texts for each program and set integer parameters
        onlyInt = QIntValidator()
        onlyInt.setRange(0, 999)

        # create spin box for term number
        self.term = QSpinBox()
        self.term.setMaximum(3)
        self.term.setMinimum(1)

        # create text edit box that will only take integer numbers
        self.PCOM = QLineEdit()
        self.PCOM.setValidator(onlyInt)
        self.BCOM = QLineEdit()
        self.BCOM.setValidator(onlyInt)
        self.PM = QLineEdit()
        self.PM.setValidator(onlyInt)
        self.BA = QLineEdit()
        self.BA.setValidator(onlyInt)
        self.GLM = QLineEdit()
        self.GLM.setValidator(onlyInt)
        self.FS = QLineEdit()
        self.FS.setValidator(onlyInt)
        self.DXD = QLineEdit()
        self.DXD.setValidator(onlyInt)
        self.BK = QLineEdit()
        self.BK.setValidator(onlyInt)
        self.SCM = QLineEdit()
        self.SCM.setValidator(onlyInt)

        # call method that inputs numbers from the entry box
        self.setup_input()

        # creating a dialog button for ok and cancel
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        # add functionality when "ok" clicked
        self.buttonBox.rejected.connect(self.reject)
        # add functionality when "ok" clicked
        self.buttonBox.accepted.connect(self.create_cohorts)

        # create a veritcal layout
        cohortLayout = QVBoxLayout()
        cohortLayout.addWidget(self.formGroupBox)
        # add button to the layout
        cohortLayout.addWidget(self.buttonBox)
        # set lay out
        self.setLayout(cohortLayout)

    def create_cohorts(self):
        # call students class
        studentCohort = Students.students()

        # assign input to class attributes
        studentCohort._term = int(self.term.text())
        studentCohort._BCOMStudents = int(self.BCOM.text())
        studentCohort._PCOMStudents = int(self.PCOM.text())
        studentCohort._PMStudents = int(self.PM.text())
        studentCohort._BAStudents = int(self.BA.text())
        studentCohort._GLMStudents = int(self.GLM.text())
        studentCohort._FSStudents = int(self.FS.text())
        studentCohort._DXDStudents = int(self.DXD.text())
        studentCohort._BKStudents = int(self.BK.text())
        studentCohort._SCMStudents = int(self.SCM.text())

        print(studentCohort.cohorts_final())

    def setup_input(self):
        # create a form layout
        studentInput = QFormLayout()

        studentInput.addRow(QLabel("Input term number: "), self.term) 
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

class ScheduleDialog(QDialog):
    # TODO: add schedules
	def __init__(self):
		# initialize the window
		super().__init__()
		self.resize(500, 400)
		self.formGroupBox = QGroupBox("Schedules")

def main():
    pyqtRemoveInputHook()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()