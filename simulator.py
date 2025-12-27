import time
import os
from queues import VehicleQueue

ROADS = ["A", "B", "C", "D"] 
GREEN_TIME = 3        # Light stays green for 3 seconds
PRIORITY_LANE = "AL2" # L2 is the incoming lane where cars wait

def calculate_v_average(queues):
    total = sum(q.size() for q in queues.values())
    return total // 4 if total > 0 else 0

def main():
    print("Traffic Simulator Logic Engine Active")

    queues = {r: VehicleQueue(f"{r}L1") for r in ROADS}
    road_sequence = ["A", "B", "C", "D"]
    current_idx = 0
    priority_active = False
 
    while True:
        for q in queues.values():
            q.sync_with_file()

# Check high-priority condition (Road A> 10 vehiles)
        road_a_count = queues["A"].size()
        if road_a_count > 10:
            priority_active = True
        elif road_a_count < 5:
            priority_active = False
 
    # Determining which road gets Green light

        if priority_active:
             current_road = "A"
             print(f"![PRIORITY MODE] Road A is congested ({road_a_count} cars). Staying Green.")
        else:
             current_road = road_sequence[current_idx]
             print(f"[NORMAL MODE] Current Green Light: Road {current_road}")
           
     # Calculate how many vehicles to serve
        v_avg = calculate_v_average(queues)
    
     # Serve atleast 1 if cars are present
        num_to_serve = max(1, v_avg) if queues[current_road].size() > 0 else 0
        
     # Removing vehicles and then update the file
        if num_to_serve > 0:
            served_vehicles = queues[current_road].dequeue_multiple(num_to_serve)
            queues[current_road].save_to_file()
            print(f"Action: Dispatched {len(served_vehicles)} vehicles from {current_road}")
           
    # Turn to next road if not in priority mode
        if not priority_active:
             current_idx = (current_idx + 1) % 4

        print("-" * 30)
        time.sleep(GREEN_TIME)


if __name__ == "__main__":
    main()
