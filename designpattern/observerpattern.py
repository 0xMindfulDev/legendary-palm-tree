'''
Python program to demonstrate the observer design pattern as
implemented on the wikipedia page. Source = https://en.wikipedia.org/wiki/Observer_pattern
The observer pattern is a software design pattern in which an object, named the subject, 
maintains a list of its dependents, called observers, and notifies them automatically 
of any state changes, usually by calling one of their methods. It is mainly used 
for implementing distributed event handling systems, in "event driven" software
'''
class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs):
        print("Got", args, kwargs, "From", observable)


subject = Observable()
observer = Observer(subject)
subject.notify_observers("test", kw="python")