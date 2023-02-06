import pygame
from pygame.sprite import Sprite
import game_settings as gs

class PlayerBullet(Sprite):
  """
    Weapon of choice for player
  """
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/green_laser.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.velocity = gs.PLAYER_BULLET_VELOCITY

  def update(self):
    """
      Move the bullet
    """
    self.rect.y -= self.velocity

    if self.rect.bottom < gs.HUD_HEIGHT:
      self.kill()