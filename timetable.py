"""
Author: Salah Mohamed
ID: 3044504
Date: 14/02/2023
Purpose: An idea for scheduling the cohorts in rooms with
         added time restriction
"""

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