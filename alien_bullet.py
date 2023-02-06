import pygame
import game_settings as gs
from pygame.sprite import Sprite

class AlienBullet(Sprite):
  """
  Alien bullet that goes pew pew pew!!!
  """
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/red_laser.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.velocity = gs.ALIEN_BULLET_VELOCITY

  def update(self):
    self.rect.y += self.velocity

    # Destroy bullet
    if self.rect.top > gs.SCREEN_HEIGHT:
      self.kill()