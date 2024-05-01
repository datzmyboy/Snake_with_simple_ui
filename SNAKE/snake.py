import random
import pygame
from pygame.font import SysFont
from SNAKE.score_records import update_player,read_players,delete_player,create_player_json
from Texts import  texts
from Constants import constants_var
from blank import run
pygame.init()
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
font = SysFont('Georgia',60,bold=True)
title_surf = font.render('SNAKE',True,'green')
title_rect = title_surf.get_rect(center=(WINDOW_WIDTH // 2-35, 110))
title_rect.width+= 70

class main_window:
    def __init__(self,screen):
        self.screen_surface = screen
        self.font = SysFont('Georgia',20,bold=True)
        self.new_game_surf = self.font.render('NEW GAME',True,'white')
        self.new_game_button = pygame.Rect(WINDOW_WIDTH//2-80,WINDOW_HEIGHT//2+20,140,40)
        self.snake_game = Game(600,600)
        # for load game_button/TOP SCORE

    def game_button_activate(self):
        pygame.init()
        a, b = pygame.mouse.get_pos()
        # this code is when the cursor is hovering the buttons and the colors will change
        if self.new_game_button.x <= a <= self.new_game_button.x + 110 and self.new_game_button.y <= b <= self.new_game_button.y + 60:
            # colors the text if it satisfies the condition
            pygame.draw.rect(self.screen_surface,(180, 180, 180) , self.new_game_button)
        else:
            # if it dose not satisty, draw a rect at this coordinates and color
            pygame.draw.rect(self.screen_surface, (110, 110, 110), self.new_game_button)

    # this is the top score button

    def run_main_window(self):
        running_1 = True
        while running_1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_1 =False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.new_game_button.collidepoint(event.pos):
                       self.snake_game.run_snake()
            self.game_button_activate()
            pygame.display.set_caption("Main")
            self.screen_surface.blit(self.new_game_surf, (self.new_game_button.x + 5, self.new_game_button.y + 5))
            self.screen_surface.blit(title_surf, (WINDOW_WIDTH // 2 - title_surf.get_width() // 2, 80))
            pygame.draw.rect(self.screen_surface, (0, 255, 0), title_rect, 6)
            pygame.display.update()




# THE CODE FOR THE SNAKE
############################################################################################################

class Game:
    def __init__(self,Window_WIDTH,Window_Height):
        self.Window_WIDTH = Window_WIDTH
        self.Window_Height = Window_Height
        self.display_surface = pygame.display.set_mode((self.Window_WIDTH,self.Window_Height))
        pygame.display.set_caption("SNAKE GAME")
        self.FPS = 6
        self.clock = pygame.time.Clock()
        self.colors = Colors()
        self.text = texts.TEXTS(self.colors)
        self.snake = Snake(self.colors)
        self.apple  = Apple(self.colors)
        self.sounds = Sounds()
        self.player_name = "USER_DATA"
        self.player_created = True
        self.to_display = False

        self.moving_left = True
        self.moving_right = True
        self.moving_up = True
        self.moving_down = True

    def update_score(self):
        user = read_players()
        my_user = user[0]
        my_user_score = my_user["player_score"]
        if self.snake.score > my_user_score:
            update_score = update_player(self.player_name,self.snake.score)
            self.to_display = True

    def run_snake(self):
        runinning = True
        while runinning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    runinning = False
                    run()
                #snake movement
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.moving_left:
                            self.snake.move_left()
                            self.moving_right = False
                            self.moving_up = True
                            self.moving_down = True

                    if event.key == pygame.K_RIGHT:
                        if self.moving_right:
                            self.snake.move_right()
                            self.moving_left = False
                            self.moving_up = True
                            self.moving_down = True
                    if event.key == pygame.K_DOWN:
                        if self.moving_down:
                            self.snake.move_down()
                            self.moving_up = False
                            self.moving_left = True
                            self.moving_right = True
                    if event.key == pygame.K_UP:
                        if self.moving_up:
                            self.snake.move_up()
                            self.moving_down = False
                            self.moving_left = True
                            self.moving_right = True
            if self.snake.snake_head_coords in self.snake.snake_body_coords:
                self.display_surface.blit(self.text.game_over_text, self.text.game_over_rect)
                self.display_surface.blit(self.text.continue_text, self.text.continue_rect)
                self.update_score()
                if self.to_display:
                    self.display_surface.blit(self.text.high_score_text_greet,self.text.high_score_text_greet_rect)
                    self.text.high_score_text = self.text.sir_sec_font.render("High Score:" + str(self.snake.score), True,
                                                                self.colors.Green, self.colors.DARKGREEN)
                is_pause = True

                while is_pause:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            self.snake.score = 0
                            self.snake.init_head_x = constants_var.Window_WIDTH // 2
                            self.snake.init_head_y = constants_var.Window_Height // 2 + 100
                            self.snake.snake_head_coords = (
                                self.snake.init_head_x, self.snake.init_head_y, constants_var.Snake_size,
                                constants_var.Snake_size)
                            self.snake.snake_body_coords = []
                            self.snake.snake_dx = 0
                            self.snake.snake_dy = 0
                            is_pause = False
                        if event.type == pygame.QUIT:
                            runinning = False
                            pygame.quit()
                    pygame.display.update()
            self.snake.update_position()
            self.snake.snake_body_coords.insert(0,self.snake.snake_head_coords)
            self.snake.snake_body_coords.pop()
            self.snake.eat_apple(self.apple,self.sounds)
            #self.snake.update_position()
            self.snake.init_head_x += self.snake.snake_dx
            self.snake.init_head_y += self.snake.snake_dy
            self.snake.snake_head_coords =(self.snake.init_head_x,self.snake.init_head_y,constants_var.Snake_size,constants_var.Snake_size)
            self.text.sore_text = self.text.font.render("Score: " + str(self.snake.score), True,self.colors.Green,self.colors.DARKGREEN)
            pygame.display.update()
            self.display_surface.fill(self.colors.WHITE)
            self.display_surface.blit(self.text.titte_text,self.text.titte_text_rect)
            self.display_surface.blit(self.text.sore_text,self.text.sore_rect)
            self.display_surface.blit(self.text.sir_sec_text,self.text.sir_sec_rect)
            self.display_surface.blit(self.text.high_score_text,self.text.high_score_rect)
            ### the assets
            for body in self.snake.snake_body_coords:
                pygame.draw.rect(self.display_surface,self.colors.DARKGREEN,body)
                print(len(self.snake.snake_body_coords))
            pygame.draw.rect(self.display_surface,self.colors.Green,self.snake.snake_head_coords)
            pygame.draw.rect(self.display_surface,self.colors.RED,self.apple.apple_coords)
            pygame.display.update()
            self.clock.tick(self.FPS)
            print(f"{self.snake.init_head_x} - {self.snake.init_head_y}")

        pygame.quit()


class Colors:
    def __init__(self):
        self.Green = (0,255,0)
        self.DARKGREEN = (10,50,10)
        self.RED = (255,0,0)
        self.DARKRED = (150,0,0)
        self.WHITE = (255,255,255)
        self.LIGHT_GREY = (180, 180, 180)
        self.DARK_GREY = (110, 110, 110)

class Sounds:
    def __init__(self):
        self.sound = pygame.mixer.Sound("pick_up_sound (1).wav")
    def play_sound(self):
        self.sound.play()


class Snake:
    def __init__(self,colors):
        self.colors = colors
        self.display_surface = pygame.display.set_mode((constants_var.Window_WIDTH, constants_var.Window_Height))
        self.snake_size  = constants_var.Snake_size
        self.init_head_x = constants_var.Window_WIDTH//2
        self.init_head_y = constants_var.Window_Height//2 + 100

        #keep track of the snake's direction
        self.snake_dx = 0
        self.snake_dy = 0
        #( position at x , position at y , width of the snake or block , height of the block)
        self.snake_head_coords = (self.init_head_x,self.init_head_y,constants_var.Snake_size,constants_var.Snake_size)
        self.snake_body_coords = []
        #self.snake_head_rect = pygame.draw.rect(self.display_surface,self.colors.RED,self.snake_head_coords)
        self.snake_head_rect = pygame.Rect(self.snake_head_coords)
        self.score = 0
        self.buffer_distance = 50

        # self.moving_left = True
        # self.moving_right = True
        # self.moving_up = True
        # self.moving_down = True

    def move_left(self):
        self.snake_dx = -1 * constants_var.Snake_size
        self.snake_dy = 0
        self.update_position()


    def move_right(self):
        self.snake_dx = 1 * constants_var.Snake_size
        self.snake_dy = 0
        self.update_position()

    def move_down(self):
        self.snake_dx = 0
        self.snake_dy =  1 * constants_var.Snake_size
        self.update_position()

    def move_up(self):
        self.snake_dx = 0
        self.snake_dy = -1 * constants_var.Snake_size
        self.update_position()

    def update_position(self):
        self.snake_head_rect.move_ip(self.snake_dx, self.snake_dy)
        if self.init_head_x >= constants_var.Window_WIDTH:
            self.init_head_x = 0
        elif self.init_head_x < 0:
            self.init_head_x = constants_var.Window_WIDTH - constants_var.Snake_size

        if self.init_head_y >= constants_var.Window_Height:
            self.init_head_y = 0
        elif self.init_head_y < 0:
            self.init_head_y = constants_var.Window_Height - constants_var.Snake_size

        self.snake_head_rect.topleft = (self.init_head_x, self.init_head_y)
    def eat_apple(self,apple,sounds):
        self.apple = apple
        self.sounds = sounds
        if self.snake_head_rect.colliderect(self.apple.apple_rect):
            self.score+=1
            print("click")
            print(self.score)
            self.sounds.play_sound()
            apple_x = random.randint(0, constants_var.Window_WIDTH - constants_var.Snake_size)
            apple_y = random.randint(0, constants_var.Window_Height - constants_var.Snake_size)
            apple.apple_coords = (apple_x, apple_y, constants_var.Snake_size, constants_var.Snake_size)
            apple.apple_rect = pygame.Rect(apple.apple_coords)
            self.snake_body_coords.append(self.snake_head_coords)



class Apple:
    def __init__(self,colors):
        self.colors = colors
        self.display_surface = pygame.display.set_mode((constants_var.Window_WIDTH, constants_var.Window_Height))
        #(topledft x and topleft y , width , height)
        self.apple_coords = (500,500,constants_var.Snake_size,constants_var.Snake_size)
        # self.apple_rect = pygame.draw.rect(self.display_surface,self.colors.RED,self.apple_coords)
        self.apple_rect = pygame.Rect(self.apple_coords)

game = main_window(screen)
game.run_main_window()