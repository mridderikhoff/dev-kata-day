import config
from event import *
from elevatorService import ElevatorService


# Manages time, dispatches events (adds events to queue
# Previously was dispatcher.py
class EventManager:
    def __init__(self, elevatorCount: int, events: [Event]):
        self.elevatorCount = elevatorCount
        self.events = events
        self.service = ElevatorService(elevatorCount)

        self.unfulfilledEvents = []
        self.processedEvents = []

    def simulateTime(self) -> [(Event, int)]:
        currentTime = 0
        while currentTime <= config.secondsPerDay:
            self.dispatchEvents(currentTime)
            currentTime += 1
        return self.processedEvents  # TODO

    def dispatchEvents(self, currentTime: int):
        eventsToDispatch = list(filter(lambda event: event.timestamp == currentTime, self.events))

        if len(eventsToDispatch) > 0:
            self.unfulfilledEvents.extend(eventsToDispatch)
            # self.printDispatchingEvents(eventsToDispatch, currentTime)

            processedEvents = self.service.processNextEvents(self.unfulfilledEvents, currentTime)
            for processedEvent, tripTime in processedEvents:
                self.unfulfilledEvents.remove(processedEvent)

            # print(processedEvents)
            self.processedEvents.extend(processedEvents)

    def printDispatchingEvents(self, events, currentTime: int):
        for event in events:
            print(f'eventDispatched for {event.timestamp} at {currentTime}')
