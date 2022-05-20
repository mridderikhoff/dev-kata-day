import config
from event import *

# Elevator class

class Elevator:
    def __init__(self):
        self.currentFloor = 1
        self.arrivalFloor = 1
        # self.eventsQueue: [Event()] = []
        self.occupants = 0
        self.speedPerFloor = 10
        self.stopTime = 20
        self.arrivalTime = 0

    def available(self, currentTime: int) -> (int, int):
        busyUntil = max(self.arrivalTime - currentTime, 0)

        if busyUntil <= 0:
            self.arrive()

        return busyUntil, self.arrivalFloor

    def free(self, currentTime: int) -> bool:
        busyUntil = max(self.arrivalTime - currentTime, 0)
        return busyUntil <= 0

    def arrive(self):
        self.currentFloor = self.arrivalFloor
        self.occupants -= 1
        # self.occupants -= event.partySize

    # assumes there is space for the occupant
    def depart(self, event: Event, currentTime: int):
        self.arrivalTime = currentTime + self.travelDuration(event)
        self.occupants += 1
        #self.occupants += event.partySize
        self.arrivalFloor = event.endFloor

    def move(self, desiredFloor: int):
        if desiredFloor > self.currentFloor:
            self.currentFloor += 1
        elif desiredFloor < self.currentFloor:
            self.currentFloor -= 1
        self.arrivalFloor = self.currentFloor

    def travelDuration(self, event) -> int:
        return (abs(event.startFloor - event.endFloor) * self.speedPerFloor) + self.stopTime

    # def enter_elevator(self) -> bool:
    #     if self.is_full():
    #         return False
    #     else:
    #         self.occupants += 1
    #         return True

    # def is_full(self) -> bool:
    #     return self.occupants >= config.capacity
