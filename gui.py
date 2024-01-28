import pygame
from game_logic import GameLogic
from tkinter import messagebox

class GameGUI:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.game_logic = GameLogic()
        self.full_message = self.new_level()

        # text display and input
        self.font = pygame.font.Font(None, 36)
        self.input_font = pygame.font.Font(None, 28)

        # input box variable
        self.input_box = pygame.Rect(280, 300, 800, 40)
        self.input_text = ""
        self.input_active = False

        #Button variables
        self.submit_button = pygame.Rect(600, 500, 150, 40)
        self.button_color = (0, 128, 255)
        self.button_text = self.font.render("   Submit", True, (255, 255, 255))

    def new_level(self):
        self.random_message = self.game_logic.generate_random_message()
        self.cipher = self.game_logic.encrypt_message(self.random_message[0])
        print(self.cipher)
        self.full_message = f"{self.random_message[1]}\nCipher : {self.cipher[0]}"
        if self.cipher[1] != {}:
            self.full_message += f"\nHint: {self.cipher[1]}"
        return self.full_message        

    def run_game(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.input_box.collidepoint(event.pos):
                            self.input_active = not self.input_active

                        else:
                            self.input_active = False

                        #check for submit button click
                        if self.submit_button.collidepoint(event.pos):
                            self.handle_submit_button()

                if event.type == pygame.KEYDOWN:
                    if self.input_active:
                        if event.key == pygame.K_RETURN:
                            self.handle_submit_button()
                        elif event.key == pygame.K_BACKSPACE:
                            self.input_text = self.input_text[:len(self.input_text)-1]
                        else:
                            self.input_text += event.unicode

            self.screen.fill((255,255,255)) # white

            #score panel
            score = self.font.render("Score:", True, (0,0,0))
            self.screen.blit(score, (20,510))

            s_value = self.font.render(str(self.game_logic.score), True, (0,0,0))
            self.screen.blit(s_value, (100, 512))

            # draw the message
            #encrypted_text = self.font.render(self.full_message, True, (0,0,0))
            #self.screen.blit(encrypted_text, (20,20))

            message_to_decipher = self.full_message
            message_text = self.font.render(message_to_decipher, True, (0,0,0))
            self.screen.blit(message_text , (20,60))

            #input box

            pygame.draw.rect(self.screen, (0,0,0), self.input_box, 2)
            input_surface  = self.input_font.render(self.input_text, True, (0,0,0))
            width = max(200, input_surface.get_width()+10)
            self.input_box.w = width
            self.screen.blit(input_surface, (self.input_box.x+5, self.input_box.y+5))

            #submit button
            
            pygame.draw.rect(self.screen, self.button_color, self.submit_button)
            self.screen.blit(self.button_text, (self.submit_button.x + 10, self.submit_button.y+ 10))

            
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def handle_submit_button(self):
        player_solution = self.input_text.lower()
        is_solution_correct = self.game_logic.check_solution(player_solution, self.cipher[3])

        if is_solution_correct:
            print("Correct")
            print(player_solution)
            self.game_logic.update_score()
            self.new_level()

        else:
            print("Incorrect")
            messagebox.showinfo("CipherQuest", "Incorrect, Try again!")

        self.input_text = ""