import pygame
from Variables import *
def MovementMachine(Player):
    if Player.Health <= 0:
        return True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_w] or keys[pygame.K_s]:

        if len(Player.history) < 50:
            Player.history.append((Player.rect.x,Player.rect.y))
        else:
            Player.history.pop(0)
            Player.history.append((Player.rect.x,Player.rect.y))

        Player.rollback()

        if keys[pygame.K_d] and Player.rect.x<SCREENWIDTH-50:
            Player.MoveRight()
            if Player.velocity < 3:
                Player.velocity += 0.05

        elif keys[pygame.K_a] and Player.rect.x>0:
            Player.MoveLeft()
            if Player.velocity < 3:
                Player.velocity += 0.05

        if keys[pygame.K_w] and Player.rect.y>0:
            Player.MoveUp()
            if Player.velocity < 3:
                Player.velocity += 0.05

        elif keys[pygame.K_s] and Player.rect.y<SCREENHEIGHT-50:
            Player.MoveDown()
            if Player.velocity < 3:
                Player.velocity += 0.05
    else:
        Player.velocity = 0

