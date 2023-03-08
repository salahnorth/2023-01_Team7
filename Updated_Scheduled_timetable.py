class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.schedule = []  # A list to store scheduled slots
    
    def __str__(self):
        return f'{self.name} ({self.capacity})'
    
    # Check if the room is available for the given time slot
    def is_available(self, day, start, end):
        for slot in self.schedule:
            if day == slot[0] and (start >= slot[1] and start < slot[2] or 
                                   end > slot[1] and end <= slot[2]):
                return False
        return True
    
    # Schedule a slot in the room
    def schedule_slot(self, day, start, end):
        self.schedule.append((day, start, end))
    
    # Clear the timetable of the room
    def clear_timetable(self):
        self.schedule = []

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
        room_scheduled = False
        for room in self.rooms:
            # Only consider rooms that have enough capacity and are available during the requested time
            if room.capacity >= cohort['size'] and room.is_available(day, start, end):

                # Check if the cohort is a lab or a regular course
                if cohort['type'] == 'lab':

                    # If it's a lab, only schedule it in the afternoon (12pm - 5pm)
                    if start >= 12 and end <= 17:
                        room.schedule_slot(day, start, end)
                        cohort['schedule'].append((room, day, start, end))
                        room_scheduled = True
                        break
                else:
                    # If it's a core course, only schedule it on Mondays or Wednesdays in the mornings (9am - 12pm)
                    if cohort['program'] == 'core':
                        if start >= 9 and end <= 12 and (day == 'Monday' or day == 'Wednesday'):
                            room.schedule_slot(day, start, end)
                            cohort['schedule'].append((room, day, start, end))
                            room_scheduled = True
                            break

                    else:
                        # If it's not a core course, only schedule it on Tuesdays or Thursdays in the mornings (9am - 12pm)
                        if start >= 9 and end <= 12 and (day == 'Tuesday' or day == 'Thursday'):
                            room.schedule_slot(day, start, end)
                            cohort['schedule'].append((room, day, start, end))
                            room_scheduled = True
                            break

                   
        if not room_scheduled:
            print(f'{cohort["name"]} could not be scheduled in any available room during this time.')

rooms = [Room('R1', 100), Room('R2', 75), Room('R3', 50)]

# Create cohorts

cohort1 = {'name': 'PCOM 0101', 'size': 30, 'type': 'lecture', 'schedule': [], 'program': 'core'}
cohort2 = {'name': 'PRDV 0202_1', 'size': 30, 'type': 'lecture', 'schedule': [], 'program': 'specifc'}
cohort3 = {'name': 'PRDV 0202_2', 'size': 15, 'type': 'lecture', 'schedule': [], 'program': 'spcific'}
cohort4 = {'name': 'PRDV 0203_1', 'size': 30, 'type': 'lecture', 'schedule': [], 'program': 'specific'}
cohort5 = {'name': 'PRDV 0203_2', 'size': 30, 'type': 'lecture', 'schedule': [], 'program': 'specific'}
cohort6 = {'name': 'PRDV 0204_1', 'size': 30, 'type': 'lab', 'schedule': [], 'program': 'specific'}
cohort7 = {'name': 'PRDV 0204_1', 'size': 30, 'type': 'lecture', 'schedule': [], 'program': 'specific'}


# Create a timetable with the three rooms and the cohorts from the course
all_cohorts = [cohort1] + [cohort2] + [cohort3] + [cohort4] + [cohort5] + [cohort6] + [cohort7]
timetable = Timetable([rooms[0], rooms[1], rooms[2]], all_cohorts)

timetable.schedule_cohort(cohort1, 'Thursday', 9, 10)
timetable.schedule_cohort(cohort2, 'Thursday', 9, 10)
timetable.schedule_cohort(cohort3, 'Thursday', 9, 10)

timetable.schedule_cohort(cohort4, 'Thursday', 9, 10)
timetable.schedule_cohort(cohort5, 'Thursday', 9, 10)
timetable.schedule_cohort(cohort6, 'Tuesday', 9, 10)
timetable.schedule_cohort(cohort7, 'Tuesday', 9, 10)
