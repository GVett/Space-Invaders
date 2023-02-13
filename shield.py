import pygame
from pygame.sprite import Sprite
import game_settings as gs

class Shield(Sprite):
  """
  Shield for the player after 3 aliens are killed
  """
  def __init__(self, x, y):
    super().__init__()
    self.image = pygame.image.load("assets/shield.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.velocity = gs.PLAYER_SPEED

  def update(self):
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.rect.left > 0):
      self.rect.x -= self.velocity 
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.rect.right < gs.SCREEN_WIDTH):
      self.rect.x += self.velocity
