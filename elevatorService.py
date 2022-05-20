#!/usr/bin/python3

from elevator import Elevator
from event import Event


# Tracks state of elevator but not state of events
class ElevatorService:
    elevators = []

    def __init__(self, elevatorCount):
        self.elavators = []
        for i in range(elevatorCount):
            self.elevators.append(Elevator(i))

    def __getNextElevator(self, event: Event, currentTime: int) -> (Elevator, int):
        bestElevator: Elevator = None
        bestWhenAvailable = 1000000

        # Find the closest available one
        for elevator in self.elevators:
            elevatorWhenAvailable, elevatorNextFloor = elevator.available(currentTime)
            elevatorFloorChange = abs(elevatorNextFloor - event.startFloor)
            whenAvailable = elevator.speedPerFloor * elevatorFloorChange + elevatorWhenAvailable
            if whenAvailable <= bestWhenAvailable:
                bestElevator = elevator
                bestWhenAvailable = elevatorWhenAvailable

        return bestElevator, bestWhenAvailable

    # Returns processed event that has been assigned to an elevator, and the wait time for processing it
    def processNextEvents(self, events: [Event], currentTime: int) -> [(Event, int)]:
        processedEvents = []
        nextToProcessEvents = []

        # Take elevator when on the right floor
        for event in events:
            bestElevator, bestWhenAvailable = self.__getNextElevator(event, currentTime)
            if bestWhenAvailable <= 0:
                bestElevator.depart(event, currentTime)
                processedEvents.append((event, currentTime - event.timestamp + bestElevator.travelDuration(event)))
            elif bestElevator.free(currentTime):
                nextToProcessEvents.append((event, bestElevator, bestWhenAvailable))

        # Move the other elevator in the right direction up/down
        nextToProcessEvents.sort(key=lambda x: x[2])
        numberOfElevatorToMove = min(len(self.elevators) - len(processedEvents), len(nextToProcessEvents))
        for i in range(numberOfElevatorToMove):
            event, elevator, whenAvailable = nextToProcessEvents[i]
            elevator.move(event.endFloor)

        return processedEvents
