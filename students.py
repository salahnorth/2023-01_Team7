'''
Author: Fahad Ali
Student ID: 3099218
Description: This program will create cohorts of the best size depending on 
the class space available, and suggest (if required) more class space
'''

class students:
    
    def __init__(self):

        self._BCOMStudents = None
        self._PCOMStudents = None

        self._PMStudents = None
        self._BAStudents = None
        self._GLMStudents = None
        self._FSStudents = None
        self._DXDStudents = None
        self._BKStudents = None
        self._SCMStudents = None
        
        self._term = None

    def cohorts_final(self):
        cohortList = []
        cohortList.append(self.divide_to_cohorts(self._BCOMStudents, 0))
        cohortList.append(self.divide_to_cohorts(self._PCOMStudents, 1))

        cohortList.append(self.divide_to_cohorts(self._PMStudents, 2))
        cohortList.append(self.divide_to_cohorts(self._BAStudents, 3))
        cohortList.append(self.divide_to_cohorts(self._GLMStudents, 4))
        cohortList.append(self.divide_to_cohorts(self._FSStudents, 5))
        cohortList.append(self.divide_to_cohorts(self._DXDStudents, 6))
        cohortList.append(self.divide_to_cohorts(self._BKStudents, 7))
        cohortList.append(self.divide_to_cohorts(self._SCMStudents, 8))

        return(cohortList)

    def divide_to_cohorts(self, students, ID):
        cohortDict = {0:"BC", 1: "PC", 2:"PM", 3:"BA", 4:"GL", 5:"FS", 6:"DXD",\
                      7:"BK", 8:"SCM"}
        cohortProgramList = []
        cohortGroup = 0
        studentRemaining = 0

        for student in range(students):
            studentRemaining = students

            if student % 30 == 0: 
                # If for whatever reason we need to make cohort > or < than 30,
                # we can.
                cohortGroup += 1
                studentRemaining -= student
                cohortProgramList.append(f"{cohortDict.get(ID)}{self._term}{cohortGroup}") 

            if studentRemaining <= 25:
                # TODO: average out the cohorts if moer than 1 cohort is made 
                # and the last cohort is under 25 people
                pass

        return (cohortProgramList)
    
if __name__ == "__main__":
    x = students()
    for i in x.cohorts_final():
        print(i)