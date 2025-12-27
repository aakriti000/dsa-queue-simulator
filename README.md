## DSA Queue Simulator 

This project is a simulation of a traffic junction implemented using queue data structure as part of the  Data Structures and Algorithms(COMP 202) assignment.

The system simulates real-time vehicle generation, traffic light control, priority lane handling, and visualizes the traffic flow using Pygame.

## Project Description

A traffic junction connects four major roads (A, B, C, and D).  
Each road has three lanes:

L1 : Incoming lane
L2 : Outgoing lane (traffic light controlled)
L3 : Free left-turn lane

Lane AL2 is treated as a priority lane.  
When the number of vehicles in AL2 exceeds a threshold, it is served first until congestion reduces.

## Data Structures used
Queue (FIFO) : To store vehicles waiting in each lane 
Priority Logic : To give priority to lane AL2 when congested 

Queues ensure fair servicing of vehicles in First-In-First-Out order.

## Functions that use data structures

# Append 
`generate_vehicle` - Simulates a vehicle arriving at the back(tail) of the queue

# Deque initialization
`sync_with_file` - Loads the current queue state into memory for processing

# Fifo popleft()
`dequeue_multiple` - Removes vehicles from the front(head) when the light is green

# To check length
`size()` - Monitors congestion for priority lane

## Features

**Priority logic**:  Priority logic is designed to handle congestion specially for Lane AL2( Priority lane).

**Left-Hand Traffic (LHT)**: Vehicles follow LHT rules, standard in Nepal and the UK.

**Real-time Visualization**: `visualizer.py` is built with `pygame`, which features visual cues for traffic light along with glowing effects, moving vehicles, and lane markings.

**Dynamic Traffic Generation**: A separate generator script `traffic_generator.py` simulates varying vehicle loads by writing data to file buffers in real-time.
 
## Project Files

# traffic_generator.py
  Generates vehicles randomly and writes them to lane-specific files.
  
# simulator.py 
  Reads vehicle data, applies traffic light and priority logic, and removes vehicles from lanes.

# visualization.py  
  Uses Pygame to visualize the traffic junction and display real-time vehicle counts.

# queues.py 
  Contains Queue implementation used in the simulator.

# Time complexity analysis
| Operation / Function | Time Complexity | File / Location        | Technical Explanation |
|----------------------|-----------------|------------------------|-----------------------|
| Vehicle Arrival      | O(1)            | `traffic_generator.py` | Appending a single line to a file and choosing a random road are constant-time operations. |
| Queue Dispatch       | O(1)            | `queues.py`            | `deque.popleft()` removes the first element without shifting others in memory, unlike a standard list. |
| Lane Access          | O(1)            | `simulator.py`         | Accessing `queues[current_road]` uses a dictionary (hash map) lookup, which runs in constant time. |
| File Syncing         | O(n)            | `queues.py`            | `sync_with_file()` uses `readlines()`, which scans the entire file to rebuild the queue. |
| State Persistence    | O(n)            | `queues.py`            | `save_to_file()` iterates through every vehicle ID in the queue to rewrite the file. |
| Traffic Calculation  | O(R) → O(1)     | `simulator.py`         | `calculate_v_average()` loops through the number of roads. Since R = 4 (fixed), this is effectively O(1). |


## Installation and prerequisites
This project requires **Python 3.x** to run as intended. So, ensure you have **Python 3.x** installed.

You can check your installed Python version by typing the command `python --version` in the terminal.

1. **Install dependencies**
The only external dependency is `pygame` for the visualization. 
```bash
pip install pygame 
```
If you have multiple Python versions, use:
```bash
pip3 install pygame
```
The recommended method of installation is inside a **Virtual Environment**:
```bash
python -m venv venv
source venv/bin/activate    # for Linux/ macOS
venv\Scripts\activate       # for Windows
pip install pygame
```

2. **Environment setup**
Clone the repository
```bash
git clone https://github.com/aakriti000/dsa-queue-simulator.git
```
Ensure the folder looks like this:

/dsa-queue-simulator/
    |─`lane_data`/  # Created automatically after running `traffic_generator.py`
       |── `queues.py`
       |── `simulator.py`
       |── `traffic_generator.py`
       |── `visualization.py`
    |── `.gitignore`
    |── `README.md`

 ## Execution Instructions
 After cloning the repository, open you terminal/ command prompt to go to the project directory.
 ```bash
cd traffic-light-simulation-dsa
```
To simulate real-time traffic using this project, you must run the **Generator** `traffic_generator.py` next is **Simulator** `simulator.py` and the **Visualizer** `visualizer.py` simultaneously in three separate terminal windows.

First, start the **Generator** by opening a terminal and writing the following command: 
```bash
python traffic_generator.py
```
Output: You should see logs like `[GENERATOR]  Vehicle V**** arrived at Al2`.
 
 Keep this window **open**.

Next, start the **Simulator** by opening a **second** terminal window and running the following command:
```bash
python simulator.py
```
Output:
[NORMAL MODE] Current Green Light: Road D
Action: Dispatched 1 vehicles from D 

Next, start the **Visualization** by opening a **third** terminal window and running the following command:
```bash
python visualization.py
```
Output:A **Pygame** window will launch that simulates real-time traffic intersection.

## Demo(GIF/video)
Add your demo files in the repo and link them here:
  ![Image](https://github.com/user-attachments/assets/af8c5045-562e-4549-8cf5-5a98c2c9a39a)

# Author: Aakriti K.C  





