import pygame
import os
from queues import VehicleQueue

WIDTH, HEIGHT = 800, 800
ROAD_W = 150
BG_COLOR = (245, 245, 220)
CAR_BLUE = (30, 144, 255)
WINDSHIELD = (200, 230, 255)

def draw_vehicle(screen, x, y, road_name):
    """Draws a vehicle shape oriented towards the junction center."""
    if road_name in ["A", "C"]: # Vertical roads
        width, height = 30, 45
        pygame.draw.rect(screen, CAR_BLUE, (x, y, width, height), border_radius=5)
        w_y = y + 30 if road_name == "A" else y + 5
        pygame.draw.rect(screen, WINDSHIELD, (x + 3, w_y, 24, 8))
    else: # Horizontal roads
        width, height = 45, 30
        pygame.draw.rect(screen, CAR_BLUE, (x, y, width, height), border_radius=5)
        w_x = x + 5 if road_name == "B" else x + 30
        pygame.draw.rect(screen, WINDSHIELD, (w_x, y + 3, 8, 24))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Traffic Junction Visualization")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 20)
    
    # Initializing Queues 
    queues = {r: VehicleQueue(f"{r}L1") for r in ["A", "B", "C", "D"]}
    
    # Drawing coordinates
    offsets = {
        "A": (WIDTH//2 - 45, 80, 0, 60),      # Top
        "C": (WIDTH//2 + 15, HEIGHT-120, 0, -60), # Bottom
        "B": (WIDTH-120, HEIGHT//2 - 45, -60, 0), # Right
        "D": (80, HEIGHT//2 + 15, 60, 0)      # Left
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BG_COLOR)
        
        # Drawing Road Surface
        pygame.draw.rect(screen, (50, 50, 50), (WIDTH//2 - ROAD_W//2, 0, ROAD_W, HEIGHT))
        pygame.draw.rect(screen, (50, 50, 50), (0, HEIGHT//2 - ROAD_W//2, WIDTH, ROAD_W))

        for r, q in queues.items():
            # SYNC with the .txt files
            q.sync_with_file()
            
            start_x, start_y, step_x, step_y = offsets[r]
            
            # Draw Vehicles
            for i in range(q.size()):
                if i > 8: break 
                vx = start_x + (i * step_x)
                vy = start_y + (i * step_y)
                draw_vehicle(screen, vx, vy, r)

            # Draw Labels
            text = font.render(f"Road {r}: {q.size()}", True, (0, 0, 0))
            screen.blit(text, (start_x, start_y - 50 if r in ["A","C"] else start_y - 30))

        pygame.display.flip()
        clock.tick(30) 

    pygame.quit()

if __name__ == "__main__":
    main()