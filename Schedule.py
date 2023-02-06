"""
Author: Salah Mohamed
ID: 3044504
Date: 05/02/2023
Purpose: A basic idea for scheduling the cohorts in rooms
"""
# Basic Room class for testing
class Room:
    def __init__(self, room_id, capacity):
        self._room_id = room_id
        self._capacity = capacity

    def get_room_id(self):
        return self._room_id

    def get_capacity(self):
        return self._capacity

# Basic Cohort class for testing
class Cohort:
    def __init__(self, cohort_id, students):
        self._cohort_id = cohort_id
        self._students = students

    def get_cohort_id(self):
        return self._cohort_id

    def get_students(self):
        return self._students

class Schedule:
    def __init__(self, rooms, cohorts):
        self._rooms = rooms
        self._cohorts = cohorts

    def get_rooms(self):
        return self._rooms

    def get_cohorts(self):
        return self._cohorts

    def schedule_program(self):
        # Assign rooms to the cohorts
        for cohort in self._cohorts:
            for room in self._rooms:
                if room._capacity >= cohort._students:
                    # Assign the room to the cohort
                    cohort._room = room
                    break
        # Schedule the lectures in the rooms
        for cohort in self._cohorts:
            # Schedule the Core Courses on Mondays and Wednesdays
            if "PCOM" in cohort._cohort_id or "BCOM" in cohort._cohort_id:
                print(f"Cohort {cohort._cohort_id} is scheduled in Room {cohort._room._room_id} on Mondays and Wednesdays")
                cohort._room._room_id += 1
            # Schedule the Program Specific courses on Tuesdays and Thursdays
            else:
                print(f"Cohort {cohort._cohort_id} is scheduled in Room {cohort._room._room_id} on Tuesdays and Thursdays")
                cohort._room._room_id += 1

if __name__ == '__main__':

    # Define the rooms
    rooms = [Room(1, 36), Room(2, 36), Room(3, 24), Room(4, 24), Room(5, 24), Room(6, 40), Room(7, 30), Room(8, 30)]

    # Define the cohorts
    cohorts = [Cohort("PCOM", 36), Cohort("BCOM", 30), Cohort("PM", 24), Cohort("BA", 28), Cohort("FS", 33), Cohort("DXD", 35)]

    # Create a Schedule object
    schedule = Schedule(rooms, cohorts)
    
    # Schedule the program
    schedule.schedule_program()
