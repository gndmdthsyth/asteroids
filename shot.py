from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def collision(self, object):
        distance = pygame.math.Vector2.distance_to(self.position, object.position)
        if distance <= self.radius + object.radius:
            self.kill()
            object.split()