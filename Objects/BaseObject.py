import pygame
class GameObject:
    def __init__(self,rect):
        self.rect = rect
        self.x = rect.x
        self.y = rect.y

    def render(self,screen,color):
        pygame.draw.rect(screen,color,self.rect)