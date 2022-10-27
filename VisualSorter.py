import pygame
import random

from Algorithms import BubbleSort, SelectionSort, InsertionSort
from Button import Button

ARRAYSIZE = 100
arr = [0 for x in range(ARRAYSIZE)]


def randomizeArray(array):
    for i in range(ARRAYSIZE):
        temp = random.randrange(1, ARRAYSIZE, 1)
        while temp in array:
            temp += 1
            if temp > ARRAYSIZE:
                while temp in array:
                    temp -= 1
        array[i] = temp

if __name__ == "__main__":
    pygame.init()

    # Window
    size = (1200, 800)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Visual Sorting - By Joshua Maitland")

    # Text
    title_font = pygame.font.Font('freesansbold.ttf', 50)
    subtitle_font = pygame.font.Font('freesansbold.ttf', 30)
    body_font = pygame.font.Font('freesansbold.ttf', 10)

    # Buttons
    bubble_button = Button((255,255,255), 175,200, 200,50, "Bubble Sort")
    selection_button = Button((255,255,255), 425,200, 200,50, "Selection Sort")
    insertion_button = Button((255,255,255), 175,275, 200,50, "Insertion Sort")





    started = False

    # Cursor
    pygame.mouse.set_cursor(*pygame.cursors.tri_left)

while not started:
    pygame.draw.rect(screen, (0,0,0), [0,0,800,600], 0)
    title_text = title_font.render("Algorithm Visualizer", 1, (255, 255, 255))
    title_shadow = title_font.render("Algorithm Visualizer", 1, (200, 0, 0))
    screen.blit(title_shadow, (147,98))
    screen.blit(title_text, (150,100))
    bubble_button.draw(screen)
    selection_button.draw(screen)
    insertion_button.draw(screen)

    pygame.display.flip()

    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        if event.type == pygame.MOUSEBUTTONDOWN:
            if bubble_button.checkHover():
                arr = [0 for x in range(ARRAYSIZE)]
                randomizeArray(arr)
                algorithm1 = BubbleSort(arr)
                algorithm1.sort(screen)
            if selection_button.checkHover():
                arr = [0 for x in range(ARRAYSIZE)]
                randomizeArray(arr)
                algorithm2 = SelectionSort(arr)
                algorithm2.sort(screen)
            if insertion_button.checkHover():
                arr = [0 for x in range(ARRAYSIZE)]
                randomizeArray(arr)
                algorithm3 = InsertionSort(arr)
                algorithm3.sort(screen)