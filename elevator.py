import config
from event import *


class Elevator:
    def __init__(self, id: int):
        self.currentFloor = 1
        self.arrivalFloor = 1
        self.occupants = 0
        self.speedPerFloor = config.speedPerFloor
        self.stopTime = config.stopTime
        self.arrivalTime = 0
        self.id = id

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
        # self.occupants += event.partySize
        self.arrivalFloor = event.endFloor

    def move(self, desiredFloor: int):
        if desiredFloor > self.currentFloor:
            self.currentFloor += 1
        elif desiredFloor < self.currentFloor:
            self.currentFloor -= 1
        self.arrivalFloor = self.currentFloor

    def travelDuration(self, event) -> int:
        return (abs(event.startFloor - event.endFloor) * self.speedPerFloor) + self.stopTime
