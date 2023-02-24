"""
Author: Salah Mohamed
ID: 3044504
Date: 14/02/2023
Purpose: Testing the room scheduling of cohorts.

"""

# Import the room, cohort and timetable classes
from Room import *
from Cohort import *
from Timetable import *

# Create some rooms and cohorts
rooms = [Room('R1', 100), Room('R2', 75), Room('R3', 50)]
cohorts = [Cohort('C1', 90, 'non_lab'), Cohort('C2', 60, 'lab'), Cohort('C3', 40, 'non_lab'), Cohort('C4', 92, 'lab')]

# Create a timetable with the rooms and cohorts
timetable = Timetable(rooms, cohorts)

# Schedule some cohorts in some rooms
timetable.schedule_cohort(cohorts[0], 'Monday', 9, 10)
timetable.schedule_cohort(cohorts[0], 'Monday', 10, 11)
timetable.schedule_cohort(cohorts[1], 'Monday', 13, 16)
timetable.schedule_cohort(cohorts[2], 'Monday', 11, 12)
timetable.schedule_cohort(cohorts[3], 'Monday', 9, 10)

# Print out the timetable and room for the cohorts
for cohort in cohorts:
    print(f'{cohort}:')
    for room, day, start, end in cohort.cohort_scheduled:
        print(f'\t{room} on {day} from {start} to {end}')