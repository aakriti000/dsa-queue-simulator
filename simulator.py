"""
simulator.py
------------
This program simulates traffic light control.
It reads vehicles from lane files, applies traffic rules,
removes vehicles when a lane gets green, and updates files
so visualization.py can reflect the changes.
"""

import time
import os

# ---------------- CONFIGURATION ---------------- #

ROADS = ["A", "B", "C", "D"]
LANES = ["L1", "L2", "L3"]

GREEN_TIME = 3           # seconds a light stays green
VEHICLES_PER_GREEN = 1  # vehicles removed per green cycle

PRIORITY_LANE = "AL2"
PRIORITY_START = 10      # >10 → priority
PRIORITY_END = 5         # <5 → normal

# ----------------------------------------------- #


def read_lane_file(filename):
    """
    Reads all vehicles from a lane file.
    Returns list of vehicles.
    """
    if not os.path.exists(filename):
        return []

    with open(filename, "r") as f:
        return f.readlines()


def write_lane_file(filename, vehicles):
    """
    Writes remaining vehicles back to lane file.
    """
    with open(filename, "w") as f:
        for v in vehicles:
            f.write(v)


def get_lane_count(lane):
    """
    Returns number of vehicles in a given lane.
    """
    vehicles = read_lane_file(f"{lane}.txt")
    return len(vehicles)


def serve_lane(lane):
    """
    Removes vehicles from a given lane (GREEN light).
    """
    filename = f"{lane}.txt"
    vehicles = read_lane_file(filename)

    if not vehicles:
        print(f"[GREEN] {lane} (no vehicles)")
        return

    print(f"[GREEN] {lane}")

    # Remove vehicles
    served = vehicles[:VEHICLES_PER_GREEN]
    remaining = vehicles[VEHICLES_PER_GREEN:]

    for v in served:
        print(f"[PASS] Vehicle {v.strip()} passed from {lane}")

    write_lane_file(filename, remaining)


def choose_next_lane(priority_active):
    """
    Chooses which L2 lane gets green.
    """
    if priority_active:
        return PRIORITY_LANE

    # Round-robin over L2 lanes
    for road in ROADS:
        lane = f"{road}L2"
        if get_lane_count(lane) > 0:
            return lane

    return None


def main():
    print("Traffic Simulator Started...\n")

    priority_active = False

    try:
        while True:
            al2_count = get_lane_count(PRIORITY_LANE)

            # ---------------- PRIORITY LOGIC ---------------- #
            if al2_count > PRIORITY_START:
                priority_active = True
                print("[PRIORITY] AL2 activated")

            elif al2_count < PRIORITY_END:
                if priority_active:
                    print("[PRIORITY] Normal mode resumed")
                priority_active = False

            # ---------------- SERVE LANE ---------------- #
            green_lane = choose_next_lane(priority_active)

            if green_lane:
                serve_lane(green_lane)
            else:
                print("[IDLE] No vehicles to serve")

            time.sleep(GREEN_TIME)

    except KeyboardInterrupt:
        print("\nTraffic Simulator Stopped.")


if __name__ == "__main__":
    main()
