"""
This program simulates traffic management at a junction by handling vehicles in lanes
and deciding which lane shoudl get priority at a traffic light
"""
import os
from collections import deque

# Defined a class VehicleQueue
class VehicleQueue:
    def __init__(self, lane_name):
        self.lane_name = lane_name
        self.queue = deque()
    
    def sync_with_file(self):
        filename = f"{self.lane_name}.txt"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                lines = f.readlines()

            # Update internal deque with IDs from the file
                self.queue = deque([line.strip() for line in lines if line.strip()])

    def save_to_file(self):
         filename = f"{self.lane_name}.txt"
         with open(filename, "w") as f:
            for v in self.queue:
                f.write(v + "\n")

    
    def dequeue_multiple(self, count):
        served =[]
        for _ in range(int(count)):
            if self.queue:
                served.append(self.queue.popleft())
                
                return served
       

    def size(self):
        """
        Return the number of vehicles in the queue
        """
        return len(self.queue)

    