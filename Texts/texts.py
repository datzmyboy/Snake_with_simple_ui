import pygame
from Constants import constants_var

class TEXTS:
    def __init__(self,Colors):
        self.font = pygame.font.SysFont('gabriola',48)
        self.sir_sec_font = pygame.font.SysFont('gabriola',30)
        self.color = Colors
        self.titte_text = self.font.render("--Snake--",True,self.color.Green,self.color.DARKGREEN)
        self.titte_text_rect = self.titte_text.get_rect()
        self.titte_text_rect.center = (constants_var.Window_WIDTH//2,constants_var.Window_Height//2)

        self.sore_text = self.font.render("Score: " + str(constants_var.player_score),True,self.color.Green,self.color.DARKGREEN)
        self.sore_rect = self.sore_text.get_rect()
        self.sore_rect.topleft = (10,10)

        self.game_over_text = self.font.render("GAME OVER",True,self.color.RED,self.color.DARKGREEN)
        self.game_over_rect = self.game_over_text.get_rect()
        self.game_over_rect.center = (constants_var.Window_WIDTH//2,constants_var.Window_Height//2)

        self.continue_text = self.font.render("Press any key to play again",True,self.color.RED,self.color.DARKGREEN)
        self.continue_rect = self.continue_text.get_rect()
        self.continue_rect.center =(constants_var.Window_WIDTH//2,constants_var.Window_Height//2 + 64)

        self.sir_sec_text = self.sir_sec_font.render("DELTA GOLF(PPL)", True ,self.color.RED,self.color.Green)
        self.sir_sec_rect = self.sir_sec_text.get_rect()
        self.sir_sec_rect.bottomright = (constants_var.Window_WIDTH-5,constants_var.Window_Height-10)

        self.high_score_text = self.sir_sec_font.render("High Score: "+ str(constants_var.high_score),True,self.color.Green,self.color.DARKGREEN)
        self.high_score_rect = self.high_score_text.get_rect()
        self.high_score_rect.bottomleft = (constants_var.Window_WIDTH-600,constants_var.Window_Height-10)

        self.high_score_text_greet= self.sir_sec_font.render("CONGRATULATIONS YOU GOT A HIGH SCORE!", True, self.color.Green, self.color.DARKGREEN)
        self.high_score_text_greet_rect = self.game_over_text.get_rect()
        self.high_score_text_greet_rect.center = (constants_var.Window_WIDTH // 2 - 120, constants_var.Window_Height // 2 + 120)




