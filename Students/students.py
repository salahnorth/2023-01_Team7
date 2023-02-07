'''
Author: Fahad Ali
Student ID: 3099218
Description: This program will create cohorts of the best size depending on 
the class space available, and suggest (if required) more class space
'''

class Classroom:

    def __init__(self, name, cap):
        self._name = name.strip()
        self._cap = cap
        self._current_students = cap
        self._in_use = False

class students:
    '''
    Description: this class will input students for each program and create
    appropriate cohorts. It will be implemented into the GUI app.
    '''
    def __init__(self):
        # initialize attributes
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

        # Setup list of classrooms. Done by reading from a csv
        # file, where each class and it's capacity are added to
        # the list as a Classroom object.
        self._classrooms = []
        with open("data/classrooms.csv", "r") as rooms_file:
            rooms_data = [line.strip() for line in rooms_file if "sep=" not in line]
        for room in rooms_data:
            room_name, room_cap = room.split(",")[0], int(room.split(",")[1])
            self._classrooms.append(Classroom(room_name, room_cap))

        # Sort rooms from largest to smallest
        self._classrooms = sorted(self._classrooms, key=lambda x:x._cap, reverse=True)

    def cohorts_final(self):
        '''
        Description: this function will call divide_to_cohorts() and append
        the results to a list
        Returns: a list of lists of all the cohorts
        '''
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

        for classroom in self._classrooms:

            # If any of the classroom space is used, skip over for now
            if classroom._in_use:
                continue
            
            # If all students are added to all classrooms, break the loop.
            if students == 0:
                break

            # Check if amount of students passed to function fits in room.
            # If there are more students than space in a room, fill the room.
            if students >= classroom._cap:
                
                # Fill space in classrooms by simply removing the cap from the space
                # remaining. This is done because there are more students than capcity,
                # so we fill it entirely.
                students -= classroom._current_students
                cohortGroup += 1
                cohort_name = f"{cohortDict.get(ID)}{self._term}{cohortGroup}: {classroom._name}, {classroom._current_students}/{classroom._cap}"
                cohortProgramList.append(cohort_name)

                # Set the boolean to reflect the classroom in use
                classroom._in_use = True

            elif students < classroom._cap:

                # Just remove remaining students from space remaining.
                classroom._current_students = students
                students -= students
                cohortGroup += 1
                cohort_name = f"{cohortDict.get(ID)}{self._term}{cohortGroup}: {classroom._name}, {classroom._current_students}/{classroom._cap}"
                cohortProgramList.append(cohort_name)

                # Set the classroom boolean as in use
                classroom._in_use = True
        
        # If the ID is one 1, reset dictionary as we are moving on to electives
        if ID == 1:
            for classroom in self._classrooms:
                classroom._in_use = False
                classroom._current_students = classroom._cap

        return (cohortProgramList)
    
    """

    def divide_to_cohorts(self, students, ID):
        '''
        Description: this function will assign the appropriate prefix and 
        divide by cohort size and return a list
        Returns: a list of cohort strings
        '''
        # initialize values
        cohortDict = {0:"BC", 1: "PC", 2:"PM", 3:"BA", 4:"GL", 5:"FS", 6:"DXD",\
                      7:"BK", 8:"SCM"}
        cohortProgramList = []
        cohortGroups = 0
        studentRemaining = 0
        cohortSize = 30 # change to whatever size cohort is needed

        # loop through students in a program
        for student in range(students):
            studentRemaining = students
            # put into cohort groups
            if student % cohortSize == 0: 
                cohortGroups += 1
                studentRemaining -= student
                # proper name convention 
                if cohortGroups < 10:
                    cohortProgramList.append(f"{cohortDict.get(ID)}0{self._term}0{cohortGroups}") 
                elif cohortGroups < 20:
                    cohortProgramList.append(f"{cohortDict.get(ID)}1{self._term}1{cohortGroups}") 
                    
            if studentRemaining <= 25:
                # TODO: average out the cohorts if moer than 1 cohort is made 
                # and the last cohort is under 25 people
                pass

        return (cohortProgramList)
        """