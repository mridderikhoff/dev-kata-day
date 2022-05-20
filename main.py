from event import Event
# from eventManager import EventManager
from eventGenerator import EventGenerator


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def printEvents(events):
    eventsString = '[\n'
    for event in events:
        eventsString += f'  {{ startFloor: {event.startFloor} endFloor: {event.endFloor} timestamp: {event.timestamp} }}\n'
    eventsString += ']'
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
    # events = EventGenerator.generateEvents(10)
    # printEvents(events)
    #
    # # lowest elevator count with waitTime threshold met
    # # maxElevators = range(1, 3)
    # # for numElevators in maxElevators:
    # #     dispatcher = EventManager(numElevators, events)
    # #     EventManager.simulateTime(events)
    #
    # dispatcher = EventManager(2, events)
    # dispatcher.simulateTime()

    printStats([
        (Event(1, 2, 1), 150),
        (Event(1, 2, 1), 300),
        (Event(1, 2, 1), 100),
        (Event(1, 2, 1), 100),
        (Event(1, 2, 1), 150),
    ], 3)

    # call Service.printResults
