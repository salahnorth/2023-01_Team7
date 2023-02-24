"""
Author: Salah Mohamed
ID: 3044504
Date: 14/02/2023
Purpose: An idea for scheduling the cohorts in rooms with
         added time restriction
"""

# A class to represent a room
class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.room_scheduled = []  # A list to store scheduled slots
    
    def __str__(self):
        return f'{self.name} ({self.capacity})'
    
    # Check if the room is available for the given time slot
    def is_available(self, day, start, end):
        for slot in self.room_scheduled:
            if day == slot[0] and (start >= slot[1] and start < slot[2] or 
                                   end > slot[1] and end <= slot[2]):
                return False
        return True
    
    # Schedule a slot in the room
    def schedule(self, day, start, end):
        self.room_scheduled.append((day, start, end))
    
    # Clear the timetable of the room
    def clear_timetable(self):
        self.room_scheduled = []

# A class to represent a cohort
class Cohort:
    def __init__(self, name, size, course_type):
        self.name = name
        self.size = size
        self.course_type = course_type
        self.cohort_scheduled = []  # A list to store scheduled slots
    
    def __str__(self):
        return f'{self.name} ({self.size})'
    
    # Schedule the cohort in a room for the given time slot
    def schedule_in_room(self, rooms, day, start, end):
        room_scheduled = False
        for r in rooms:
            # Only consider rooms that have enough capacity and are available during the requested time
            if r.capacity >= self.size and r.is_available(day, start, end):
                # Check if the cohort is a lab or a regular course
                if self.course_type == 'lab':
                    # If it's a lab, only schedule it in the afternoon (12pm - 5pm)
                    if start >= 12 and end <= 17:
                        r.schedule(day, start, end)
                        self.cohort_scheduled.append((r, day, start, end))
                        room_scheduled = True
                        break
                else:
                    # If it's a regular course, only schedule it in the morning (9am - 12pm)
                    if start >= 9 and end <= 12:
                        r.schedule(day, start, end)
                        self.cohort_scheduled.append((r, day, start, end))
                        room_scheduled = True
                        break
        if not room_scheduled:
            print(f'{self} could not be scheduled in any available room during this time.')
    
    # Clear the schedule of the cohort
    def clear_schedule(self):
        self.cohort_scheduled = []

# A class to represent a timetable
class Timetable:
    def __init__(self, rooms, cohorts):
        self.rooms = rooms  # A list of rooms
        self.cohorts = cohorts  # A list of cohorts
    
    # Get all the rooms in the timetable
    def get_rooms(self):
        return self.rooms

    # Get all the cohorts in the timetable
    def get_cohorts(self):
        return self.cohorts
    
    # Schedule a cohort in a room for the given time slot
    def schedule_cohort(self, cohort, day, start, end):
        cohort.schedule_in_room(self.rooms, day, start, end)
    
    # Clear the timetable
    def clear(self):
        for cohort in self.cohorts:
            cohort.clear_schedule()
        for room in self.rooms:
            room.clear_timetable()

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