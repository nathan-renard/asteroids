import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    dt = 60  # Assuming a fixed delta time for simplicity
    clock = pygame.time.Clock()
  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.Surface.fill(screen, (0, 0, 0))  
        pygame.display.flip()
        dt = clock.tick() / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":    
    main()