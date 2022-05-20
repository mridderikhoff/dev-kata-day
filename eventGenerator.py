import random
from event import *
import config

#Generates random events & list of those events

class EventGenerator():
    @staticmethod
    def generateEvents(eventCount: int) -> [Event]:
        events = []
        i = 0
        while i < eventCount:
            events.append(EventGenerator.generateEvent())
            i += 1

        return sorted(events, key=lambda x: x.timestamp)

    @staticmethod
    def generateEvent():
        startFloor = random.randint(1, config.floors)
        endFloor = EventGenerator.getEndFloor(startFloor)
        timestamp = random.randint(0, config.secondsPerDay)
        # partySize = random.rantint(1, config.capacity)
        return Event(startFloor, endFloor, timestamp)

    @staticmethod
    def getEndFloor(startFloor):
        endFloor = random.randint(1, config.floors)
        while endFloor == startFloor:
            endFloor = random.randint(1, config.floors)
        return endFloor
