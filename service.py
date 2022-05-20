#!/usr/bin/python3

from elevator import Elevator
from event import Event

class Service:
    elevators = []

    def __init__(self, size):
        self.elevators = [Elevator()] * size

    # Returns next available elevator
    def getNextElevator(self, event: Event, currentTime: int) -> (Elevator, int):
        bestElevator: Elevator
        bestWhenAvailable = 1000000

        # Find the closest available one
        for elevator in self.elevators:
            elevatorWhenAvailable, elevatorNextFloor = elevator.available(currentTime)
            elevatorFloorChange = abs(elevatorNextFloor - event.startFloor)
            whenAvailable = elevator.speedPerFloor * elevatorFloorChange + elevatorWhenAvailable
            if whenAvailable <= 0 and bestWhenAvailable:
                bestElevator = elevator
                bestWhenAvailable = elevatorWhenAvailable

        return bestElevator, bestWhenAvailable

    # Returns processed event
    def processNextEvent(self, events: [Event], currentTime: int) -> Event:
