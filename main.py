from dispatcher import Dispatcher
from event import Event
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    events = EventGenerator.generateEvents(10)
    printEvents(events)
    Dispatcher.simulateTime(events)

    # call Service.printResults
