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
from Course import *

# Create some rooms and cohorts
rooms = [Room('R1', 100), Room('R2', 75), Room('R3', 50)]
'''
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
'''
# Create a course and split it into cohorts
c1 = Course('PRDV 0201', 90, 'lecture')
c2 = Course('PRDV 0202', 75, 'lecture')
c3 = Course('PRDV 0203', 60, 'lab')

c1.split_cohorts()
c2.split_cohorts()
c3.split_cohorts()

# Create a timetable with the three rooms and the cohorts from the course
all_cohorts = c1.cohorts + c2.cohorts + c3.cohorts
timetable = Timetable([rooms[0], rooms[1], rooms[2]], all_cohorts)

timetable.schedule_cohort(c1.cohorts[0], 'Wednesday', 9, 10)
timetable.schedule_cohort(c1.cohorts[1], 'Wednesday', 9, 10)
timetable.schedule_cohort(c1.cohorts[2], 'Wednesday', 9, 10)

timetable.schedule_cohort(c2.cohorts[0], 'Tuesday', 9, 10)
timetable.schedule_cohort(c2.cohorts[1], 'Wednesday', 9, 10)

timetable.schedule_cohort(c3.cohorts[0], 'Tuesday', 13, 15)
timetable.schedule_cohort(c3.cohorts[1], 'Thursday', 9, 11)


# Print out the scheduled slots for each cohort and room
for cohort in timetable.get_cohorts():
    print(f'{cohort.name}:')
    for slot in cohort.cohort_scheduled:
        room_name = slot[0].name
        day = slot[1]
        start = slot[2]
        end = slot[3]
        print(f'\tScheduled in {room_name} on {day} from {start} to {end}.')