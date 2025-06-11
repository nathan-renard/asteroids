import pygame
from constants import *
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x, y):
        """
        Initialize the player at a given position.
        :param x: X coordinate of the player
        :param y: Y coordinate of the player
        """                
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def draw(self, screen):
        """
        Draw the player as a triangle on the screen.
        :param screen: The pygame screen to draw on
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def triangle(self):
        """
        Calculate the vertices of the triangle representing the player.
        :return: List of vertices (pygame.Vector2) for the triangle
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def move(self, dt):
        """
        Move the player forward in the direction of its rotation.
        :param dt: Delta time since the last update
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        """
        Rotate the player left or right based on the input.
        :param dt: Delta time since the last update
        """        
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        """
        Update the player position and rotation based on input.
        :param dt: Delta time since the last update
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            self.move(dt)
        if keys[pygame.K_d]:
            self.move(dt)
            self.rotate(dt)