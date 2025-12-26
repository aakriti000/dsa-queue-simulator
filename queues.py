"""
This program simulates traffic management at a junction by handling vehicles in lanes
and deciding which lane shoudl get priority at a traffic light
"""

from collections import deque

# Defined a class VehicleQueue
class VehicleQueue:

    def __init__(self, lane_name):
        self.lane_name = lane_name
        self.queue = deque()

    def enqueue(self, vehicle_id):
        """
        Adding a vehicle to the queue
        """
        self.queue.append(vehicle_id)

    def dequeue(self):
        """
        To remove and return the first vehicle from the queue
        """
        if self.is_empty():
            return None
        return self.queue.popleft()

    def is_empty(self):
        """
        Checking if the queue is empty
        Returns True if empty, otherwise returns False
        """
        return len(self.queue) == 0

    def size(self):
        """
        Return the number of vehicles in the queue
        """
        return len(self.queue)

    def display(self):
        """
        Display all vehicles in the queue (for debugging)
        """
        return list(self.queue)

#Lane priority queue for traffic light control

class LanePriorityQueue:
    
    # Priority queue to decide which lane should be given priority first

    def __init__(self):
        self.priority = {}

    def add_lane(self, lane_name):
        """
        Adding a lane with default priority 1
        """
        self.priority[lane_name] = 1

    def set_priority(self, lane_name, value):
        """
        Update the priority of a lane
        """
        if lane_name in self.priority:
            self.priority[lane_name] = value

    def get_next_lane(self):
        """
        Returning the lane with the highest priority
        """
        if not self.priority:
            return None
        return max(self.priority, key=self.priority.get)

    def reset_priority(self):
        """
        Reset all lanes to normal priority
        """
        for lane in self.priority:
            self.priority[lane] = 1
