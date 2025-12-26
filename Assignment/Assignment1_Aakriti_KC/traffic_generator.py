#Author: Aakriti KC
#Description: "This code simulates traffic by randomly generating vehicles and distributing them across three lanes per road, with lane L2 acting as the priority lane."

import random
import time

# Defining roads and their lanes
roads = ["A", "B", "C", "D"]
lanes = ["L1", "L2", "L3"]   # L2 is priority lane

# Defining a function to generate vehicle
def generate_vehicle(): 
    # Randomly to choose the roads and lanes
    road = random.choice(roads)
    lane = random.choice(lanes)

    vehicle_id = f"V{random.randint(1000, 9999)}" # Choose vehicle id number between 1000 and 9999

    """
    Opening the lane files
    """
    with open(f"{road}{lane}.txt", "a") as f:
        f.write(vehicle_id + "\n")

    print(f"[GENERATOR] Added {vehicle_id} to lane {road}{lane}")

def main():
    print("Traffic Generator Running...")
    while True:
        generate_vehicle()
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    main()