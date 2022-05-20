import config
# import service
from event import *


class Dispatcher:
    @staticmethod
    def simulateTime(events: [Event]):
        currentTime = 0
        while currentTime <= config.secondsPerDay:
            Dispatcher.dispatchEvents(events, currentTime)
            currentTime += 1

    @staticmethod
    def dispatchEvents(events: [Event], currentTime: int):
        while len(events) > 0 and events[0].timestamp == currentTime:
            Dispatcher.dispatchEvent(events[0], currentTime)
            events.pop(0)

    @staticmethod
    def dispatchEvent(event: Event, currentTime: int):
        print(f'eventDispatched for {event.timestamp} at {currentTime}', )
        service.Service.getNextElevator(event)
