'''
Author: Fahad Ali
Student ID: 3099218
Description: This program will create cohorts of the best size depending on 
the class space available, and suggest (if required) more class space
'''

class students:
    
    def __init__(self):
        self._BCOMStudents = int(input("Enter number of BCOM Students: "))
        self._PCOMStudents = int(input("Enter number of PCOM Students: "))

        self._PMStudents = int(input("Enter number of PM Students: "))
        self._BAStudents = int(input("Enter number of BA Students: "))
        self._GLStudents = int(input("Enter number of GL Students: "))
        self._FSStudents = int(input("Enter number of FS Students: "))
        self._DXDStudents = int(input("Enter number of DXD Students: "))
        self._BKStudents = int(input("Enter number of BK Students: "))
        self._SCMStudents = int(input("Enter number of SCM Students: "))

        self._totalStudents = self._BCOMStudents + self._PCOMStudents # temp

    def cohort_name(self):
        cohortList = []
        
        cohortList.append(self.divide_to_cohorts(self._BCOMStudents))
        cohortList.append(self.divide_to_cohorts(self._PCOMStudents))
        cohortList.append(self.divide_to_cohorts(self._PMStudents))
        cohortList.append(self.divide_to_cohorts(self._BAStudents))
        cohortList.append(self.divide_to_cohorts(self._GLStudents))
        cohortList.append(self.divide_to_cohorts(self._FSStudents))
        cohortList.append(self.divide_to_cohorts(self._DXDStudents))
        cohortList.append(self.divide_to_cohorts(self._BKStudents))
        cohortList.append(self.divide_to_cohorts(self._SCMStudents))

        for i in cohortList:
            print(i)

    def divide_to_cohorts(self, cohortProgram):
        cohortDict = {self._BCOMStudents:"BC", self._PCOMStudents: "PC", \
                      self._PMStudents:"PM", self._BAStudents:"BA", \
                        self._GLStudents:"GL", self._FSStudents:"FS", \
                            self._DXDStudents:"DXD", self._BKStudents:"BK", \
                                self._SCMStudents:"SCM"}
        cohortProgramList = []
        cohortGroup = 0

        for student in range(cohortProgram):
            studentRemaining = cohortProgram
            term = 1 # temp, will depend on what term it currently is

            if (student > 0) and (student % 30 == 0): 
                # If for whatever reason we need to make cohort > or < than 30,
                # we can.
                cohortGroup += 1
                studentRemaining -= student
                cohortProgramList.append(f"{cohortDict.get(cohortProgram)}{term}{cohortGroup}") 

            if studentRemaining <= 25:
                # TODO: average out the cohorts if moer than 1 cohort is made 
                # and the last cohort is under 25 people
                pass
        return cohortProgramList
    
if __name__ == "__main__":
    x = students()
    x.cohort_name()