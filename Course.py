from Cohort import *

class Course:
    def __init__(self, name, size, course_type):
        self.name = name
        self.size = size
        self.course_type = course_type
        self.cohorts = []  # A list to store cohorts
    
    def __str__(self):
        return f'{self.name} ({self.size})'
    
    # Split the course into cohorts of equal size
    def split_cohorts(self):
        num_cohorts = self.size // 30  # Each cohort has a maximum size of 30
        cohort_size = self.size // num_cohorts
        for i in range(num_cohorts):
            cohort = Cohort(f'{self.name}_{i+1}', cohort_size, self.course_type)
            self.cohorts.append(cohort)
