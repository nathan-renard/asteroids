import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    dt = 0  # Assuming a fixed delta time for simplicity
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update(dt)
        pygame.Surface.fill(screen, (0, 0, 0))  
        player.draw(screen)
        pygame.display.flip()        
        dt = clock.tick() / 1000.0  # Convert milliseconds to seconds

if __name__ == "__main__":    
    main()