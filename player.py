import pygame
import game_settings as gs
from player_bullet import PlayerBullet
from pygame.sprite import Sprite
from shield import Shield

class Player(Sprite):
  """
  Player defends against alien horde
  """
  def __init__(self, player_bgroup):
    super().__init__()
    self.image = pygame.image.load("assets/player_ship.png")
    self.rect = self.image.get_rect()
    self.rect.centerx = gs.PLAYER_X
    self.rect.bottom = gs.PLAYER_Y
    self.velocity = gs.PLAYER_SPEED
    self.bullet_group = player_bgroup

  def update(self):
    # Look for keyboard presses
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and (self.rect.left > 0):
      self.rect.x -= self.velocity 
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and (self.rect.right < gs.SCREEN_WIDTH):
      self.rect.x += self.velocity

  def fire_weapon(self):
    """
    Create a bullet and let if fly  
    """
    if len(self.bullet_group) < 2:
      bullet = PlayerBullet(self.rect.centerx, self.rect.top)
      self.bullet_group.add(bullet)

  def spawn_shield(self):
    shield = Shield(self.rect.centerx, self.rect.bottom)
    return shield