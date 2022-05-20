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

    # Returns processed event that has been assigned to an elevator, and the wait time for processing it
    def processNextEvents(self, events: [Event], currentTime: int) -> [(Event, int)]:
        processedEvents = []

        for event in events:
            bestElevator, bestWhenAvailable = self.getNextElevator(event, currentTime)
            if bestWhenAvailable <= 0:
                bestElevator.depart(event, currentTime)
                processedEvents.add((event, currentTime - event.timestamp))

        return processedEvents
