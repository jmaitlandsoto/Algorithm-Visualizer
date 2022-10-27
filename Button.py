import pygame
import random


class Button():
    def __init__(self, colour, x, y, width, height, string):
        self.colour = colour
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.string = string
        self.text = pygame.font.Font('freesansbold.ttf', 20).render(self.string, 1, (255, 255, 255))


    def draw(self, screen):
        randomcolor = (random.randrange(255), random.randrange(255), random.randrange(255))
        if self.checkHover():
            pygame.draw.rect(screen, randomcolor, [self.x, self.y, self.width, self.height], 8)
            screen.blit(self.text, (self.x + self.width/2 - 6.1*len(self.string), self.y + self.height/2 - 10))
        else:
            pygame.draw.rect(screen, self.colour, [self.x, self.y, self.width, self.height], 4)
            screen.blit(self.text, (self.x + self.width/2 - 6.1*len(self.string), self.y + self.height/2 - 10))

    def checkHover(self):
        if pygame.mouse.get_pos()[0] > self.x:
            if pygame.mouse.get_pos()[0] < self.x + self.width:
                if pygame.mouse.get_pos()[1] > self.y:
                    if pygame.mouse.get_pos()[1] < self.y + self.height:
                        return True
        else:
            return False

    def setText(self, newString):
        self.string = newString
        self.text = pygame.font.Font('freesansbold.ttf', 20).render(newString, 1, (255, 255, 255))
