"""
Author: Sankalp Shrivastav
ID: 3106374
Date: 02/02/2023
Purpose: A basic idea for the Cohort data structure
"""

class Cohort:

    def __init__(self) -> None:
        #Cohort init 
        #testing Ignore
        
        self._cohortNumber = 1
        self._isLab = False
        self._cohortSize = 0
        self._courseFinished = []
        self._courseNotFinished = []
        self.timeTable = None
    
    def __str__(self) -> str:
        
        return  f"\nCohort: {self._cohortNumber}\n"\
                f"Size: {self._cohortSize}\n"\
                f"Courses Done: {self._courseFinished}\n"\
                f"Courses NotDone: {self._courseNotFinished}\n"
    
    def changeType(self, type = False) -> None:

        #change the type of class

        self._isLab = type

    def display(self) -> None:

        print(self)


if __name__ == '__main__':

    print("Testing Cohort")

    cohort1 = Cohort()

    print(cohort1)