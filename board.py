import pygame
import game_settings as gs
from alien import Alien
from shield import Shield

class Board():
  """
  Board object that holds all game players
  """
  # Constructor
  def __init__(self, screen, alien_group, alien_bgroup, player_group, player, player_bgroup, shield_group):
    self.__screen = screen
    self.score = 0
    self.round = 1
    self.lives = gs.LIVES
    self.alien_group = alien_group
    self.alien_bgroup = alien_bgroup
    self.player_bgroup = player_bgroup
    self.player_group = player_group
    self.player = player
    self.shield_group = shield_group
    self.shield_counter = 0
    self.shield_lives = 3

  def __draw_text(self, text, font, color, x, y):
    text_img = font.render(text, True, color)
    self.__screen.blit(text_img, (x, y))

  def update(self):
    self.shift_aliens()
    self.check_collisions()
    self.check_round_complete()

    if not self.lives:
      self.game_over()
    
  def draw(self):
    # Background
    self.__screen.fill(gs.BLACK)

    # HUD

    # Round
    self.__draw_text("Round: " + str(self.round), gs.DEFAULT_FONT, gs.WHITE, 15, 10)
    
    # Score
    self.__draw_text("Score: " + str(self.score), gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH // 2 - 50, 10)

    # Lives 
    self.__draw_text("Lives: " + str(self.lives), gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH - 150, 10)

    # Line
    pygame.draw.line(self.__screen, gs.RED, (0, gs.HUD_HEIGHT), (gs.SCREEN_WIDTH, gs.HUD_HEIGHT), 4)


  def start_round(self):
    """
    Starts a new round by creating aliens and placing them on the screen
    """
    for i in range(11):
      for j in range(5):
        alien = Alien(gs.ALIEN_SPACING + i * gs.ALIEN_SPACING, gs.ALIEN_SPACING + j * gs.ALIEN_SPACING, self.round + gs.ALIEN_BASE_SPEED, self.alien_bgroup)
        self.alien_group.add(alien)    

  def shift_aliens(self):
    """
    Check if any alien is at the extent of the screen.
    If there, shift aliens down by alien width and reverse all directions.
    """
    shift = False
    
    for alien in self.alien_group.sprites():
      if alien.rect.left <= 0 or alien.rect.right >= gs.SCREEN_WIDTH:
        shift = True

    if shift:
      breach = False
      for alien in self.alien_group.sprites():
        # Reverse direction
        alien.direction = -1 * alien.direction
        # Move alien down
        alien.rect.y += gs.ALIEN_DOWN
        # Check for breach
        if alien.rect.bottom >= gs.SCREEN_HEIGHT:
          breach = True

      if breach:
        # Decrease lives by 1
        self.lives -= 1
        # Set screen depending on # of lives
        if self.lives:
          self.game_over()
        else:
          self.game_pause()

  def check_collisions(self):
    """
    Check for any and all collisions
    """
    if pygame.sprite.groupcollide(self.player_bgroup, self.alien_group, True, True):
      self.score += 100
      if self.shield_counter < 5 and not self.shield_group:
        self.shield_counter += 1

    if self.shield_counter >= 5 and not self.shield_group:
      self.shield_group.add(self.player.spawn_shield())
      self.shield_lives = 3
      self.shield_counter = 0

    if pygame.sprite.groupcollide(self.shield_group, self.alien_bgroup, False, True):
      self.shield_lives -= 1
      
    if self.shield_lives <= 0:
      self.shield_group.empty()
      
    if pygame.sprite.groupcollide(self.player_group, self.alien_bgroup, False, True):
      self.lives -= 1
      self.alien_bgroup.empty()
      if self.lives:
        self.game_pause()
      else:
        self.game_over()
      
  
  def game_over(self):
    paused = True
    self.alien_group.empty()

    while paused:
      # Events
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.round = 1
            self.score = 0
            self.lives = 3
            self.start_round()
            paused = False

      # Updates
      self.__screen.fill(gs.BLACK)
      self.__draw_text("Game Over", gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH // 2 - 125, gs.SCREEN_HEIGHT // 2 - 50)
      self.__draw_text("Final Score: " + str(self.score), gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH // 2 - 150, gs.SCREEN_HEIGHT // 2)
      self.__draw_text("Press [ENTER] to Restart", gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH // 2 - 230, gs.SCREEN_HEIGHT // 2 + 50)

      # Push to video card
      pygame.display.update()

  def game_pause(self):
    paused = True
    self.alien_group.empty()

    while paused:
      # Events
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_RETURN:
            self.start_round()
            paused = False

      # Updates
      self.__screen.fill(gs.BLACK)
      self.__draw_text("Press [ENTER] to continue", gs.DEFAULT_FONT, gs.WHITE, gs.SCREEN_WIDTH // 2 - 200, gs.SCREEN_HEIGHT // 2)

      # Push to video card
      pygame.display.update()

  def check_round_complete(self):
    """
    Round completed when all aliens are destroyed
    """
    if not self.alien_group:
      self.score += 1000 * self.round
      self.round += 1
      self.shield_counter = 0
      self.shield_lives = 3
      self.alien_bgroup.empty()
      self.start_round()
      self.game_pause()