from event import Event
from eventManager import EventManager
from eventGenerator import EventGenerator


def printEvents(events):
    eventsString = '[\n'
    for event in events:
        eventsString += f'  {{ startFloor: {event.startFloor} endFloor: {event.endFloor} timestamp: {event.timestamp} }}\n'
    eventsString += ']\n'
    print(eventsString)


# input is list of tuples of (Event, totalTime)
def printStats(results: [(Event, int)], elevatorCount: int):
    totalTime = 0
    maxTime = 0

    # average and max wait
    for result in results:
        (event, tripTime) = result
        totalTime += tripTime
        if tripTime > maxTime:
            maxTime = tripTime

    averageWait = totalTime / len(results)
    print(f'Elevators: {elevatorCount} | max: {maxTime}s | avg: {averageWait}s')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    events = EventGenerator.generateEvents(20)

    print(f'Event c#: {len(events)}')
    for elevatorCount in range(1, 4):
        eventManager = EventManager(elevatorCount, events)
        results = eventManager.simulateTime()
        printStats(results, elevatorCount)

