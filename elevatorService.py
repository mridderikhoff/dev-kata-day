#!/usr/bin/python3

from elevator import Elevator
from event import Event

# Tracks state of elevator but not state of events

class ElevatorService:
    elevators = []

    def __init__(self, elevatorCount):
        self.elevators = [Elevator()] * elevatorCount

    # Returns next available elevator
    def __getNextElevator__(self, event: Event, currentTime: int) -> (Elevator, int):
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
        nextToProcessEvents = []

        # Take elevator when on the right floor
        for event in events:
            bestElevator, bestWhenAvailable = self.getNextElevator(event, currentTime)
            if bestWhenAvailable <= 0:
                bestElevator.depart(event, currentTime)
                processedEvents.add((event, currentTime - event.timestamp + bestElevator.travelDuration(event)))
            else:
                nextToProcessEvents.add((event, bestElevator, bestWhenAvailable))

        

        # Move the other elevator in the right direction up/down




        return processedEvents
