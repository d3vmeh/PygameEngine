import pygame
from pygame.locals import *


import engine_utility
from engine_utility import *


from classes.widget import Widget






pygame.init()
pygame.font.init()

#do pygame.font.get_fonts() to see all fonts


def initialize_engine(screen_width=1920,screen_height=1080):

    #Display surface
    global screen
    global screenwidth
    global screenheight

    screen = pygame.display.set_mode((screen_width, screen_height))
    screenwidth = screen_width
    screenheight = screen_height

    #Variable for convenience
    global centerx
    global centery

    centerx = screen_width/2
    centery = screen_height/2

    global screenalign
    screenalign = Alignment(0,0)





    #All Widget-related definitions
    global widgets
    global buttons

    widgets = []
    buttons = []


    #all colors go here
    global black
    global white
    global red
    global green
    global blue

    black = (0, 0, 0)
    white = (255, 255, 255)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

    global background_color
    background_color = black




def menu():

    main_text_width = 500
    main_text_height = 100

    main_text_x = screenalign.align_center_x(screenwidth,main_text_width)
    main_text_y = 50

    main_text_widget =  Widget(main_text_x,main_text_y,main_text_width,main_text_height,color=red,
                               text="Welcome",text_color=white,text_coords=Alignment(main_text_x,main_text_y).align_center(main_text_width,main_text_height,400,75),text_size=100)


    while True:
        pygame.display.update()

        main_text_widget.draw(screen)


        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()


def run():
    while True:
        pygame.display.update()
        screen.fill(background_color)
        #code goes here








        #^^^
        draw_all(widgets, screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == MOUSEBUTTONDOWN:
                mousex,mousey = event.pos
                for button in buttons:
                    if button.isClicked(mousex,mousey):
                        buttons[buttons.index(button)].onClicked()


initialize_engine()
menu()
run()
