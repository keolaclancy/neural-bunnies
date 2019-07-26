import pygame


# This is the interface that should be displayed.
# Determine the score
class Interface:

    def __init__(self, screen, height, width):
        self.high_score = 0
        self.color = 255, 171, 0
        self.screen = screen
        self.screen_width = width
        self.screen_height = height
        self.font = pygame.font.Font('ressources/font/DroidSansMono.ttf', 20)

    # Display the score.
    def display_score(self, score):
        score_string = 'Score: {:05d}'.format(score)

        text = self.font.render(score_string, True, self.color)
        text_rect = text.get_rect()
        text_rect.top = 20
        text_rect.right = self.screen_width - 20

        self.screen.blit(text, text_rect)

        if score > self.high_score:
            self.high_score = score

            new_high = 'HI'
            text = self.font.render(new_high, True, self.color)
            text_rect = text.get_rect()
            text_rect.top = 20
            text_rect.right = self.screen_width - 180

            self.screen.blit(text, text_rect)

    # Display the end screen.
    def display_end_screen(self, score):
        # Save high score.
        if score > self.high_score:
            self.high_score = score

        string = 'You loose, Press any key to restart'
        text = self.font.render(string, True, self.color)
        text_rect = text.get_rect()
        text_rect.top = self.screen_height / 2
        text_rect.right = (self.screen_width / 2) + 150
        self.screen.blit(text, text_rect)

        score_string = 'Score: {:05d}'.format(score)
        text = self.font.render(score_string, True, self.color)
        text_rect = text.get_rect()
        text_rect.top = (self.screen_height / 2) - 80
        text_rect.right = self.screen_width / 2
        self.screen.blit(text, text_rect)

        high_score_string = 'High score: {:05d}'.format(self.high_score)
        text = self.font.render(high_score_string, True, self.color)
        text_rect = text.get_rect()
        text_rect.top = (self.screen_height / 2) - 50
        text_rect.right = self.screen_width / 2
        self.screen.blit(text, text_rect)
