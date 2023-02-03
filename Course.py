"""
Author: Sankalp Shrivastav
ID: 3106374
Date: 30/01/2023
Purpose: A basic idea for the course data structure
"""

class Course:

    def __init__(self):

        """
        Members for the Course class, contains name of the course, 
        any prequsites, duration of the course, time finished, and is the course
        completed.
        """
        
        self._name = ""
        self._preReq = []
        self._classTime = 0
        self._timeDone = 0
        self._courseFinished = False

        # these features are examples, will need to be chaecked
    
    def setName(self, Name):

        #set the name of the course

        self._name = Name
    
    def isFinished(self) -> bool:

        """
        Check if the course is finished, 
        return : true is finished, false if not finished

        finished condition: if total required is equal to time done
                            Time Required = Time Done

        """

        if self._classTime == self._timeDone:
            self._courseFinished = True; return True
        
        else: return False
    
    def canTakeCourse(self):
        """
        Will check if the student has met the prerequsite for the course
        """
        pass
    
    def courseInfo(self) -> str:
        """
        Display the string representation of the course
        """

        self.isFinished()

        return  f"Course Name: {self._name}\n"\
                f"Course Prerequsites: {self._preReq}\n"\
                f"Course Time: {self._classTime}\n"\
                f"Course Time Done: {self._courseFinished}"


if __name__ == "__main__":

    print("Testing Course")

    courses = ["abc101", "abc201"]

    course1 = Course()
    course2 = Course()

    course1.setName(courses[0])
    course2.setName(courses[1])

    print(course1.courseInfo())

