import pygame
import game_settings as gs
from board import Board
from player import Player


# Setup the game   
def setup():
  # Initializing the game engine   
  pygame.init() 
  # Create a surface 
  screen = pygame.display.set_mode((gs.SCREEN_WIDTH, gs.SCREEN_HEIGHT))
  pygame.display.set_caption("Space Invade My Space")
  # Create a clock
  clock = pygame.time.Clock()
  # Create fonts 
  gs.DEFAULT_FONT = pygame.font.Font("assets/Facon.ttf", 32)
  return screen, clock


def main():
  print("Welcome to Space Invaders")
  screen, clock = setup() 
  # Running variable
  running = True

  # Groups
  alien_group = pygame.sprite.Group()
  alien_bgroup = pygame.sprite.Group()
  player_group = pygame.sprite.Group()
  player_bgroup = pygame.sprite.Group()
  
  # Create a player 
  player1 = Player(player_bgroup)
  player_group.add(player1)
 
  # Board 
  board = Board(screen, alien_group, alien_bgroup, player1, player_bgroup)
  board.start_round()
  
  while running:
    # Look at events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:  
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE or event.key == pygame.K_z:
          player1.fire_weapon()

    # Updates
    board.update()
    board.draw()
    alien_group.update()
    alien_group.draw(screen)
    alien_bgroup.update()
    alien_bgroup.draw(screen)
    player_group.update()
    player_group.draw(screen)
    player_bgroup.update()
    player_bgroup.draw(screen)

    clock.tick(60)
    pygame.display.update()
 
  pygame.quit()


if __name__ == "__main__":
  main()