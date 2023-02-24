"""
Author: Salah Mohamed
ID: 3044504
Date: 14/02/2023
Purpose: A class object for classrooms.
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
