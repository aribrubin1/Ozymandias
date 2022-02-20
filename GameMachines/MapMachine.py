from Variables import black
import pygame
from Objects.Enemy import Enemy
def MapMachine(screen,grid,Player,Subject):

    for i in grid:
        for g in i:
            pygame.draw.rect(screen,g.colour,(g.x,g.y,g.width,g.width))

    if Subject.path!=None:
        Subject.Move()
        print("reg move\n")
    else:
        Subject.secondarymove(Player)
        print("sec move\n")
    Subject.render(screen, (255,0,0))