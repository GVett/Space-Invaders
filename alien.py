import pygame
from pygame.sprite import Sprite
from alien_bullet import AlienBullet
import random

class Alien(Sprite):
  """ 
    Alien class that is the primary enemy in gameplay
  """
  def __init__(self, x, y, velocity, bullet_group):
    super().__init__()
    self.image = pygame.image.load("assets/alien.png")
    self.rect = self.image.get_rect()
    self.rect.topleft = (x,y)
    self.velocity = velocity
    self.direction = 1
    self.bullet_group = bullet_group

  def update(self):
    self.rect.x += self.direction * self.velocity

    # Look for chance to pew pew
    if random.randint(0, 1000) > 999 and len(self.bullet_group) < 3:
      self.shoot()

  def shoot(self):
    bullet = AlienBullet(self.rect.centerx, self.rect.bottom)
    self.bullet_group.add(bullet)