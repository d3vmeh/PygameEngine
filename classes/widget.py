import pygame
from pygame.locals import *

pygame.init()
pygame.font.init()



class Widget():
    def __init__(self,x,y,width,height,color=(255,255,255),thickness=0,
                 text="",text_font=None,text_color=(255,255,255),text_coords=(),text_object = None,text_size=20
                 ):


        #Widget Setup
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.thickness = thickness

        #Widget text
        self.text = text
        self.text_coords = text_coords
        self.text_font = text_font
        self.text_color = text_color
        self.text_object = text_object
        self.text_size = text_size

        self.text_font = pygame.font.Font(text_font,text_size)
        self.textsurface = self.text_font.render(self.text,True,self.text_color)




    def draw(self,display):
        pygame.draw.rect(display,self.color, (self.x,self.y,self.width,self.height))
        display.blit(self.textsurface,self.text_coords)
