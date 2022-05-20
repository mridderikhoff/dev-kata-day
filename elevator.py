from event import *


class Elevator:
    def __init__(self):
        self.capacity = 1
        self.currentFloor = 1
        self.arrivalFloor = None
        # self.eventsQueue: [Event()] = []
        self.occupants = 0
        self.speedPerFloor = 10
        self.stopTime = 20
        self.arrivalTime = 0
        self.currentTime = 0

    def available(self, currentTime: int) -> (int, int):
        busyUntil = max(self.arrivalTime - currentTime, 0)

        if busyUntil == 0:
            self.arrive()

        return busyUntil, self.arrivalFloor

    def arrive(self):
        self.currentFloor = self.arrivalFloor
        self.occupants -= 1

    # assumes there is space for the occupant
    def add_occupant(self, event: Event, currentTime: int):
        self.currentTime = currentTime
        self.arrivalTime = currentTime + (abs(event.startFloor - event.endFloor) * self.speedPerFloor) + self.stopTime
        self.occupants += 1
        self.arrivalFloor = event.endFloor

    # def enter_elevator(self) -> bool:
    #     if self.is_full():
    #         return False
    #     else:
    #         self.occupants += 1
    #         return True

    # def is_full(self) -> bool:
    #     return self.occupants >= self.capacity
