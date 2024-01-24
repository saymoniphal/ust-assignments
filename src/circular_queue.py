# Problem: Write a program to create a circular queue using dictionaries in python
# Maximum length of the queue is 5:
# if it crosses the maximum length it has to delete the latest added element
# in the queue and add the new element to the queue
"""
Circular queue of maximum size 5. If it crosses the maximum length it has to delete the latest added element in the queue and add the new element to the queue
"""

class CircularQueue():

    def __init__(self, max_size: int=5) -> None:
        self.max_size = max_size
        self.__queue__ = {}
        self.front = self.rear = -1

    def enqueue(self, value: any) -> None:
        if len(self.__queue__) == self.max_size:  # queue is reach max lenght
            # delete latest added element (last element in the queue)
            k,v = self.__queue__.popitem() # remove the last added element
            self.__queue__[k] = value
        else:
            if self.front == -1 and self.rear == -1: # queue is empty
                self.front = self.rear = 0
                self.__queue__[self.rear] = value
            else:
                self.rear += 1
                self.__queue__[self.rear] = value
    
    def dequeue(self) -> any:
        if not self.__queue__:
            return None
        if self.front == self.rear: # only 1 element in queue
            value = self.__queue__.pop(self.front)
            self.front == self.rear == -1 # empty queue
        else:
            value = self.__queue__.pop(self.front)
            self.front = self.front + 1
        return value

    def queueSize(self) -> int:
        return len(self.__queue__)

    def displayQueue(self) -> None:
        for index, v in enumerate(self.__queue__.values()):
            if index == len(self.__queue__) - 1:
                print(v)
            else:
                print(v, end=' ')