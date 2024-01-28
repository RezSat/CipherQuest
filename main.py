import pygame
from gui import GameGUI

def main():
    pygame.init()

    window_size = (800, 600)
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("CipherQuest")


    game_gui = GameGUI(screen)
    game_gui.run_game()

    pygame.quit()

if __name__ == "__main__":
    main()