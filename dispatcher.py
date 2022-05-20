import config
import service
from event import *


class Dispatcher:
    def __init__(self, events: []):
        self.events = events

    def simulateTime(self):
        currentTime = 0
        while currentTime < config.secondsPerDay:
            self.dispatchEvents(currentTime)
            currentTime += 1

    def dispatchEvents(self, currentTime: int):
        nextEvent = self.events[0]

        while nextEvent.timestamp == currentTime:
            self.dispatchEvent(nextEvent)
            self.events.pop(0)
            nextEvent = self.events[0]

    @staticmethod
    def dispatchEvent(event: Event):
        service.Service.getNextElevator(event)
