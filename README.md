# DSA Queue Simulator 

This project is a simulation of a traffic junction implemented using queue data structure as part of the  Data Structures and Algorithms(COMP 202) assignment.

The system simulates real-time vehicle generation, traffic light control, priority lane handling, and visualizes the traffic flow using Pygame.

# Problem Description

A traffic junction connects four major roads (A, B, C, and D).  
Each road has three lanes:

L1 : Incoming lane
L2 : Outgoing lane (traffic light controlled)
L3 : Free left-turn lane

Lane AL2 is treated as a priority lane.  
When the number of vehicles in AL2 exceeds a threshold, it is served first until congestion reduces.


# Data Structures used
Queue (FIFO) : To store vehicles waiting in each lane 
Priority Logic : To give priority to lane AL2 when congested 

Queues ensure fair servicing of vehicles in First-In-First-Out order.

# Project Files

  # traffic_generator.py
  Generates vehicles randomly and writes them to lane-specific files.

  # simulator.py 
  Reads vehicle data, applies traffic light and priority logic, and removes vehicles from lanes.

  # visualization.py  
  Uses Pygame to visualize the traffic junction and display real-time vehicle counts.

  # queues.py 
  Contains Queue implementation used in the simulator.



# How to Run the Project

Open three terminals in the project directory.

# Terminal 1 : Vehicle Generator
python traffic_generator.py

#  Terminal 2 : Simulator
python simuator.py

# Terminal 3 : visualization.py
python visualization.py

# Author: Aakriti K.C  



