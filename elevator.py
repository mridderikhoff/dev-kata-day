import config
from event import *

# Elevator class

class Elevator:
    def __init__(self):
        self.currentFloor = 1
        self.arrivalFloor = None
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

    def move(self, moveUp: bool):
        if moveUp:
            self.currentFloor += 1
        else:
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
