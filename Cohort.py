"""
Author: Salah Mohamed
ID: 3044504
Date: 14/02/2023
Purpose: A class object for cohorts.
"""

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