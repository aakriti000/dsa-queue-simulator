#Author: Aakriti KC
#Description: "This code simulates traffic by randomly generating vehicles and distributing them across three lanes per road, with lane L2 acting as the priority lane."

import random
import time
import os

# Defining roads and their lanes
ROADS = ["A", "B", "C", "D"]


def generate_vehicle():
    # Randomly to choose the roads and lanes
    road = random.choice(ROADS)
    lane = "L1" # L1 is the incoming lane
    vehicle_id = f"V{random.randint(1000, 9999)}" # Choose vehicle id number between 1000 and 9999

    """
    Opening the lane files
    """
    with open(f"{road}{lane}.txt", "a") as f:
        f.write(vehicle_id + "\n")
    print(f"[GENERATOR] Vehicle {vehicle_id} arrived at {road}{lane}")

if __name__ == "__main__":
    for r in ROADS: open(f"{r}L1.txt", "w").close()
    while True:
        generate_vehicle()
        time.sleep(random.uniform(0.5, 1.5))

