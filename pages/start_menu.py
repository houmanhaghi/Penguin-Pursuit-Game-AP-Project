import pygame, sys
from pygame.locals import *
from components.constants import *


def start_menu(player_information):
    player_command = None
    player_name, player_scores, player_last_level, player_last_result = player_information

    mainClock = pygame.time.Clock()
    pygame.init()
    pygame.display.set_caption('Penguin Pursuit')
    
    
    #setting font2 settings
    
    """
    A function that can be used to write text on our screen and buttons
    """
    def draw_text(text, font2, color, surface, x, y):
        textobj = font2.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    
    # A variable to check for the status later
    click = False
    
    # Main container function that holds the buttons and game functions
    def main_menu():
        global clock
        while True:
            screen.blit(background, (0, 0))

            draw_text('Main Menu', header_font, (0, 0, 0), screen, screen_width // 2 - 95, 117)
    
            mx, my = pygame.mouse.get_pos()

            #creating buttons
            button_1 = pygame.Rect(screen_width // 2 - 100, 250, 200, 50)
            button_2 = pygame.Rect(screen_width // 2 - 100, 350, 200, 50)
            button_3 = pygame.Rect(screen_width // 2 - 100, 450, 200, 50)

            #defining functions when a certain button is pressed
            if button_1.collidepoint((mx, my)):
                if click:
                    # one_player_game.one_player_game(player_information)
                    return 'one_player_game'
            if button_2.collidepoint((mx, my)):
                if click:
                    # two_player_game.two_player_game(player_information)
                    return 'two_player_game'
            if button_3.collidepoint((mx, my)):
                if click:
                    # score_table.score_table(player_information)
                    return 'score_table'

            pygame.draw.rect(screen, (0,191,255), button_1)
            pygame.draw.rect(screen, (0,191,255), button_2)
            pygame.draw.rect(screen, (0,191,255), button_3)
    
            #writing text on top of button
            draw_text('One Player', font2, (255,255,255), screen, screen_width // 2 - 65, 257)
            draw_text('Two Player', font2, (255,255,255), screen, screen_width // 2 - 65, 357)
            draw_text('Score Table',font2, (255,255,254), screen, screen_width // 2 - 65, 457)


            click = False

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        click = True
    
            pygame.display.update()
            mainClock.tick(60)
    
    main_menu()



# start_menu(("hello", "23, 45, 80", 1, "win"))
