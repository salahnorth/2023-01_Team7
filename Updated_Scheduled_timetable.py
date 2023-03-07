class Course:
    def __init__(self, name, size, course_type, program):
        self.name = name
        self.size = size
        self.course_type = course_type
        self.cohorts = []  # A list to store cohorts
        self.program = program
    
    def __str__(self):
        return f'{self.name} ({self.size})'
    
    # Split the course into cohorts of equal size
    def split_cohorts(self):
        num_cohorts = self.size // 30  # Each cohort has a maximum size of 30
        cohort_size = self.size // num_cohorts
        for i in range(num_cohorts):
            cohort_name = f'{self.name}_{i+1}'
            cohort = {'name': cohort_name, 'size': cohort_size, 'type': self.course_type, 'schedule': [], 'program': self.program}
            self.cohorts.append(cohort)

    

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

# Create a course and split it into cohorts
c1 = Course('PRDV 0201', 90, 'lecture', 'core')
c2 = Course('PRDV 0202', 75, 'lecture', 'specific')
c3 = Course('PRDV 0203', 60, 'lab', 'specfic')

c1.split_cohorts()
c2.split_cohorts()
c3.split_cohorts()

# Create a timetable with the three rooms and the cohorts from the course
all_cohorts = c1.cohorts + c2.cohorts + c3.cohorts
timetable = Timetable([rooms[0], rooms[1], rooms[2]], all_cohorts)

timetable.schedule_cohort(c1.cohorts[0], 'Thursday', 9, 10)
timetable.schedule_cohort(c1.cohorts[1], 'Wednesday', 9, 10)
timetable.schedule_cohort(c1.cohorts[2], 'Wednesday', 9, 10)

timetable.schedule_cohort(c2.cohorts[0], 'Tuesday', 9, 10)
timetable.schedule_cohort(c2.cohorts[1], 'Wednesday', 14, 15)

timetable.schedule_cohort(c3.cohorts[0], 'Thursday', 12, 13)
timetable.schedule_cohort(c3.cohorts[1], 'Tuesday', 12, 13)